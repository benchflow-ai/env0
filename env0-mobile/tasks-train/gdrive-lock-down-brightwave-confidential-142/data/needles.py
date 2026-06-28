"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1PNmgltw1O31TqkltujRNKjCMzSGMx5vGyUNidmzBLzd",
    "1hm8iPH4ZD5lHe0qAexQWJRKf3s7u992Kbwj8uhI5Dgk",
    "1t8L67YrOGeT5Z49Y0Pfh5IyUtiti33JSaaIarLX9fKs",
    "1NyRUZ4VQwV4Ze1lPBjaBIDijc6HYYErU2RXxnwsqmwc"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "8eb9223a8a9d435e7f3724b82326dcae",
    "5a51a64007af2cbcbe583a050ecefd5d",
    "f58787b55fc75324237257e91ddfedfb",
    "91406927b70f7e28c5124101ab8f7355"
]

LEGIT_PERM_IDS = [
    "6fad41a3808817f97a5c6c1e4b5452dc"
]

NEEDLES = [
    {
        "id": "1PNmgltw1O31TqkltujRNKjCMzSGMx5vGyUNidmzBLzd",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "8eb9223a8a9d435e7f3724b82326dcae",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1hm8iPH4ZD5lHe0qAexQWJRKf3s7u992Kbwj8uhI5Dgk",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "5a51a64007af2cbcbe583a050ecefd5d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1t8L67YrOGeT5Z49Y0Pfh5IyUtiti33JSaaIarLX9fKs",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f58787b55fc75324237257e91ddfedfb",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1NyRUZ4VQwV4Ze1lPBjaBIDijc6HYYErU2RXxnwsqmwc",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "91406927b70f7e28c5124101ab8f7355",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Arg2tN0wuCIHlL5hiQoWoJr4IAjLVquwXREuTukp6cV",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "12Tu4oJmDXQ0J7DTEzIFqhraoyYLwV0w0DXRFA539us8",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "6fad41a3808817f97a5c6c1e4b5452dc",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1GjCnREM91lJ9jHPG8DRPRHRucvFK12wMq0OnSQKxPIU",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1etfj3139wcnvP1iQccrmuy4DnrQrF4dKJCl2VH7b2vr",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1Q0KBUk0qFWy3h6FJoDi8sky1aVL7c8Y1Hf4EY4ZkeOF",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
