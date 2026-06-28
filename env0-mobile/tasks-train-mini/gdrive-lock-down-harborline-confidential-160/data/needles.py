"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1le2GorIIbZuIMJ02NjBEH0XQLTq3BUpauuFX6hlTier",
    "1adCWwL41hiyXyJxXdOvWNwRslCSCxlfXy8UEJdofOtH",
    "1JN9Ljl5OIQe2KgUWkXyUTkVoXAgLtsB2vTbFMvUTwI0",
    "1irf8vmEvqPwMvxE8tvyyKJpW7Uwe3kBDXym3KVdAc1o",
    "1G8VLd5qL24wwzdNHK19RqjHeKq71ZygadVau7Jsverf"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "65e4c474dd9629232fb6ef2b2c2f1341",
    "c3fe96e75b1a5e7f4605078a11c5fe24",
    "74429887a8a1d016f045d234ba0fe072",
    "44984c5f4295cc0da99f244563164272",
    "4fc3b577258018536c019b806ba0cbb5"
]

LEGIT_PERM_IDS = [
    "5f852fb1e7d35041d24676c47ce621c8",
    "f532f2a491e781471e0afc75ea1bb046"
]

NEEDLES = [
    {
        "id": "1le2GorIIbZuIMJ02NjBEH0XQLTq3BUpauuFX6hlTier",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "65e4c474dd9629232fb6ef2b2c2f1341",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1adCWwL41hiyXyJxXdOvWNwRslCSCxlfXy8UEJdofOtH",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "c3fe96e75b1a5e7f4605078a11c5fe24",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JN9Ljl5OIQe2KgUWkXyUTkVoXAgLtsB2vTbFMvUTwI0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "74429887a8a1d016f045d234ba0fe072",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1irf8vmEvqPwMvxE8tvyyKJpW7Uwe3kBDXym3KVdAc1o",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "44984c5f4295cc0da99f244563164272",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1G8VLd5qL24wwzdNHK19RqjHeKq71ZygadVau7Jsverf",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "4fc3b577258018536c019b806ba0cbb5",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1oNfyg7tGOHvdGB3JpmuZF5iU2wgJ9Jl9bBOPvu12hzl",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "5f852fb1e7d35041d24676c47ce621c8",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1jesPDvWpNzm0AAEihihTDyBBlFTtolI1sPlsNH4HOF2",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1LnkpA7RtYDnriirkS2P4cT19nSTZmqEBpJ2AypZMU1Q",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1TxOiqbZ4Pkp3o3xRFxF2ZWXpadESrg28SGhvFGKog70",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1ziA2YkNYhPDqGUnpN8Bw2KAPCxXkxtyxJ5CdERxkwwx",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f532f2a491e781471e0afc75ea1bb046",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
