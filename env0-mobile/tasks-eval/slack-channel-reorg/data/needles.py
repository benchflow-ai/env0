"""Seed data for slack-channel-reorg task.

Scenario:
  The Metaverse division is being shut down. Five other teams have opened
  internal talent-match channels. The agent must read each Metaverse
  member's Slack profile (title field) and add them to the channel whose
  skills requirements match. Slot limits and seniority gates apply.

  Two additional engineers (diana_fox, noah_patel) are hidden in the
  private #metaverse-stealth channel. The agent must DM chris_taylor
  (the EM) to be auto-invited to that channel.

  Correct placements (11 people across 5 channels):
    platform-team-hiring  : james_wright, alex_johnson, diana_fox
                            (Senior ICs only, 3 slots)
    aiml-team-hiring      : kevin_liu, ryan_kim, noah_patel
    commerce-team-hiring  : emma_davis, sophie_martin
                            (2 slots)
    infra-team-hiring     : priya_sharma
    product-team-hiring   : sarah_chen, lisa_park

  Unmatched (6 people):
    - chris_taylor   Engineering Manager — no manager slots open
    - mike_torres    AR/VR PM — too specialised, no AR/VR team hiring
    - mia_garcia     Vue.js frontend — no Vue teams hiring
    - david_lee      Ruby on Rails backend — no Ruby teams hiring
    - natalie_brown  Junior Python engineer — platform is Senior-only
    - tom_wilson     Frontend engineer (Tailwind/Storybook) — no matching team
"""

# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

SEED_USERS = [
    # ---- Metaverse team: PMs ----
    {
        "key": "sarah_chen",
        "name": "sarah.chen",
        "real_name": "Sarah Chen",
        "email": "sarah.chen@company.com",
        "title": "Senior Product Manager · Product Strategy · User Research · Go-to-Market",
    },
    {
        "key": "mike_torres",
        "name": "mike.torres",
        "real_name": "Mike Torres",
        "email": "mike.torres@company.com",
        "title": "Product Manager · Spatial Computing · AR/VR · Immersive Experiences",
    },
    {
        "key": "lisa_park",
        "name": "lisa.park",
        "real_name": "Lisa Park",
        "email": "lisa.park@company.com",
        "title": "Product Manager · Growth Analytics · A/B Testing · Conversion Optimisation",
    },
    # ---- Metaverse team: Senior Engineers ----
    {
        "key": "james_wright",
        "name": "james.wright",
        "real_name": "James Wright",
        "email": "james.wright@company.com",
        "title": "Senior Backend Engineer · Go · gRPC · Distributed Systems · Microservices",
    },
    {
        "key": "emma_davis",
        "name": "emma.davis",
        "real_name": "Emma Davis",
        "email": "emma.davis@company.com",
        "title": "Senior Frontend Engineer · React · TypeScript · WebGL · Three.js",
    },
    {
        "key": "kevin_liu",
        "name": "kevin.liu",
        "real_name": "Kevin Liu",
        "email": "kevin.liu@company.com",
        "title": "Senior ML Engineer · PyTorch · Computer Vision · CUDA · Neural Rendering",
    },
    {
        "key": "priya_sharma",
        "name": "priya.sharma",
        "real_name": "Priya Sharma",
        "email": "priya.sharma@company.com",
        "title": "Senior Infrastructure Engineer · Kubernetes · AWS · Terraform · GitOps",
    },
    {
        "key": "alex_johnson",
        "name": "alex.johnson",
        "real_name": "Alex Johnson",
        "email": "alex.johnson@company.com",
        "title": "Senior Backend Engineer · Python · FastAPI · PostgreSQL · Event-Driven Architecture",
    },
    {
        "key": "chris_taylor",
        "name": "chris.taylor",
        "real_name": "Chris Taylor",
        "email": "chris.taylor@company.com",
        "title": "Engineering Manager · Metaverse Platform · Team Leadership · Technical Roadmap",
    },
    # ---- Metaverse team: Junior Engineers ----
    {
        "key": "tom_wilson",
        "name": "tom.wilson",
        "real_name": "Tom Wilson",
        "email": "tom.wilson@company.com",
        "title": "Frontend Engineer · Tailwind CSS · Storybook · Accessibility · Figma",
    },
    {
        "key": "natalie_brown",
        "name": "natalie.brown",
        "real_name": "Natalie Brown",
        "email": "natalie.brown@company.com",
        "title": "Backend Engineer · Python · Django · REST APIs · Celery",
    },
    {
        "key": "ryan_kim",
        "name": "ryan.kim",
        "real_name": "Ryan Kim",
        "email": "ryan.kim@company.com",
        "title": "ML Engineer · TensorFlow · Data Pipelines · Feature Engineering · Pandas",
    },
    {
        "key": "mia_garcia",
        "name": "mia.garcia",
        "real_name": "Mia Garcia",
        "email": "mia.garcia@company.com",
        "title": "Frontend Engineer · Vue.js · Nuxt.js · GSAP · Motion Design",
    },
    {
        "key": "david_lee",
        "name": "david.lee",
        "real_name": "David Lee",
        "email": "david.lee@company.com",
        "title": "Backend Engineer · Ruby on Rails · Sidekiq · PostgreSQL · Shopify Integrations",
    },
    {
        "key": "sophie_martin",
        "name": "sophie.martin",
        "real_name": "Sophie Martin",
        "email": "sophie.martin@company.com",
        "title": "Full-Stack Engineer · Node.js · React · MongoDB · Serverless · AWS Lambda",
    },
    # ---- Metaverse Stealth Project (hidden in private channel) ----
    {
        "key": "diana_fox",
        "name": "diana.fox",
        "real_name": "Diana Fox",
        "email": "diana.fox@company.com",
        "title": "Senior Platform Engineer · Go · gRPC · Distributed Systems · Service Mesh",
    },
    {
        "key": "noah_patel",
        "name": "noah.patel",
        "real_name": "Noah Patel",
        "email": "noah.patel@company.com",
        "title": "Senior ML Research Engineer · PyTorch · NLP · Transformer Models · RLHF",
    },
    # ---- Non-Metaverse: department leads + HR ----
    {
        "key": "hr_admin",
        "name": "hr.admin",
        "real_name": "HR Admin",
        "email": "hr@company.com",
        "title": "HR Business Partner · Talent Mobility · Internal Transfers",
    },
    {
        "key": "platform_lead",
        "name": "platform.lead",
        "real_name": "Platform Team Lead",
        "email": "platform-lead@company.com",
        "title": "Engineering Lead · Platform · Backend Systems · Distributed Infrastructure",
    },
    {
        "key": "aiml_lead",
        "name": "aiml.lead",
        "real_name": "AI/ML Team Lead",
        "email": "aiml-lead@company.com",
        "title": "Engineering Lead · AI/ML · Applied Research · Model Deployment",
    },
    {
        "key": "commerce_lead",
        "name": "commerce.lead",
        "real_name": "Commerce Team Lead",
        "email": "commerce-lead@company.com",
        "title": "Engineering Lead · Commerce · Frontend Systems · Consumer Experience",
    },
    {
        "key": "infra_lead",
        "name": "infra.lead",
        "real_name": "Infrastructure Team Lead",
        "email": "infra-lead@company.com",
        "title": "Engineering Lead · Infrastructure · SRE · Platform Reliability",
    },
    {
        "key": "product_lead",
        "name": "product.lead",
        "real_name": "Product Team Lead",
        "email": "product-lead@company.com",
        "title": "Director of Product · Consumer Products · Strategy · Org Growth",
    },
]

# Shorthand for all 15 Metaverse members
_METAVERSE_ALL = [
    "sarah_chen", "mike_torres", "lisa_park",
    "james_wright", "emma_davis", "kevin_liu", "priya_sharma", "alex_johnson", "chris_taylor",
    "tom_wilson", "natalie_brown", "ryan_kim", "mia_garcia", "david_lee", "sophie_martin",
]

# Engineering channel: 9 engineers + EM (chris_taylor)
# Missing from here: PMs (sarah, mike, lisa), mia_garcia, david_lee
_METAVERSE_ENGINEERS = [
    "james_wright", "emma_davis", "kevin_liu", "priya_sharma", "alex_johnson", "chris_taylor",
    "tom_wilson", "natalie_brown", "ryan_kim", "sophie_martin",
]

# Product channel: PMs + EM + james_wright (tech lead) + kevin_liu (ML research)
# Creates overlap: chris_taylor in all 3, james_wright/kevin_liu in 2
_METAVERSE_PRODUCT = ["sarah_chen", "mike_torres", "lisa_park", "chris_taylor", "james_wright", "kevin_liu"]

# ---------------------------------------------------------------------------
# Channels
# ---------------------------------------------------------------------------

SEED_CHANNELS = [
    # ---- Metaverse source channels ----
    {
        "name": "metaverse-general",
        "is_private": False,
        "creator": "chris_taylor",
        "topic": "General announcements for the Metaverse division",
        "purpose": "Company-wide Metaverse team channel",
        "members": _METAVERSE_ALL + ["hr_admin"],
    },
    {
        "name": "metaverse-engineering",
        "is_private": False,
        "creator": "chris_taylor",
        "topic": "Engineering discussions for the Metaverse platform",
        "purpose": "Metaverse engineering team",
        "members": _METAVERSE_ENGINEERS,
    },
    {
        "name": "metaverse-product",
        "is_private": False,
        "creator": "sarah_chen",
        "topic": "Product roadmap and PM discussions",
        "purpose": "Metaverse product team — PMs, EM, and cross-functional leads",
        "members": _METAVERSE_PRODUCT,
    },
    # ---- Private stealth channel (hidden members, access via DM trigger) ----
    {
        "name": "metaverse-stealth",
        "is_private": True,
        "creator": "chris_taylor",
        "topic": "Metaverse Stealth Project — confidential",
        "purpose": (
            "Private channel for the Metaverse Stealth Project sub-team. "
            "These engineers were not publicly announced and are not in the main Metaverse channels. "
            "They must also be included in the reorg placement process."
        ),
        "members": ["chris_taylor", "diana_fox", "noah_patel"],
    },
    # ---- Destination: internal talent-match channels ----
    {
        "name": "platform-team-hiring",
        "is_private": False,
        "creator": "platform_lead",
        "topic": "Internal talent match — Platform team · Senior ICs only · 3 slots",
        "purpose": (
            "Seeking Senior-level backend ICs with production experience in Go or Python "
            "(gRPC, FastAPI, Django, distributed systems, microservices, event-driven architecture). "
            "We have 3 open slots and are hiring Senior Engineers only — "
            "junior and mid-level engineers are not a fit for this round. "
            "Note: Ruby/Rails, PHP, or language-agnostic generalists are also not a fit. "
            "Engineering managers and non-IC roles are out of scope."
        ),
        "members": ["platform_lead", "hr_admin"],
    },
    {
        "name": "aiml-team-hiring",
        "is_private": False,
        "creator": "aiml_lead",
        "topic": "Internal talent match — AI/ML team",
        "purpose": (
            "Seeking ML Engineers with hands-on experience in PyTorch or TensorFlow — "
            "model training, computer vision, neural rendering, or ML data pipelines. "
            "Note: general backend engineers or data analysts without ML framework experience are not a fit."
        ),
        "members": ["aiml_lead", "hr_admin"],
    },
    {
        "name": "commerce-team-hiring",
        "is_private": False,
        "creator": "commerce_lead",
        "topic": "Internal talent match — Commerce team · 2 slots remaining",
        "purpose": (
            "Seeking frontend and full-stack engineers whose primary stack is React or TypeScript "
            "(Next.js, Node.js, serverless, WebGL welcome). "
            "We have 2 open slots remaining — once filled, further candidates cannot be accommodated this round. "
            "Note: our stack is React-based — Vue.js or Angular specialists without React experience are not a match."
        ),
        "members": ["commerce_lead", "hr_admin"],
    },
    {
        "name": "infra-team-hiring",
        "is_private": False,
        "creator": "infra_lead",
        "topic": "Internal talent match — Infrastructure team",
        "purpose": (
            "Seeking infrastructure and SRE engineers with hands-on Kubernetes, Terraform, or GitOps experience. "
            "Must have operated cloud infrastructure at scale (AWS, GCP). "
            "Note: general backend engineers or DevOps generalists without IaC/container-orchestration depth are not a fit."
        ),
        "members": ["infra_lead", "hr_admin"],
    },
    {
        "name": "product-team-hiring",
        "is_private": False,
        "creator": "product_lead",
        "topic": "Internal talent match — Product team",
        "purpose": (
            "Seeking data-driven Product Managers with a background in growth, A/B testing, "
            "conversion optimisation, user research, or go-to-market strategy. "
            "Note: PMs specialised in spatial computing, AR/VR, or hardware are not aligned with our consumer analytics roadmap. "
            "Engineering managers are out of scope."
        ),
        "members": ["product_lead", "hr_admin"],
    },
]

# ---------------------------------------------------------------------------
# Messages — #metaverse-general announcement thread
# ---------------------------------------------------------------------------

SEED_MESSAGES = {
    "metaverse-general": [
        # Layoff announcement thread (10 days ago)
        {
            "sender": "chris_taylor",
            "text": (
                "Team — I have some very difficult news to share. After much deliberation, "
                "leadership has decided to wind down the Metaverse division. "
                "This is effective at the end of the month. I know this is hard to hear. "
                "HR will reach out individually to discuss next steps and severance. "
                "I'm incredibly proud of what we built together."
            ),
            "days_ago": 10,
            "thread": [
                {
                    "sender": "emma_davis",
                    "text": "This is devastating news. Thank you for telling us directly, Chris.",
                },
                {
                    "sender": "james_wright",
                    "text": "Appreciate the transparency. What's the timeline for internal transfers?",
                },
                {
                    "sender": "hr_admin",
                    "text": (
                        "Hi all — HR here. We've set up internal talent-match channels for teams "
                        "that are actively hiring from the Metaverse reorg pool. "
                        "Check #platform-team-hiring, #aiml-team-hiring, #commerce-team-hiring, "
                        "#infra-team-hiring, and #product-team-hiring. "
                        "Each channel's topic describes the skills they're looking for. "
                        "We'll be coordinating placements over the next two weeks."
                    ),
                },
                {
                    "sender": "kevin_liu",
                    "text": "Thanks for the info. Will the hiring managers reach out, or do we self-nominate?",
                },
                {
                    "sender": "hr_admin",
                    "text": (
                        "We'll be facilitating the match based on your Slack profiles. "
                        "Make sure your title/bio is up to date so we can match you accurately. "
                        "Not everyone will have a match — some skills don't align with current openings, "
                        "and that's okay. We'll communicate clearly either way."
                    ),
                },
                {
                    "sender": "mia_garcia",
                    "text": "Are there any frontend roles? I work primarily in Vue.js.",
                },
                {
                    "sender": "commerce_lead",
                    "text": (
                        "Hi Mia — our Commerce team is hiring frontend engineers but we're "
                        "a React/TypeScript shop. Vue experience is valuable but we'd need "
                        "React as the primary skill. Tough call on our side."
                    ),
                },
                {
                    "sender": "david_lee",
                    "text": "Any Rails teams? That's my main stack.",
                },
                {
                    "sender": "hr_admin",
                    "text": (
                        "David — unfortunately none of the five participating teams use Ruby on Rails. "
                        "We'll flag you as unmatched and explore options with other divisions "
                        "outside this round."
                    ),
                },
                {
                    "sender": "priya_sharma",
                    "text": "Is the infra channel looking for SRE or pure DevOps? I do both.",
                },
                {
                    "sender": "infra_lead",
                    "text": "Priya — both! We need someone who can wear either hat. You'd be a great fit.",
                },
            ],
        },
        # Follow-up message (8 days ago)
        {
            "sender": "hr_admin",
            "text": (
                "Reminder: the internal talent match process is underway. "
                "If you have questions about your placement, reply in this channel or DM me directly. "
                "The goal is to have everyone placed (or officially marked unmatched) within 10 days."
            ),
            "days_ago": 8,
        },
        # Mike Torres follow-up (7 days ago)
        {
            "sender": "mike_torres",
            "text": (
                "Any product teams interested in someone with a spatial computing background? "
                "I've been focused on AR/VR for 3 years — happy to pivot but wanted to flag my niche."
            ),
            "days_ago": 7,
        },
        {
            "sender": "product_lead",
            "text": (
                "Mike — appreciate you flagging. Our product team is focused on e-commerce and "
                "consumer analytics right now. AR/VR is a fascinating area but doesn't align with "
                "our current roadmap. We'll mark you as unmatched for this round."
            ),
            "days_ago": 7,
        },
        # Sophie Martin question (6 days ago)
        {
            "sender": "sophie_martin",
            "text": "Is the commerce team open to full-stack profiles or strictly frontend?",
            "days_ago": 6,
        },
        {
            "sender": "commerce_lead",
            "text": (
                "Sophie — full-stack is great! We need someone who can own both the React frontend "
                "and the Node.js backend services. Your profile looks like a strong fit."
            ),
            "days_ago": 6,
        },
        # Chris Taylor note (5 days ago)
        {
            "sender": "chris_taylor",
            "text": (
                "For those wondering about my own placement — as EM I'm working directly with "
                "VP Engineering on options outside the standard reorg pool. "
                "Don't worry about me, focus on your own process."
            ),
            "days_ago": 5,
        },
        # Stealth team hint (4 days ago)
        {
            "sender": "chris_taylor",
            "text": (
                "One more heads-up for whoever is coordinating the placement: "
                "there are two engineers from the Metaverse Stealth Project who were on a "
                "separate private channel (#metaverse-stealth) and are not in the main Metaverse channels. "
                "They also need to be included in the reorg. DM me if you need access to that channel."
            ),
            "days_ago": 4,
        },
    ],
    "metaverse-engineering": [
        {
            "sender": "james_wright",
            "text": "Keeping this channel open for any eng-specific questions during the transition.",
            "days_ago": 9,
        },
        {
            "sender": "natalie_brown",
            "text": "Should we update our Slack profiles before HR runs the matching? Want to make sure my Python/Django experience is visible.",
            "days_ago": 8,
        },
        {
            "sender": "james_wright",
            "text": "Yes — HR confirmed they're reading the title field on your Slack profile. Make sure it's current.",
            "days_ago": 8,
        },
        {
            "sender": "ryan_kim",
            "text": "Mine has TensorFlow and Pandas listed. Should cover the ML angle.",
            "days_ago": 8,
        },
    ],
    "metaverse-product": [
        {
            "sender": "sarah_chen",
            "text": "Lisa and I are both hoping for product-team-hiring. Our backgrounds are complementary — strategy vs growth.",
            "days_ago": 9,
        },
        {
            "sender": "lisa_park",
            "text": "Agreed. Fingers crossed the product team has two slots.",
            "days_ago": 9,
        },
        {
            "sender": "mike_torres",
            "text": "I'm less optimistic for myself given my AR/VR focus. Will see what comes up.",
            "days_ago": 9,
        },
    ],
}

# ---------------------------------------------------------------------------
# Invite triggers (DM-based access control for private channels)
# ---------------------------------------------------------------------------

# When the bot sends a DM to chris_taylor, it is auto-invited to #metaverse-stealth.
# This simulates chris_taylor (the EM) granting the placement bot access.
SEED_INVITE_TRIGGERS = [
    {"grant_channel": "metaverse-stealth", "when_dm_to": "chris_taylor"},
]

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

FILL_CONFIG = {
    "base_scenario": "default",
}
