#!/usr/bin/env python3
"""Validate structured/thread_*.json against the fixed classification vocabulary.

Enum drift is the main failure mode of the classification pass -- one stray
"tone_of_voice" instead of "tone" and the pattern aggregation silently misses it.
Exits non-zero if anything is out of vocabulary or structurally wrong.

Usage: python scripts/validate_structured.py [--dir structured]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

FEEDBACK_TYPES = {"critique", "approval", "rewrite", "question", "general_comment"}
TARGETS = {
    "subject_line", "opening_line", "body", "cta", "tone", "length",
    "personalization", "overall",
}
COPY_TYPES = {
    "cold_email", "follow_up", "sequence", "reply_handling", "linkedin_dm",
    "subject_line_only", "landing_page", "other", "none",
}
OUTCOMES = {"revised", "approved", "abandoned", "no_consensus", "unresolved"}

# Added after surveying the real channel: it is not uniformly copy review.
# Only copy_review and discussion feed the playbook; banter is excluded.
THREAD_CLASSES = {"copy_review", "discussion", "banter"}


def validate_file(path: Path, errors: list, warnings: list, stats: dict) -> None:
    try:
        rec = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append("%s: not valid JSON (%s)" % (path.name, e))
        return

    for field in ("thread_id", "date", "thread_class", "source_ts",
                  "original_copy", "feedback", "outcome"):
        if field not in rec:
            errors.append("%s: missing required field '%s'" % (path.name, field))

    tclass = rec.get("thread_class")
    if tclass not in THREAD_CLASSES:
        errors.append("%s: thread_class %r not in vocabulary" % (path.name, tclass))
    stats["thread_class"][tclass] += 1

    # source_ts is the traceability link back to the Slack messages.
    src = rec.get("source_ts")
    if not isinstance(src, list) or not src:
        errors.append("%s: source_ts must be a non-empty list" % path.name)

    copy = rec.get("original_copy") or {}
    if not isinstance(copy, dict):
        errors.append("%s: original_copy is not an object" % path.name)
    else:
        ct = copy.get("copy_type")
        if ct not in COPY_TYPES:
            errors.append(
                "%s: copy_type %r not in vocabulary" % (path.name, ct)
            )
        stats["copy_type"][ct] += 1
        if rec.get("thread_class") == "copy_review" and not (copy.get("text") or "").strip():
            warnings.append(
                "%s: copy_type is %r but original_copy.text is empty" % (path.name, ct)
            )
        if rec.get("thread_class") == "copy_review" and not (copy.get("author") or "").strip():
            warnings.append("%s: copy_review record has no copy author" % path.name)

    outcome = rec.get("outcome")
    if outcome not in OUTCOMES:
        errors.append("%s: outcome %r not in vocabulary" % (path.name, outcome))
    stats["outcome"][outcome] += 1

    feedback = rec.get("feedback")
    if not isinstance(feedback, list):
        errors.append("%s: feedback is not a list" % path.name)
        return
    if not feedback and rec.get("thread_class") == "copy_review":
        warnings.append("%s: no feedback entries on a copy_review record" % path.name)

    for i, fb in enumerate(feedback):
        where = "%s feedback[%d]" % (path.name, i)
        if not isinstance(fb, dict):
            errors.append("%s: not an object" % where)
            continue
        ftype = fb.get("type")
        target = fb.get("target")
        if ftype not in FEEDBACK_TYPES:
            errors.append("%s: type %r not in vocabulary" % (where, ftype))
        if target not in TARGETS:
            errors.append("%s: target %r not in vocabulary" % (where, target))
        stats["type"][ftype] += 1
        stats["target"][target] += 1
        if not (fb.get("text") or "").strip():
            errors.append("%s: empty text" % where)
        if not (fb.get("author") or "").strip():
            warnings.append("%s: no author" % where)
        # A rewrite must actually carry replacement copy.
        if ftype == "rewrite" and not (fb.get("rewrite_suggested") or "").strip():
            warnings.append("%s: type=rewrite but rewrite_suggested is empty" % where)
        stats["_fb_total"][0] += 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="structured", type=Path)
    args = ap.parse_args()

    files = sorted(args.dir.glob("rec_*.json"))
    if not files:
        print("error: no rec_*.json found in %s" % args.dir, file=sys.stderr)
        return 1

    errors: list = []
    warnings: list = []
    stats = {
        "type": Counter(), "target": Counter(), "copy_type": Counter(),
        "outcome": Counter(), "thread_class": Counter(), "_fb_total": [0],
    }

    for f in files:
        validate_file(f, errors, warnings, stats)

    print("=" * 60)
    print("VALIDATE STRUCTURED  (%d files, %d feedback entries)"
          % (len(files), stats["_fb_total"][0]))
    print("=" * 60)
    for key in ("thread_class", "type", "target", "copy_type", "outcome"):
        print("\n%s:" % key)
        for val, n in stats[key].most_common():
            print("  %-22s %d" % (val, n))

    if warnings:
        print("\n--- %d WARNING(S) ---" % len(warnings))
        for w in warnings[:40]:
            print("  " + w)
        if len(warnings) > 40:
            print("  ... and %d more" % (len(warnings) - 40))

    if errors:
        print("\n--- %d ERROR(S) ---" % len(errors))
        for e in errors[:60]:
            print("  " + e)
        if len(errors) > 60:
            print("  ... and %d more" % (len(errors) - 60))
        print("\nFAIL")
        return 1

    print("\nOK: every type/target/copy_type/outcome is in vocabulary.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
