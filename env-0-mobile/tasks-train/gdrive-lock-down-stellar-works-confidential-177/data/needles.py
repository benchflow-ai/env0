"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1jCEpGahctuOtyRbOg1VT7krg5HdMeHSkpheE3EcQ7ej",
    "1LAdBAdncZMIMsaDQJ9xw7ULYUCg0FWVPXRqlccKMFiA",
    "1QGqxd1YiCACEbxx9PaxE7NkZ2WapNNTNg1MH5rxAJsd",
    "196Atp3fFbjVYCznzhEBVaS2csNDJwgOIRFW0sgBwQAH",
    "1Zu5VpSnZMoFT0pFlDxgeQv0Ayy4QFyfUHzBDYGBl7OA"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "18e4c3dc83dec9c71e4c9065b2a58daf",
    "353e4466bbc5ab7cac21216559d13e27",
    "9911044a5883f70878c02f44a392f818",
    "3fb866a4fc54b2564d537caf81b20c6f",
    "a5583633f7ed2042b0cd79f323318ef4"
]

LEGIT_PERM_IDS = [
    "5c17847254924f4289df8b4eecc9345e",
    "bdf7f0c872cea7714c86f60a3da652d8"
]

NEEDLES = [
    {
        "id": "1jCEpGahctuOtyRbOg1VT7krg5HdMeHSkpheE3EcQ7ej",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "18e4c3dc83dec9c71e4c9065b2a58daf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LAdBAdncZMIMsaDQJ9xw7ULYUCg0FWVPXRqlccKMFiA",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "353e4466bbc5ab7cac21216559d13e27",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QGqxd1YiCACEbxx9PaxE7NkZ2WapNNTNg1MH5rxAJsd",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "9911044a5883f70878c02f44a392f818",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "196Atp3fFbjVYCznzhEBVaS2csNDJwgOIRFW0sgBwQAH",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3fb866a4fc54b2564d537caf81b20c6f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Zu5VpSnZMoFT0pFlDxgeQv0Ayy4QFyfUHzBDYGBl7OA",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "a5583633f7ed2042b0cd79f323318ef4",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1AytKiV7qehennQvDTEmt2EYSvlzdDWMHMeoFvjJ3yJg",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "12A3iEf7OVAZMfHXg0DefUB2N0kznCFKEKl9cNXX0CwZ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "5c17847254924f4289df8b4eecc9345e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fZlfznMAHZOdZM92zE5znjRB8kSpXcTuOx5JO6DAscq",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1Wx9uXKcVSYKOcrWAbXV5EsJzrf5btrWNqbxbri1tIcQ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bdf7f0c872cea7714c86f60a3da652d8",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1sK5u7dFb0eErqu7a7bkzA9CDpM8BqZttfJyfhS88Ymo",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1hhbtkvuWGAWkuBQT83cvKDgq2A9vhDwWYnydrVXXODf",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
