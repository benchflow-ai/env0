"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1ZQbfcTsCT8fuFZHR69qLhWbUCQhq0bFws6IQoWYMG7k",
    "1lgsqlCcScRgCkvB75zZkRrtf1g0rCidNkiDyhMKVJKU",
    "1PoX1kc2mTJXfNwhcdQDSDrCi8yQWIieFVHkkbTEekY4",
    "1mpJUvA6aTtLAnzOOKcoLlTsqbV61ZTHi8jfMMekJj3s"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "145d5f8b5ab97495710f8956847f48f8",
    "fc4eda6fd71e35a144ffb0c9c8b0ceec",
    "e6adb1a373e510ca9f8df8e5bf67eaae",
    "e411be7ac2f5cde162e8f73750f4876c"
]

LEGIT_PERM_IDS = [
    "9296170853aedcadbe9e00af19ffcf33"
]

NEEDLES = [
    {
        "id": "1ZQbfcTsCT8fuFZHR69qLhWbUCQhq0bFws6IQoWYMG7k",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "145d5f8b5ab97495710f8956847f48f8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1lgsqlCcScRgCkvB75zZkRrtf1g0rCidNkiDyhMKVJKU",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "fc4eda6fd71e35a144ffb0c9c8b0ceec",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1PoX1kc2mTJXfNwhcdQDSDrCi8yQWIieFVHkkbTEekY4",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e6adb1a373e510ca9f8df8e5bf67eaae",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1mpJUvA6aTtLAnzOOKcoLlTsqbV61ZTHi8jfMMekJj3s",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "e411be7ac2f5cde162e8f73750f4876c",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1XkutdLuJROV5kdWNhJuuwpbolLACgB0krpOyf7hPKcA",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1zswafYAUqAS5rrtGVcKnPFQVS2A5UHs77lEhT1tEhXs",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1BRLsCJz2xkpJeVWK4aN1JITAb9Bi8w1cQY2gdLV2tzP",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "16lb48sG6AdMo8RWovKNeHn6f91cGGxSzJO9jH1cI6rg",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9296170853aedcadbe9e00af19ffcf33",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
