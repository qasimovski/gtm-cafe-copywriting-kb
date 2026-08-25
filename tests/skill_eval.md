# Skill evaluation — 6 drafting tasks

Run against `~/.claude/skills/email-copywriting-gtm` after Phase 5 install.
Each task: the input, the skill's output, and an honest verdict against what a
strong reviewer in `#copywriting-feedback` would actually say.

---

## Task 1 — Full cold email from a brief
**Brief:** Terrapinn selling exhibition space at an EV charging infrastructure event to
Charge Point Operators.

**Output:**

```
Subject: site pipeline

{{first_name}}, most CPOs are still chasing site-host deals one landlord at a time.

That gets harder as the network scales - the good sites go to whoever got there first.

{{event_name}} puts {{host_count}} site hosts and property owners in one room in {{month}}.

Would it be useful to see which of them are already shortlisting charge point partners?
```

62 words. Subject two lowercase words. Signal-based opener. Mechanism explicit. Reply-ask CTA.

**Verdict: PASS.** Notable: the first attempt invented "180 site hosts". The pre-flight
checklist's "never invent performance numbers" rule caught it and forced `{{host_count}}`.
The rule earned its place.

---

## Task 2 — Subject line rewrite
**Input:** `Quick question about your Q3 roadmap and how we might be able to help`

**Output:** `q3 roadmap` — with `roadmap q` and `q3 gap` as split-test variants.

Reasoning applied: 1–3 lowercase words `[subject_lines.md]`; strip the "quick question"
hedge; "and how we might be able to help" is we-focused and gives away the pitch, which
Youssef Hesham flagged as costing opens.

**Verdict: PASS.** Matches the observed house pattern (`case flow`, `cart leak`, `intern q`).

---

## Task 3 — Weak CTA
**Input:** `Worth a quick 15-minute call to explore synergies?`

**Output:**
```
Would it be useful to see the {{artifact}} we put together for {{company}}?
```
Variants: `Can I send the {{artifact}}?` / `Open to seeing what we'd test first?`

Three failures named: it's a meeting-ask not a reply-ask (rule 3); "quick" is a hedge that
adds nothing; "explore synergies" is vendor-speak carrying no concrete artifact.

**Verdict: PASS.** This is the channel's single most mechanical fix and the skill applied it
cleanly.

---

## Task 4 — Compress a too-long body
**Input:** The 4-step D2C audit sequence from `rec_20260709_saad_ahmad` — stacked stats
(30-40% revenue, 25-35% checkout drop-off), two named case studies, a bulleted audit
contents list, competitor-shaming final step.

**Output:**
```
Subject: checkout leak

{{first_name}}, I went through {{company}}'s checkout as a customer last week.

Two things in the flow are where most first-time buyers quietly drop off.

I wrote up what I found - where the leaks are and which are 2-week fixes.

Want me to send it over?
```

51 words, down from ~320. One tension (checkout friction) instead of four. Stats dropped —
they were doing the persuading, which rule 6 flags. The customer-side observation survives
because it is a real signal.

**Verdict: PASS.** Correctly identified that the strongest asset was "I went through your
store as a customer" — buried in the original — and led with it. That mirrors Youssef
Hesham's ideal in `rec_20260712_varun_y` (run the product against the prospect, lead with
what you found).

---

## Task 5 — Over-personalised opener
**Input:** `Hi Sarah, I saw on LinkedIn that you've been at Siemens for 7 years, that you
studied at TU Munich, and that you recently posted about grid resilience — really
impressive career!`

**Output:**
```
Seven years on the grid side at Siemens, you've probably watched interconnection queues
go from an annoyance to a structural problem, Sarah.
```

Applied *presumed personalization* `[playbook 13]`: the tenure fact is folded into the
argument rather than announced. Three stacked facts cut to one. "Really impressive career"
removed as fake warmth (rule 8).

**Verdict: PASS.** Exactly the transformation Kellen praised in `rec_20260616_kyle_nelson`.

---

## Task 6 — Event invite sequence
**Brief:** Invite senior rail operators to a Terrapinn conference; 40 delegate places left.

**Output:**
```
Email 1
Subject: berlin in march

{{first_name}}, are you going to be in Berlin for {{event_name}} in March?

{{peer_name}} and {{peer_name_2}} are both speaking - we know them well and can make an intro.

We've got 40ish places left and thought you'd be one of the right people to invite.

Wanted to check before offering them elsewhere.

Email 2 (bump, same thread)
{{first_name}}, what did you think here?

Happy to hold one of the remaining places while you decide.
```

Applied *sincere scarcity* `[playbook 15]`: the real 40-place constraint stated plainly
rather than engineered into FOMO. Them-centric opener ("are you going to be in Berlin")
instead of "join us", per Kellen's fix in `rec_20260722_ivan`. Two steps, not three, per
Mikulas on diminishing returns.

**Verdict: PASS with one gap found.** The output is right, but the skill had to reach into a
*thread* file to get the follow-up guidance — the playbook had no standalone section on
sequences or bumps, despite 7 sequence records in the data. **Fixed:** added a "Sequences
and follow-ups" section to `playbook.md`. This is the one genuine deficiency the eval surfaced.

---

## Summary

| Task | Verdict |
|---|---|
| 1. Full cold email | PASS |
| 2. Subject line rewrite | PASS |
| 3. Weak CTA | PASS |
| 4. Compress long body | PASS |
| 5. Over-personalised opener | PASS |
| 6. Event invite sequence | PASS — playbook gap found and fixed |

**Playbook change made as a result:** added the sequences/follow-ups section (Tier 2).

**Where the skill is genuinely strong:** mechanical fixes (subject lines, CTAs, compression,
personalization framing) are near-deterministic because the source data is dense and
consistent on them.

**Where it stays weak, honestly:** offer *design* — what to actually offer a prospect — is
thin in the source data and the skill can only gesture at it (`lead with a lead magnet or
give away`). Threads like `rec_20260814_eddy_okun` show the channel itself struggling here.
The skill will give good line-level copy on a weak offer without reliably telling you the
offer is the problem.
