"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1cTnHlraQgrAvrGfMSwHEKOciRYoCKqnGEOKwmlLvJ3f",
    "13QCPp3l2MYJucxRyBZ1ncSvaK951d0wpcwDiByUi4in",
    "1m274MYzEJ9kIwA7JN7WrAExgN5xzvB4z6zocURgGQj9",
    "1iPVpTbI3hwS4AdWJc9SfLcx8S440YlAanPM3501bqOF"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "4179f205e231a12bee142390a5f5b518",
    "1372997a365fb0429d536e01203be6c9",
    "e954215e4e4f1c981a9ea17bd8431e5f",
    "266f872cf743d236c2fac2ada21c5ec8"
]

LEGIT_PERM_IDS = [
    "eef444e9e6a31157e9e53a91d3c7cef3",
    "bc3ba0796fb319c2c743f4db3d4acc95"
]

NEEDLES = [
    {
        "id": "1cTnHlraQgrAvrGfMSwHEKOciRYoCKqnGEOKwmlLvJ3f",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "4179f205e231a12bee142390a5f5b518",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13QCPp3l2MYJucxRyBZ1ncSvaK951d0wpcwDiByUi4in",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "1372997a365fb0429d536e01203be6c9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1m274MYzEJ9kIwA7JN7WrAExgN5xzvB4z6zocURgGQj9",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "e954215e4e4f1c981a9ea17bd8431e5f",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1iPVpTbI3hwS4AdWJc9SfLcx8S440YlAanPM3501bqOF",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "266f872cf743d236c2fac2ada21c5ec8",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "10W0cw80e7BHGJJF0wqygVZSRf5ETfFcKXENFizOyGoP",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1t0wm1gs914piw6TKFlRmZgg4DSk67HMGmfaSsAlLMOv",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1OtZryRfJlg9KNw8RHB86uzB1dcm4Y6z79d7OHAw2SnQ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1AKRNKfmbAWM7ppMH9te34dC1Ze4ijn76keip9BBxEED",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "eef444e9e6a31157e9e53a91d3c7cef3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1NlsLwXS62A9XpGp5Zsft0qciOqsnSTkTjLw0w1DBKSS",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bc3ba0796fb319c2c743f4db3d4acc95",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1fKSNLfRXqEX4rYaZXSocTauAbi5jE14Uzzj556Z7pGf",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
