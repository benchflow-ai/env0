"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1dpkjAusdjytEmPUD07f9GDjn0hi6Befa6wXfpwIxXm3",
    "1zndcWBClrRq9wG4lVN5JuKYoyEVYWS9TE1KG2wT5a1G",
    "1hHOSoSEshsYdKir2SiM0ZOGDul9nQA657WGA3tu439U",
    "13lfKypObzpTTEWOjknxEDE1QXrSfrzyLYvybPi16ZPs"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "6d2f972446d2444bb43444d344f3edf8",
    "44c2d87af01ef017254d34e92ec7e638",
    "09701749532bf28add07cc673f561bde",
    "bf53012417c2b757c331903b5d99b39a"
]

LEGIT_PERM_IDS = [
    "15b95d954b9119ee1b5cf2ef6f8f65ed",
    "32106aeeb6881da7728fc56174f9703d",
    "58022b44f4004cafb38f4e6552501028"
]

NEEDLES = [
    {
        "id": "1dpkjAusdjytEmPUD07f9GDjn0hi6Befa6wXfpwIxXm3",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "6d2f972446d2444bb43444d344f3edf8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1zndcWBClrRq9wG4lVN5JuKYoyEVYWS9TE1KG2wT5a1G",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "44c2d87af01ef017254d34e92ec7e638",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1hHOSoSEshsYdKir2SiM0ZOGDul9nQA657WGA3tu439U",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "09701749532bf28add07cc673f561bde",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13lfKypObzpTTEWOjknxEDE1QXrSfrzyLYvybPi16ZPs",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "bf53012417c2b757c331903b5d99b39a",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1bp8pFhRkbWQydCrb1LsJfwpT6ABQmHS6c56QBCu0RhS",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1VMS5AbU5Cp8rlXoHrdtianBUQRWQ7xQCl4PAD79co5e",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1qcEoXorSFaSPE4htgwq0YR0ci1wbZzLT8nzXzeqCu5x",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1ZuL3Ag20fGkdz2hDma6xW5bWNPU2Uctta6uxuSN6QPL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "15b95d954b9119ee1b5cf2ef6f8f65ed",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Oxu8rujQMbPTbNVQro3F5QsIAzyqfycNAHVwmYfxxnQ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "32106aeeb6881da7728fc56174f9703d",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1mopkz8p1RyQE4mSxZwgrbDy3OHNZ3ucSzzu13hJgo6E",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "58022b44f4004cafb38f4e6552501028",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
