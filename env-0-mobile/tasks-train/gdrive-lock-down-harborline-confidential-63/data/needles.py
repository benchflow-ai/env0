"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1BIDeYJNilmJJMVpM9JpfJD0uazTR7JBqU8hLaDJmZlS",
    "1nXriWM2FNLWzgtC5lJ7X89h30gPwmQHIAWJ9YOK6qf0",
    "16X4gCBTeQJj2oP9Izdt9DSxevYsYRBhm42eD96SHzEu",
    "1ZtMiYI8FcDxE0iwFDKP9SEacBI4xK1bk6GHAitpejMS",
    "1vJQxHr3gD0fEJErv65f92ot4QSCif03cHztwFozQvaR"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "beda8a1e421b663973968fcf4c091c03",
    "993b816cac429bce644613dcf7e179b2",
    "2678b213731bf2847bfb92ed30254553",
    "5a1823ca414547f6044981df0af1bc68",
    "798018ace071103722a1b13c689c6810"
]

LEGIT_PERM_IDS = [
    "9289a0fcdea16b6774439e7f0adde749",
    "0007bbc689b17613ca80a0d1104a6401"
]

NEEDLES = [
    {
        "id": "1BIDeYJNilmJJMVpM9JpfJD0uazTR7JBqU8hLaDJmZlS",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "beda8a1e421b663973968fcf4c091c03",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1nXriWM2FNLWzgtC5lJ7X89h30gPwmQHIAWJ9YOK6qf0",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "993b816cac429bce644613dcf7e179b2",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "16X4gCBTeQJj2oP9Izdt9DSxevYsYRBhm42eD96SHzEu",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "2678b213731bf2847bfb92ed30254553",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ZtMiYI8FcDxE0iwFDKP9SEacBI4xK1bk6GHAitpejMS",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "5a1823ca414547f6044981df0af1bc68",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vJQxHr3gD0fEJErv65f92ot4QSCif03cHztwFozQvaR",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "798018ace071103722a1b13c689c6810",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1sjrz9xhmnJSzLUDquhNtwXgRUnIXA6NAfvqKHlMlo5A",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "9289a0fcdea16b6774439e7f0adde749",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1UK1WfG7qX900d8aZtWOlhuC4I8Z3gniR2vfrYOF21hf",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "19Wq9y7Jz32cxa2F9d97UNph0wfysDwYDbUoykO9UJIw",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0007bbc689b17613ca80a0d1104a6401",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1JYEknV2zzyGFdcXOfY3Up4PLpIndSZ0tYm2ZDNulcSc",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1UiqT0nVbRbesj89byB4T6FBeeppZZq3hg2pXFEQw1D5",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
