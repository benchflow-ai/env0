"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1YylKb0YJwJaGVp5U7MGFbzpcS25BQ8LOb1cCTkDFMbJ",
    "1VNx4RYKWvwwci6q8cuKxvStZrGK7V7EEChjUmQXoCBo",
    "1PWiGPuWfzPXHbWzX7x9GkckG6MxRYPqXreGss6MQqrR",
    "1yQvCkrq23A7s9L9PX679Pupnzqk7tCVbhiL1VcteAJG"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "0eb1fe8849789c35991093fda2c253ef",
    "f9bac0ea72b3f3af956a8d86edef05fe",
    "0451296dc9b41734888ef22cfedda8b0",
    "75df3fb881ee2a46f35c678907113137"
]

LEGIT_PERM_IDS = [
    "6292bc681b8d00ac8db40f8d55660acb"
]

NEEDLES = [
    {
        "id": "1YylKb0YJwJaGVp5U7MGFbzpcS25BQ8LOb1cCTkDFMbJ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0eb1fe8849789c35991093fda2c253ef",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1VNx4RYKWvwwci6q8cuKxvStZrGK7V7EEChjUmQXoCBo",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "f9bac0ea72b3f3af956a8d86edef05fe",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1PWiGPuWfzPXHbWzX7x9GkckG6MxRYPqXreGss6MQqrR",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0451296dc9b41734888ef22cfedda8b0",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1yQvCkrq23A7s9L9PX679Pupnzqk7tCVbhiL1VcteAJG",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "75df3fb881ee2a46f35c678907113137",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "15eBiYnjEUWiR9t6ibyVdACSfMNaLfofSpqhNSwq6bJU",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1cy3P8eztQumnIKCI2BhVwpThvnFu8rLfNTvQX4TWXy0",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6292bc681b8d00ac8db40f8d55660acb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "18XAibZVd94gsBTyl2GaBNUmCvPO7MO58wc2nj6kqxWo",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1VHVt8Gh6EvrORDuzclMMksOpzWf7Xgr4WXS7xXBA7fi",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
