"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1QzeThVjC5l1GukRssdJM5H1bi1wuB6GuVgXHoLP3reh",
    "1byY6jgVm3WvmiCTJ1dyGcoGx5LStwLPaLXc5t1TFeeR",
    "1BiI1uQhNVtrx5SJJLv2We87UF6WiQGet0wqPeT4GtDt",
    "1lRes8079raBYXgqybIdquZu3x79VEPTfuYZT1jNbHAh"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "a278ef20270f9295664db470632203af",
    "01201d85a5f3657db1eeb2e98bec0d76",
    "bb41eab94aad7405c62cc75390031b53",
    "abbe331447be8e3193df943393336613"
]

LEGIT_PERM_IDS = [
    "c8eee22a3dedb02be56c851752dfc661",
    "4b92e4600bc0569b611321cc151a9ec6"
]

NEEDLES = [
    {
        "id": "1QzeThVjC5l1GukRssdJM5H1bi1wuB6GuVgXHoLP3reh",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a278ef20270f9295664db470632203af",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1byY6jgVm3WvmiCTJ1dyGcoGx5LStwLPaLXc5t1TFeeR",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "01201d85a5f3657db1eeb2e98bec0d76",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1BiI1uQhNVtrx5SJJLv2We87UF6WiQGet0wqPeT4GtDt",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "bb41eab94aad7405c62cc75390031b53",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1lRes8079raBYXgqybIdquZu3x79VEPTfuYZT1jNbHAh",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "abbe331447be8e3193df943393336613",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "17fMZmRI5afP8pgFiBpKi8C21ZygG6sRiMt9cocOCNXA",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "13df0KEbOqYaOzV4yWH00XALacl1G25c2gDaqjWP6c5R",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c8eee22a3dedb02be56c851752dfc661",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1xpAko77TaeEtrfqLyoKN35qbbbXP6ecVrZDhFNm9WUv",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1yL96fS2P8KtiRVJUnJBuojRFHbFf5U8mKkFf30yVRev",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "4b92e4600bc0569b611321cc151a9ec6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Ckgr5M5wU2erUregylj4LbUF2fJ8soaDmoiYkFyZOgD",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
