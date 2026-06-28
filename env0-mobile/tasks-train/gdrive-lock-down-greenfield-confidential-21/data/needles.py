"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1G5ZKuNGlPJh0wtKkWDCIrpgl8Fg2t3Pilyg6IXJtxYI",
    "1oVEieW1zyr8VdFmX2w6B4RoHoUm1onIQJjf37H0YvD3",
    "1queFdcRxbv9xsnijF8tvJtTTA1aVdkXjqboI24hb3OS",
    "1pJIo8Vi48enxxILr58fCrBeKTebtRSTcYAYzQ0OxdYe"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "3302acf7b341bdc48e5b7af91ae8a618",
    "c4a44acf3e08346fb889b9fab2e17a44",
    "5ce4e664719d0c42dbf2868fc8fa9c4a",
    "d870540f212a2d22087abfbf03345766"
]

LEGIT_PERM_IDS = [
    "b0f96064778a2f1571f911b335aab1bf",
    "8e182d5071bd8a166dd4d41a4323a245"
]

NEEDLES = [
    {
        "id": "1G5ZKuNGlPJh0wtKkWDCIrpgl8Fg2t3Pilyg6IXJtxYI",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "3302acf7b341bdc48e5b7af91ae8a618",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1oVEieW1zyr8VdFmX2w6B4RoHoUm1onIQJjf37H0YvD3",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "c4a44acf3e08346fb889b9fab2e17a44",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1queFdcRxbv9xsnijF8tvJtTTA1aVdkXjqboI24hb3OS",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5ce4e664719d0c42dbf2868fc8fa9c4a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1pJIo8Vi48enxxILr58fCrBeKTebtRSTcYAYzQ0OxdYe",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d870540f212a2d22087abfbf03345766",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YXnhVkDRRHS6e5B0tVq5wouf5idUBOlzDm7F9Ek822M",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1hIfD7XpWv1BmARMwUPs7O9bDa8SOShopgo39jM1agyA",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1kPZZgale7eobzbOG7cjLit6GpflOFofhVKzemXnQ3tO",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1NZDcK9nQCM07XB0oQqKdnA7BYpLPwUNkJ0PWTxG52vh",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "105Yx7xLA65V13dTJWnaZY2LTfcPpz9ZQsqZcy3FK1Pk",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b0f96064778a2f1571f911b335aab1bf",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1x2KlbWQkhitvDeUVfbesu5KpRb8xua4P15yVL3dzbNo",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "8e182d5071bd8a166dd4d41a4323a245",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
