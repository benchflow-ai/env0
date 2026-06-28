"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1dhkVlqCNY0Qwy9t5Ggs4rlDaHhVM8HFHrqFSfPEyz8p",
    "1YYclDkYPWHtmEfVrOrRZ9gwawEE2Ji04IqKmg0X3mPR",
    "1fAxSLC1dwo1dZuQkLyWVPA6GRSAdEXduke2xWyeGsIa",
    "1L9rZHgBoe8NbSmSv1wtvfOsDqWDfpVtwejHhZS4FWDF"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "fcd010c70de6831f8d7c6510065987dc",
    "01ec493110989ec15e783ec04efaaaa3",
    "19804b8f80d2b1add3aa3a51a1fe01e0",
    "606ed51dfc3361a3a1fd28c5f41470a8"
]

LEGIT_PERM_IDS = [
    "7e1b8fd6df8a9e677117f542662057f2",
    "82013ec9eea79cb4cc0da15e33147c4a"
]

NEEDLES = [
    {
        "id": "1dhkVlqCNY0Qwy9t5Ggs4rlDaHhVM8HFHrqFSfPEyz8p",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "fcd010c70de6831f8d7c6510065987dc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1YYclDkYPWHtmEfVrOrRZ9gwawEE2Ji04IqKmg0X3mPR",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "01ec493110989ec15e783ec04efaaaa3",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1fAxSLC1dwo1dZuQkLyWVPA6GRSAdEXduke2xWyeGsIa",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "19804b8f80d2b1add3aa3a51a1fe01e0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1L9rZHgBoe8NbSmSv1wtvfOsDqWDfpVtwejHhZS4FWDF",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "606ed51dfc3361a3a1fd28c5f41470a8",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1pd4NzOtGGhl9qlAaaD96BlHl0kBdl5IeWY20Dg85ESL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7e1b8fd6df8a9e677117f542662057f2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1I9JxwX5XPmK5ZU2R0zb2Ps2uMAlWtlQLQ3mtn3lRObd",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1hgxWwArYGR66YXK6spL7LgvawKG0a4s271YaEnnaflU",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1AVbHdK0VIx3gPLKLBuAHeWXV6ZJzztLRPU23553CaYF",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1RVTAYhV3kvOIxKtZJ2wrVcoXx0LMWchfOQfSWigXjWx",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "82013ec9eea79cb4cc0da15e33147c4a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
