"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1tKhPASU79znzxQSzAshj4Y4stXQPFbNlkvc0OKLBP40",
    "17gH1QuZJyIbx0wAgw42WrAXpmnzi2zbRNRfx2e8tnwF",
    "1HrfES6tJY2x1muZIoy2M010cYNB9t4bdsZsZQ1JKZB1",
    "1eCJjXjee4Ggd5vMR7123qVoPg7Rj8ioRQWgQ4LL3KV7",
    "1Jfg7INUJzj6T4Y3687jehyBbTLpEZZ41hTkFiEMK17J"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "cb25596e692a54f7f3c674798ce12de4",
    "ca155a33ea4826374feafe3c43722ad3",
    "898d2ffaa4b8af502e903ea9e0de8107",
    "70447d03e33c77b1b61f8c6d8275b2b0",
    "eadd4a07c974e835a75c8de0f8701caa"
]

LEGIT_PERM_IDS = [
    "a2412ff7ac4951ddcced5fe1d182a6b0",
    "1bf76ae5dd5524bffd0a5544348a3fb4",
    "f8e828a2518c086a1d8291cc416cbf7c"
]

NEEDLES = [
    {
        "id": "1tKhPASU79znzxQSzAshj4Y4stXQPFbNlkvc0OKLBP40",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "cb25596e692a54f7f3c674798ce12de4",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "17gH1QuZJyIbx0wAgw42WrAXpmnzi2zbRNRfx2e8tnwF",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ca155a33ea4826374feafe3c43722ad3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1HrfES6tJY2x1muZIoy2M010cYNB9t4bdsZsZQ1JKZB1",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "898d2ffaa4b8af502e903ea9e0de8107",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1eCJjXjee4Ggd5vMR7123qVoPg7Rj8ioRQWgQ4LL3KV7",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "70447d03e33c77b1b61f8c6d8275b2b0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Jfg7INUJzj6T4Y3687jehyBbTLpEZZ41hTkFiEMK17J",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "eadd4a07c974e835a75c8de0f8701caa",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "11uuTEIBxC3r76xJYRSxZ00DVJNH39d2f1R6KYggqeXK",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1f77dLwN5xB5yOs1AEal0ZObsSBNvj089BeD4auufq4c",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a2412ff7ac4951ddcced5fe1d182a6b0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "17CRcMcDsaFSzQWJEn6HEndrvxgOpCtSyEwuJEHqqnbN",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "1bf76ae5dd5524bffd0a5544348a3fb4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1qd4VUnR8ZOUR0tZ7tdnpFCRXKbfCDDH8rwl2FLl6K39",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1EzyTmjwGfwHzKBAitfTH1tBotpei12EqQ7s5by5BF2G",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f8e828a2518c086a1d8291cc416cbf7c",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
