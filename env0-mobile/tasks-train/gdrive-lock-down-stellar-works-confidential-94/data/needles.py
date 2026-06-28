"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "10OUlNkSklrzmO3zPqaK3hnR4spwBNxQAkypdizMG4aq",
    "1M0LkpTsfZZm0C3YhdsZOTDezgYgih7WlpiW0dMepkeH",
    "1EJWIHxDYF8ys7wUyzx6DptbMt0Tz3dWUsnU8UDD8oNS",
    "15plPiF4jxn5LR2DR7Ptb18tGzQsPdtyzQNRNol3OTjZ"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "d9fc320f7796d32408723fe98ca01ddc",
    "c1b44293670402a6da86b27c1fc9cb17",
    "2a8e31afa3094008dca6c8c938a0f87c",
    "3fa829fb08541c104d703eebb9a27b29"
]

LEGIT_PERM_IDS = [
    "3a9c4ba6f2f93f4ec80752df9d2916ef",
    "72e495015ea1fb252338c23fbd15eb05"
]

NEEDLES = [
    {
        "id": "10OUlNkSklrzmO3zPqaK3hnR4spwBNxQAkypdizMG4aq",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "d9fc320f7796d32408723fe98ca01ddc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1M0LkpTsfZZm0C3YhdsZOTDezgYgih7WlpiW0dMepkeH",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c1b44293670402a6da86b27c1fc9cb17",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1EJWIHxDYF8ys7wUyzx6DptbMt0Tz3dWUsnU8UDD8oNS",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "2a8e31afa3094008dca6c8c938a0f87c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15plPiF4jxn5LR2DR7Ptb18tGzQsPdtyzQNRNol3OTjZ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "3fa829fb08541c104d703eebb9a27b29",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MxlUum5AHlcAEa5UPZVYDHz6DmgvlbcD0OdlHLI6WYx",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1tl1jGGcPMw86VcroBj36tbbQIHYEQ9SNz4rqLmYQLgJ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "183GiwFfVPO2HNOuS0uNcPTDlsxsGO4Ar3a5wYovEyih",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1aOuwtmowuRloQauEPUoZ60U91FklEt8w3Zl8PhlbcHw",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1T8iSzjxK8hVZQm6vFMsgkgrDz65RFHMzojUlBhqItBE",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "3a9c4ba6f2f93f4ec80752df9d2916ef",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1NuFq7UBN29XfdRslqSm9f7Ej11rUw5yKQDB5VufY88v",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "72e495015ea1fb252338c23fbd15eb05",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
