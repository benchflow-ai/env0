"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1GOD74rnCDK8Q1I0YxAGPxHer9anCFbFeAUroXOmJcFP",
    "1wivPmdMwy0bE5Dz5d61ic24QGvJmHPur1XofnLLo37P",
    "1OA4c74Gjd2p2IAcLJhaxLouhBlxnQRTEuxeBFWDKup8"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "06968ce3a3e9bd0acd3f326d358eabc8",
    "2342467e4cdde96373c72e4cc7a3a92d",
    "9f5b3e964341fd0c9620a9bb9f93ce77"
]

LEGIT_PERM_IDS = [
    "61d3bc499b9d724de82bbd838b91d3a0",
    "cdbad0e020e8e68f7a2ba80c1eee3089"
]

NEEDLES = [
    {
        "id": "1GOD74rnCDK8Q1I0YxAGPxHer9anCFbFeAUroXOmJcFP",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "06968ce3a3e9bd0acd3f326d358eabc8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1wivPmdMwy0bE5Dz5d61ic24QGvJmHPur1XofnLLo37P",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "2342467e4cdde96373c72e4cc7a3a92d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1OA4c74Gjd2p2IAcLJhaxLouhBlxnQRTEuxeBFWDKup8",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "9f5b3e964341fd0c9620a9bb9f93ce77",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1bPBX2si4UI9NjfGqt6pnFf5gStL3cX8wf2buXlnZvNu",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "61d3bc499b9d724de82bbd838b91d3a0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "11Apo5DyQNNp9QDy51zQqa1cxyaS5PaWVp58jqjeqMjv",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1oF53NUz0WBIjytewjNOcj097FHA7a0Kkq6R0nhElCY6",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1e1EzsTmeGQ8Mjl10DqClBYtagfMTNF2SDFWx8GamYFJ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1C3xm6eD2sLm3KWSKUjQaeSh3DmjSlp205w7ikF4XBG5",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "cdbad0e020e8e68f7a2ba80c1eee3089",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1aZYn3kyS91I4MIMG3Rw8IJysg2jEPcA5nBpJkBEk13J",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
