#!/usr/bin/env python3
"""Build readable per-day channel transcripts from a slackdump export.

Why this exists alongside build_threads.py: in #copywriting-feedback a single
review conversation is frequently split across one real Slack thread PLUS
several separate top-level messages (reviewers reply to the channel, not to the
thread). Strict thread grouping files those critiques as contentless fragments
and loses them. A chronological day transcript keeps the conversation intact.

Reads  : export/<channel>/YYYY-MM-DD.json + export/users.json
Writes : raw/days/<date>.md   (readable, for classification)
         raw/days/<date>.json (same content, structured)

Usage: python scripts/build_sessions.py [--export DIR] [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_threads import (  # reuse the tested helpers
    SKIP_SUBTYPES,
    author_of,
    clean_text,
    load_channels,
    load_users,
)


def hhmm(ts: str) -> str:
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).strftime("%H:%M")
    except (TypeError, ValueError):
        return "--:--"


def datestr(ts: str) -> str:
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError):
        return "unknown"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", default="export", type=Path)
    ap.add_argument("--out", default=Path("raw/days"), type=Path)
    args = ap.parse_args()

    export_dir = args.export
    if not export_dir.is_dir():
        print("error: export dir %s does not exist" % export_dir, file=sys.stderr)
        return 1

    users = load_users(export_dir)
    channels = load_channels(export_dir)

    day_files = sorted(export_dir.glob("*/[0-9]*.json"))
    if not day_files:
        print("error: no day files found under %s" % export_dir, file=sys.stderr)
        return 1

    # Collect and de-duplicate every message.
    by_ts: dict = {}
    for f in day_files:
        try:
            msgs = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print("warn: could not parse %s: %s" % (f, e), file=sys.stderr)
            continue
        for m in msgs:
            if m.get("subtype") in SKIP_SUBTYPES:
                continue
            ts = m.get("ts")
            if ts and ts not in by_ts:
                by_ts[ts] = m

    # Split into top-level messages and replies keyed by parent ts.
    replies = defaultdict(list)
    tops = []
    for ts, m in by_ts.items():
        tts = m.get("thread_ts")
        if tts and tts != ts:
            replies[tts].append(m)
        else:
            tops.append(m)

    tops.sort(key=lambda m: float(m.get("ts", 0)))
    for lst in replies.values():
        lst.sort(key=lambda m: float(m.get("ts", 0)))

    # Orphan replies: parent not in the window. Surface them at top level so the
    # feedback is not silently dropped.
    top_ts = {m.get("ts") for m in tops}
    orphan_parents = [p for p in replies if p not in top_ts]
    for p in orphan_parents:
        for m in replies[p]:
            tops.append(m)
    tops.sort(key=lambda m: float(m.get("ts", 0)))
    orphan_ts = {m.get("ts") for p in orphan_parents for m in replies[p]}

    days = defaultdict(list)
    for m in tops:
        days[datestr(m.get("ts", ""))].append(m)

    out_dir = args.out
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in list(out_dir.glob("*.md")) + list(out_dir.glob("*.json")):
        old.unlink()

    n_msgs = 0
    for date, day_tops in sorted(days.items()):
        md = ["# #copywriting-feedback - %s" % date, ""]
        structured = {"date": date, "messages": []}
        for m in day_tops:
            ts = m.get("ts", "")
            author = author_of(m, users)
            text = clean_text(m.get("text", ""), users, channels)
            kids = replies.get(ts, []) if ts not in orphan_ts else []
            tag = " [orphan-reply: parent pre-dates window]" if ts in orphan_ts else ""
            md.append("## %s  %s%s" % (hhmm(ts), author, tag))
            md.append("")
            md.append(text if text else "_(no text)_")
            md.append("")
            n_msgs += 1
            entry = {
                "ts": ts, "time_utc": hhmm(ts), "author": author,
                "text": text, "is_orphan_reply": ts in orphan_ts, "replies": [],
            }
            for r in kids:
                r_author = author_of(r, users)
                r_text = clean_text(r.get("text", ""), users, channels)
                md.append("> **%s  %s**  %s" % (hhmm(r.get("ts", "")), r_author,
                                                r_text.replace("\n", "\n> ")))
                md.append("")
                n_msgs += 1
                entry["replies"].append({
                    "ts": r.get("ts"), "time_utc": hhmm(r.get("ts", "")),
                    "author": r_author, "text": r_text,
                })
            structured["messages"].append(entry)
            md.append("---")
            md.append("")

        (out_dir / ("%s.md" % date)).write_text("\n".join(md), encoding="utf-8")
        (out_dir / ("%s.json" % date)).write_text(
            json.dumps(structured, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    print("=" * 60)
    print("BUILD SESSIONS SUMMARY")
    print("=" * 60)
    print("days written        : %d -> %s/" % (len(days), out_dir))
    print("messages rendered   : %d" % n_msgs)
    print("top-level messages  : %d" % len(tops))
    print("orphan replies kept : %d" % len(orphan_ts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
