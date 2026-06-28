"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1vCdnR2gLYEuNIyUpzAsMF4ZdlcEgkfIomOU9L2N4dXG",
    "1jow31JUmgqCpWo3aQiWXsqCMvOMNZVM3g8VE8mAOyv3",
    "1RuCKtGauY8leALFAsnYXwDEHmVADpBVhHKq4vFFW0je",
    "1XMEZKqtOFcG8tek4Fi8wU95e6wdKvblyrkqxD0tDkFo",
    "1STVa68IbH5tlAhN6ykdJaN0dLKnPr4VAh57JmJgtxfU"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "4c1a8e41ea83586ff64281aaf66e349b",
    "5cc034e0f949e1178fa0cb47e0e294b0",
    "4a096263f92cfb9214ab3d9f78f983ec",
    "66b4d788fd1f238d117a4494ca39a0c7",
    "7bb50a7564ca0458cc4af69da764d2d1"
]

LEGIT_PERM_IDS = [
    "0799d85faf7ea18674189a4e50eb3938",
    "dc0a27b8d0c014122401f20ab4a562db",
    "c5a56fe20a06db2a8875ab77229d3f6b"
]

NEEDLES = [
    {
        "id": "1vCdnR2gLYEuNIyUpzAsMF4ZdlcEgkfIomOU9L2N4dXG",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "4c1a8e41ea83586ff64281aaf66e349b",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1jow31JUmgqCpWo3aQiWXsqCMvOMNZVM3g8VE8mAOyv3",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "5cc034e0f949e1178fa0cb47e0e294b0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1RuCKtGauY8leALFAsnYXwDEHmVADpBVhHKq4vFFW0je",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "4a096263f92cfb9214ab3d9f78f983ec",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1XMEZKqtOFcG8tek4Fi8wU95e6wdKvblyrkqxD0tDkFo",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "66b4d788fd1f238d117a4494ca39a0c7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1STVa68IbH5tlAhN6ykdJaN0dLKnPr4VAh57JmJgtxfU",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "7bb50a7564ca0458cc4af69da764d2d1",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1PvM8WuqvvEirz7kyQaH0d9PwpB8RHgDtHqIuD7TRWzz",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1kLa4AL36m2GyWQkLEG1nnkDbQEkUK7XJ3RrLvp35XZK",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0799d85faf7ea18674189a4e50eb3938",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1mlskZ4CvRFnAU6iSegEqiaj1EMD5hQjwgYw2FLptYuA",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1lfBt7iRxhgbHe88IqHQpCIWDtBsddikrBnnJLlkQjij",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "dc0a27b8d0c014122401f20ab4a562db",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "114Ii5W8TKEvFwmG0UlbfsZrmMhYTW2Dq0O21o2ngYZA",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c5a56fe20a06db2a8875ab77229d3f6b",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1Ho0k5mHenNtuZuwi81o834W4kDYbnUdncN4Wccs6q74",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
