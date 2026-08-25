#!/usr/bin/env python3
"""Emit structured/rec_*.json from the hand-classified records.

source_ts is not hand-written: it is resolved here against raw/days/<date>.json
by matching the record's `anchor` (the person whose top-level message(s) the
record is built from) and the authors that appear in its feedback. That keeps
every record traceable back to real Slack messages.

Usage: python scripts/emit_structured.py [--days raw/days] [--out structured]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from records_a import RECORDS as RECORDS_A
from records_b import RECORDS as RECORDS_B
from records_c import RECORDS as RECORDS_C

ALL_RECORDS = RECORDS_A + RECORDS_B + RECORDS_C


def slug(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return s or "unknown"


def resolve_source_ts(day: dict, anchor: str, feedback_authors: set) -> list:
    """Top-level messages by the anchor (plus their replies), and any top-level
    message from a reviewer who appears in this record's feedback."""
    out = []
    for m in day.get("messages", []):
        author = m.get("author", "")
        take = author == anchor or author in feedback_authors
        if take:
            out.append(m["ts"])
            out.extend(r["ts"] for r in m.get("replies", []))
        else:
            # The anchor may only appear inside someone else's thread.
            if any(r.get("author") == anchor for r in m.get("replies", [])):
                out.append(m["ts"])
                out.extend(r["ts"] for r in m.get("replies", []))
    # De-dupe, keep chronological order.
    seen = set()
    ordered = []
    for ts in sorted(out, key=float):
        if ts not in seen:
            seen.add(ts)
            ordered.append(ts)
    return ordered


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", default=Path("raw/days"), type=Path)
    ap.add_argument("--out", default=Path("structured"), type=Path)
    args = ap.parse_args()

    out_dir = args.out
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("rec_*.json"):
        old.unlink()

    # Guard against two records claiming the same anchor on the same day.
    seen_ids = {}
    written = 0
    missing_days = []
    empty_src = []

    for rec in ALL_RECORDS:
        date = rec["date"]
        anchor = rec["anchor"]
        day_path = args.days / ("%s.json" % date)
        if not day_path.exists():
            missing_days.append(date)
            continue
        day = json.loads(day_path.read_text(encoding="utf-8"))

        fb_authors = {f["author"] for f in rec["feedback"] if f.get("author")}
        source_ts = resolve_source_ts(day, anchor, fb_authors)
        if not source_ts:
            empty_src.append("%s / %s" % (date, anchor))

        rec_id = "rec_%s_%s" % (date.replace("-", ""), slug(anchor))
        n = seen_ids.get(rec_id, 0)
        seen_ids[rec_id] = n + 1
        if n:
            rec_id = "%s_%d" % (rec_id, n + 1)

        out = {
            "thread_id": rec_id,
            "date": date,
            "thread_class": rec["thread_class"],
            "source_ts": source_ts,
            "source_day_file": "raw/days/%s.md" % date,
            "anchor": anchor,
            "original_copy": rec["original_copy"],
            "feedback": rec["feedback"],
            "outcome": rec["outcome"],
        }
        if rec.get("notes"):
            out["notes"] = rec["notes"]

        (out_dir / ("%s.json" % rec_id)).write_text(
            json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        written += 1

    print("=" * 60)
    print("EMIT STRUCTURED")
    print("=" * 60)
    print("records written : %d -> %s/" % (written, out_dir))
    by_class = {}
    n_fb = 0
    for rec in ALL_RECORDS:
        by_class[rec["thread_class"]] = by_class.get(rec["thread_class"], 0) + 1
        n_fb += len(rec["feedback"])
    for k, v in sorted(by_class.items()):
        print("  %-14s %d" % (k, v))
    print("feedback entries: %d" % n_fb)
    if missing_days:
        print("\nWARN missing day files: %s" % ", ".join(sorted(set(missing_days))))
    if empty_src:
        print("\nWARN records with no resolved source_ts:")
        for e in empty_src:
            print("  " + e)
    return 0


if __name__ == "__main__":
    sys.exit(main())
