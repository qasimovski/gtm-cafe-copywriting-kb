# Monthly refresh

Re-run this when you want the skill to reflect new `#copywriting-feedback` activity.
Roughly 15 minutes, most of which is the classification step.

All values live in `scripts/config.env` — update the window there, not inline.

---

## 0. Check auth (30 seconds)

```bash
C:/Users/qasim/bin/slackdump.exe workspace list
```

Expect `=> gtmcafe`. If it says "no authenticated workspaces", the session expired.
Re-auth **in a real terminal window** (PowerShell from the Start menu, not Claude Code —
slackdump refuses browser login in a non-interactive shell):

```
C:\Users\qasim\bin\slackdump.exe workspace new gtmcafe
```

Pass the bare name `gtmcafe`, not the full URL — passing a URL makes it save under a
sanitized name and then fail to select it.

## 1. Export the new window

Edit `TIME_FROM` / `TIME_TO` in `scripts/config.env` first. To extend rather than replace
history, set `TIME_FROM` to a few days before the last run's `TIME_TO`; the thread builder
de-duplicates by message timestamp, so overlap is safe.

```bash
cd /c/Users/qasim/gtm_cafe
C:/Users/qasim/bin/slackdump.exe export -o export/ -files=false -y \
  'C073STR74JV,2026-08-20T00:00:00,2026-11-20T23:59:59'
```

`-files=false` skips attachment downloads (we only need text). `-y` avoids an overwrite
prompt that would hang with no stdin.

**GTM Cafe is very likely on Slack's free plan**, which caps API history at ~90 days no
matter what window you request. Always confirm what you actually got in step 2 rather than
trusting the requested range.

## 2. Rebuild the raw layer

```bash
python scripts/build_threads.py     # raw/thread_*.json  (well-formed threads)
python scripts/build_sessions.py    # raw/days/*.md|json (full chronological transcripts)
```

Read the summary output. Check:
- `date range in export` — did the 90-day ceiling bite?
- `threads written` vs `dropped (no replies)`
- `dropped (orphan reply...)` — replies whose parent pre-dates the window

**Use `raw/days/*.md` for classification, not `raw/thread_*.json`.** In this channel a single
review conversation is routinely split across one Slack thread plus several separate
top-level messages; thread-only grouping loses much of the best feedback. The day
transcripts keep it intact.

## 3. Classify the new days

This is the manual step. Read the new `raw/days/*.md` files and append records to the
appropriate module in `scripts/records_{a,b,c}.py` (or start `records_d.py` and import it in
`scripts/emit_structured.py`).

Each record needs: `date`, `anchor` (whoever's top-level message the record is built from),
`thread_class`, `original_copy`, `feedback[]`, `outcome`. `source_ts` is resolved
automatically — don't hand-write it.

Vocabularies are fixed; the validator will reject anything outside them:

- `thread_class`: `copy_review` | `discussion` | `banter`
- `type`: `critique` | `approval` | `rewrite` | `question` | `general_comment`
- `target`: `subject_line` | `opening_line` | `body` | `cta` | `tone` | `length` |
  `personalization` | `overall`
- `copy_type`: `cold_email` | `follow_up` | `sequence` | `reply_handling` | `linkedin_dm` |
  `subject_line_only` | `landing_page` | `other` | `none`
- `outcome`: `revised` | `approved` | `abandoned` | `no_consensus` | `unresolved`

Rules that keep the data honest:
- Only populate `rewrite_suggested` when a reviewer actually wrote replacement copy.
- A reply making two distinct points becomes two feedback entries.
- Classify banter as `banter` — it is excluded from the KB automatically.

```bash
python scripts/emit_structured.py
python scripts/validate_structured.py    # must exit 0
```

## 4. Rebuild the KB and re-synthesise

```bash
python scripts/build_kb.py    # regenerates kb/threads/ and kb/patterns/
```

`kb/playbook.md` and `kb/glossary.md` are **hand-written synthesis** — `build_kb.py` does not
touch them. Re-read them against the new material and update:

- Has a Tier 3 (single-source) rule now been stated by other reviewers? Promote it.
- Has a new contradiction appeared? Add it to "Known contradictions" rather than picking a side.
- Rank by *distinct reviewers*, not mention count — one prolific reviewer would otherwise
  dominate. Check the current balance with:

```bash
python - <<'PY'
import json, glob
from collections import Counter, defaultdict
rev, recs = Counter(), defaultdict(set)
for f in glob.glob("structured/rec_*.json"):
    d = json.load(open(f, encoding="utf-8"))
    if d["thread_class"] == "banter": continue
    for fb in d["feedback"]:
        rev[fb["author"]] += 1; recs[fb["author"]].add(d["thread_id"])
for a, n in rev.most_common(12):
    print("%-24s %4d entries  %3d records" % (a, n, len(recs[a])))
PY
```

## 5. Push to the skill

```bash
python scripts/sync_skill.py
python scripts/sync_skill.py --check     # exits 0 when in sync
```

`SKILL.md` is never overwritten by the sync — edit it by hand if the rules themselves change.
Keep it under 500 lines.

## 6. Re-test

Re-run the six tasks in `tests/skill_eval.md` and check the outputs still hold up. If the
advice reads generic, that usually means the playbook has drifted toward summary and away
from the reviewers' actual words — put the quotes back.

---

## Notes

- `export/`, `raw/` and `structured/` are gitignored: they contain other members' messages.
  Keep them local.
- Automated Slack access can trip security alerts or notify workspace admins. This is a
  low-volume, read-only, personal-use export, but it is not invisible.
- If `build_threads.py` reports 0 threads, the export probably landed in an unexpected
  directory shape — check that `export/<channel-name>/YYYY-MM-DD.json` files exist. The
  channel folder is named by channel *name*, not ID.
