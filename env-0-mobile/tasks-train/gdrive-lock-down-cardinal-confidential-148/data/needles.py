"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1yLQ8xt6xXkMQVoz0RBTOaIG1XA5FQxFBRVSJ0d1PYx7",
    "1mLwElAW4O3IaGtisJsf1FdSnuTspQgyO4z4Gu92TS8s",
    "1ne4AJmHoXp4CWO2CuIkTgu8hWbXM5chOchenDM5LSOf",
    "1FfO1JVdoLdaVh7CGlpe0DYvMNVwrRDFLvHxJhxLaIZs",
    "1Ff09R3Ho3ohpsVlVNTyEBZokYwjMfz0CWzxXLoiOIhz"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "72794886021ff421e993c5d7676ea3b7",
    "6dcf5e1f4126b25bd818c5a00a54d129",
    "8cfcbd920dccbe39481c65e2a9ba58b1",
    "1ad4683f9a7cea9eb8b6154666ba6c00",
    "373d7b65f7d73de4f71b22857484cb33"
]

LEGIT_PERM_IDS = [
    "653a260a5814ef6c859e3b63a1a10d22",
    "b84b4012ddd431530d9f99c7e1c66d6c"
]

NEEDLES = [
    {
        "id": "1yLQ8xt6xXkMQVoz0RBTOaIG1XA5FQxFBRVSJ0d1PYx7",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "72794886021ff421e993c5d7676ea3b7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1mLwElAW4O3IaGtisJsf1FdSnuTspQgyO4z4Gu92TS8s",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "6dcf5e1f4126b25bd818c5a00a54d129",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ne4AJmHoXp4CWO2CuIkTgu8hWbXM5chOchenDM5LSOf",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "8cfcbd920dccbe39481c65e2a9ba58b1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FfO1JVdoLdaVh7CGlpe0DYvMNVwrRDFLvHxJhxLaIZs",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "1ad4683f9a7cea9eb8b6154666ba6c00",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Ff09R3Ho3ohpsVlVNTyEBZokYwjMfz0CWzxXLoiOIhz",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "373d7b65f7d73de4f71b22857484cb33",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1bgjealCM7KOmXdP0iH1k9oUM05XJEc9yqfC85UkuoOW",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "143Er72YOx0GX8Gz3F0DUbglKHdQoEHCNXhmYhb7yi7g",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1bInGse6lmlsguHFUwVYNBTnMVh5bfrdNdLZ1FGEj5bL",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "653a260a5814ef6c859e3b63a1a10d22",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1BJqzkL6kYXYQAtSsbpL3TaQ2LH8IUHPjP626Zd14c8G",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b84b4012ddd431530d9f99c7e1c66d6c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
