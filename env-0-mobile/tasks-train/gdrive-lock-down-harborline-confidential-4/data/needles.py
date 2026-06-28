"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1LA1ipW0xd5uWggfpqNKenURXQMGAUeT8SJaEo379NdR",
    "1rDCLjVEj8vFIhCjTUhEkDIdW19cTk2u3bMHjBcb97m6",
    "1YwK3vFQq1q9Uex8YXoocTm9CJ0qK9lm8MdXPgpGqyzS",
    "1j28dPkLmDY9r3hVIrj27INrnIo3qLRTHazkSRgPWn8K",
    "1ijn8DfNLn8lOnY6GaXCKwdqU51fMoJy7p004EMjTWwS"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "41a3097b647028a6756c3c73cf37edab",
    "28e378ca3d1c4ea59ac66d0560905304",
    "5656c9626e41c7e7cb38cf72485c0f36",
    "01237b4bb2add3b55f4b3bb11e20e726",
    "f9b79a0215373cbeabfa07239de35236"
]

LEGIT_PERM_IDS = [
    "6ba7532902ac4c254f3e9f43b4bcd0d8",
    "c9aecf652203facbca748365fbb1d36b"
]

NEEDLES = [
    {
        "id": "1LA1ipW0xd5uWggfpqNKenURXQMGAUeT8SJaEo379NdR",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "41a3097b647028a6756c3c73cf37edab",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1rDCLjVEj8vFIhCjTUhEkDIdW19cTk2u3bMHjBcb97m6",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "28e378ca3d1c4ea59ac66d0560905304",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1YwK3vFQq1q9Uex8YXoocTm9CJ0qK9lm8MdXPgpGqyzS",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5656c9626e41c7e7cb38cf72485c0f36",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1j28dPkLmDY9r3hVIrj27INrnIo3qLRTHazkSRgPWn8K",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "01237b4bb2add3b55f4b3bb11e20e726",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1ijn8DfNLn8lOnY6GaXCKwdqU51fMoJy7p004EMjTWwS",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "f9b79a0215373cbeabfa07239de35236",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ia4nTDvcOBLSQ8ZkdxLnK7iymPBARqg0oojuUmqAP0Z",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "6ba7532902ac4c254f3e9f43b4bcd0d8",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1d8JNMn3PAXTI06njVM7FaVRc9Yr0Kk9EvLdhwZv580C",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1W9hFnRLLWIPBSYZD2uFVKIYFL11HpE0dI5G9jDIHP1j",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1BQ98jO4X370s72xfaigC6QTb68wAXbP2oySaEPCwGxn",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c9aecf652203facbca748365fbb1d36b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
