"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1zNnCYa2yVFF88H3tUFoKkFKkIXxJsgHUlBsmL1dWLmb",
    "1Pl2n4bwn4LHlWInO8uwxNlCDUk4mwBWLTxEX1lMhYHB",
    "1cZxwLPJyDLlXFSS8CniPIeY1pCXZGB580jXS2Awv6M9",
    "1NVGytH35Du7fLljaGHbUTaW3rN8Kn1NNgLktNrE27GL",
    "19ILGn1qDmmWZFabhn2PL62gDIgfMQjJ5VeJiheA1BiF"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "a5628f9120ac786bcc14d1ef8302973a",
    "1d19d64c3e861f13c61a0ccff3334938",
    "a0ebeac89f44ec26475b1519db7425a6",
    "01ba45d1d11104d4337f60db7aaa4f67",
    "3a8fbf9d88c24953469a21bbf2345cb6"
]

LEGIT_PERM_IDS = [
    "844fa2c30080aace2ed48e00dab4283d",
    "77575c7fb5cb485ea39b9ef8a6c0402f",
    "61f2d50d2456b794fe6f27b263478eab"
]

NEEDLES = [
    {
        "id": "1zNnCYa2yVFF88H3tUFoKkFKkIXxJsgHUlBsmL1dWLmb",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "a5628f9120ac786bcc14d1ef8302973a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Pl2n4bwn4LHlWInO8uwxNlCDUk4mwBWLTxEX1lMhYHB",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1d19d64c3e861f13c61a0ccff3334938",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cZxwLPJyDLlXFSS8CniPIeY1pCXZGB580jXS2Awv6M9",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a0ebeac89f44ec26475b1519db7425a6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NVGytH35Du7fLljaGHbUTaW3rN8Kn1NNgLktNrE27GL",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "01ba45d1d11104d4337f60db7aaa4f67",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "19ILGn1qDmmWZFabhn2PL62gDIgfMQjJ5VeJiheA1BiF",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "3a8fbf9d88c24953469a21bbf2345cb6",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "19HGnZcMpCif2hfkuJ66oEmPNcmgQc2LvQ82RiTuYIMc",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "844fa2c30080aace2ed48e00dab4283d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1S34V554dSLCVplLGXhV2YT8n5MkyTiW201GQfRtShfm",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "77575c7fb5cb485ea39b9ef8a6c0402f",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1S1GqfyLffT15TAHOeOdgrW7WjjXtdqx1iExvXOOCklt",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1weshYz6glhstf5JthfW0cuhixl3E4u7P2LYt6F7XZcO",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1yhGtrQqdwHGttwElXFyChJYzac1Hx7rElweb4HG9Mt6",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "61f2d50d2456b794fe6f27b263478eab",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
