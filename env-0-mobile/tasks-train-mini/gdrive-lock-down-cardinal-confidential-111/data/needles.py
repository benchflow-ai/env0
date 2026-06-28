"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1BPII6EBph82z32ERtxbHVykwoEgfawl5XoLg886joEW",
    "13bMgGmjdVBMWRgQKqmK4HDUZYfw3hLKoykqZzFnGFOS",
    "1HoMZbz2oVqbygMhgIbClOrstp1XyrcOJWDoP8Yu6BEl",
    "16ZeFXfeyTYyBLZwQxXf9RpFTeBwjv8rCkauLx55ZtUT",
    "1bAEEaP2egTLB5Lufn85a2p5f2HkZ9NT0HweB9TaDo2Q"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "0325ddc4760baab72d30f1a00ec8cb86",
    "111c6e9b88b935ef3b4114a5f508876a",
    "7c77ef052ad3a21a99332198bac52603",
    "c2fea9acec5ec854819c4232b5789e78",
    "3ff70be653b4335dc35039617d71005c"
]

LEGIT_PERM_IDS = [
    "6e3e9ce41e1eed66dd87d27b157dac7d",
    "2e8125285b13fc445d9793d131fe225d"
]

NEEDLES = [
    {
        "id": "1BPII6EBph82z32ERtxbHVykwoEgfawl5XoLg886joEW",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "0325ddc4760baab72d30f1a00ec8cb86",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13bMgGmjdVBMWRgQKqmK4HDUZYfw3hLKoykqZzFnGFOS",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "111c6e9b88b935ef3b4114a5f508876a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1HoMZbz2oVqbygMhgIbClOrstp1XyrcOJWDoP8Yu6BEl",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "7c77ef052ad3a21a99332198bac52603",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "16ZeFXfeyTYyBLZwQxXf9RpFTeBwjv8rCkauLx55ZtUT",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "c2fea9acec5ec854819c4232b5789e78",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1bAEEaP2egTLB5Lufn85a2p5f2HkZ9NT0HweB9TaDo2Q",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3ff70be653b4335dc35039617d71005c",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ReZfC666am87qzXc2hDMuTxQDBvmJPMN8mimeeVIKFP",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1yPvt0fUyYncKq9lMNkDRRn1OTVoHlxXLJJnxZo8wtf1",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "6e3e9ce41e1eed66dd87d27b157dac7d",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1iKOHkjbf7He4fwnX8bY7zvWTrQnpVCQqdMUuw49rtt1",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1WZiusbpHcoXixms0pgbimelLpW2Ke4Aq9gM5FsPIPW0",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "2e8125285b13fc445d9793d131fe225d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1xdJQdf1i8dfl7BCdRdk3YNXHd7vImOu9wTAJR4dgmij",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
