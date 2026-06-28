"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1MdZidPiDpxoJTT2aoXAnbnicmakfoVsKLKEMuaGt2nW",
    "12xUc0UUuR7dtD28SbYBMX9sfI0KW9O65mOY86xYSuci",
    "1ZyYNduIhKlW7QzbNO9uWIgDBBH0zbZmgI2l0ZiOHDbZ"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "69131ef71b8fe7d97e1ba31ebc2cd105",
    "3f5caef09994903fff03ab9936ed2ed3",
    "6d42fc19d1bcec75f09abe1ae42bb2ee"
]

LEGIT_PERM_IDS = [
    "76a67519df252eba1d082dc5db85d9cd",
    "f3edf6222d32f401b4ca50a4764a5bfa",
    "c62b56e4f20e5cc0937674e7253269eb"
]

NEEDLES = [
    {
        "id": "1MdZidPiDpxoJTT2aoXAnbnicmakfoVsKLKEMuaGt2nW",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "69131ef71b8fe7d97e1ba31ebc2cd105",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12xUc0UUuR7dtD28SbYBMX9sfI0KW9O65mOY86xYSuci",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3f5caef09994903fff03ab9936ed2ed3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ZyYNduIhKlW7QzbNO9uWIgDBBH0zbZmgI2l0ZiOHDbZ",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "6d42fc19d1bcec75f09abe1ae42bb2ee",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1caMi8Mwa8mlsMYHa1I1GbPLUE2zKNBSC31bVeYtvzrq",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "76a67519df252eba1d082dc5db85d9cd",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "12CEOd0tMdM43rzZmujoupTfxMMPC3hQx935u9CJbPcl",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f3edf6222d32f401b4ca50a4764a5bfa",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1vlj0LO9bkU0cNAX4sVS7Cfcf4mEuom11pbVKROi9Xd8",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c62b56e4f20e5cc0937674e7253269eb",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1ykoK4zhKCMPnUvC9lkdKYVq6T84eNsAR4wHy7WeuguU",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
