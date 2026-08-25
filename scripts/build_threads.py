#!/usr/bin/env python3
"""Reshape a slackdump export into one JSON file per thread.

Reads  : export/<channel>/YYYY-MM-DD.json  + export/users.json
Writes : raw/thread_<parent_ts>.json  (dot in the ts becomes an underscore)

Usage: python scripts/build_threads.py [--export DIR] [--out DIR] [--keep-singletons]
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# Subtypes that are channel noise, not content.
SKIP_SUBTYPES = {
    "channel_join", "channel_leave", "channel_topic", "channel_purpose",
    "channel_name", "channel_archive", "channel_unarchive", "bot_add",
    "bot_remove", "pinned_item", "unpinned_item", "channel_convert_to_private",
    "channel_convert_to_public", "reminder_add", "app_conversation_leave",
}

ZERO_WIDTH = ("​", "‌", "‍", "﻿")


def strip_zw(s: str) -> str:
    for zw in ZERO_WIDTH:
        s = s.replace(zw, "")
    return s


MENTION_RE = re.compile(r"<@([UWB][A-Z0-9]+)(?:\|[^>]*)?>")
CHANNEL_RE = re.compile(r"<#(C[A-Z0-9]+)(?:\|([^>]*))?>")
LINK_RE = re.compile(r"<(https?://[^|>]+)(?:\|([^>]*))?>")
SPECIAL_RE = re.compile(r"<!(here|channel|everyone)(?:\|[^>]*)?>")


def load_users(export_dir: Path) -> dict:
    """user_id -> display name. Prefers display_name, then real_name, then name."""
    path = export_dir / "users.json"
    if not path.exists():
        print("warn: %s not found; user IDs will not be resolved" % path, file=sys.stderr)
        return {}
    users = json.loads(path.read_text(encoding="utf-8"))
    out = {}
    for u in users:
        uid = u.get("id")
        if not uid:
            continue
        profile = u.get("profile") or {}
        name = (
            (profile.get("display_name") or "").strip()
            or (profile.get("real_name") or "").strip()
            or (u.get("real_name") or "").strip()
            or (u.get("name") or "").strip()
            or uid
        )
        out[uid] = strip_zw(name)
    return out


def load_channels(export_dir: Path) -> dict:
    path = export_dir / "channels.json"
    if not path.exists():
        return {}
    try:
        chans = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {c["id"]: c.get("name", c["id"]) for c in chans if c.get("id")}


def clean_text(text: str, users: dict, channels: dict) -> str:
    """Resolve inline mentions, channel refs and links to readable text."""
    if not text:
        return ""
    text = MENTION_RE.sub(lambda m: "@" + users.get(m.group(1), m.group(1)), text)
    text = CHANNEL_RE.sub(
        lambda m: "#" + (m.group(2) or channels.get(m.group(1), m.group(1))), text
    )
    text = LINK_RE.sub(lambda m: m.group(2) or m.group(1), text)
    text = SPECIAL_RE.sub(lambda m: "@" + m.group(1), text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    # Slack sprinkles zero-width chars into display names and pasted copy.
    return strip_zw(text).strip()


def author_of(msg: dict, users: dict) -> str:
    uid = msg.get("user") or ""
    if uid and uid in users:
        return users[uid]
    # Bot / app messages carry no `user`.
    for key in ("username", "bot_id", "user"):
        if msg.get(key):
            return str(msg[key])
    return "unknown"


def ts_to_iso(ts: str) -> str:
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).isoformat()
    except (TypeError, ValueError):
        return ""


def ts_to_date(ts: str) -> str:
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError):
        return ""


def shape(msg: dict, users: dict, channels: dict) -> dict:
    out = {
        "ts": msg.get("ts"),
        "datetime_utc": ts_to_iso(msg.get("ts", "")),
        "author": author_of(msg, users),
        "author_id": msg.get("user") or msg.get("bot_id") or "",
        "text": clean_text(msg.get("text", ""), users, channels),
    }
    reactions = [
        {"name": r.get("name"), "count": r.get("count", 0)}
        for r in (msg.get("reactions") or [])
    ]
    if reactions:
        out["reactions"] = reactions
    attachments = msg.get("files") or []
    if attachments:
        out["files"] = [
            {"name": f.get("name"), "filetype": f.get("filetype")} for f in attachments
        ]
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", default="export", type=Path)
    ap.add_argument("--out", default="raw", type=Path)
    ap.add_argument(
        "--keep-singletons",
        action="store_true",
        help="also write threads that have no replies (default: drop them)",
    )
    args = ap.parse_args()

    export_dir = args.export
    out_dir = args.out
    if not export_dir.is_dir():
        print("error: export dir %s does not exist" % export_dir, file=sys.stderr)
        return 1

    users = load_users(export_dir)
    channels = load_channels(export_dir)

    day_files = sorted(export_dir.glob("*/[0-9]*.json"))
    if not day_files:
        print(
            "error: no day files matched %s/*/[0-9]*.json" % export_dir, file=sys.stderr
        )
        return 1

    threads = defaultdict(list)
    seen_ts = set()
    n_msgs = 0
    n_skipped_subtype = 0
    day_dates = []

    for f in day_files:
        day_dates.append(f.stem)
        try:
            msgs = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print("warn: could not parse %s: %s" % (f, e), file=sys.stderr)
            continue
        for msg in msgs:
            if msg.get("subtype") in SKIP_SUBTYPES:
                n_skipped_subtype += 1
                continue
            ts = msg.get("ts")
            if not ts or ts in seen_ts:
                continue  # de-dupe: a reply can appear in more than one day file
            seen_ts.add(ts)
            n_msgs += 1
            threads[msg.get("thread_ts") or ts].append(msg)

    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("thread_*.json"):
        old.unlink()

    written = 0
    dropped_singletons = 0
    dropped_orphans = 0
    reply_counts = []
    authors = set()

    for parent_ts, msgs in sorted(threads.items()):
        msgs.sort(key=lambda m: float(m.get("ts", 0)))
        real_parent = next((m for m in msgs if m.get("ts") == parent_ts), None)
        # No message owns this thread_ts: the parent was posted before the export
        # window, so we have feedback with no copy attached to it. Not usable.
        if real_parent is None:
            dropped_orphans += 1
            continue
        parent = real_parent
        replies = [m for m in msgs if m.get("ts") != parent.get("ts")]

        if not replies and not args.keep_singletons:
            dropped_singletons += 1
            continue

        record = {
            "thread_id": parent_ts,
            "date": ts_to_date(parent_ts),
            "reply_count": len(replies),
            "parent": shape(parent, users, channels),
            "replies": [shape(m, users, channels) for m in replies],
        }
        safe = parent_ts.replace(".", "_")
        (out_dir / ("thread_%s.json" % safe)).write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        written += 1
        reply_counts.append(len(replies))
        authors.add(record["parent"]["author"])
        authors.update(r["author"] for r in record["replies"])

    print("=" * 60)
    print("BUILD THREADS SUMMARY")
    print("=" * 60)
    print("day files read       : %d" % len(day_files))
    if day_dates:
        print("date range in export : %s .. %s" % (min(day_dates), max(day_dates)))
    print("messages kept        : %d" % n_msgs)
    print("skipped (join/leave) : %d" % n_skipped_subtype)
    print("threads written      : %d  -> %s/" % (written, out_dir))
    print("dropped (no replies) : %d" % dropped_singletons)
    print("dropped (orphan reply, parent pre-dates window) : %d" % dropped_orphans)
    if reply_counts:
        print(
            "replies/thread       : median %.1f, mean %.1f, max %d"
            % (
                statistics.median(reply_counts),
                statistics.mean(reply_counts),
                max(reply_counts),
            )
        )
    print("distinct authors     : %d" % len(authors))
    if written == 0:
        print("\nWARNING: no threads written. Check the export and the date window.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
