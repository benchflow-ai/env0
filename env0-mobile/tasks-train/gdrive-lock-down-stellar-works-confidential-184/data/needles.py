"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1KjSkIR0Aub9coArzbQSd3RLv9pjH8p8niSSwmqz60xL",
    "1MCtLmwEDeSoTEDQqEm1P6Vg4qVGd2c16XGdplHJX9ea",
    "1gIIht4e0IhIROcIir4mNpmnhLtDotLSAAiNNivY4PdR",
    "1Lmk87Pib6ZzSQVBnwAh0guliJ23jOq6FDGAXjv7e1OX"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "c587f2393a5543dcd07e12e6a1e407a2",
    "48219fcca26a42f611b0b01756683f4d",
    "c862821ec88753c289ec8f3e607e74fe",
    "3b44b67df1f8bf0f8c9b55f609b27e01"
]

LEGIT_PERM_IDS = [
    "f8f2ecc24511f24dd604c57aea65ba31",
    "239b065f22f7fca4f04fe6a128cbb2a7",
    "ff541fabea877db435c45edab640a9f1"
]

NEEDLES = [
    {
        "id": "1KjSkIR0Aub9coArzbQSd3RLv9pjH8p8niSSwmqz60xL",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c587f2393a5543dcd07e12e6a1e407a2",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1MCtLmwEDeSoTEDQqEm1P6Vg4qVGd2c16XGdplHJX9ea",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "48219fcca26a42f611b0b01756683f4d",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1gIIht4e0IhIROcIir4mNpmnhLtDotLSAAiNNivY4PdR",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "c862821ec88753c289ec8f3e607e74fe",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Lmk87Pib6ZzSQVBnwAh0guliJ23jOq6FDGAXjv7e1OX",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "3b44b67df1f8bf0f8c9b55f609b27e01",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1HVJPHJcu89gDFhdqjv7rYwo04B0jkpKaILsrFXFz2JU",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f8f2ecc24511f24dd604c57aea65ba31",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1f3MMQKkmtZjSNIj1CXwb19W60TiE0CJV3vPPhgkbYvJ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1f9wrao5hG2pqEn0mVozIUkXl407WWaWq8nwSl89T6tT",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "12gKE5QXfM9h6AYjgsN2mWQXgFr33v15rLqPnvQt51ct",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "239b065f22f7fca4f04fe6a128cbb2a7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ZgvRLs9FmINQDLYu99KXJnEQ0ApWzSDm1V1UgLHrLAA",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ff541fabea877db435c45edab640a9f1",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
