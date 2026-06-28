"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1aQpUkOtqXm3QhGF1Ufnh3osLBCIQA9LYt8BcGHv9Z8w",
    "1LWbqW7Fw2CoqfKkwSNjmo3CZGveICwvsG9d57wl4fwT",
    "1IZnC5B5nAJy4KWI9FTQaMUg7bwJNN0k6uklNSB5zC1i",
    "1ygStJ9uSQ4aBHyaHunT5kcb6aJyKZoYjkQVZdwVUz0d",
    "1MuiozPPIleIvnaRvai8cbCVZcLnmNrS4o3q3nzoxwa0"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "9655705fa2632ccf5e118b7c490568dd",
    "7ef20de3fb32f507af46fc083e6f61b2",
    "84fb21a61b7fe4478b9053da0d649423",
    "be051456f53bea766ac05bc9220f4b3a",
    "04b8427fae435646be2e5cab5868630b"
]

LEGIT_PERM_IDS = [
    "fd8ef8b63080289c857bb6eb03853f42",
    "00542fc40e2f4afd412274968f5afd47",
    "4b51958829161dceb564e0a3b39a09fe"
]

NEEDLES = [
    {
        "id": "1aQpUkOtqXm3QhGF1Ufnh3osLBCIQA9LYt8BcGHv9Z8w",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "9655705fa2632ccf5e118b7c490568dd",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LWbqW7Fw2CoqfKkwSNjmo3CZGveICwvsG9d57wl4fwT",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "7ef20de3fb32f507af46fc083e6f61b2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1IZnC5B5nAJy4KWI9FTQaMUg7bwJNN0k6uklNSB5zC1i",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "84fb21a61b7fe4478b9053da0d649423",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ygStJ9uSQ4aBHyaHunT5kcb6aJyKZoYjkQVZdwVUz0d",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "be051456f53bea766ac05bc9220f4b3a",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1MuiozPPIleIvnaRvai8cbCVZcLnmNrS4o3q3nzoxwa0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "04b8427fae435646be2e5cab5868630b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1w9qE1Uths2wvPmhz5ut5hUh2jGTEk2ZWaGgD3iYCd6Q",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "fd8ef8b63080289c857bb6eb03853f42",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1hselINa6tD71oNGTV0yZpnFurv9xrCwZKbdR5QfY9ts",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "13rL20RDObw9ajM2h6g9YNfwn4NZThiOphnf66lN3JtK",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "00542fc40e2f4afd412274968f5afd47",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "16qS5eUqTJljqg9Szi7TArqXdD0ycntU5FVjTrFmWzJC",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1uRNuNspwcUVVew6MLdkBB2EUjI3CKLEWjW7viZW3DmE",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1jGLB54NWy4rBEzs2ou0dI31vVE9G5sLi1vmFfgwNHYG",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4b51958829161dceb564e0a3b39a09fe",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
