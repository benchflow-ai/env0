"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1BhooRZ1pyqUEg6yEyV4rwPcODcI4rvo66U7a0kj5Ado",
    "1CNf9LlWm42ztKWGGXduQLUcPlkqiGxW3svb7sdaxyT3",
    "1Pp0By5lOK2UXvrEPkHQQzp4gikFT56HLyGs9OjxDHmv",
    "1BR3HCGwrbMhqkZliKGS00S8ropPMsxbq5DH5HyiU0eX"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "2651c0ad20a59e7a1da8f84d7b0d3412",
    "5817b8e28d58ea186fbd4af4671b760e",
    "a800b5cc5706a2f1c8611a4fa8fdaf89",
    "0fa8c21f49ee408b39f759f2a4e8b2f3"
]

LEGIT_PERM_IDS = [
    "25e961a60ceb0bdae84a1cee4bc5a25e"
]

NEEDLES = [
    {
        "id": "1BhooRZ1pyqUEg6yEyV4rwPcODcI4rvo66U7a0kj5Ado",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "2651c0ad20a59e7a1da8f84d7b0d3412",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1CNf9LlWm42ztKWGGXduQLUcPlkqiGxW3svb7sdaxyT3",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "5817b8e28d58ea186fbd4af4671b760e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Pp0By5lOK2UXvrEPkHQQzp4gikFT56HLyGs9OjxDHmv",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a800b5cc5706a2f1c8611a4fa8fdaf89",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1BR3HCGwrbMhqkZliKGS00S8ropPMsxbq5DH5HyiU0eX",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "0fa8c21f49ee408b39f759f2a4e8b2f3",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ShcVAvO2KvySFDYW5gyduBclbcbAledBiN4h4NyrtHY",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "25e961a60ceb0bdae84a1cee4bc5a25e",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1Ah3wTlAtAxS6uwXQR6a507wziitceGnYyudoyed5EMx",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1sY2v1U5yDWCxkwfs4w6jcxYjZxv9H7lpprVjxaeDihf",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1Yim1WlKjKgdMCurBvYozyE0xpC5UA5CRPACFFlrgor8",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
