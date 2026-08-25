# gtm_cafe

Turns the GTM Cafe `#copywriting-feedback` Slack channel into a Claude Code skill that
drafts and reviews GTM email copy the way that channel's senior reviewers would.

**Installed skill:** `~/.claude/skills/email-copywriting-gtm/` (personal scope — fires in
every project on this machine).

## Pipeline

```
Slack  --slackdump-->  export/  --build_threads-->   raw/thread_*.json
                               \-build_sessions-->  raw/days/*.md      <- classify from these
                                                          |
                                     records_{a,b,c}.py  (hand-classified)
                                                          |
                                    emit_structured -->  structured/rec_*.json
                                                          |
                                          build_kb -->  kb/threads/ + kb/patterns/
                                                          |
                              (hand-written synthesis)  kb/playbook.md + kb/glossary.md
                                                          |
                                        sync_skill -->  ~/.claude/skills/.../references/
```

## What's in the data

| | |
|---|---|
| Window | 2026-05-28 → 2026-08-22 (requested 05-24 → 08-24; free-plan ceiling did not bite) |
| Messages | 713 across 47 active days |
| Top-level posts | 209, of which 61 drew replies |
| Classified records | 58 — 41 copy reviews, 14 discussions, 3 banter |
| Feedback entries | 208 (91 critiques, 47 rewrites, 15 approvals) |
| Reviewers | Kellen (116 entries / 37 records), Ihor Seheda, Will Allred, ben - aperoadvisors.com, Youssef Hesham, Max Pidvalnyi, and 30+ others |

## The one non-obvious design decision

This channel does **not** keep review conversations inside Slack threads. A single review is
routinely split across one thread plus several separate top-level messages — reviewers reply
to the channel, not to the thread. Strict thread-grouping files those critiques as
contentless fragments and discards some of the best feedback in the channel
(see `raw/days/2026-08-07.md` for the clearest case).

So classification works from **day transcripts** (`raw/days/*.md`), not thread files.
`build_threads.py` is retained because well-formed threads are still useful and its
summary is a good integrity check, but it is not the classification input.

## Scripts

| Script | Does |
|---|---|
| `build_threads.py` | Export → one JSON per well-formed thread. De-dupes cross-day replies, resolves user IDs and inline mentions. |
| `build_sessions.py` | Export → chronological day transcripts, threads nested inline. **Classification input.** |
| `emit_structured.py` | `records_*.py` → `structured/rec_*.json`, resolving `source_ts` against the real export. |
| `validate_structured.py` | Enforces the fixed vocabularies. Exits non-zero on enum drift. |
| `build_kb.py` | `structured/` → `kb/threads/` + `kb/patterns/`. |
| `sync_skill.py` | `kb/` → the installed skill's `references/`. `--check` reports drift. |
| `config.env` | Channel ID, team ID, export window. Single source of truth. |
| `refresh.md` | The monthly re-run procedure. |

Rebuild everything from an existing export:

```bash
python scripts/build_threads.py && python scripts/build_sessions.py \
  && python scripts/emit_structured.py && python scripts/validate_structured.py \
  && python scripts/build_kb.py && python scripts/sync_skill.py
```

## Privacy

`export/`, `raw/` and `structured/` are gitignored — they hold other members' messages.
`kb/` and the shipped skill quote reviewers by their Slack display name where the quote is
the evidence for a rule. If you'd rather ship paraphrase-only, that's a change to
`build_kb.py` (patterns) plus a pass over `kb/playbook.md`.

## Known limits

- **Offer design is thin.** The source data is dense on line-level copy and sparse on what to
  actually offer. The skill will polish good copy on a weak offer without reliably telling
  you the offer is the problem. See `tests/skill_eval.md`.
- **One reviewer dominates.** Kellen wrote 56% of all feedback. `playbook.md` ranks by
  distinct reviewers and marks single-source rules as Tier 3 to stop his taste reading as
  community consensus — re-check that balance on every refresh.
- **Slack free-plan ceiling.** ~90 days of history maximum, so refreshes must run at least
  quarterly or history is lost permanently.
