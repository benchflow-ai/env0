"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1sPgj4ZEI7SCniPzZdkKRNI9OthirnjiipzA70xG1HTB",
    "1LemxCJSyY1Vb8EBRGVG38cOPiGpeImjkIzKjxGjhegw",
    "15g3rJTJzWovscmrRkXFthPm9CDdUOEw7aZTf1xPIKO1"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "67471a210f4f6e8133271d359522e6f1",
    "97d7753124712cdb4650b8ca2a025e32",
    "43e8fc17b76d9642c2135811d01b0358"
]

LEGIT_PERM_IDS = [
    "4666f0b00610c8fbc8c9a17cfb91d610",
    "8f379ffb038637d70311a4cef9752414",
    "e0da9524c10b5704a6f2aa9915a67ba1"
]

NEEDLES = [
    {
        "id": "1sPgj4ZEI7SCniPzZdkKRNI9OthirnjiipzA70xG1HTB",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "67471a210f4f6e8133271d359522e6f1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LemxCJSyY1Vb8EBRGVG38cOPiGpeImjkIzKjxGjhegw",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "97d7753124712cdb4650b8ca2a025e32",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "15g3rJTJzWovscmrRkXFthPm9CDdUOEw7aZTf1xPIKO1",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "43e8fc17b76d9642c2135811d01b0358",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1HMvDmEI7chwefjtsjJJvAOOj6oMP6bSGHyqPY60sORc",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1ltijf6ZjJ4oYiBJJXMwBd2qb1p8LX50B1U0qJamQ0fN",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1M5eByZeF8zTRB42JgSovMUMZHrbmgTw3nhjpx6u6jnh",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "18vDukG8D4aoGNOdHkEyeVJ5aiIPlOUnkmDUssnAzS25",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "4666f0b00610c8fbc8c9a17cfb91d610",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "11Wk2Hl6pj4weA4kx8qoEbX5AflTmp0yXP5EW4obv4KL",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "8f379ffb038637d70311a4cef9752414",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1UIbwlfyglDcLz0OB84aTNknjaSOlPPdl7nW0zi6tBW7",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "e0da9524c10b5704a6f2aa9915a67ba1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
