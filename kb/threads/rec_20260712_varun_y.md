# rec_20260712_varun_y

- **Date:** 2026-07-12
- **Type:** copy_review
- **Outcome:** revised
- **Posted by:** Varun Y
- **Source:** `raw/days/2026-07-12.md` (7 messages)

## Copy under review

**Varun Y** - `cold_email`

> QA automation tool to Tech Leads/CTOs/EMs. Subject 'How are you currently handling QA before releases?', 'Most teams we talk to deal with the same challenge', a plain-English test pitch, a 2-minute demo link, 'Worth a quick chat?'

## Feedback

### Adnan Manna - critique / opening_line

'Most teams...' pass. Statements of fact and assumptions don't get replies. See their product's change logs, subreddits complaining about a recent update that broke something, and use that for a first line.

### Adnan Manna - critique / body

The pitch doesn't answer the 'what if the tool breaks something' question. Also shorten it. Plus mention the benefit. Sell the destination, not the vehicle. Unless the vehicle is a Rolls Royce.

### Adnan Manna - rewrite / cta

Make the CTA about their specific product.

Suggested replacement:

```
Would you like to see how it would work for 'their product'?
```

### Youssef Hesham - critique / subject_line

'How are you currently handling QA before releases?' is too long and giving away too much and will end up getting so little opens.

### Youssef Hesham - critique / personalization

Do a better job on your account discovery & qualification to personalize vs throwing 'Most teams deal with X' - they might not be, and will just skip it if that's the case. Avoid shooting blind darts.

### Youssef Hesham - critique / body

'We help your engineers do xyz without 123' is a better way to pitch this. Also avoid redundancy on startup name.

### Youssef Hesham - critique / cta

Have a better offer for them - ideally something they would steal from you if they had access to your platform, vs something that is publicly available already.

### Youssef Hesham - rewrite / overall

Ideal version: run the product against the prospect first and lead with the actual bug found.

Suggested replacement:

```
Subject: bug on {{Company}} / I pointed our agent at {{company_name}}'s signup flow yesterday. Setup was one sentence of plain English, we never wrote a script. It caught your coupon field erroring on mobile Safari. / Looks like you shipped 11 releases last month (I counted the changelog). That's normally 11 rounds of fixing broken test scripts. The agent just re-ran itself each time. / Happy to send the checkout and onboarding replays too. You don't have to get on a call for them.
```

### Youssef Hesham - rewrite / overall

Fallback if that can't be automated across the whole TAM: hiring-signal opener with an 'or am I off' close.

Suggested replacement:

```
Subject: question / {{first_name}}, saw the QA engineer role on your careers/LinkedIn page + noticed you're also shipping weekly, so I'm guessing test scripts are breaking faster than one person can patch them. / That's the thing we work on. Your engineers describe a test in plain English and the agent runs the whole flow itself, recording video and logs as it goes. / Is script upkeep actually the bottleneck for you, or am I off?
```
