"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1TQ8XlSZyOo6zbFrhExe90keVzspv7PB3g28pqTYOLZC",
    "1RVaUshdzvk4Y7TjRA5ey62i4vvbDtS5ZzTk5O3lqvPQ",
    "1hulvMFlCLkd4Q84Tlj5vcpGUOO7chgDBEpaDW6xVsNq",
    "1TNKl7KrFelkQy6tCUdL8ge2JRALwDoNk8DZYe9pcZUm",
    "1nkFfFZDSMv7839N3dRpTl7y9lKgecVUG7YmMnik4oLf"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "99562f80612db6036b74145cfb696fa6",
    "af413e7ab407559b4afd2de984af8496",
    "24416ee5df94bc66bd3122991f56336f",
    "76690caa66a950a0c957b9884e6aa559",
    "24bdf5bfddc1ba66a6d21276b8e9e6be"
]

LEGIT_PERM_IDS = []

NEEDLES = [
    {
        "id": "1TQ8XlSZyOo6zbFrhExe90keVzspv7PB3g28pqTYOLZC",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "99562f80612db6036b74145cfb696fa6",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1RVaUshdzvk4Y7TjRA5ey62i4vvbDtS5ZzTk5O3lqvPQ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "af413e7ab407559b4afd2de984af8496",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1hulvMFlCLkd4Q84Tlj5vcpGUOO7chgDBEpaDW6xVsNq",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "24416ee5df94bc66bd3122991f56336f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1TNKl7KrFelkQy6tCUdL8ge2JRALwDoNk8DZYe9pcZUm",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "76690caa66a950a0c957b9884e6aa559",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1nkFfFZDSMv7839N3dRpTl7y9lKgecVUG7YmMnik4oLf",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "24bdf5bfddc1ba66a6d21276b8e9e6be",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1PfYUrV93P3IGErNa8UP10I7fQ2x2cTC7nMM3xalo6Gv",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1lxy7bhSSr85IFcYadhiaFyDmF7b2pZwaoRzjeXHFzCU",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1SunostxPqaknX2B82IIRg0hEFcEMp30IuXLkNiYHQs4",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1Z79mUOQq5Y3IBx5XfXSnl9TMAJtAFo5jCwTdTB8ROYG",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
