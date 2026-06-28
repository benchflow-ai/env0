"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1ttm9otHjiIiNdYryrybQPrfsRcuiaOivyOjDAJxe9mz",
    "1FUO7b6tU2epQitJ6ct5GuVid0Xg3TDHou6JUepZDjQO",
    "1b72D9jm5O3wGkD2Y44ceUOKiOpIPeeI021JA6xtLNkU",
    "1TSoCJanebQNBRnNaCN1jL1HkT5aVRKTLPHha78L3kc8",
    "1qiQUl0SYZ5QOklvqV0oIgK56BqMvduBWjACefnjBnZQ"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "4998b4ff448e1ec2ebbd1a38d35207f0",
    "fb731bab97b59b9567a7277921bc5fe8",
    "0a5a78ed45c05095776363dd77f8046e",
    "2f8449ab6fea98065446ab4962662294",
    "dc67f3c328d7f69e1d705d76b3ca9bfe"
]

LEGIT_PERM_IDS = [
    "ebd88a8861837c462d2c2e27a4fafd5a"
]

NEEDLES = [
    {
        "id": "1ttm9otHjiIiNdYryrybQPrfsRcuiaOivyOjDAJxe9mz",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "4998b4ff448e1ec2ebbd1a38d35207f0",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1FUO7b6tU2epQitJ6ct5GuVid0Xg3TDHou6JUepZDjQO",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "fb731bab97b59b9567a7277921bc5fe8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1b72D9jm5O3wGkD2Y44ceUOKiOpIPeeI021JA6xtLNkU",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "0a5a78ed45c05095776363dd77f8046e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1TSoCJanebQNBRnNaCN1jL1HkT5aVRKTLPHha78L3kc8",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "2f8449ab6fea98065446ab4962662294",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1qiQUl0SYZ5QOklvqV0oIgK56BqMvduBWjACefnjBnZQ",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "dc67f3c328d7f69e1d705d76b3ca9bfe",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1s0svTAyWUHkYZrTxIJMlQ2jjegdGlLOCeVC7uCGIS0G",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1K3p9A4O7A0vC2jSwWwFMHKTIpR8ZEepdghzhIOzf71D",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "11TfubKTPCzdxpkUb49jFNnZ7HFVbTHrrHc6PFngaNHY",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1HqssQCPPrBPjjn38KZzqBTPpaXZ3UIlN6BjY0WAwQWX",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ebd88a8861837c462d2c2e27a4fafd5a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
