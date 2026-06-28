"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1Ib7hgT5kFAbqS4alK6ngwFT9UcStzfh2x5lf2KzKu6H",
    "1jO0JcigyrVUWdnf37REltE5ln6WsakwEj1cUBTvXfFL",
    "1wsrTNnYa3xhIdpvVT0Baj5MLOqGpdgtLMyBzD3nUGQu",
    "1ucAro4L84tQ63rVncvkpDtmg1r8Ymo6J3D9BFa8rktL"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "08679fe70a30e47cc7b9844d6f74a4f8",
    "dcb7e27e764deb03119a1069b1302362",
    "fa1ba781cf83c91453ef358de22c5a23",
    "9ccc2e612027e9239099674b8fe5d4fa"
]

LEGIT_PERM_IDS = [
    "3002ff1ca79b852aad07f2daf90a1657",
    "c1ebfc43692424fe2b54f5bd645ed156"
]

NEEDLES = [
    {
        "id": "1Ib7hgT5kFAbqS4alK6ngwFT9UcStzfh2x5lf2KzKu6H",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "08679fe70a30e47cc7b9844d6f74a4f8",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1jO0JcigyrVUWdnf37REltE5ln6WsakwEj1cUBTvXfFL",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "dcb7e27e764deb03119a1069b1302362",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1wsrTNnYa3xhIdpvVT0Baj5MLOqGpdgtLMyBzD3nUGQu",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "fa1ba781cf83c91453ef358de22c5a23",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ucAro4L84tQ63rVncvkpDtmg1r8Ymo6J3D9BFa8rktL",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "9ccc2e612027e9239099674b8fe5d4fa",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1snqou7Ku1DTCK9WaNUurrcuhHRz8UjV2b0tpIgTnsUc",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1vhpGYNNTFRuBfvagt3CtYHrtZfSIdveAV1OdBYbIPgs",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "3002ff1ca79b852aad07f2daf90a1657",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LXAH0HfbizcsYoNGEobkrMN8mc6vgakrg6SdQQzyhk9",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c1ebfc43692424fe2b54f5bd645ed156",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1c5UQqqbMQaJkO5FYgrMlloMUschxi3AY8LtyC0YPQKK",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1xZOq6BU0umNAvs76bDhvABmz5QfyE4fEDALxnlCNt0i",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
