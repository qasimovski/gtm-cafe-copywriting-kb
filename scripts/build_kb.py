#!/usr/bin/env python3
"""Generate kb/threads/*.md and kb/patterns/*.md from structured/rec_*.json.

playbook.md and glossary.md are written by hand (synthesis), not generated here.

Usage: python scripts/build_kb.py [--src structured] [--out kb]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

# target -> pattern file. body and overall share a file: together they are the
# largest group and carry the offer/structure guidance.
PATTERN_FILES = {
    "subject_lines.md": (["subject_line"], "Subject lines"),
    "openers.md": (["opening_line"], "Opening lines"),
    "cta.md": (["cta"], "CTAs"),
    "tone_and_length.md": (["tone", "length"], "Tone and length"),
    "personalization.md": (["personalization"], "Personalization and targeting"),
    "body_and_offer.md": (["body", "overall"], "Body, offer and structure"),
}

# critique -> what not to do; approval -> what reviewers endorsed.
BUCKET = {
    "critique": "DON'T",
    "approval": "DO",
    "rewrite": "REWRITE",
    "general_comment": "PRINCIPLE",
    "question": "PRINCIPLE",
}


def esc(s: str) -> str:
    return (s or "").replace("\r", " ").strip()


def write_threads(records: list, out: Path) -> int:
    tdir = out / "threads"
    tdir.mkdir(parents=True, exist_ok=True)
    for old in tdir.glob("*.md"):
        old.unlink()
    n = 0
    for rec in records:
        if rec["thread_class"] == "banter":
            continue
        L = ["# %s" % rec["thread_id"], ""]
        L.append("- **Date:** %s" % rec["date"])
        L.append("- **Type:** %s" % rec["thread_class"])
        L.append("- **Outcome:** %s" % rec["outcome"])
        L.append("- **Posted by:** %s" % rec["anchor"])
        L.append("- **Source:** `%s` (%d messages)" %
                 (rec["source_day_file"], len(rec["source_ts"])))
        L.append("")
        copy = rec["original_copy"]
        if esc(copy.get("text")):
            L += ["## Copy under review", "",
                  "**%s** - `%s`" % (copy.get("author") or "unknown", copy.get("copy_type")),
                  "", "> " + esc(copy["text"]).replace("\n", "\n> "), ""]
        if rec.get("notes"):
            L += ["## Why this thread matters", "", esc(rec["notes"]), ""]
        if rec["feedback"]:
            L += ["## Feedback", ""]
            for fb in rec["feedback"]:
                L.append("### %s - %s / %s" % (fb["author"], fb["type"], fb["target"]))
                L.append("")
                L.append(esc(fb["text"]))
                L.append("")
                if esc(fb.get("rewrite_suggested")):
                    L += ["Suggested replacement:", "",
                          "```", esc(fb["rewrite_suggested"]), "```", ""]
        (tdir / ("%s.md" % rec["thread_id"])).write_text("\n".join(L), encoding="utf-8")
        n += 1
    return n


def write_patterns(records: list, out: Path) -> int:
    pdir = out / "patterns"
    pdir.mkdir(parents=True, exist_ok=True)
    for old in pdir.glob("*.md"):
        old.unlink()

    by_target = defaultdict(list)
    for rec in records:
        if rec["thread_class"] == "banter":
            continue
        for fb in rec["feedback"]:
            by_target[fb["target"]].append((rec, fb))

    for fname, (targets, title) in PATTERN_FILES.items():
        items = []
        for t in targets:
            items.extend(by_target.get(t, []))
        # Group by bucket, then by reviewer volume so the most-cited voices lead.
        buckets = defaultdict(list)
        for rec, fb in items:
            buckets[BUCKET[fb["type"]]].append((rec, fb))

        reviewers = defaultdict(int)
        for rec, fb in items:
            reviewers[fb["author"]] += 1

        L = ["# %s" % title, ""]
        L.append("Aggregated from #copywriting-feedback, 2026-05-28 to 2026-08-22. "
                 "Every line cites the record it came from; open `kb/threads/<id>.md` for full context.")
        L.append("")
        L.append("**%d observations from %d reviewers.** Most active here: %s."
                 % (len(items), len(reviewers),
                    ", ".join("%s (%d)" % (a, n)
                              for a, n in sorted(reviewers.items(), key=lambda x: -x[1])[:5])))
        L.append("")
        for bucket in ("DON'T", "DO", "REWRITE", "PRINCIPLE"):
            rows = buckets.get(bucket) or []
            if not rows:
                continue
            heading = {
                "DON'T": "What reviewers flag",
                "DO": "What reviewers endorse",
                "REWRITE": "Rewrites they actually wrote",
                "PRINCIPLE": "Stated principles",
            }[bucket]
            L += ["## %s" % heading, ""]
            for rec, fb in rows:
                L.append("- **%s:** %s  `[%s]`" % (fb["author"], esc(fb["text"]), rec["thread_id"]))
                if esc(fb.get("rewrite_suggested")):
                    L.append("")
                    L.append("  ```")
                    for line in esc(fb["rewrite_suggested"]).split("\n"):
                        L.append("  " + line)
                    L.append("  ```")
                    L.append("")
            L.append("")
        (pdir / fname).write_text("\n".join(L), encoding="utf-8")
    return len(PATTERN_FILES)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=Path("structured"), type=Path)
    ap.add_argument("--out", default=Path("kb"), type=Path)
    args = ap.parse_args()

    files = sorted(args.src.glob("rec_*.json"))
    if not files:
        print("error: no records in %s" % args.src, file=sys.stderr)
        return 1
    records = [json.loads(f.read_text(encoding="utf-8")) for f in files]
    records.sort(key=lambda r: (r["date"], r["thread_id"]))

    n_threads = write_threads(records, args.out)
    n_patterns = write_patterns(records, args.out)

    print("=" * 60)
    print("BUILD KB")
    print("=" * 60)
    print("thread files   : %d -> %s/threads/" % (n_threads, args.out))
    print("pattern files  : %d -> %s/patterns/" % (n_patterns, args.out))
    print("(playbook.md and glossary.md are hand-written, not generated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
