"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "12RqBBzXEYCGQ8JALoRGGA3sTaXIHl4rv8Sj2ndlut3E",
    "1rmmvg5zINiAXJSZV9HzScMmwGN3yXBIO5VcR3NFtsvW",
    "12q8M4lbVfa2hnr3MI4qmja5GTbNcHtufnqM9v7Nh8Ou"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "1a8023f10b864ae48e9863fae35fc3b0",
    "29a5c5c0cd33f3c71a2c32eb7deb8e50",
    "edbed5d925a0ce55107e380fa83d3590"
]

LEGIT_PERM_IDS = [
    "5aca64ca072adfc88712727c1ce63fd7",
    "03521b731d3c60fddce4d8157e5a8cc3"
]

NEEDLES = [
    {
        "id": "12RqBBzXEYCGQ8JALoRGGA3sTaXIHl4rv8Sj2ndlut3E",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "1a8023f10b864ae48e9863fae35fc3b0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1rmmvg5zINiAXJSZV9HzScMmwGN3yXBIO5VcR3NFtsvW",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "29a5c5c0cd33f3c71a2c32eb7deb8e50",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "12q8M4lbVfa2hnr3MI4qmja5GTbNcHtufnqM9v7Nh8Ou",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "edbed5d925a0ce55107e380fa83d3590",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1sDOc7NrEP9QAz1BhqPLDWRM7RWjxEE6oxe92L4RXN2G",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1gE8V2rVygzlfh78rZLoHInYcZTZZ6Pko6PjsGWJPQ4J",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1yCAJJ2tXh3lEkI9EXylrdfrCaIUZhUY9blwG28Mdkt5",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "5aca64ca072adfc88712727c1ce63fd7",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "180ehmQxKVmaRwq5ngLFDiTYDMwMneSzWOt1Hzhy8AxW",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "03521b731d3c60fddce4d8157e5a8cc3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
