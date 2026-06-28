"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1FwhIFHxJsEBKqqYYYheIFASDXGsHj7Ez5h1ofBzlChD",
    "19ZRQpGXC6G1HOdgrQPaYRDi2ue24stq5rYxMD0eMU2O",
    "1JpXgX3rD7qAJl0C6HE4GXXPQ72LyIl6gMWEuSUccNLg",
    "1FSzPo04rkLp5hQPOnfkJepOCUbuN4WayjIpe8MzAXZ8",
    "1ArMOmFodjxXeTgsnWEn2NwPkqBzgSprt1Eq0hYJpjsL"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "e7a727464d54746cb5df3534cdc166d4",
    "def35cab9a780cd9c68b49819444e715",
    "19412d67bbd8c7be5ecddb62bc730f53",
    "9ae0488062c1993df384c84ce17ecd1d",
    "6a2df643a4b706142e875b541995e455"
]

LEGIT_PERM_IDS = [
    "374584be1b4aa13d7cae1e3a96d4e7c5",
    "2e8b9d38c8acfa5f5161fd2f16b419ec",
    "3ca44f7185de4ddb397dd1cb0348001f"
]

NEEDLES = [
    {
        "id": "1FwhIFHxJsEBKqqYYYheIFASDXGsHj7Ez5h1ofBzlChD",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "e7a727464d54746cb5df3534cdc166d4",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "19ZRQpGXC6G1HOdgrQPaYRDi2ue24stq5rYxMD0eMU2O",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "def35cab9a780cd9c68b49819444e715",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JpXgX3rD7qAJl0C6HE4GXXPQ72LyIl6gMWEuSUccNLg",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "19412d67bbd8c7be5ecddb62bc730f53",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1FSzPo04rkLp5hQPOnfkJepOCUbuN4WayjIpe8MzAXZ8",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "9ae0488062c1993df384c84ce17ecd1d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ArMOmFodjxXeTgsnWEn2NwPkqBzgSprt1Eq0hYJpjsL",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "6a2df643a4b706142e875b541995e455",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1JHytPVJ4igMZMAZVUIFEvX6A4GSZtUP4qfzlzC057rn",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1mRmgVbONnwS0joa2CQpFjFpgV3RGcYfwAsYB3VHEmYt",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "374584be1b4aa13d7cae1e3a96d4e7c5",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1MtQeCUQld54eEk9Nqn5StUrsFvIICcB7c1njeicosis",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "2e8b9d38c8acfa5f5161fd2f16b419ec",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1bRRFAfc0DHrOXjQentoymsAgOxEF96rcgsPquhpel4f",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "13UVnQpYI4AVKSu0IaLvpCdWnLNmF9DapLKDFlQSLkW4",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "3ca44f7185de4ddb397dd1cb0348001f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
