"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1vizvZCuABWTFgES71DyQDo5mwdr8Bg68lDWUSlQ55eO",
    "17CAf9NvE5lAYJ0FZSuyBG5Hzb5CohMawSVUAwkOXFeG",
    "1ZZBtgly8M7VnjM8ZKwfpQNBf2qCsAFe2RlxaDQBrpqu"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "f452e9e2def737b9e4b1997a24064ae9",
    "49a923baffacaecde7e998972462fcaf",
    "b65a1a1ffb1a4916170ec96700c4a77e"
]

LEGIT_PERM_IDS = [
    "d081664a8da811694c4d4322db873d12",
    "f6db244084a4014df5cfe9c7d23397a1"
]

NEEDLES = [
    {
        "id": "1vizvZCuABWTFgES71DyQDo5mwdr8Bg68lDWUSlQ55eO",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "f452e9e2def737b9e4b1997a24064ae9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "17CAf9NvE5lAYJ0FZSuyBG5Hzb5CohMawSVUAwkOXFeG",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "49a923baffacaecde7e998972462fcaf",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1ZZBtgly8M7VnjM8ZKwfpQNBf2qCsAFe2RlxaDQBrpqu",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "b65a1a1ffb1a4916170ec96700c4a77e",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "15m5WQnOsbbq564FmJTRzQ0SBJ5rQWpHjSyUunpaYGX2",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "14Oiwqn4xSeZT70SKZQyjq1TTGmUA1L3cc76A8Qea4Be",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1ikCUcKFgEBB29Nxin0CXOHHcvy3v8zH532uWNXGnzcZ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d081664a8da811694c4d4322db873d12",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1tFwgdyr2w2B8zl7ro9lNO30hmbNmoax8qwLB7EekieJ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f6db244084a4014df5cfe9c7d23397a1",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1GTtZITXvyIurwn0SftoyeRnMgpU7Gw4nxURhu2ee2WO",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
