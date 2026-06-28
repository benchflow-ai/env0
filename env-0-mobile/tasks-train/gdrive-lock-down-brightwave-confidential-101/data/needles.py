"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1nwmgCZTzJVL9XqKkTOV4ADPgfngQeS7iUfDLtVSQLXN",
    "1qGizIypLvZTUT8AiDch5yFijijCaM6mY7s3V4ktmA16",
    "1ObyNHdSm1MpJ35SrFZkWJCRBQA022bDCHtAEceTYpeQ",
    "1NxWAPCpS3gi9JntW6JvpWUYEIFRjyMS7N8zYJJg0Zlg",
    "16WejZC22OiFYVmtMYOFuVYOGKxBO5Dw2WAICZofXQAr"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "3b7a2da9de602059c49120126ebf0d68",
    "c169a8029df4f0178c421c49fc6b5e32",
    "2b07c49f25c202d2fd547e7da667d85b",
    "4ba272324ba62d3671bb4eb6698a3aea",
    "1e052dadb33bc7b3c9c1a26714583be0"
]

LEGIT_PERM_IDS = [
    "7f22d2af44befab58e04bd19c15d9661",
    "2029f8c6bfee6a261b1854423bdffb71"
]

NEEDLES = [
    {
        "id": "1nwmgCZTzJVL9XqKkTOV4ADPgfngQeS7iUfDLtVSQLXN",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "3b7a2da9de602059c49120126ebf0d68",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1qGizIypLvZTUT8AiDch5yFijijCaM6mY7s3V4ktmA16",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "c169a8029df4f0178c421c49fc6b5e32",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1ObyNHdSm1MpJ35SrFZkWJCRBQA022bDCHtAEceTYpeQ",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "2b07c49f25c202d2fd547e7da667d85b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NxWAPCpS3gi9JntW6JvpWUYEIFRjyMS7N8zYJJg0Zlg",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "4ba272324ba62d3671bb4eb6698a3aea",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "16WejZC22OiFYVmtMYOFuVYOGKxBO5Dw2WAICZofXQAr",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "1e052dadb33bc7b3c9c1a26714583be0",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1wmkBIrS4CilyZWrFFmHyMc6mDb72koorxUv4gaAIg0L",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "17TNzJT5SoWlZkqrJs89moeWCVmzfU4mvwHMFmkVfGn7",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7f22d2af44befab58e04bd19c15d9661",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1TDyPyWtxKTsJtcK4EMfIexg4tALVOkyNdZABnKYI6tD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "2029f8c6bfee6a261b1854423bdffb71",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1v3QhM98MxUOKZn7NfauB3mAQlg1yoOX2lMQymNI30jz",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
