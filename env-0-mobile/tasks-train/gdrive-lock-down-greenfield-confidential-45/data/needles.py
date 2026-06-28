"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "19i9hLDfoHFqY6rDPcZZjShutnMckcQs3RFBAG6XrypU",
    "15NweJWkZhN4vzAz1rC9W1xH5ACR4tp0dKmvGfMsOptY",
    "1gtyE6jFP1XHXYyl3cHqCuaROcxY4YYMbY91dnSfVrFD",
    "1zRlgl5r3BSiQNJq1LxEZlgIwPrPEDvvMa6jWbsRbKFH"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "2895d8eb7d15c8aa360eae15b93db3eb",
    "33d6d50f834f86a3db058433f37d17ab",
    "8546fe447b8c1f3531d2f515e96f645d",
    "9078105df81e0a6e3448fadafc7bdbf1"
]

LEGIT_PERM_IDS = [
    "ff8d1d9209d415fbb47fe5e7a1f8ab40",
    "dd4d71f1dc369a838179da0b5b0ae422",
    "7c0cc51ce6a01da1374a365a1d9daab9"
]

NEEDLES = [
    {
        "id": "19i9hLDfoHFqY6rDPcZZjShutnMckcQs3RFBAG6XrypU",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "2895d8eb7d15c8aa360eae15b93db3eb",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "15NweJWkZhN4vzAz1rC9W1xH5ACR4tp0dKmvGfMsOptY",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "33d6d50f834f86a3db058433f37d17ab",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gtyE6jFP1XHXYyl3cHqCuaROcxY4YYMbY91dnSfVrFD",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "8546fe447b8c1f3531d2f515e96f645d",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1zRlgl5r3BSiQNJq1LxEZlgIwPrPEDvvMa6jWbsRbKFH",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "9078105df81e0a6e3448fadafc7bdbf1",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "12IoPMQNK7g5FSP4uZ5MLQARa55DvhxefWILeRPMoZQv",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1GXtrmhF1JjyuJjLSTuvVO783fYTSrB5s35v8fA4jG64",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ff8d1d9209d415fbb47fe5e7a1f8ab40",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LNFKi4D232cRC9xzLZ86WUx2VejuZTztt55aqbWO9pp",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1h2IdsT1LvxnlZR5ZRBOCSWG5PTPWRgT8VxAq1UhiGGw",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "dd4d71f1dc369a838179da0b5b0ae422",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1eW5UTHrkxmupZhI2PwdNIk0IKxsObFixJJBBLJ8r7Hh",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1HdJ6rgUbwH2Vuk9y05hsN1UISSUkQ7pPbdqZBoTX4EH",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7c0cc51ce6a01da1374a365a1d9daab9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
