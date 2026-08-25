#!/usr/bin/env python3
"""Copy the KB's synthesis files into the installed skill's references/.

kb/ is the source of truth; references/ is a copy. Run this after any refresh so
the skill reflects the current knowledge base. SKILL.md itself is never touched.

Usage: python scripts/sync_skill.py [--kb kb] [--skill <skill dir>] [--check]
"""
from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

DEFAULT_SKILL = Path.home() / ".claude" / "skills" / "email-copywriting-gtm"

# (source relative to kb/, destination filename in references/)
FILES = [
    ("playbook.md", "playbook.md"),
    ("glossary.md", "glossary.md"),
    ("patterns/subject_lines.md", "subject_lines.md"),
    ("patterns/openers.md", "openers.md"),
    ("patterns/cta.md", "cta.md"),
    ("patterns/tone_and_length.md", "tone_and_length.md"),
    ("patterns/personalization.md", "personalization.md"),
    ("patterns/body_and_offer.md", "body_and_offer.md"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", default=Path("kb"), type=Path)
    ap.add_argument("--skill", default=DEFAULT_SKILL, type=Path)
    ap.add_argument("--check", action="store_true",
                    help="report drift without copying (exit 1 if out of date)")
    args = ap.parse_args()

    refs = args.skill / "references"
    if not args.check:
        refs.mkdir(parents=True, exist_ok=True)

    missing, copied, same, stale = [], [], [], []
    for src_rel, dst_name in FILES:
        src = args.kb / src_rel
        dst = refs / dst_name
        if not src.exists():
            missing.append(str(src))
            continue
        if dst.exists() and filecmp.cmp(src, dst, shallow=False):
            same.append(dst_name)
            continue
        if args.check:
            stale.append(dst_name)
            continue
        shutil.copyfile(src, dst)
        copied.append(dst_name)

    print("=" * 60)
    print("SYNC SKILL %s" % ("(check only)" if args.check else ""))
    print("=" * 60)
    print("skill dir : %s" % args.skill)
    if copied:
        print("copied    : %s" % ", ".join(copied))
    if same:
        print("unchanged : %d file(s)" % len(same))
    if stale:
        print("OUT OF DATE: %s" % ", ".join(stale))
    if missing:
        print("MISSING   : %s" % ", ".join(missing))
        return 1
    if args.check and stale:
        return 1
    if not (args.skill / "SKILL.md").exists():
        print("\nNOTE: %s/SKILL.md does not exist yet." % args.skill)
    return 0


if __name__ == "__main__":
    sys.exit(main())
