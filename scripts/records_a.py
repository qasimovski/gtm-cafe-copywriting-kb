"""Classified records, part A: 2026-05-28 .. 2026-06-29.

Hand-classified in-session from raw/days/*.md. Vocabulary is fixed --
see scripts/validate_structured.py. `anchor` names the person whose
top-level message(s) the record is built from; the emitter resolves
source_ts from that.
"""

RECORDS = [
    {
        "date": "2026-05-28", "anchor": "John Richards", "thread_class": "copy_review",
        "original_copy": {
            "author": "John Richards", "copy_type": "cold_email",
            "text": "Two variants for a fractional CRE analyst offer. V1 subject 'underwriting capacity', "
                    "closing 'Am I off base here?'. V2 subject 'deal model' with a Loom walkthrough ask.",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "cta",
             "text": "Make cta better. The thesis is good so make the cta a more direct literal ask aka move the ball forward."},
            {"author": "Kellen", "type": "critique", "target": "cta",
             "text": "Who tf cares if you're off. You care if he wants to learn more or you care if she wants to see samples of your work.",
             "rewrite_suggested": "if you want - I can do a {form type} by hand on video to prove I know my stuff"},
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "I'd make it clearer and less interpretive."},
            {"author": "Kellen", "type": "rewrite", "target": "cta",
             "text": "Suggested video-ask framing that leads with the question rather than the credential.",
             "rewrite_suggested": "hey name - would you watch a video on xyz if I send it to you? Asking because I've helped other blah blah. I work fractionally on xyz. Any interest?"},
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "Try an a/b test and do one hella specific and one more vague on purpose."},
        ],
        "outcome": "revised",
        "notes": "Author self-diagnosed the weak CTA as 'hedging to the middle... im not confident in targeting'.",
    },
    {
        "date": "2026-05-29", "anchor": "Sana Choudary", "thread_class": "copy_review",
        "original_copy": {
            "author": "Sana Choudary", "copy_type": "cold_email",
            "text": "Subject '{{Company}}'s reviews'. Opens on founder story, pivots to 2-3 star reviews, "
                    "offers a pulled review report, closes 'Waste of your time?'",
        },
        "feedback": [
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Full rewrite: shorter subject, softened claims, personalization folded into the argument, "
                     "and a 'would it be useful to see' close.",
             "rewrite_suggested": "Subject: reviews / The way {{Company}} started from {{founder_story}} makes the brand feel more personal than financial, {{First_Name}}. / That is probably why a few 2-star reviews could sting more than they should. / I pulled the patterns into a short review report around what customers seem to be missing. / Would it be useful to see what showed up for {{Company}}?"},
            {"author": "Kellen", "type": "rewrite", "target": "personalization",
             "text": "Provided a second variant for prospects with no founder story, swapping in brand promise.",
             "rewrite_suggested": "Subject: reviews / {{Company}} seems built around {{brand_promise}}, which makes the lower reviews feel especially useful, {{First_Name}}. / A few 2-star comments often show where the customer expectation starts to break. / Would it be useful to see what showed up for {{Company}}?"},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-05-30", "anchor": "Harshil", "thread_class": "copy_review",
        "original_copy": {
            "author": "Harshil", "copy_type": "cold_email",
            "text": "Four variants across two law-firm segments (with and without a marketing team). "
                    "Subjects: 'bandwidth question', '{{first_name}} led campaigns', '{{first_name}}'s bold ideas', 'vendor questions'.",
        },
        "feedback": [
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Rewrote to a single tension line, a capability line with no 'you', and a soft fit question.",
             "rewrite_suggested": "Subject: case flow / Still trying to keep cases moving while marketing sits on your plate, {first_name}. / That usually leaves firms choosing between referrals and owner-led campaigns. / We have helped injury firms create steadier demand without pulling partners into execution. / Would it be useful to see where that might fit for {company}?"},
            {"author": "Nikhil Nainwani", "type": "approval", "target": "overall",
             "text": "Bang on! (endorsing Kellen's rewrite)"},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-06-03", "anchor": "Donnel Charles", "thread_class": "copy_review",
        "original_copy": {
            "author": "Donnel Charles", "copy_type": "subject_line_only",
            "text": "A received email that landed in spam; author flagged the subject line as unlikely to earn attention.",
        },
        "feedback": [
            {"author": "Mitchell Keller", "type": "critique", "target": "subject_line",
             "text": "SL doesn't really scream internal email."},
            {"author": "Mitchell Keller", "type": "rewrite", "target": "subject_line",
             "text": "Offered a plainer, more internal-sounding subject line.",
             "rewrite_suggested": "SL: can you share it"},
            {"author": "Mitchell Keller", "type": "general_comment", "target": "overall",
             "text": "Get AI to whip up like 20 diff versions of the copy and do a test email on all, see which one leaks."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-06-04", "anchor": "ben - aperoadvisors.com", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Kellen", "type": "general_comment", "target": "tone",
             "text": "I think empathy is underrated. Like self awareness and chippy empathy - not soft // apologetic "
                     "but more like shit eating grin empathy."},
            {"author": "Kellen", "type": "general_comment", "target": "personalization",
             "text": "1:1 doesn't matter. People get excited to buy a Diet Coke or Starbucks coffee every day without "
                     "personalization. Your iPhone isn't personalized. Empathy, awareness, uniqueness are all underrated concepts."},
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "People buy for what they perceive to be their pain, their opportunity to gain, the risk, and how much "
                     "they personally care. Helping them get what they personally want while getting it done via what the "
                     "company wants - so it presents as org benefit not personal preference - is square 1."},
            {"author": "ben - aperoadvisors.com", "type": "general_comment", "target": "tone",
             "text": "B2C buying behavior is the dominant mode. If B2B marketers were smart, they'd take more cues from them. "
                     "We all want to act like CMOs don't buy dumb stuff on Amazon like the rest of us."},
            {"author": "John Kitsmiller", "type": "general_comment", "target": "personalization",
             "text": "WIIFM - What's In It For Me. For gov there is almost never a single decision maker so you have to "
                     "answer the WIIFM for every persona in your messaging."},
        ],
        "outcome": "no_consensus",
        "notes": "Kellen vs Max Pidvalnyi disagree on whether B2C personalization logic transfers to B2B. Recorded as genuine disagreement.",
    },
    {
        "date": "2026-06-08", "anchor": "Rachel Fiegler", "thread_class": "copy_review",
        "original_copy": {
            "author": "Rachel Fiegler", "copy_type": "sequence",
            "text": "Three-email sequence for Pinpointe / NYCbound relocation service to People teams. "
                    "Email 1 opens 'It's clear you value [X], having [done Y at Z]'.",
        },
        "feedback": [
            {"author": "Kellen", "type": "approval", "target": "overall",
             "text": "it's good"},
            {"author": "Kellen", "type": "critique", "target": "length",
             "text": "I'd a/b test using a shorter email 1 - same line 1 and 2, then a shorter value prop and cta."},
            {"author": "Kellen", "type": "rewrite", "target": "tone",
             "text": "Soften the certainty of the opener.",
             "rewrite_suggested": "soften maybe the phrasing to 'seems like' or 'feels like' vs 'it's clear'"},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-06-14", "anchor": "Noil", "thread_class": "copy_review",
        "original_copy": {
            "author": "Noil", "copy_type": "cold_email",
            "text": "Two variants for a Klaviyo/retention offer to supplement brands. V1 subject 'recovery update'; "
                    "V2 subject 'genuinely impressed, [First Name]' with a fly-you-to-your-supplier guarantee.",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "my #1 would be make clearer what youre offering vs burying at the end."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Two sample rewrites leading with the offer as the first-line question.",
             "rewrite_suggested": "Subject: cart leak / Can I send the revenue leak breakdown I made for {company}, {first_name}? / It shows which abandoned cart, welcome, and reorder emails could recover more sales. / We used the same review to help another supplement brand turn missed follow-up into revenue."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-06-15", "anchor": "Muhammad Abbas", "thread_class": "copy_review",
        "original_copy": {
            "author": "Muhammad Abbas", "copy_type": "linkedin_dm",
            "text": "LinkedIn message to the SVP of a Visa acceptance company requesting an in-person coffee, "
                    "anchored on agentic payments and the integration layer.",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "focus on them vs you imo"},
            {"author": "Kellen", "type": "critique", "target": "cta",
             "text": "id ask them something direct tbh"},
            {"author": "Ihor Seheda", "type": "critique", "target": "personalization",
             "text": "The main bottleneck is persona-level specificity, not the idea or tone. You lack one explicit link "
                     "between your angle and a concrete pressure this SVP actually wakes up worrying about."},
            {"author": "Ihor Seheda", "type": "rewrite", "target": "body",
             "text": "Add a concrete acceptance pressure to tie the angle to the persona's owned problem.",
             "rewrite_suggested": "Everyone's focused on the network, but the real pressure from agentic flows is going to hit the integration layer - where issuers, merchants and orchestration platforms all expect Visa-level reliability from third-party APIs - which is exactly where we operate."},
            {"author": "Ihor Seheda", "type": "general_comment", "target": "personalization",
             "text": "On referencing that the founder met a team member in London: the more relevant contextual reference "
                     "the better. Kinda warm intro social proof - shows internal demand and explains why the SVP is the right next step."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-06-16", "anchor": "Kyle Nelson", "thread_class": "copy_review",
        "original_copy": {
            "author": "Kyle Nelson", "copy_type": "cold_email",
            "text": "Zoho CRM hidden-revenue email opening 'In the 26 years you've been CEO, you know how much revenue "
                    "can slip through the cracks of a CRM that isn't set up right.'",
        },
        "feedback": [
            {"author": "Kellen", "type": "approval", "target": "opening_line",
             "text": "love the opener, i am a fan of 'presumed personalization'. Instead of 'hey name - noticed x' where focus "
                     "is on x at the end, this subtly lands 'i know youve been ceo for x long' and focuses on the argument "
                     "you're making. understated personalization ftw."},
            {"author": "Kellen", "type": "rewrite", "target": "body",
             "text": "Remove 'you' from the mechanism line so it reads as a general truth rather than a personal claim.",
             "rewrite_suggested": "instead of 'the two places I find' maybe 'two low hanging fruit sources for zoho users....' aka remove 'you' from it"},
            {"author": "ben - aperoadvisors.com", "type": "approval", "target": "opening_line",
             "text": "I like that ^^"},
        ],
        "outcome": "approved",
    },
    {
        "date": "2026-06-17", "anchor": "Max Pidvalnyi", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "I bet you make the emails too complex. Break down complex solutions into simpler mechanisms, and focus "
                     "less on 'the full solution' vs 'why they'd say yes'."},
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "Selling HubSpot CRM you may think you need to pitch all it does, but an email focused solely on "
                     "'never miss a deal follow-up' may be all the email needs to entice a meeting."},
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "Making the focus 'why it's worth talking' vs 'why people buy' is good. If 10-30% of deals close from "
                     "meeting, 70-90% came to learn something - way more % of TAM has intrigue and curiosity around ideas "
                     "vs intent to do things. So sometimes people try to solve too much in email vs entice a convo."},
            {"author": "Kellen", "type": "rewrite", "target": "body",
             "text": "Sample that baits one specific idea rather than the whole solution.",
             "rewrite_suggested": "Max - 50,000 funded saas companies folded last year due to lack of growth. / Of those still running, most lean on a single growth mechanism to stay alive. / Had some ideas about what that could look like for <company>, given you seem to sell to <audience>. / Would 15 min for me to share some ideas be worth sending the calendar hold?"},
            {"author": "Kellen", "type": "general_comment", "target": "cta",
             "text": "Complex products can feel like they 'give homework' - hard or long to derive value, thus not enticing. "
                     "Getting them to say yes to seeing or reading something may work better, or offering a quick 5-min back and forth."},
        ],
        "outcome": "unresolved",
    },
    {
        "date": "2026-06-17", "anchor": "Atif Irshad", "thread_class": "copy_review",
        "original_copy": {
            "author": "Atif Irshad", "copy_type": "linkedin_dm",
            "text": "LinkedIn connection note about AI search traffic (ChatGPT/Gemini) for a fashion site, "
                    "plus a follow-up asking whether they're getting AI traffic.",
        },
        "feedback": [
            {"author": "Kellen", "type": "question", "target": "overall",
             "text": "Send samples of your notes (asked to see the actual copy before advising)."},
            {"author": "pyami", "type": "rewrite", "target": "overall",
             "text": "Offered a what-if scenario opener that dramatises the buyer's own search result.",
             "rewrite_suggested": "Hey Abdel - quick one: if someone from Saudi Arabia asked ChatGPT for 'luxury Arabic perfumes,' would Mohammed Alkhuraiji show up? / We help personal care and fragrance brands stay discoverable as search shifts to AI. / Worth sharing the kind of strategies working in 2025?"},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-06-18", "anchor": "Jules", "thread_class": "copy_review",
        "original_copy": {
            "author": "Jules", "copy_type": "linkedin_dm",
            "text": "Two DM variants to B2B SaaS ($1M-$10M) offering a Twitter strategy doc and scraped lead list.",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "id make it 'you' vs 'we/I' focused"},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Rewrote opening as a question about their current channel, and reframed the doc as self-implementable.",
             "rewrite_suggested": "Ishan - do you already get clients via twitter? / Another xy brand was able to poach xyz users using a play that {{company}} could easily recreate. / I made a doc you could use to self implement this if you have bandwidth. / Want to see it?"},
            {"author": "Kellen", "type": "approval", "target": "overall",
             "text": "but the copy as is is good id send yours too"},
        ],
        "outcome": "revised",
        "notes": "Author's takeaway was specifically 'I like the self implement part'.",
    },
    {
        "date": "2026-06-19", "anchor": "Bharat", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Saksham", "type": "general_comment", "target": "body",
             "text": "We generally include the address and just a simple opt out like reply 'X' to not receive any more emails."},
            {"author": "Will Allred", "type": "general_comment", "target": "overall",
             "text": "Can-Spam wasn't built with AI personalization in mind."},
        ],
        "outcome": "unresolved",
    },
    {
        "date": "2026-06-19", "anchor": "ben - aperoadvisors.com", "thread_class": "banter",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [], "outcome": "unresolved",
        "notes": "CAN-SPAM wordplay. Excluded from playbook.",
    },
    {
        "date": "2026-06-20", "anchor": "pyami", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Ivan", "type": "general_comment", "target": "overall",
             "text": "We tried CMMS and OEM offers - flopped big time with regular campaigns targeting the US. "
                     "Invites to webinars worked well. Targeting EU markets in the local language was okay. "
                     "The US market was hard to penetrate as most already had a system in place."},
            {"author": "Jake Stratton", "type": "general_comment", "target": "overall",
             "text": "Extremely tough. Easier through phone but still really hard. Tough category for agencies unless the "
                     "client is in it for the long run - complicated, time dependent, and insanely sticky."},
        ],
        "outcome": "unresolved",
        "notes": "Channel-level intel: when a category resists outbound, the fix may be channel/offer (webinar invite), not copy.",
    },
    {
        "date": "2026-06-22", "anchor": "Jai Toor", "thread_class": "copy_review",
        "original_copy": {
            "author": "Jai Toor", "copy_type": "cold_email",
            "text": "Research-interview recruitment email offering $100 for 30 minutes with an AI interviewer. "
                    "Subject 'Supabase research (with an AI interviewer) - $100 for 30 min'.",
        },
        "feedback": [
            {"author": "Sana Choudary", "type": "critique", "target": "overall",
             "text": "I don't think the value is the AI interviewer. Value is time savings for the person receiving it. "
                     "Fear is the AI interviewer might put words in my mouth or change my meaning. So being able to review "
                     "quotes before publishing is key."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-06-23", "anchor": "Liam Ellul", "thread_class": "discussion",
        "original_copy": {"author": "", "copy_type": "none", "text": ""},
        "feedback": [
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "yes imo fine to re send"},
            {"author": "Nikhil Nainwani", "type": "general_comment", "target": "overall",
             "text": "Results take a hit over time with the same copy; it depends on no. of sends as well. We change after "
                     "20-30k sends; if it's under 10k over 3 months, let it be."},
            {"author": "Kush", "type": "general_comment", "target": "overall",
             "text": "We change the copy a bit if we have found a new winning angle resonating more."},
        ],
        "outcome": "no_consensus",
        "notes": "Author reported back that re-running the same copy did NOT work; Kellen conceded ('damn my b'). "
                 "Recorded because the reported outcome contradicts the initial advice.",
    },
    {
        "date": "2026-06-25", "anchor": "Abrar Hussain", "thread_class": "copy_review",
        "original_copy": {
            "author": "Abrar Hussain", "copy_type": "cold_email",
            "text": "Three variants to founders of B2B AI companies (4-20 headcount). A: credential-led, "
                    "'I'll keep this short', PS 'This is a cold email'. B: retainer-churn angle with 500k+ emails/month "
                    "proof and 5 free meetings. C: very long, self-aware 'chances of you replying are practically nil'.",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "Email A is closest. Keep the 'founder-led sales starts to cap out' idea. Cut the proof pile, LinkedIn "
                     "line, and PS. It feels too much like you are trying to establish credibility instead of naming their problem."},
            {"author": "Kellen", "type": "critique", "target": "personalization",
             "text": "Email B is the wrong audience. It sounds like it was written for agencies with retainer churn, not B2B "
                     "AI founders. Also '500k+ emails a month' may hurt you because AI founders will worry about spam and market damage."},
            {"author": "Kellen", "type": "critique", "target": "length",
             "text": "Email C is way too long. The insight is good, but it reads like you are trying to prove you understand "
                     "every possible pressure they face. Pick one tension only. Keep it around 50 words."},
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "Do not offer '5 free meetings' in the first email. It makes the offer feel cheap and creates skepticism."},
            {"author": "Kellen", "type": "critique", "target": "cta",
             "text": "Avoid 'quick Loom.' It is overused. Ask to send the specific outbound wedge or test instead."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Sample built on the single founder-attention tension.",
             "rewrite_suggested": "Subject: founder led / Founder-led sales usually works until it starts costing too much founder attention, {{first_name}}. / We help lean AI teams test outbound before hiring sales too early. / The aim is predictable pipeline without pulling more time from product. / Would it help to see the first wedge we would test for {{company_name}}?"},
            {"author": "Drew Coryer", "type": "critique", "target": "opening_line",
             "text": "Leading with 'I'll keep this short...' adds unnecessary words (especially if it's not short)."},
            {"author": "Drew Coryer", "type": "critique", "target": "overall",
             "text": "Every line in 1A is framed as 'I', might be worth testing against their situation and saying I less. "
                     "The framing Kellen shared made it all about the problem, instead of the service you provide."},
        ],
        "outcome": "revised",
    },
    {
        "date": "2026-06-28", "anchor": "Abrar Hussain", "thread_class": "copy_review",
        "original_copy": {
            "author": "Abrar Hussain", "copy_type": "cold_email",
            "text": "Three short variants to $2-10M e-commerce brands for D2C email marketing, rev-share offer. "
                    "All three end with 'PS - Not for you? Reply pass and I'll leave you alone. Promise.'",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "body",
             "text": "id delete promise from the end"},
            {"author": "Kellen", "type": "approval", "target": "overall",
             "text": "overall looks cool to send"},
        ],
        "outcome": "approved",
        "notes": "Contrast with 2026-06-25: same author, much shorter copy, near-immediate approval.",
    },
    {
        "date": "2026-06-29", "anchor": "Ali Qureshi", "thread_class": "copy_review",
        "original_copy": {
            "author": "Ali Qureshi", "copy_type": "cold_email",
            "text": "Three variants to digital marketing agencies (11-50 staff) for LinkedIn outbound, all built on "
                    "'we guarantee a minimum of 15 qualified meetings in 3 months' plus an Ardith Publishing case study.",
        },
        "feedback": [
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "Core issue: these read like lead-gen vendor emails, not agency-owner emails. You're pitching the offer "
                     "too early, and the offer sounds suspiciously commodity. That puts you in the same bucket as every "
                     "LinkedIn appointment setter in their inbox."},
            {"author": "Kellen", "type": "critique", "target": "overall",
             "text": "Motivation lens: you're mostly hitting the functional layer ('we book meetings'). Agency owners care "
                     "more about inconsistent pipeline, founder-led sales bottlenecks, feast-or-famine months, and not "
                     "wanting to hire SDRs before the motion is proven."},
            {"author": "Kellen", "type": "critique", "target": "personalization",
             "text": "Targeting lens: 'digital marketing agencies, 11 to 50 employees' is okay, but the angle is still broad. "
                     "Strong targeting defines market, persona, and angle - not just firmographics."},
            {"author": "Kellen", "type": "critique", "target": "tone",
             "text": "Skepticism lens: the guarantee is doing too much work. It triggers doubt because agencies hear claims "
                     "like this constantly. Cold emails should use softer, tentative language and reduce skepticism, not "
                     "force certainty too early."},
            {"author": "Kellen", "type": "critique", "target": "body",
             "text": "Proof lens: 'Ardith Publishing' may not map cleanly to digital marketing agencies. If the prospect is an "
                     "agency, proof from a publisher creates a relevance gap. The proof should make them think 'that sounds "
                     "like my situation.'"},
            {"author": "Kellen", "type": "critique", "target": "cta",
             "text": "CTA lens: 'Worth a conversation?' and 'Worth 10 minutes?' are meeting asks - too heavy for this much "
                     "skepticism. Better CTAs start a reply, like 'Would it be useful to see the targeting angle?' Campaign "
                     "performance often depends on whether the CTA matches the buyer's readiness."},
            {"author": "Kellen", "type": "critique", "target": "opening_line",
             "text": "Email 1: too much fake warmth, too much certainty. 'Love your work' and 'crushing it' feel templated."},
            {"author": "Kellen", "type": "critique", "target": "opening_line",
             "text": "Email 3: strongest hook, weakest trust. Opening with a guarantee screams 'appointment setter.' It may "
                     "get attention, but likely from lower-quality or skeptical replies."},
            {"author": "Kellen", "type": "rewrite", "target": "overall",
             "text": "Four rewrite variants, all two-word lowercase subjects and a 'would it be useful/helpful to see' close.",
             "rewrite_suggested": "Subject: pipeline / Still relying on referrals while outbound feels too noisy to trust, {{firstName}}. / A few agencies use LinkedIn to create sales conversations without hiring SDRs first. / The useful part is usually the targeting, not the sending volume. / Would it be helpful to see the agency angle we're testing for {{companyName}}?"},
            {"author": "Kellen", "type": "general_comment", "target": "overall",
             "text": "On why he avoids the 'we will get you X meetings' angle: 'i just dont like that angle, not how i feel or "
                     "approach what i do, idk what i will get someone.'"},
        ],
        "outcome": "revised",
        "notes": "The clearest articulation of Kellen's five-lens review framework: motivation, targeting, skepticism, proof, CTA.",
    },
]
