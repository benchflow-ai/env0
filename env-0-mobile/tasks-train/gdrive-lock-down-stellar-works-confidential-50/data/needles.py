"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1jg6KMyRAGNU8tQaw6UphQY7VlF7wub0HpreBwvIuC9T",
    "1j3dxCOsTdNWCEUOTyTasoHDkgFongEnXKMx6cgqMkue",
    "1Of3qxvqHKkBk6LsFxO7ZhW0bG91ldVyrIpCJUEqxXUt",
    "1JQwJQJcy0wH7miMFvJO6PGrr8XzaiStqS05w9hhs4C0"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "c5e01cebd5c256ab51599c821b02a763",
    "16d54d6e7e996da669a7cc23c4d76537",
    "a3b4c6df4dc2ca2b0d4b5e0ef1c15988",
    "4985e15cdcff368b0491148e77b85910"
]

LEGIT_PERM_IDS = [
    "39fc8bdde1011d153a362701751e31df",
    "eade8eb925fcc42658feec885b7b5cbf"
]

NEEDLES = [
    {
        "id": "1jg6KMyRAGNU8tQaw6UphQY7VlF7wub0HpreBwvIuC9T",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "c5e01cebd5c256ab51599c821b02a763",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1j3dxCOsTdNWCEUOTyTasoHDkgFongEnXKMx6cgqMkue",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "16d54d6e7e996da669a7cc23c4d76537",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Of3qxvqHKkBk6LsFxO7ZhW0bG91ldVyrIpCJUEqxXUt",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a3b4c6df4dc2ca2b0d4b5e0ef1c15988",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JQwJQJcy0wH7miMFvJO6PGrr8XzaiStqS05w9hhs4C0",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "4985e15cdcff368b0491148e77b85910",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1vtesOHfrqoaijRghCtrA2DkNLZcqk7ocwv7byCN0OXa",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1BtlBWblHlZnJgLunGf8FxskxiajRcZE6B4q5i5eXh78",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "39fc8bdde1011d153a362701751e31df",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1G4VJJes6F77iBzZqRrQMTiw3lxcHNqAkAL1SbIxq2m7",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1WXf4Aqmo3OBuzZWYbQtWwRzoCuj6Az2CiCpP7IUFLSC",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1ToBzcJNZCgTgk90gJX00f7NS5fMrGL9dsBsWl2y9vPf",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "eade8eb925fcc42658feec885b7b5cbf",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
