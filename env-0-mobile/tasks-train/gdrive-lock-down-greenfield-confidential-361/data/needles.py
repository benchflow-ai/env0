"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1QsZIBbXTl7TbD2ahXJdLRGGlAmVyqniAsgproo57JWD",
    "1JxsFmmSJhVLSpYZq9rS2WlnsJbczsknZARtgN0z8BWt",
    "13Axnfyw9viKvwfBaOzkfa7SIGlTsKqpD7cUyzssYuXy",
    "1cLI6xB3srKghsjieLuI3RsDvY6P5avLaB4VGWY57faK"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "700d53fa8d1e588965cd7e8a27de4709",
    "46531f97e9e6f5c03ad9ef687478ffe5",
    "7981c6a876e435e34e218a3ca10dfd5a",
    "809e5ecf376a9d34365e485417f54f6b"
]

LEGIT_PERM_IDS = [
    "a114d71223ccdf385af932cb7255204e",
    "b28ac8f944f908d2eb6ef015a2cc4a7c",
    "a35ec02dbcf136ebdb7d6cfb1af07812"
]

NEEDLES = [
    {
        "id": "1QsZIBbXTl7TbD2ahXJdLRGGlAmVyqniAsgproo57JWD",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "700d53fa8d1e588965cd7e8a27de4709",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1JxsFmmSJhVLSpYZq9rS2WlnsJbczsknZARtgN0z8BWt",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "46531f97e9e6f5c03ad9ef687478ffe5",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "13Axnfyw9viKvwfBaOzkfa7SIGlTsKqpD7cUyzssYuXy",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "7981c6a876e435e34e218a3ca10dfd5a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cLI6xB3srKghsjieLuI3RsDvY6P5avLaB4VGWY57faK",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "809e5ecf376a9d34365e485417f54f6b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1rpf6cV79XqeQ18UzCyS17aqRC4rxA54ih4c5o6qWShf",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1cKoysD1FiHJeEIulUDQbQkAW3DdOXlgJylI3kt8Qr3h",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1y4S6ByK64pN2ZMJdhxjR74HFKzBrQUYBE38eCV3twu8",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a114d71223ccdf385af932cb7255204e",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1kE9gLhjWxN3uOyQe99t33hH6Gf1nNhWdCZmlX3ON2Ii",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b28ac8f944f908d2eb6ef015a2cc4a7c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1PCyjhAsGyj6GoLOfovVrfo72JimZKNXA6uBOo9NL6RB",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1NPVg3FzjSTipXaH5FlJu5gMFf9fvzZC8ifwQpfMJoO4",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a35ec02dbcf136ebdb7d6cfb1af07812",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
