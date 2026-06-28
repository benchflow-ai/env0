"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1lXCEy5AXGBbWxRmcjtVEHI9pcKTSp6m3tz6Nu4hS2bZ",
    "1jyqlaAVGvmyVgLmLT9csKLNHpXEabSMLG7xyHP099Ng",
    "1qf3zI2L1C2vEuOKBr6ivj2rYhxd9AKQuLMEUl2aRIef",
    "1V5okOo507TR8pun3zpgEnE4Wyc1uLTj0a8yT6WNLWpe",
    "1bPvMvLY6rnb25a3u5wtTTPUc0pdH4duf2zoHIp42GDF"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "ab33d4759652d1ccc6522d39e3cbc1f4",
    "a72b8165989441a36b29dc24033bd511",
    "178a3f18bc82451b6cc14acddee64844",
    "5428d9ebd1b22b9924d4c3bcb4f079f2",
    "5ed6672b8137a3345d2d1c047560e106"
]

LEGIT_PERM_IDS = [
    "7b62a831851bf4b15eeb1feaf80d2ffe",
    "88c89ac770711cc8482e4819f3d457e2",
    "e49590d4a7e5b1ab3bcd0aabbaec42d8"
]

NEEDLES = [
    {
        "id": "1lXCEy5AXGBbWxRmcjtVEHI9pcKTSp6m3tz6Nu4hS2bZ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ab33d4759652d1ccc6522d39e3cbc1f4",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1jyqlaAVGvmyVgLmLT9csKLNHpXEabSMLG7xyHP099Ng",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "a72b8165989441a36b29dc24033bd511",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1qf3zI2L1C2vEuOKBr6ivj2rYhxd9AKQuLMEUl2aRIef",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "178a3f18bc82451b6cc14acddee64844",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1V5okOo507TR8pun3zpgEnE4Wyc1uLTj0a8yT6WNLWpe",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "5428d9ebd1b22b9924d4c3bcb4f079f2",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1bPvMvLY6rnb25a3u5wtTTPUc0pdH4duf2zoHIp42GDF",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "5ed6672b8137a3345d2d1c047560e106",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1UeQ651r5FNX3lrWeVaXnOloIWx0yiSl8EaPWhhKSPuv",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1q8RapaiU0bu2Cz6OoDqwiMzteM4SOn55y4Cf2MFhBnH",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1kWLBf8baJCFZRttH2MmgVoXZpGusYf6IjuMYrGFeYj5",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7b62a831851bf4b15eeb1feaf80d2ffe",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1BHtQWZoV2wVo0LoOWJ1cb5UO0TxuV4PnHzVpkYg8e2n",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "88c89ac770711cc8482e4819f3d457e2",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1c1rKWSCtCoQ7FU7TbrUvrB30GOFjYxrql16Ths5psDi",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e49590d4a7e5b1ab3bcd0aabbaec42d8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "13ND52oOfOtbVOaKDUxphf9CkYBSHSZs0mAbYbFPch2o",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
