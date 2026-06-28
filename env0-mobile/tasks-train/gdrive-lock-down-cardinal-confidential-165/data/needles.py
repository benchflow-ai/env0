"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1oTqUzhY1Tz6w8exbPgMl3dClpmUlOXmwLiDKVIIptkv",
    "13rgfCHzl8wb1ie1L4iEUbnnwaeq5XgrTtwnQoIoD0Rh",
    "1T8mP99lp8d9qgeaH1TYFq22N4lrDT39rrFezLrEywzH"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "f77b838385056cee8c362c0b230c17e9",
    "d80b6fd70c7c1e02c003845c1cb254ae",
    "d5eba58d41d91adbb60bf46e6e9cc66b"
]

LEGIT_PERM_IDS = [
    "3b187f6bc07baa531fab540480a5697c",
    "8c8715d836b1582ec6684fd78e4d93fc"
]

NEEDLES = [
    {
        "id": "1oTqUzhY1Tz6w8exbPgMl3dClpmUlOXmwLiDKVIIptkv",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "f77b838385056cee8c362c0b230c17e9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13rgfCHzl8wb1ie1L4iEUbnnwaeq5XgrTtwnQoIoD0Rh",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "d80b6fd70c7c1e02c003845c1cb254ae",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1T8mP99lp8d9qgeaH1TYFq22N4lrDT39rrFezLrEywzH",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d5eba58d41d91adbb60bf46e6e9cc66b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1RFs3RLaD5k51QcMEtHdqFNqK0fuxDa9kQ7RPFPMqiHu",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "15S4ZjyAp1c9FTvcXEzvgqy2DVFSg4CVLSpq3u5iuhj3",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1XUTgL5GMcrSCHv5tom4MJxraLVO4U1PHeBfLR4PQTKj",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "3b187f6bc07baa531fab540480a5697c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1vVyYCUJ5kP9a56gtzk5IIdQamci7bkZucx0B0QKJitb",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "8c8715d836b1582ec6684fd78e4d93fc",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1UpdgNixYBYUeVRS3KPtNE4lTTjnbm47IphgQwYh2wta",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
