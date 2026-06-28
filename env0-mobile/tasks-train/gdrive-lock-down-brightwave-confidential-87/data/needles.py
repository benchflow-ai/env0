"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1kQlU9G6MmqTpgkFhTdqMfFWphr3TX6T8xvbexfkWlZr",
    "1vfEKUSVUIadOWyEd8uetVGZtAICm4EzavbvMHY03pY0",
    "1TYPEiSW9GnJ1TRZ2o4uoxS6K5M6fLtaNxqF1whZ3PPB",
    "1T448oCjRqOxVthazUEdzdJLUxZ1LQTdW5ApKW3Dol14"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "3c875b8d14098354ea94e0a215e02718",
    "74f06a56f16b6883de2e0d23bd8264d6",
    "89bef2d946a9af5cea57f73afa13c314",
    "cb779f6f59ede963e180e4b9dd47b066"
]

LEGIT_PERM_IDS = [
    "e44129122df3f6998034fb48691f822c",
    "8276961899629528a1235a28c9ec1fcb"
]

NEEDLES = [
    {
        "id": "1kQlU9G6MmqTpgkFhTdqMfFWphr3TX6T8xvbexfkWlZr",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "3c875b8d14098354ea94e0a215e02718",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vfEKUSVUIadOWyEd8uetVGZtAICm4EzavbvMHY03pY0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "74f06a56f16b6883de2e0d23bd8264d6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1TYPEiSW9GnJ1TRZ2o4uoxS6K5M6fLtaNxqF1whZ3PPB",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "89bef2d946a9af5cea57f73afa13c314",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1T448oCjRqOxVthazUEdzdJLUxZ1LQTdW5ApKW3Dol14",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "cb779f6f59ede963e180e4b9dd47b066",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "14wgH83XNVdlCZjBvUHY3gvTOsLBqtFB5F9rMer1SK5U",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e44129122df3f6998034fb48691f822c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "10Jc3X3aC52hXZJvnoGIHAF2F28il2sqBBLX0RLSPQsK",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1BJawhxFYrpsoqBi4ZxJBtWFIY36j9Zd91ziSDKuTL5s",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1wS0oEUlqK44Q3Hp884TiZ1aNuisVaV5gu8vBCXaBGHZ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1Mr976rLImbxWzwvXnicKhvHbwuSGO1BPNBW2YqEyxkj",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1w7FcnwKqVSaGWqthtvLjP3ABMxXPizcv2P73XTGmX26",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "8276961899629528a1235a28c9ec1fcb",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
