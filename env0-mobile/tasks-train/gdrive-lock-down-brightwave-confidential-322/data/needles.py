"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1RMVo2SuBfzc6plAgSYEgZXGyEeRj8tPF3i2Orn68eXB",
    "1VwcGr5SECFhdnf3zhT2MzLQsaKy2xwZZYwza8P8TLXQ",
    "1Tt59nH0Tz8aIxal5bnt2WBCfN7SEd4t1TZW8Nnmua6e",
    "1u67tmBvnEvf4rnyFD14X775wXKYZGBwLfDJzY8gihYN",
    "126VC42SrPONY5raVPHno0r4pnQ1IvucnUSBOtxIQUYg"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "98d3681c28f6c114829c3b67f1b5d8d3",
    "a1b9b1f3ca4916440839671accb27fbf",
    "7f04794e87482b5b0bcddaccfa595bbd",
    "925f38db88cc8a48d7bdcc683d85e355",
    "af403adc874f053ec1c4f9ae95120923"
]

LEGIT_PERM_IDS = [
    "23982df0fb3d353a17bcf76a85a18c52",
    "6958aa9fc40a393e388d41982ad94ad8"
]

NEEDLES = [
    {
        "id": "1RMVo2SuBfzc6plAgSYEgZXGyEeRj8tPF3i2Orn68eXB",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "98d3681c28f6c114829c3b67f1b5d8d3",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1VwcGr5SECFhdnf3zhT2MzLQsaKy2xwZZYwza8P8TLXQ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "a1b9b1f3ca4916440839671accb27fbf",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1Tt59nH0Tz8aIxal5bnt2WBCfN7SEd4t1TZW8Nnmua6e",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "7f04794e87482b5b0bcddaccfa595bbd",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1u67tmBvnEvf4rnyFD14X775wXKYZGBwLfDJzY8gihYN",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "925f38db88cc8a48d7bdcc683d85e355",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "126VC42SrPONY5raVPHno0r4pnQ1IvucnUSBOtxIQUYg",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "af403adc874f053ec1c4f9ae95120923",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1pYTIFlrfGQn3VGjTsVEQypA89Verkk7pbyW0poRTDSG",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "23982df0fb3d353a17bcf76a85a18c52",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1wZ3X5q472XRp0xbtm3cpjXlnIqZNZbCwXCDu0UdQDcS",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "6958aa9fc40a393e388d41982ad94ad8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1F3eTHrvnKE4GKpQ3AUTUsMXJddy9LGMGhpjQygQPznS",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1fiC9fFOU5zOGaopNCIjcV8OZZdlLc3t0nyk3vtjKU6O",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
