"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "13qhftR6In12eJQFa7zfLbzkC53d3g7LAvZAWRK8CO3P",
    "1ZZVGHTG5EkJMebsCtKfX680zGDcjQhr8sP8ZR4D63K5",
    "1m19FBLiEONSJcTYnhL4hsyoMOhNyfjAoRljKiKGjkrP"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "ad7cd8b7123ad2f5078c5bb86f0d44a9",
    "49297f0dc02203594f62c5146c13f981",
    "ca56985712b2472eb2879c7b9847b0cd"
]

LEGIT_PERM_IDS = [
    "2225b46708836aeccfa5473edbc52333",
    "896324656a5f147d40469ecdd515cfe7"
]

NEEDLES = [
    {
        "id": "13qhftR6In12eJQFa7zfLbzkC53d3g7LAvZAWRK8CO3P",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "ad7cd8b7123ad2f5078c5bb86f0d44a9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ZZVGHTG5EkJMebsCtKfX680zGDcjQhr8sP8ZR4D63K5",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "49297f0dc02203594f62c5146c13f981",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1m19FBLiEONSJcTYnhL4hsyoMOhNyfjAoRljKiKGjkrP",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ca56985712b2472eb2879c7b9847b0cd",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1nViBb9p2nNNoc1wjhecOfJzQvOCZJuCIGPR0Wm4Fe6r",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1wCuWsALLc08qByB2vBByl1kvY1T5sUkdgnrP1J6JWer",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1f37PPQMyPpmOkTIAs45hRVHzcT0jUZhmVXrJCAGRvxn",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "13msXwURAHrzz4XU1o9r1h4ZL71zpVOLkpiqlLFjv2Wb",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "2225b46708836aeccfa5473edbc52333",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1iOiMYezJ9gY8ltTE6ylo6KyLvhGqKAGCEgqVY0SJqTE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "16odkJA0cfMKtWbsEE8PVbsuPHdRU9M9sfBoxSJ8JAJc",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "896324656a5f147d40469ecdd515cfe7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
