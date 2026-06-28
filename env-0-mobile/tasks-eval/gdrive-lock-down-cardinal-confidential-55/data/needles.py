"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1TvbfU56IChEFcU8rtVhqHTg9uTD1P7XP4nMiG3tz6s2",
    "1yPDg9mAAX5sO3IDA3c4M3VuiFhoopOvC0obAIatVRIS",
    "14uROq97Sptvddu9ocGtZGJaW27fc69l6108hj4gt6hJ",
    "17MUN9UpsDLoX55rnXi0M7g9jZCgMXxIf2JTDzL7p148",
    "1nbZuaQ6EufPO551SrfhaDmEnSriQUqbHS3pxjncFHvd"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "7bebab8b28bce79af355d6614f996670",
    "bd7b889af2164223a41a4d6810bf7a74",
    "a98a63e869b5f3c08562aea43b82d4b1",
    "25b12453012ae10a6d0fa0edfc8e077c",
    "44bb5e2d7dbe287f070e2285f66f1af7"
]

LEGIT_PERM_IDS = [
    "ce86acc3ebb81dbbf3c180d376482918",
    "ad6d223cd4c5a30bce9ec93ca3925ec3"
]

NEEDLES = [
    {
        "id": "1TvbfU56IChEFcU8rtVhqHTg9uTD1P7XP4nMiG3tz6s2",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "7bebab8b28bce79af355d6614f996670",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1yPDg9mAAX5sO3IDA3c4M3VuiFhoopOvC0obAIatVRIS",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "bd7b889af2164223a41a4d6810bf7a74",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "14uROq97Sptvddu9ocGtZGJaW27fc69l6108hj4gt6hJ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "a98a63e869b5f3c08562aea43b82d4b1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "17MUN9UpsDLoX55rnXi0M7g9jZCgMXxIf2JTDzL7p148",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "25b12453012ae10a6d0fa0edfc8e077c",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1nbZuaQ6EufPO551SrfhaDmEnSriQUqbHS3pxjncFHvd",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "44bb5e2d7dbe287f070e2285f66f1af7",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1LI2gNQhVvGYFPl0YWTy2lUWSUT8ie7FlA7YtZ7u1HKx",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "ce86acc3ebb81dbbf3c180d376482918",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1vaNjQts4yT02uG8OIJ4S1TMZv9KcITAlJrlVwgaqIrx",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1ncMgyqgZbrs6VCx8YqN5rX83QovseTT9If1FZEWz2Id",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1EejNmTnItZ9AWh2DYOZ2iJTbOSSu4fHijuOrOOqqMDH",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ad6d223cd4c5a30bce9ec93ca3925ec3",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1Zy125wuKqnmnVMVtaTcJCq1jmss1PFg3KucaSgwXB99",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1mMRkleLah4ClOZT2WyXFN88BNgTtFaQWu5MmPkKMag1",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
