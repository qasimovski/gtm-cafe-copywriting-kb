"""Classified records, part B: 2026-07-01 .. 2026-07-22."""

RECORDS = [
    {
        "date": "2026-07-01", "anchor": "MattyIce", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "MattyIce", "type": "general_comment", "target": "personalization",
             "text": "An AE got a CRO from an AI lab responding after taking a picture of their subway ad and sending it over "
                     "with 'haha what a sweet ad, saw this on the way home you guys are crushing it'. Sometimes it's just not that deep."},
            {"author": "Selim Adi.", "type": "general_comment", "target": "personalization",
             "text": "A top-performing AE used to take a photo of corporate offices selfie-style, send a DM about being in "
                     "the area and ask to chat; it really is that simple."},
        ],
        "outcome": "unresolved",
        "notes": "Counterweight to heavy-machinery personalization: a real, low-effort observation can outperform.",
    },
    {
        "date": "2026-07-01", "anchor": "Malak", "thread_class": "copy_review",
        "original_copy": {
            "author": "Malak", "copy_type": "sequence",
            "text": "Winery corporate-gifting campaign to real estate agencies. Email 1 asks to confirm the office address "
                    "in order to send a complimentary wine gift box; follow-up adds personalized note and logo mockup.",
        },
        "feedback": [
            {"author": "ben - aperoadvisors.com", "type": "approval", "target": "overall",
             "text": "This copy seems pretty good to me. Are we sure we shouldn't be blaming infra? Like 9/10 times we "
                     "shouldn't be. But this seems like it would rip. Targeting possibly an issue."},
            {"author": "Kellen", "type": "critique", "target": "opening_line",
             "text": "I would open w the offer first sentence maybe, but agree if this isn't getting volume, infra or list "
                     "likely issue. Or they just don't want it."},
            {"author": "ben - aperoadvisors.com", "type": "general_comment", "target": "overall",
             "text": "we spend too much time writing and not enough time sending. ^^ put it on a poster"},
        ],
        "outcome": "approved",
        "notes": "Key diagnostic habit: before rewriting, ask whether the problem is infra, list or targeting rather than copy.",
    },
    {
        "date": "2026-07-02", "anchor": "Safouan", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Safouan", "type": "general_comment", "target": "overall",
             "text": "when in doubt, send more emails"},
        ],
        "outcome": "unresolved",
    },
    {
        "date": "2026-07-03", "anchor": "Matt Sezgin", "thread_class": "copy_review",
        "original_copy": {
            "author": "Matt Sezgin", "copy_type": "cold_email",
            "text": "CX agency to Shopify stores hiring a CX rep. Opens on the job posting, stacks ramp/PTO/management "
                    "objections, then 100+ brands and most-reviewed Gorgias partner proof, pay-per-resolved-ticket, "
                    "'Worth a chat?' and a PS offering a box of snacks.",
        },
        "feedback": [
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Compressed to four lines: hiring signal, the operational tension, the mechanism, and a comparison CTA.",
             "rewrite_suggested": "Saw you're hiring for CX coverage tied to {{jd_one_liner}}, {first_name}. / That might mean volume is rising faster than training, weekends, and PTO can comfortably absorb. / We support DTC teams with Canada and US-based reps, paid only per resolved ticket. / Would it help to compare that path against hiring inside {{company}}?"},
            {"author": "Kellen", "type": "critique", "target": "length",
             "text": "The original is too long for a cold email and stacks too many claims, which increases cognitive load."},
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "The strongest idea is not 'you only pay per ticket'. It is the operational tension of needing reliable "
                     "CX coverage without ramp time, idle cost, or management burden."},
            {"author": "Kellen", "type": "critique", "target": "body",
             "text": "I'd cut the snack P.S. It risks making the reply feel transactional and distracts from the business problem."},
            {"author": "Kellen", "type": "critique", "target": "body",
             "text": "The proof line should be simpler. '100+ brands' and 'most-reviewed Gorgias CX partner' are useful, but "
                     "together they feel pitch-heavy. Lead with the mechanism first, then use proof in follow-up."},
            {"author": "Kellen", "type": "critique", "target": "cta",
             "text": "'Worth a chat?' is easy, but generic. A stronger soft ask should open a specific loop, like comparing "
                     "outsourced resolved-ticket coverage against the planned hire."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-07-03", "anchor": "Jules", "thread_class": "copy_review",
        "original_copy": {
            "author": "Jules", "copy_type": "linkedin_dm",
            "text": "Two DM variants for a payments company: failed payments / auth rates, name-dropping ElevenLabs, "
                    "Replit and Kalshi.",
        },
        "feedback": [
            {"author": "Jules", "type": "critique", "target": "overall",
             "text": "Self-critique: 'I know Variant 2 is very we focused so I'm figuring out how to make it more abt the lead.'"},
        ],
        "outcome": "unresolved",
        "notes": "No senior review landed. Kept because the author's self-diagnosis matches the channel's dominant critique.",
    },
    {
        "date": "2026-07-04", "anchor": "Ali Qureshi", "thread_class": "copy_review",
        "original_copy": {
            "author": "Ali Qureshi", "copy_type": "cold_email",
            "text": "Revised email 1 after the 06-29 teardown: leads with a hiring signal, drops the guarantee, "
                    "softer 'Ok if I share our strategy?' CTA and a 'quick yes works' PS.",
        },
        "feedback": [],
        "outcome": "unresolved",
        "notes": "No reviewer replied, but the revision itself shows which of Kellen's 06-29 points were adopted: "
                 "guarantee removed, CTA softened from a meeting ask to a reply ask.",
    },
    {
        "date": "2026-07-06", "anchor": "Abhi at GTMcafe", "thread_class": "copy_review",
        "original_copy": {
            "author": "Abhi at GTMcafe", "copy_type": "linkedin_dm",
            "text": "InMail copy (original message later deleted) for a YouTube/video engine offer; follow-up version "
                    "opens '6k searches for \"data platform\" happen every month, Saad.'",
        },
        "feedback": [
            {"author": "Will Allred", "type": "critique", "target": "overall",
             "text": "Feels solid. But initial objections in my head are: What is the service? Do I believe you on time needed?"},
            {"author": "Kellen", "type": "rewrite", "target": "opening_line",
             "text": "Open on the search-volume number rather than the service.",
             "rewrite_suggested": "6k searches for 'xyz' happen every month, name"},
            {"author": "Kellen", "type": "rewrite", "target": "body",
             "text": "Suggested an exclusivity/scarcity play available to an agency (not a SaaS).",
             "rewrite_suggested": "I can only work with 1 company in the {industry space}, wanted to connect with you before {competitor name}"},
            {"author": "Kellen", "type": "general_comment", "target": "cta",
             "text": "even better if the proposal is the finish line vs the reply"},
            {"author": "Will Allred", "type": "rewrite", "target": "body",
             "text": "Reference their own existing content as the raw material for the offer.",
             "rewrite_suggested": "Your blog 'xyz' would make a killer video resource. Have you thought about doing this for articles like that and '123'?"},
        ],
        "outcome": "revised",
        "notes": "Author reported the reworked version booked a meeting.",
    },
    {
        "date": "2026-07-08", "anchor": "Sharad", "thread_class": "copy_review",
        "original_copy": {
            "author": "Sharad", "copy_type": "cold_email",
            "text": "Multi-branch receptionist AI email: 'somewhere across your 7 branches sits your best receptionist... "
                    "she only works 8 hours a day', a 27-branch cloning proof point, and 'Open to throw your hardest "
                    "questions at her?'",
        },
        "feedback": [
            {"author": "Ihor Seheda", "type": "rewrite", "target": "overall",
             "text": "Tightened the opener and made the scaling problem explicit.",
             "rewrite_suggested": "Adam, across your branches there's usually one receptionist who handles calls better than the rest. The problem is that quality doesn't scale with her. / {Existing Customer Name} cloned their best one into all 27 branches, while keeping each branch's routing, language, and accent rules intact, and gave HQ full visibility across locations. / We put together one for {Company Name} using just your website. / Open to throwing your hardest questions at her?"},
            {"author": "Kellen", "type": "critique", "target": "length",
             "text": "I like this more. I'd also maybe even try to shorten - break up first 2 sentences into own paragraph and "
                     "make line 3, which I love, shorter. And cta I would do one sentence only too."},
            {"author": "Kellen", "type": "general_comment", "target": "length",
             "text": "I'm brevity pilled, not as much as Will Allred, but their extensive data says brevity wins."},
            {"author": "Will Allred", "type": "critique", "target": "length",
             "text": "Pilled by data, but outliers still thrive. Lavender data shows you can write a long email that gets good "
                     "reply rates. You just need to balance the length variable with clarity and formality variables - so you "
                     "write super casually with hella choppy sentences."},
            {"author": "Will Allred", "type": "general_comment", "target": "body",
             "text": "Big fan of going long on BAR (Background, Action, Results - an old interviewing framework). Combine their "
                     "work history + company stage + a couple triggers and create a look-alike customer story, going in depth "
                     "on what they saw and exactly how you helped. Odds are they won't reply, but it creates really good meat "
                     "to do shorter emails around in thread."},
            {"author": "Will Allred", "type": "critique", "target": "length",
             "text": "On the long variant: 1. Longer. More detail. Step by step what happened. 2. Richer personalization - "
                     "going longer means you gotta earn the attention. 3. Shorter sentences."},
            {"author": "Sharad", "type": "general_comment", "target": "length",
             "text": "In my career there have only been a couple of times where I've made long-form cold emails work, around "
                     "100-120 words. The first line has to be a strong hook that keeps their curiosity until the end. "
                     "The more words you use, the stronger your copywriting needs to be."},
        ],
        "outcome": "revised",
        "notes": "The channel's central length disagreement, stated explicitly by both camps. Not a settled rule.",
    },
    {
        "date": "2026-07-09", "anchor": "Saad Ahmad", "thread_class": "copy_review",
        "original_copy": {
            "author": "Saad Ahmad", "copy_type": "sequence",
            "text": "Four-step D2C audit sequence with heavy stats (30-40% revenue, 25-35% checkout drop-off), two named "
                    "case studies, a bulleted audit contents list, and a competitor-shaming final follow-up.",
        },
        "feedback": [],
        "outcome": "unresolved",
        "notes": "Posted without reply. Retained as an example of the claim-stacking pattern reviewers consistently flag elsewhere.",
    },
    {
        "date": "2026-07-09", "anchor": "Austin Jouett", "thread_class": "copy_review",
        "original_copy": {
            "author": "Austin Jouett", "copy_type": "sequence",
            "text": "Three-email MSP partnership sequence to resell pentesting. Subject 'your white label pentest vendor'; "
                    "long educational body on auditors, manual validation vs scanner reports, ending with a CEO intro ask.",
        },
        "feedback": [
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Cut to a question opener, the single scanner-report insight, an opt-out line, and a checklist offer "
                     "instead of a meeting.",
             "rewrite_suggested": "Are the new standards for a 'pen test' something you've seen, {name}? / A Scanner report + logo used to pass - not anymore. / If you love your current setup - lmk and I'll remove you. / Otherwise I can share the renewal checklist we're using w/ our customers, to make sure these new standards don't cause a 'fail'."},
            {"author": "Kellen", "type": "critique", "target": "length",
             "text": "Shorter, and have 1-C splits (author's summary of the verbal feedback)."},
        ],
        "outcome": "revised",
        "notes": "Author restructured into three splits: educational+rapport, educational+direct, direct.",
    },
    {
        "date": "2026-07-10", "anchor": "Mikulas", "thread_class": "copy_review",
        "original_copy": {
            "author": "Mikulas", "copy_type": "sequence",
            "text": "Podcast-guest invitation, three step-1 variants plus a step-2 bump. Variants use SL "
                    "'{{firstName}} <> Podcast', 'is this your thing?', and a longer version with a SOC 2 joke and "
                    "'no fee' reassurance.",
        },
        "feedback": [
            {"author": "Youssef Hesham", "type": "critique", "target": "overall",
             "text": "1-A is your best bet. 1-B is full of fluff. 1-C 'as a thank you' should be your PS line. Step 2 is cool."},
            {"author": "Adnan Manna", "type": "critique", "target": "body",
             "text": "Why should they attend? Share some social proof too - your social media reach, audience size, number of "
                     "plays each episode gets. They need to get something out of it."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Three versions built on audience demand, guest fit, and low friction.",
             "rewrite_suggested": "Subject: 3 questions for {{firstName}} / There are three questions the audience at {{cybershow}} would love your take on. / They are around building {{companyName}}, what changed your thinking, and where cyber leaders still get it wrong. / Open to seeing them?"},
            {"author": "Kellen", "type": "approval", "target": "body",
             "text": "agree on social proof too - either volume or quality of audience. make it feel epic and special. niche."},
            {"author": "Kellen", "type": "general_comment", "target": "tone",
             "text": "I think of it as 'inject dopamine' - like chemically alter the person they are by the time they realize "
                     "they're reading your cold email."},
            {"author": "Kellen", "type": "critique", "target": "personalization",
             "text": "On scraping their previous podcast appearances to open with: you could, but imo easy to mess up w AI."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-07-12", "anchor": "Varun Y", "thread_class": "copy_review",
        "original_copy": {
            "author": "Varun Y", "copy_type": "cold_email",
            "text": "QA automation tool to Tech Leads/CTOs/EMs. Subject 'How are you currently handling QA before releases?', "
                    "'Most teams we talk to deal with the same challenge', a plain-English test pitch, a 2-minute demo link, "
                    "'Worth a quick chat?'",
        },
        "feedback": [
            {"author": "Adnan Manna", "type": "critique", "target": "opening_line",
             "text": "'Most teams...' pass. Statements of fact and assumptions don't get replies. See their product's change "
                     "logs, subreddits complaining about a recent update that broke something, and use that for a first line."},
            {"author": "Adnan Manna", "type": "critique", "target": "body",
             "text": "The pitch doesn't answer the 'what if the tool breaks something' question. Also shorten it. Plus mention "
                     "the benefit. Sell the destination, not the vehicle. Unless the vehicle is a Rolls Royce."},
            {"author": "Adnan Manna", "type": "rewrite", "target": "cta",
             "text": "Make the CTA about their specific product.",
             "rewrite_suggested": "Would you like to see how it would work for 'their product'?"},
            {"author": "Youssef Hesham", "type": "critique", "target": "subject_line",
             "text": "'How are you currently handling QA before releases?' is too long and giving away too much and will end "
                     "up getting so little opens."},
            {"author": "Youssef Hesham", "type": "critique", "target": "personalization",
             "text": "Do a better job on your account discovery & qualification to personalize vs throwing 'Most teams deal "
                     "with X' - they might not be, and will just skip it if that's the case. Avoid shooting blind darts."},
            {"author": "Youssef Hesham", "type": "critique", "target": "body",
             "text": "'We help your engineers do xyz without 123' is a better way to pitch this. Also avoid redundancy on "
                     "startup name."},
            {"author": "Youssef Hesham", "type": "critique", "target": "cta",
             "text": "Have a better offer for them - ideally something they would steal from you if they had access to your "
                     "platform, vs something that is publicly available already."},
            {"author": "Youssef Hesham", "type": "rewrite", "target": "overall",
             "text": "Ideal version: run the product against the prospect first and lead with the actual bug found.",
             "rewrite_suggested": "Subject: bug on {{Company}} / I pointed our agent at {{company_name}}'s signup flow yesterday. Setup was one sentence of plain English, we never wrote a script. It caught your coupon field erroring on mobile Safari. / Looks like you shipped 11 releases last month (I counted the changelog). That's normally 11 rounds of fixing broken test scripts. The agent just re-ran itself each time. / Happy to send the checkout and onboarding replays too. You don't have to get on a call for them."},
            {"author": "Youssef Hesham", "type": "rewrite", "target": "overall",
             "text": "Fallback if that can't be automated across the whole TAM: hiring-signal opener with an 'or am I off' close.",
             "rewrite_suggested": "Subject: question / {{first_name}}, saw the QA engineer role on your careers/LinkedIn page + noticed you're also shipping weekly, so I'm guessing test scripts are breaking faster than one person can patch them. / That's the thing we work on. Your engineers describe a test in plain English and the agent runs the whole flow itself, recording video and logs as it goes. / Is script upkeep actually the bottleneck for you, or am I off?"},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-07-14", "anchor": "Matt Sezgin", "thread_class": "copy_review",
        "original_copy": {
            "author": "Matt Sezgin", "copy_type": "cold_email",
            "text": "Voice AI for Shopify stores. Opens on their help desk, abandoned checkout math, human+AI calling "
                    "mechanism, a $54K in 5 weeks case study, exclusive pilot with first week covered, 'Worth a chat?' "
                    "plus a snack PS.",
        },
        "feedback": [
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Trimmed to five short lines with the help desk in the subject.",
             "rewrite_suggested": "Subject: abandoned checkouts at {{company_name}} / {{first_name}}, looks like you're running support on {{help_desk}}. / Even with Email and SMS flows, abandoned checkouts still leave revenue behind. / We combine human recovery calls with an AI voice agent connected to Shopify and {{help_desk}}. / {{customer_name}} added $54K in five weeks doing this. / We'll cover your first week. Worth a chat?"},
            {"author": "Will Allred", "type": "rewrite", "target": "overall",
             "text": "Alternative three-email sequence with A/B/C subject tests, a bump that pre-empts cherry-picking "
                     "skepticism, and a final email that names the likely objection.",
             "rewrite_suggested": "Subj A: {{help_desk}} Abandon Carts / Subj B: Abandon Cart Idea / Subj C: Abandon Cart Opp -- {{first_name}}, pretty sure {{help_desk}} just gives you email + SMS flows for abandoned carts. / Think adding calls to the mix could help? / {{customer_name}} added $54K in five weeks doing this. Works w their Shopify & {{help_desk}} set up. || Email 2 BUMP: {{first_name}}, what did you think here? Realize {{customer_name}}'s $54K in 5 weeks might seem like seller cherry picking. If we cover the 1st week to let you test it, think its worth a look? || Email 3: {{first_name}}, last note from me. Seems like calling your abandon carts might not be interesting? ... Offer to test for a week stands. Just let me know if you're opposed to the concept or if there's a better time to follow up."},
        ],
        "outcome": "revised",
        "notes": "Rare side-by-side of both senior reviewers rewriting the same copy: Kellen compresses to one email, "
                 "Will Allred spreads the claims across a three-step thread.",
    },
    {
        "date": "2026-07-15", "anchor": "John Oz", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Preeti", "type": "general_comment", "target": "cta",
             "text": "I call them and say hey you replied to my email, then ask two questions: how do they currently acquire "
                     "customers, and what are their current challenges with acquisition. That usually leads to them sharing "
                     "what's going on, then I ask for 15-20 mins tomorrow and walk them through the system."},
        ],
        "outcome": "unresolved",
    },
    {
        "date": "2026-07-22", "anchor": "Ivan", "thread_class": "copy_review",
        "original_copy": {
            "author": "Ivan", "copy_type": "sequence",
            "text": "Event invite sequence for a casino games company, using a shared-industry connection where possible "
                    "and a fallback with no mention. Email 2 leaned on FOMO; email 3 offered an intro.",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "opening_line",
             "text": "Line 1 email 1 could be clearer - it is an open loop and warrants asking for what? You answer it line 2, "
                     "but line 1 needs to make sense stand alone to get them to keep going."},
            {"author": "Kellen", "type": "approval", "target": "tone",
             "text": "Overall I like the tone // weight of it - feels human."},
            {"author": "Kellen", "type": "critique", "target": "opening_line",
             "text": "'Joining us' is hurting you // makes it more about you imo vs 'are you planning to be in xyz?' which is "
                     "fully them centric.",
             "rewrite_suggested": "are you going to be at the xyz in location this weekend, name?"},
            {"author": "barash", "type": "critique", "target": "tone",
             "text": "On email #2 feels a bit too forced of a FOMO in my opinion. I'm reading it and it's rubbing me the wrong way."},
            {"author": "barash", "type": "approval", "target": "body",
             "text": "I like the happy to intro you on email #3."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Rewrote as a plain question plus an honest capacity statement.",
             "rewrite_suggested": "Hey are you gonna be at x? / So and such will be there - we know them well - can make an intro. / The room's small to keep things xyz. / Wanted to check beforehand to make sure everyone gets the most"},
            {"author": "barash", "type": "rewrite", "target": "body",
             "text": "Added the real ticket count as sincere scarcity rather than manufactured FOMO.",
             "rewrite_suggested": "Have 40ish tickets left and thought you'd be one of the right people we should invite / Wanted to check beforehand instead of giving it to someone else"},
            {"author": "Kellen", "type": "general_comment", "target": "tone",
             "text": "Sincere scarcity is great. If there's a legitimate limitation you're not baiting, it's just honest. "
                     "People try to force the 'ooooh look at me this is a special thing' and thus the recipient tries to find "
                     "the hole. Being direct and clear, there's no gap."},
            {"author": "Kellen", "type": "general_comment", "target": "length",
             "text": "You may write it longer to give deeper explanation if you think you need to. If they understand why "
                     "you're targeting them, and why you're offering what you are (aka how you benefit too), it'll land fine."},
        ],
        "outcome": "revised",
        "notes": "Best example of the 'sincere scarcity' rule: state the real constraint plainly instead of engineering FOMO.",
    },
    {
        "date": "2026-07-22", "anchor": "Mikulas", "thread_class": "copy_review",
        "original_copy": {
            "author": "Mikulas", "copy_type": "cold_email",
            "text": "Med spa Google-reviews offer whose mechanism is a personalized photo of the owner holding a whiteboard "
                    "with the client's name. Variant 1 SL 'photo reviews'; variant 2 SL '{{rival_name}} reviews' with a "
                    "competitor review-count comparison and a free-for-first-3 offer.",
        },
        "feedback": [
            {"author": "barash", "type": "critique", "target": "overall",
             "text": "The image of myself would probably creep me out. I like the personalization but is it doing anything? "
                     "On their offer itself it makes sense."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Reframed as a permission-to-send-strategy ask with the competitor comparison as the proof.",
             "rewrite_suggested": "name - can i send you the strategy we've used to help x other medspa owners to outcome? / competitor in city has x reviews vs your y count / Within z months, you could xyz. / Lmk if i can send a sample + the psychology of why it never fails?"},
            {"author": "Kellen", "type": "question", "target": "overall",
             "text": "why do scaled email vs like walking in to local ones first"},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Suggested a give-away framing when there are no case studies yet.",
             "rewrite_suggested": "name can i give you a 10,000 service for free so i can sell it to the next 500 med spa owners outside your customer range?"},
        ],
        "outcome": "revised",
        "notes": "Author admitted having no case studies yet; Kellen's answer was to trade the work for the proof.",
    },
]
