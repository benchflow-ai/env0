"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1NtodpMwS1jo4iAxt1SYb06UpCzvZyQnWLoHyRjTyJEs",
    "19klXlxD3Eu80MDEMt30erzcrXpaxGe1aGVv09qFUjs4",
    "1sxBq8Uu3twj0Yv31nieXMBjGekuURzfz6ZhQtKDKdBz"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "af0f63f269908413f92a33cf05689d82",
    "9327d7d477ba8a23b062d3ce491c827e",
    "373014d67fdcba6ef6495593ca90594e"
]

LEGIT_PERM_IDS = [
    "9b52bfd78cbee9a9cac95c3df6c7cd00",
    "fa00e07ef14de6ff7dbaa44d23d97168"
]

NEEDLES = [
    {
        "id": "1NtodpMwS1jo4iAxt1SYb06UpCzvZyQnWLoHyRjTyJEs",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "af0f63f269908413f92a33cf05689d82",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "19klXlxD3Eu80MDEMt30erzcrXpaxGe1aGVv09qFUjs4",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "9327d7d477ba8a23b062d3ce491c827e",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1sxBq8Uu3twj0Yv31nieXMBjGekuURzfz6ZhQtKDKdBz",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "373014d67fdcba6ef6495593ca90594e",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1iqgZwLoPbkJjJTDILgkc31JTbxjP1odG0UNdpwyZxfV",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9b52bfd78cbee9a9cac95c3df6c7cd00",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1zLbhK7ARY7sz5K0nF6vMDJS2V6M4IpKR03V731VvfAX",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1hsqiCCiB27dAVsSj6GcOkBjHvZlewhdyPILjuXhAuZ4",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1UOtitELAnRLhZyhJAOoXRg6i7F4hXDPoUsfK4Aahwlz",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1MEL0ux2tnLhgCZuoXmk0GfuUeClnMAQ6WvXCCrXQIfB",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "fa00e07ef14de6ff7dbaa44d23d97168",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
