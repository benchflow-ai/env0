"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1MiMJNGoqkSHzEuseElD1gZC0MeuwgihRZhvHQap85Nv",
    "1tOFtYh1enacvmVLSwhG6kVsC2lJNm2tw2SN5tPf83NT",
    "1akkZZ4XOfdQDELvWBVqioT8yeg8scobnYAhEoYG2BfU"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "251d408e4a7f4507fb629e389c91492b",
    "44484128bb3814aa80230e40725a23df",
    "c5c88ef8b6d576fb39a1a2e2538eeb68"
]

LEGIT_PERM_IDS = [
    "cf82475994f918d0301de783c6a75147",
    "031611ab497860fe58e7d1798c05c771",
    "0ea19b7171f462cc84dca3ea84d72cae"
]

NEEDLES = [
    {
        "id": "1MiMJNGoqkSHzEuseElD1gZC0MeuwgihRZhvHQap85Nv",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "251d408e4a7f4507fb629e389c91492b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tOFtYh1enacvmVLSwhG6kVsC2lJNm2tw2SN5tPf83NT",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "44484128bb3814aa80230e40725a23df",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1akkZZ4XOfdQDELvWBVqioT8yeg8scobnYAhEoYG2BfU",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c5c88ef8b6d576fb39a1a2e2538eeb68",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1up9PlpQ2hOxGmHDfnVp4Bk6eFbu5MUCYLkHtedIUlTD",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "10uRFctPCFYmpiFoBNg2DulkVlT8Yq7j7FucisreWvb0",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "cf82475994f918d0301de783c6a75147",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1wp3EDKqNcScM5ohH0iVx0tx5psxbEpGmgdW7h2OdJZ9",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1bP0yaiTBd4lkxFaooRWsEbmQPf8TL8JAQU9BYzycp1X",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1D4qiKFns8p10nmVxgHWt2GmGpVDQSKO4S7em14tWgBF",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "031611ab497860fe58e7d1798c05c771",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1Qd7dbrY2BErH4qGZCnarKyKubGnbLBOUf65oyaSpf5p",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0ea19b7171f462cc84dca3ea84d72cae",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
