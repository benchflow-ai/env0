"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1dg9qTU7HAVrmMgwzCLcURMQil9g4hrgwqTwBSe4nDuz",
    "1q1pkFUl6azwqLtzvSTvUlRAjklfFgAaFX19yfEWgdtn",
    "1CIpaQA5uWG84TgD37yRWSEmCOTDQ3dOapTb5Gt3X1BO",
    "10z3TNzQsZ83iaY6NbGBXqcKatIM89vpYuLK11Q2EHYg",
    "1Fv6laHhOgAo8cnrnhfujbcZOnfMA2oGwOeeGJP5mwlu"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "87f64d666d0b5023183cb0dbcd6cca9d",
    "ff29b931243763c736940c06b872200e",
    "09743c3b90e045ecf16b2b6153563128",
    "4267eaf36d979f61e0f77cc8c568379d",
    "247f47174d7c823eb0ad6b900fdac17d"
]

LEGIT_PERM_IDS = [
    "427519263d401a1accb508f8ed0d7499",
    "42d88ca3b0edef5539d6b44ca432d6b6"
]

NEEDLES = [
    {
        "id": "1dg9qTU7HAVrmMgwzCLcURMQil9g4hrgwqTwBSe4nDuz",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "87f64d666d0b5023183cb0dbcd6cca9d",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1q1pkFUl6azwqLtzvSTvUlRAjklfFgAaFX19yfEWgdtn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ff29b931243763c736940c06b872200e",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1CIpaQA5uWG84TgD37yRWSEmCOTDQ3dOapTb5Gt3X1BO",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "09743c3b90e045ecf16b2b6153563128",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "10z3TNzQsZ83iaY6NbGBXqcKatIM89vpYuLK11Q2EHYg",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "4267eaf36d979f61e0f77cc8c568379d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Fv6laHhOgAo8cnrnhfujbcZOnfMA2oGwOeeGJP5mwlu",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "247f47174d7c823eb0ad6b900fdac17d",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MgFZryCJ4eA2G12AQ2C8yfbYYjnU8z2XKs4ngvRIH77",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1qFBTkUFm8DdBizt2boe4D6MR4xEogJghcQ0EeIxyMDq",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "427519263d401a1accb508f8ed0d7499",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1zpLPmVwuNFa9FrAEFddonywyh5FqdppLGSeBnNy6Ddi",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1GPOhaxUYm9MRJIASPaM5aKAOzwNOD0HuSXzHheDa5NL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1N5TFkcguKbEnSFl63mENkqJAiKfi3mlGwOvScI5YVht",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "42d88ca3b0edef5539d6b44ca432d6b6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1MkyhIEbApaxb6nX9HWSpKxOauU57NBRNoWgEhfneqIQ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
