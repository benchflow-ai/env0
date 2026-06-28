"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1pLnN6Ovj2EWnyOz1yvXPOkki9I3apshj6cTrZZXDmMg",
    "1wnkEYZlRSZuiiQ4NGpS8xLzcuQ7lHe7Pjm7HZhZ62ql",
    "1fv6HMngUTBX9xvj9ZAo4DaArqwgEB6Syef96tSB7suz",
    "13JyyD8Sq2yquBT80ozBCP9ZNb7qv6Tw1BoT0yxe2BNH",
    "1TIkTsXpTILOXtE9qq05HBVJTX116RURqobLV2POVYAT"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "7d54f0a9f33ff4e2ef289b06adacdf8f",
    "6a6506f0c59952b278ce9a218f04a35c",
    "338c4a067866ce0c2caa141684fb51ea",
    "4e52200513719f922eced814c500f85a",
    "d9bd9bd2a97f653c3b38881c55bdf674"
]

LEGIT_PERM_IDS = [
    "f52b84699c077bad963cc60ae6e4c23c",
    "25fafe29fa67539fed65ae44459769ea"
]

NEEDLES = [
    {
        "id": "1pLnN6Ovj2EWnyOz1yvXPOkki9I3apshj6cTrZZXDmMg",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7d54f0a9f33ff4e2ef289b06adacdf8f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1wnkEYZlRSZuiiQ4NGpS8xLzcuQ7lHe7Pjm7HZhZ62ql",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "6a6506f0c59952b278ce9a218f04a35c",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1fv6HMngUTBX9xvj9ZAo4DaArqwgEB6Syef96tSB7suz",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "338c4a067866ce0c2caa141684fb51ea",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "13JyyD8Sq2yquBT80ozBCP9ZNb7qv6Tw1BoT0yxe2BNH",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "4e52200513719f922eced814c500f85a",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1TIkTsXpTILOXtE9qq05HBVJTX116RURqobLV2POVYAT",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "d9bd9bd2a97f653c3b38881c55bdf674",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1aQ6MggwgdCkJW29f8ymiDPUc7ZV8nmz56MM9QTtLzul",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "114qZ4kBLWdTXW0TbYwcrggfpkH75yDzxm1KNbRxbah9",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f52b84699c077bad963cc60ae6e4c23c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1UxFC1a0SbLVQ2YZMrC6n4a95WUu3sKskPeby22zf0kv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "25fafe29fa67539fed65ae44459769ea",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1uSP2DosvzxhFaOGla06FmIrCjT4OjVpksxDgMMk0qb8",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1BZJchuW62NHZdKHMYbbat2iEQmImBbFHHfpL4n3YXkU",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
