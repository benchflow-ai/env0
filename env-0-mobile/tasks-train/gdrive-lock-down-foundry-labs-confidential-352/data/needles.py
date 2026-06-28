"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1X56Jb88lKV4FaFOiZiqEf17d5OXylBDFF2mK72ACFla",
    "1bGGtJ4Fo0ieI7t3asOnaXOIRHqBEMPIN0Xju77UIl4B",
    "16bTp2ZUabba9AAAdX9ga84z9czPe4ph7DjKJhOMwp59"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "6f621475a75433f1ea4b11997b8f598a",
    "3fffc0a860032e867fe43f2c23b898e9",
    "d4d500b55c890808dd17cd6c2fce58f1"
]

LEGIT_PERM_IDS = [
    "0333933e76d97c7bf8dc671beb5e5182",
    "66d47c46186dcbf11630273b32c86e66",
    "04255c702fd39b9a550086ec5e75b7d2"
]

NEEDLES = [
    {
        "id": "1X56Jb88lKV4FaFOiZiqEf17d5OXylBDFF2mK72ACFla",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "6f621475a75433f1ea4b11997b8f598a",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1bGGtJ4Fo0ieI7t3asOnaXOIRHqBEMPIN0Xju77UIl4B",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3fffc0a860032e867fe43f2c23b898e9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "16bTp2ZUabba9AAAdX9ga84z9czPe4ph7DjKJhOMwp59",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "d4d500b55c890808dd17cd6c2fce58f1",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1B2TZg59nZyIwf13MROOxomfr2u998lmwx5ssNSQDnTi",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1fzxDzjY69cLVWUSmUDZdum9PaW4gwxuWe83teSihbKg",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0333933e76d97c7bf8dc671beb5e5182",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fzAl4xkHuW5y8fMjQgfyxACwVctcjehh6URnJTIVKWH",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "19wHTQ9JyJ5Umzmr4u6m5eYE1zgdo3fGKUKj5NIFrB6m",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "66d47c46186dcbf11630273b32c86e66",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1IjkyesB6DZPBfPPiQ6YzUTpvei5qymrm9zikyF3I1Kg",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "04255c702fd39b9a550086ec5e75b7d2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
