"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1JiI9hzKVwefxgpfzY0LaQwZE2zCIiK25jTxa2WN0sTN",
    "1SLqvzZ6KAymGLyJnFvTcJkzeoRiDZpWgloLwSIwWuNm",
    "1NcO6gZFDeiNVrPkYeoLIp7UTXDVfFTS3VTul0X1dqnu",
    "1FMdKT4eOEWR6yLxzgVI1lpcUzxY8PRkubrD1OI94nWN",
    "12jupefNuVFBhVsfunFyapTS5m5fpl1SGnFEe7H1j4ZA"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "784730bef96879fd7253c246985646f9",
    "f7e516295185bde6a3402c2f25cf8fd3",
    "f0734e5c03f9bec6da9687e4dc18b360",
    "782f27d2fac03765cbcf60bcdca10af0",
    "73793fb2f2529359e396daa31ed2612e"
]

LEGIT_PERM_IDS = [
    "5b8a307376b9900acbdeb8ed4c6a0df5"
]

NEEDLES = [
    {
        "id": "1JiI9hzKVwefxgpfzY0LaQwZE2zCIiK25jTxa2WN0sTN",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "784730bef96879fd7253c246985646f9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1SLqvzZ6KAymGLyJnFvTcJkzeoRiDZpWgloLwSIwWuNm",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f7e516295185bde6a3402c2f25cf8fd3",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1NcO6gZFDeiNVrPkYeoLIp7UTXDVfFTS3VTul0X1dqnu",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "f0734e5c03f9bec6da9687e4dc18b360",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1FMdKT4eOEWR6yLxzgVI1lpcUzxY8PRkubrD1OI94nWN",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "782f27d2fac03765cbcf60bcdca10af0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12jupefNuVFBhVsfunFyapTS5m5fpl1SGnFEe7H1j4ZA",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "73793fb2f2529359e396daa31ed2612e",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "171uy2JqOyISCtwZ5pPH3dLqCO2G7RHbw5JJyYzBeCv0",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1cmcSMhWwdsEdu3H0hTWMpJNqCIcCpuE900bQqcFQ616",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1FEPUhxCHWTLX9g8hsKZmiTMcFJA2mpWhtlXz4bOQxPI",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1mQhuPoNeXIKv7j21w8QR5XABgU0dqu6HpienDulcZxg",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "5b8a307376b9900acbdeb8ed4c6a0df5",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
