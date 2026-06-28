"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "101QCk56jvL87PEkn3c0mRiXUsueBCVSe7Lm9hLEO6f1",
    "1SbpUWnBxRz8Q1m5e6IBTtkVNP71CNwsULmBMWCqEJtb",
    "1V3aLjFLhc0ZdcYdpmDNaKKPWvP29xO5xWlazlvZ8JRp",
    "1442bG4FHtX6dy13wkUhoQkBAzHCUBaP6msO8XZNF1hR",
    "1TP7fvMhzMxmGeROExgVpBmhx8ZhaWlSxQ7lOR4SypyF"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "caccc9964be1ec1839d779f1ff08827c",
    "51e9d88a7df038a99d4f3ccc82a9d50c",
    "781915c01873357fcc793bf2c9e492b6",
    "85da589bbd52f6cfa9c6ac5e0eb9b53a",
    "a13bb6f1e5f3f005193859e01ce9fe12"
]

LEGIT_PERM_IDS = [
    "5aeb5fc913e1d26a275eb3814ad0f28b",
    "a96e34f16a5e2a9e26aa45e9825a4bce"
]

NEEDLES = [
    {
        "id": "101QCk56jvL87PEkn3c0mRiXUsueBCVSe7Lm9hLEO6f1",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "caccc9964be1ec1839d779f1ff08827c",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1SbpUWnBxRz8Q1m5e6IBTtkVNP71CNwsULmBMWCqEJtb",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "51e9d88a7df038a99d4f3ccc82a9d50c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1V3aLjFLhc0ZdcYdpmDNaKKPWvP29xO5xWlazlvZ8JRp",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "781915c01873357fcc793bf2c9e492b6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1442bG4FHtX6dy13wkUhoQkBAzHCUBaP6msO8XZNF1hR",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "85da589bbd52f6cfa9c6ac5e0eb9b53a",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1TP7fvMhzMxmGeROExgVpBmhx8ZhaWlSxQ7lOR4SypyF",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "a13bb6f1e5f3f005193859e01ce9fe12",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1GYeVm4sCfSRY51XUjZ6NAb3vZbLtKoe0SjtaotKSRW9",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1EmnPvTlIPxx3qgVCTbk16dEU2uqPkoQalyYqOaQe3I4",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "5aeb5fc913e1d26a275eb3814ad0f28b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1TmuTvxn9BILJGeFPlBa7Y9BrvGGSytuReZpSNOEkkER",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1r1Shb9tb1iAw7h5sqxJlcfWC0DaEeec4zW6AEMoEv5p",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a96e34f16a5e2a9e26aa45e9825a4bce",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
