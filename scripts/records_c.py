"""Classified records, part C: 2026-07-28 .. 2026-08-22."""

RECORDS = [
    {
        "date": "2026-07-28", "anchor": "Ivan", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Kellen", "type": "general_comment", "target": "body",
             "text": "On how strict to be about spam-flagged words like 'won't' and 'chance': Not too strict, I'd use."},
        ],
        "outcome": "unresolved",
    },
    {
        "date": "2026-07-29", "anchor": "Will Allred", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "jorge carrillo", "type": "general_comment", "target": "personalization",
             "text": "For healthcare providers, the NPI Registry gives you both companies and people. For clinics, "
                     "Discolike beats Google Maps; for individual doctors Maps is superior."},
            {"author": "Jai Toor", "type": "general_comment", "target": "personalization",
             "text": "NPI + google maps data. Public + private combo works really well for HC providers."},
        ],
        "outcome": "unresolved",
        "notes": "Sourcing/tooling thread, not copy. Kept for the data-source guidance only.",
    },
    {
        "date": "2026-07-29", "anchor": "Tim Keen", "thread_class": "copy_review",
        "original_copy": {
            "author": "Tim Keen", "copy_type": "cold_email",
            "text": "Selling his own AI implementation services to agency owners. Opens 'are you spending hours vibe-coding "
                    "galaxy-brain automations that end up consuming all your time and energy and don't drive revenue', then "
                    "'I built and sold an agency so i understand what it's like', 'Worth a quick chat?'",
        },
        "feedback": [
            {"author": "Kellen", "type": "question", "target": "personalization",
             "text": "What sorts of agencies are being targeted? (author admitted he'd just rounded up emails he already had)"},
            {"author": "Kellen", "type": "rewrite", "target": "opening_line",
             "text": "Anchor to what the prospect would choose to do rather than to your own framing.",
             "rewrite_suggested": "If you had 16 uninterrupted hours to focus on any {{company}} project you wanted, what would it be name? / Asking because after selling my own - am hoping to connect with people to support interesting projects. / You might need x, y or z... wondering if it would be useful to connect?"},
            {"author": "Ihor Seheda", "type": "critique", "target": "overall",
             "text": "Primary bottleneck is angle sharpness. The message pitches two distinct offers as one: 'we build AI "
                     "automation systems for you' and 'GTM coaching to help you sell faster'. Different engagements, likely "
                     "different buyers-within-the-buyer. Split them and test as separate sends."},
            {"author": "Ihor Seheda", "type": "critique", "target": "personalization",
             "text": "Segment meaningfulness 2/5 - the real segment (builder-type founders, not sales-led agencies) is hinted "
                     "at through the pain line but never made an explicit filter."},
            {"author": "Ihor Seheda", "type": "critique", "target": "body",
             "text": "Belief & signal fit 3/5 - 'I built and sold an agency' is real credibility but generic, not tied to "
                     "anything specific about the recipient."},
            {"author": "Ihor Seheda", "type": "approval", "target": "opening_line",
             "text": "Persona in context 4/5 - the 'vibe-coding... don't drive revenue' line is specific and well-targeted, "
                     "genuinely situational rather than generic."},
        ],
        "outcome": "revised",
        "notes": "Tim Keen is normally a reviewer here; this is him receiving. Got one good lead reply but low overall reply rate. "
                 "Ihor's MMF scoring rubric (market/segment/persona/angle/offer) is stated in full.",
    },
    {
        "date": "2026-07-30", "anchor": "Abhi at GTMcafe", "thread_class": "copy_review",
        "original_copy": {
            "author": "Abhi at GTMcafe", "copy_type": "cold_email",
            "text": "Subject 'search gap'. Google vs YouTube search-volume gap for a video production offer, "
                    "'The gap isn't another blog post. It's being missing when buyers switch from reading to watching.', "
                    "closing 'Is that something you're actively looking at?'",
        },
        "feedback": [
            {"author": "Kellen", "type": "rewrite", "target": "subject_line",
             "text": "Put the actual search term in the subject; force it to two lowercase words plus 'gap'.",
             "rewrite_suggested": "{search term} gap  -- e.g. 'gtm revops gap'. Use the term, as long as it's small. Or force into 2 words all lower case then 'gap'. Even if it sounds weird."},
            {"author": "Kellen", "type": "rewrite", "target": "body",
             "text": "Replace the balanced 'isn't x it's y' construction with a direct, slightly confrontational line.",
             "rewrite_suggested": "instead of 'the gap isn't x it's y' say 'you won't close that gap putting out another random blog post'"},
            {"author": "Kellen", "type": "rewrite", "target": "cta",
             "text": "Make the CTA a concrete effort trade.",
             "rewrite_suggested": "if I spend the 45 min to map how I'd approach this, will you take a look?"},
            {"author": "Kellen", "type": "general_comment", "target": "tone",
             "text": "On being called arrogant: 'Fuck yeah it is.' #1 goal is disrupt status quo. But imo you wanna balance "
                     "agitation with empathy - need to disrupt and get attention but then be fair."},
            {"author": "Kellen", "type": "critique", "target": "body",
             "text": "Remove the 'we' line. It adds nothing. They don't care about you bro. Classic Josh Braun is I:you ratio "
                     "and focusing on 'you' framing."},
            {"author": "Kellen", "type": "critique", "target": "length",
             "text": "Separate line 2 and 3."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-08-01", "anchor": "Zargham Saeed", "thread_class": "copy_review",
        "original_copy": {
            "author": "Zargham Saeed", "copy_type": "cold_email",
            "text": "Payroll tax savings offer ($573/year per employee). States an exact overpayment figure, names Culver's "
                    "and Buffalo Wild Wings, 'Open to a quick call to see if it's a fit?', PS 'IRS compliant and 97 percent "
                    "of our clients stay with us for life.'",
        },
        "feedback": [
            {"author": "Ivan", "type": "critique", "target": "body",
             "text": "'We did the same for Culver's' but the mechanism isn't mentioned - explain what it is that you did that "
                     "led to the decrease. Reading the email as it is now doesn't tell the reader how they'll achieve these results."},
            {"author": "Bharatt Arorah", "type": "critique", "target": "body",
             "text": "Add more context and explain the mechanism a little bit. Right now you'd be asking for 30 mins of their "
                     "time in exchange for nothing. Don't dump information, but structure it so they're genuinely curious how "
                     "you can even save them money. Everybody loves free money - the two reasons they'd pass are they don't "
                     "trust it's legit, or they didn't understand what it meant."},
            {"author": "Nick", "type": "critique", "target": "cta",
             "text": "Have a softer CTA than a quick call, because people are usually skeptical about these offers. Have a "
                     "document stating how you do it; once they reply, send the doc and then ask for a call."},
        ],
        "outcome": "revised",
        "notes": "Three independent reviewers converged on the same diagnosis: an unexplained mechanism reads as too-good-to-be-true.",
    },
    {
        "date": "2026-08-03", "anchor": "Abhi at GTMcafe", "thread_class": "copy_review",
        "original_copy": {
            "author": "Abhi at GTMcafe", "copy_type": "cold_email",
            "text": "The 07-30 YouTube-gap copy re-pointed at law firms serving startups, keeping 'You won't close that gap by "
                    "putting out another blog post' and asking for a 30-minute chat.",
        },
        "feedback": [
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Softened the whole thing and swapped the blog jab for an ads observation.",
             "rewrite_suggested": "saw a few of your ads focused on {{topic}}, name. / on youtube thats seeing about x searches per month / blogs dont capture that traffic - we help brands like yours use video to instead. / Open to a call where i show you what videos will start landing you those searches?"},
            {"author": "Kellen", "type": "critique", "target": "tone",
             "text": "imo make softer // like how someone talks. Smooth. You're leaned back, smoking a cigar, dim room, "
                     "loafers, jazz on vinyl in the background. Like chill bruh."},
            {"author": "Kellen", "type": "critique", "target": "tone",
             "text": "Accusatory or aggro or too forward causes knee jerk pull back reaction."},
        ],
        "outcome": "revised",
        "notes": "Directly qualifies the 07-30 'disrupt status quo' advice: same reviewer, three days later, pulling the "
                 "aggression back down. The two must be read together.",
    },
    {
        "date": "2026-08-03", "anchor": "Kellen", "thread_class": "banter",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [], "outcome": "unresolved",
        "notes": "California dairy tangent. Excluded from playbook.",
    },
    {
        "date": "2026-08-05", "anchor": "Donnel Charles", "thread_class": "discussion",
        "original_copy": {
            "author": "Donnel Charles", "copy_type": "subject_line_only",
            "text": "A received subject line that questioned whether the recipient was the right person.",
        },
        "feedback": [
            {"author": "Donnel Charles", "type": "critique", "target": "subject_line",
             "text": "If anyone is using this subject line, probability of getting the reader to read the email is low, as it "
                     "tells me you are unsure if this is the right person (plus it's in spam)."},
        ],
        "outcome": "unresolved",
    },
    {
        "date": "2026-08-07", "anchor": "burhan khaja", "thread_class": "copy_review",
        "original_copy": {
            "author": "burhan khaja", "copy_type": "cold_email",
            "text": "Subject 'josh, risk? @gtm hiring'. An intern/consulting pitch citing Smartlead, n8n and Claude Code "
                    "skills, opening on a hiring signal.",
        },
        "feedback": [
            {"author": "ben - aperoadvisors.com", "type": "critique", "target": "overall",
             "text": "this is confusing. i dont know what the ask is here. in the email i mean."},
            {"author": "ben - aperoadvisors.com", "type": "critique", "target": "overall",
             "text": "i'd just ask if they hire interns. the offer is free labor - that's a great offer. just lead with that. "
                     "everything else is cake."},
            {"author": "ben - aperoadvisors.com", "type": "rewrite", "target": "subject_line",
             "text": "Use exec shorthand for the subject.",
             "rewrite_suggested": "intern q"},
            {"author": "ben - aperoadvisors.com", "type": "critique", "target": "tone",
             "text": "execs speak to eachother in shorthand like that, this comes off as low status. not trying to be rude when "
                     "I say that. It comes off as like, you dont want to be direct - you're circling around the main offer "
                     "which is that you want to intern for them."},
            {"author": "ben - aperoadvisors.com", "type": "general_comment", "target": "tone",
             "text": "i think cold emails should resemble a text from a friend."},
            {"author": "Tim Keen", "type": "critique", "target": "overall",
             "text": "It feels like you recently learned a lot of different things for what you're 'meant' to do in a cold "
                     "email and you're doing them all at the same time."},
            {"author": "Tim Keen", "type": "critique", "target": "body",
             "text": "You're saying you have real skills but don't actually show anywhere that you do - you pick a pretty "
                     "generic signal and then your proof point is generic too."},
            {"author": "Tim Keen", "type": "question", "target": "overall",
             "text": "are you trying to get hired or are you trying to consult (author answered: hired)"},
        ],
        "outcome": "revised",
        "notes": "Almost all of this feedback was posted as separate top-level channel messages rather than thread replies - "
                 "the case that motivated day-session grouping.",
    },
    {
        "date": "2026-08-10", "anchor": "pyami", "thread_class": "copy_review",
        "original_copy": {
            "author": "pyami", "copy_type": "cold_email",
            "text": "FMS for commercial contractors on QuickBooks, positioned on same-day invoicing. Subject "
                    "'how fast {{companyName}} quotes'. 'Job closes today. Does the invoice go out today too?' plus "
                    "'Unlimited office users access for $0' and a tenure PS.",
        },
        "feedback": [
            {"author": "Max Pidvalnyi", "type": "critique", "target": "overall",
             "text": "I'd probably make it clearer // how you would say it out loud. I had to reread the email a couple of "
                     "times to fully comprehend everything."},
            {"author": "Max Pidvalnyi", "type": "critique", "target": "personalization",
             "text": "You might split test not saying you saw they're using QuickBooks, but just aligning the value "
                     "proposition with it - it will still sound relevant but less stalkery // spammy."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Reframed as a question about their customers' experience, with a before/after proof line.",
             "rewrite_suggested": "Name - do your customers get an invoice automatically when <company> closes an invoice in quickbooks? / ClientA and ClientB had manual processes. / we replaced them with xyz - now dream outcome. / Are you open to a quick discussion on whether your team could benefit from similar?"},
            {"author": "Kellen", "type": "general_comment", "target": "cta",
             "text": "Also good opportunity to lead w lead magnet or give away."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-08-10", "anchor": "Amirali", "thread_class": "copy_review",
        "original_copy": {
            "author": "Amirali", "copy_type": "linkedin_dm",
            "text": "Single-line direct ask: 'Hi {FIRST_NAME}, would you consider another data provider if it could offer "
                    "stronger coverage and better terms than your current setup?'",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "tone",
             "text": "Imo not ideal. It kinda puts them on the spot and is sorta aggro. Which resonates w me as a disposition "
                     "as a person but not ideal for outreach."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Replaced the switch-provider ask with an advice-seeking opener, then a second-touch qualification question.",
             "rewrite_suggested": "Name - hoping you can help me out. Trying to learn how <titles> think about making decisions on what x they use. Hoping to connect and get your lens via dm. || Then on accept: Great to connect - like I said, I am trying to figure out x. When you're thinking of y, is z enough for you to want to learn more? Or is <fair counter point>? It would be immensely helpful to get your take."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-08-11", "anchor": "Abhi at GTMcafe", "thread_class": "copy_review",
        "original_copy": {
            "author": "Abhi at GTMcafe", "copy_type": "linkedin_dm",
            "text": "Sybill vs Gong YouTube-search DM: 'Saw a few of Sybill's ads around Sybill vs Gong, Gorish. "
                    "\"Gong alternative\" sees around 4,000 searches a month on YouTube...'",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "opening_line",
             "text": "'saw' as an opener is more basic."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Replaced the 'saw' opener with a david-vs-goliath frame, converted the stat into a question, and added "
                     "a product-launch PS.",
             "rewrite_suggested": "Sybil vs Gong is b2b notetaking david vs goliath, Gorish / 4000 times per month, someone looks up 'gong alternative' on youtube. / Do you know what % of them become a sybil demo? / In a single call I can show you ways none of your competitors are winning this traffic / Lmk - Kellen / p.s. the recent xyz drop could plug into this approach easily - if you're still looking to get more marketing outcomes from that product launch"},
            {"author": "Kellen", "type": "critique", "target": "tone",
             "text": "also it may piss them off to call them so small lol"},
            {"author": "Kellen", "type": "approval", "target": "overall",
             "text": "no yours was good but imo some by hand you can make smoother."},
            {"author": "barash", "type": "approval", "target": "overall",
             "text": "love this copy (endorsing Kellen's rewrite)"},
        ],
        "outcome": "revised",
        "notes": "Author reported getting a response from the rewrite.",
    },
    {
        "date": "2026-08-11", "anchor": "groundskeep", "thread_class": "banter",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [], "outcome": "unresolved",
        "notes": "Domain-name joke thread. Excluded from playbook.",
    },
    {
        "date": "2026-08-11", "anchor": "Mick", "thread_class": "copy_review",
        "original_copy": {
            "author": "Mick", "copy_type": "linkedin_dm",
            "text": "LinkedIn DM to CEOs/CROs at Series B SaaS: 'Any surprises in this year's forecast, or is next year's plan "
                    "still riding on past quarters' average? We're helping B2B SaaS companies build GTM plans on cohort- and "
                    "distribution-based data instead of blended, naive assumptions. Worth 20 minutes...'",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "tone",
             "text": "Too technical. Like it's a calculus problem. Needs to be like 7th grade reading level for reply maxxxing."},
            {"author": "Kellen", "type": "critique", "target": "body",
             "text": "Can you send a little more about a situation or story that represents this from the VP sales mind? I "
                     "assume it's basically they either want x and can't get it, or don't know x exists and you can help them "
                     "hit what they are chasing."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Rewrote around a report the buyer would want to pull, with a stage-based before/after.",
             "rewrite_suggested": "name - as the company sales org scales - do you imagine being able to pull reports like 'x' up to make calls on what to do next? / Most sales leaders get through series a w/ xyz / But from b on, you may want xyz. / I have a blah blah I can send if interested?"},
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "Yeah that's super good, just no one is looking for it - they don't know to ask."},
            {"author": "Will Allred", "type": "rewrite", "target": "overall",
             "text": "Radically shortened version.",
             "rewrite_suggested": "Hey @Mick - helping teams w/ sales forecasts. If you're using broad assumptions from last Q, we make it easier to level up. / Lmk if you're looking to better predict $."},
            {"author": "Will Allred", "type": "general_comment", "target": "personalization",
             "text": "Depending on their work history this can be segmented well. Ex. coming from a bigger company - you can "
                     "talk about matching bigger co maturity w/o the headache."},
            {"author": "Kellen", "type": "approval", "target": "body",
             "text": "I love those 'friction' frames, things like 'all sales leaders come from the same industry' or "
                     "'no one with xyz background'."},
        ],
        "outcome": "revised",
        "notes": "Author's own summary of what worked: 'anchoring to a high-stakes moment and more judo kind of movement, "
                 "rather than a headbutt. empathetic friction.'",
    },
    {
        "date": "2026-08-12", "anchor": "Abubakarr Jaye", "thread_class": "copy_review",
        "original_copy": {
            "author": "Abubakarr Jaye", "copy_type": "linkedin_dm",
            "text": "DM describing Lumnis (buying-intent surfacing) and closing 'Want me to run a search for nutrad's target "
                    "buyers? Takes me a couple of minutes.'",
        },
        "feedback": [
            {"author": "Kellen", "type": "approval", "target": "cta",
             "text": "Last 2 sentences are best parts imo."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Led with a confirmation question, made the deliverable a validation favour, and asked for feedback "
                     "rather than a meeting.",
             "rewrite_suggested": "Hey name - company sells to xyz buyer right? / Can I send you a list and have you validate if it's better than what you get currently from xyz? / I'm building company to outcome - hoping to trade something useful for your sincere feedback / Lmk what you think - Kellen"},
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "I'd form as a question."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-08-13", "anchor": "barash", "thread_class": "copy_review",
        "original_copy": {
            "author": "barash", "copy_type": "cold_email",
            "text": "D2C email marketing client that can contractually guarantee $50k-$500k/month in 60 days. Question was "
                    "whether to lead with that promise. Later version adds an email-signup observation before the guarantee.",
        },
        "feedback": [
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "SPLIT TEST. Try 2x that are 'super confident', 2x that are normal, 2x that address that it sounds skeptical."},
            {"author": "Kellen", "type": "general_comment", "target": "personalization",
             "text": "I'd do like a 4x matrix and add this as the other dimension. Sometimes more specific isn't better. "
                     "Sometimes it is. From my experience."},
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "I'd work on you/I ratio i.e. it's very we we we rn, maybe try the other POV."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Rewrote from the subscriber's-eye view, with the guarantee held to the fourth line.",
             "rewrite_suggested": "Your <newsletter name> list got a new subscriber named <name> last week, <first name>. / Me. / Within x days, you sent me y. / <other brand> used to do similar, grew y% over z period, using our tool. / We literally guarantee a xyz increase, or you pay nothing. / No strings - can I send more on how we can make bold claims like this?"},
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "Btw sometimes we we we works. I'll literally test 'our perspective' vs 'their perspective' sometimes. "
                     "So we want an open loop. Either: you are x + you want y = open loop of how we get it. Or: you are x, "
                     "we do y-mechanism = open loop of what outcome can drive inside your company."},
        ],
        "outcome": "revised",
        "notes": "Contains the clearest statement of the open-loop construction, and an explicit caveat that the "
                 "you-not-we rule is a default to test against, not an absolute.",
    },
    {
        "date": "2026-08-13", "anchor": "Gregory", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Kellen", "type": "general_comment", "target": "length",
             "text": "75 words per Will Allred."},
            {"author": "Max Pidvalnyi", "type": "general_comment", "target": "length",
             "text": "People say shorter is better but I've been having great results with like 80-100 words."},
            {"author": "Kellen", "type": "general_comment", "target": "length",
             "text": "It depends on potency imo and attention - some things can def be longer. Nick Abraham goes hella short, "
                     "Will 75ish, I go slightly above Will's usually, but Youssef Hesham writes longer bangers too."},
            {"author": "Kellen", "type": "general_comment", "target": "length",
             "text": "On whether the same principle holds for enterprise: generally yeah, it's human psychology more than "
                     "business size based."},
            {"author": "Will Allred", "type": "general_comment", "target": "length",
             "text": "A great exercise to hone your copy - try to fit it into a tweet."},
            {"author": "Jared Holstad", "type": "general_comment", "target": "length",
             "text": "My current offer that's working is 72 words, and 9 of them are asking if they want me to give them "
                     "something useful for free."},
        ],
        "outcome": "no_consensus",
        "notes": "The channel's canonical length thread. No hard cap; range 72-100 words with named practitioners on each side.",
    },
    {
        "date": "2026-08-14", "anchor": "Eddy Okun", "thread_class": "copy_review",
        "original_copy": {
            "author": "Eddy Okun", "copy_type": "other",
            "text": "Top-of-funnel offer: $50 gift card for a 5-minute conversation with an AI, to operations/admins at "
                    "healthcare offices. Working organically via founder LinkedIn profiles, zero uptake from LinkedIn ads.",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "im a bad target for gift card type stuff"},
            {"author": "Max Pidvalnyi", "type": "rewrite", "target": "overall",
             "text": "Swap the incentive and remove the AI friction.",
             "rewrite_suggested": "offer to donate to a charity of their choice"},
            {"author": "Max Pidvalnyi", "type": "critique", "target": "overall",
             "text": "Also idk, I wouldn't speak to AI tbh, that's kinda weird. Form doesn't work? Do form - man that should "
                     "improve everything."},
            {"author": "Max Pidvalnyi", "type": "critique", "target": "overall",
             "text": "try 'you' first approach"},
            {"author": "Eddy Okun", "type": "general_comment", "target": "overall",
             "text": "Self-diagnosis: 'the voice agent thing explains the fact that it's only 5 minutes and they can do it "
                     "anytime, but it just might be adding too much cognitive load for them to take action.'"},
        ],
        "outcome": "unresolved",
        "notes": "Offer-mechanics thread rather than line-level copy: the friction was in the mechanism, not the wording.",
    },
    {
        "date": "2026-08-15", "anchor": "burhan khaja", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Eddy Okun", "type": "critique", "target": "tone",
             "text": "On a joke brand name for sunscreen: I think the name doesn't signal enough trust/reliability. When you "
                     "put on sunscreen you want to trust that the product is what it is - making a joke out of it might cause "
                     "subconscious suspicion."},
        ],
        "outcome": "unresolved",
        "notes": "Brand naming, not email copy. Kept for the trust-vs-humour principle.",
    },
    {
        "date": "2026-08-17", "anchor": "Moeed", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Kai", "type": "general_comment", "target": "body",
             "text": "On long sales cycles: the main thing was to have some clear value that you're providing them that they "
                     "probably didn't already know, or they would be surprised that you knew, that would possibly help them "
                     "in a real way. Figure out whatever your company is selling that can do something along those lines."},
        ],
        "outcome": "unresolved",
    },
    {
        "date": "2026-08-19", "anchor": "Tim Keen", "thread_class": "copy_review",
        "original_copy": {
            "author": "Tim Keen", "copy_type": "cold_email",
            "text": "Video production agency to heads of marketing at NY Series A startups. 'Does [company name] have an "
                    "in-house video production team?' then a Solstice HealthTech proof point - 'The founder told me it helped "
                    "as they were raising their $21m series A' - and an offer to send references.",
        },
        "feedback": [
            {"author": "Ihor Seheda", "type": "critique", "target": "opening_line",
             "text": "Maybe worth trying to swap the closed yes/no question for something more open-ended, like observation "
                     "plus soft question.",
             "rewrite_suggested": "Post-raise is usually when video shifts from 'nice to have' to actually mattering for {{vertical}} companies. Wondering if that's true for {{companyName}} too."},
            {"author": "Ihor Seheda", "type": "critique", "target": "body",
             "text": "The story is 'helped them raise' but you are targeting people who already raised. A different moment for "
                     "the pitch. Consider reframing the angle for post-raise needs, not pre-raise fundraising.",
             "rewrite_suggested": "I worked with Solstice, another NY HealthTech startup, to film the hero video on their website. Their founder said it changed how enterprise buyers and candidates perceived them in the months after their $21M raise."},
            {"author": "Eddy Okun", "type": "general_comment", "target": "body",
             "text": "There might be more than one motivation for someone to upgrade their brand collateral. In a world where "
                     "AI has raised the floor of asset production, the only way to stand out is with bespoke real-world assets "
                     "that are harder to replicate with AI."},
        ],
        "outcome": "revised",
        "notes": "Cleanest example of proof-timing mismatch: the case study's moment must match the prospect's current moment.",
    },
    {
        "date": "2026-08-22", "anchor": "Anu Biswas", "thread_class": "copy_review",
        "original_copy": {
            "author": "Anu Biswas", "copy_type": "sequence",
            "text": "Three-step sequence for an AI data analyst to F&B e-commerce. Subject '{{first_name}}, your data is "
                    "lying to you'; long question construction, Kellogg's proof, competitor name-drop, '5-mins for a quick "
                    "call tomorrow???', then an unrequested Loom link in step 3.",
        },
        "feedback": [
            {"author": "Mikulas", "type": "critique", "target": "cta",
             "text": "Definitely wouldn't recommend sending loom links without people opting in. 'quick call' CTAs perform "
                     "typically the worst."},
            {"author": "Mikulas", "type": "critique", "target": "length",
             "text": "I'd stick with 2-step sequences if your TAM supports it. From my exp there are diminishing returns on "
                     "the third step."},
            {"author": "Mikulas", "type": "critique", "target": "tone",
             "text": "Wouldn't use exclamation marks or caps in your copy. Would change 'demo video' for something sexier."},
            {"author": "Mikulas", "type": "rewrite", "target": "subject_line",
             "text": "Short, casual, 1-5 words.",
             "rewrite_suggested": "your data  /  pulling reports"},
            {"author": "Mikulas", "type": "critique", "target": "personalization",
             "text": "What role are you sending this to? If your message goes to the CEO they might not live in the day to day "
                     "to feel that pain of 'stitching 5 spreadsheets'.",
             "rewrite_suggested": "Does {{analystName}} ever have to pull reports from 5 different places, {{firstName}}? / Is {{analystName}} pulling data from all over the place, or do you have it in one spot?"},
            {"author": "Ihor Seheda", "type": "critique", "target": "personalization",
             "text": "F&B ecom brands with lots of tools may not be specific enough to write a sharp message. Decide if you're "
                     "going after multi-plant manufacturers (waste/yield/downtime pain) vs DTC-first brands (inventory/demand pain)."},
            {"author": "Ihor Seheda", "type": "critique", "target": "body",
             "text": "'Had an idea on how this could work for you too' is vague - just state it. And Milo is not properly "
                     "introduced; worth saying what it is right away in the first message."},
            {"author": "Kellen", "type": "rewrite", "target": "subject_line",
             "text": "Compress the subject line.",
             "rewrite_suggested": "lying data  /  data lies  /  your lying data"},
            {"author": "Kellen", "type": "critique", "target": "opening_line",
             "text": "Imo opening question too aggro and complicated."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Reframed the opener around annoyance rather than accusation, and made the ask a short video.",
             "rewrite_suggested": "How annoying is 'xyz' to answer, name? / You probably have to x and y before you can even z. / We've helped x do y. / Would you be open to me sending a 100 second video explaining more?"},
        ],
        "outcome": "revised",
        "notes": "Three reviewers, three layers: Mikulas on mechanics, Ihor on segmentation, Kellen on tone and compression.",
    },
]
