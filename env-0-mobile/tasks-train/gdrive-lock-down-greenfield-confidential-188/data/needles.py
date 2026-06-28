"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1t7ztCMtL309dAn1JoBBG5huDX62M4hPH4sLKJJ1TTyT",
    "1VyM6B9D3LZRakmPvZS0rUGmpMTaJlw5VoFaGdy0QDlg",
    "18riU3L4ZOnICEY1KyFLWzmuMs6a5jmr8biVs7VtmAN3",
    "1iUDD428B6ZjW38V9v0vj4UDhvbUjqeaR5zGqGyI9Ja4",
    "1GUoGirJ2n29axkHUpWdsX4D4VM5VnVwDWwmIJpOwPoJ"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "9b876da1322037739d1338da30e4c5f2",
    "05710b551576a12e0a97d43f8545bd0a",
    "accbae0b54028fbc2315ac3b3b2f4e02",
    "7da5141f7c5bc52306ad38a56534f6b7",
    "214a273847b0c722229d1488876ba4ed"
]

LEGIT_PERM_IDS = [
    "2cc87cf60ecffa2e6a78064813763314",
    "2249ad62d1860e10f2debcb7a826ffd7"
]

NEEDLES = [
    {
        "id": "1t7ztCMtL309dAn1JoBBG5huDX62M4hPH4sLKJJ1TTyT",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "9b876da1322037739d1338da30e4c5f2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1VyM6B9D3LZRakmPvZS0rUGmpMTaJlw5VoFaGdy0QDlg",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "05710b551576a12e0a97d43f8545bd0a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "18riU3L4ZOnICEY1KyFLWzmuMs6a5jmr8biVs7VtmAN3",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "accbae0b54028fbc2315ac3b3b2f4e02",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1iUDD428B6ZjW38V9v0vj4UDhvbUjqeaR5zGqGyI9Ja4",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "7da5141f7c5bc52306ad38a56534f6b7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1GUoGirJ2n29axkHUpWdsX4D4VM5VnVwDWwmIJpOwPoJ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "214a273847b0c722229d1488876ba4ed",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Gw8Glyd1jGH1Dk14pMJWtPqbDK05ftpQrNcVgvFfGrv",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1dJGletBlL9jhEtyIuBN9QOwsH1UXWMsAgAC9uANpzBP",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1lOrkItIBk3Omc0Bbfo1XwENt40EvMQF83nmkjIWPWHz",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "15FvaBqAlpetQCDjswFA6IdTYuJeVpeq7os6Dcc3SRAE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1weIDYgTTFw6pQKMrJWby9S56t6sBlnps96kHovgZtWZ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "2cc87cf60ecffa2e6a78064813763314",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "12h2Nug5Ep47vfo2k6Pe1GLgXIZTgh83A9xM4ykCXBHc",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "2249ad62d1860e10f2debcb7a826ffd7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
