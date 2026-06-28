"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1WKolLRdS252Vlw7O3UJbzOWwoV1HGnTXCkmXA80BcRk",
    "1vMeOQtjolYD2b5RwVsRqfKukslvn3dqhDHt5ptV4ix1",
    "1bobPzbEBrdMEAJUcTxr9FPUYqNjtVvOlDQKc8V2rIgB",
    "144gFHQkPQwMF0pxHrw6BKnzyMc0BjfyjGIX8oGvFLMB",
    "1jnsE1xL6QXfOKB5MMfyevQx7hjD1wPePSQpnb5NvDC8"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "7c29552a699be6d704f7c1a67d843a3f",
    "8967bdacf28372171bb6824adb5350bb",
    "fee5b9b7969b5c0da59838a985ec1bb0",
    "4255273fc0cf409670bdc4a4fb1ce343",
    "2a2eaea71cf145848fe8a215efab4fbb"
]

LEGIT_PERM_IDS = [
    "a33d4959bc6dfd47256b84890d5e5eeb",
    "f381eeb8c276f94f2b71bbf89bf40f26",
    "1c736619b35ad6f9d71f59a312ffc39d"
]

NEEDLES = [
    {
        "id": "1WKolLRdS252Vlw7O3UJbzOWwoV1HGnTXCkmXA80BcRk",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "7c29552a699be6d704f7c1a67d843a3f",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1vMeOQtjolYD2b5RwVsRqfKukslvn3dqhDHt5ptV4ix1",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "8967bdacf28372171bb6824adb5350bb",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bobPzbEBrdMEAJUcTxr9FPUYqNjtVvOlDQKc8V2rIgB",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "fee5b9b7969b5c0da59838a985ec1bb0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "144gFHQkPQwMF0pxHrw6BKnzyMc0BjfyjGIX8oGvFLMB",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "4255273fc0cf409670bdc4a4fb1ce343",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1jnsE1xL6QXfOKB5MMfyevQx7hjD1wPePSQpnb5NvDC8",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "2a2eaea71cf145848fe8a215efab4fbb",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1QV8XnJtNBhz7FkGwQkThfIsx2yFhBMhDipstnOoEbxT",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1s9n7bRb572XrrROtXXT4DnJh6UZv5N08OiCnmJPDkWD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a33d4959bc6dfd47256b84890d5e5eeb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Qs1RlcOO0xJkCbJ0uY2TuAinResgARDhqXJTPRRMKtW",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1sZYms7NPNYyQdGib3eg70y5wOb92tuAPYJ3ab8nj6Et",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1Cv6A2SR7G1fRJkxkGUwbuY7CneAqQgRUCgNhqz31sGi",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f381eeb8c276f94f2b71bbf89bf40f26",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1SfHsh7R64Qa396PJFF7tY3m1P1TSmXvBhhy4RTmNPtW",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "1c736619b35ad6f9d71f59a312ffc39d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
