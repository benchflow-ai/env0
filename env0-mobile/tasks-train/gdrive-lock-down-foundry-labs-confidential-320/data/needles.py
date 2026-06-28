"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1xystOmLM7RyhzssFAlbk48XTmX8bbTHIGEC5g3vyzhV",
    "1WspUwFGZVZaKPGl7IIneqbBMhinBwCeXzryahmM9CIr",
    "1ZCO43zwiJSzQjXcSqJt8UQIGTXcI4FPFzAaR33hjdAx"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "de01cc6fb04a7b0e54623c45860e0f35",
    "a6d5615aa413239d98dff0c455bf2a58",
    "f79d11fd4f39b72e2151abc36c7869ec"
]

LEGIT_PERM_IDS = [
    "85e1b98782415b553dd46d736fc104f6",
    "3e5329e310c8a2d63d7c79fa09fd1591"
]

NEEDLES = [
    {
        "id": "1xystOmLM7RyhzssFAlbk48XTmX8bbTHIGEC5g3vyzhV",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "de01cc6fb04a7b0e54623c45860e0f35",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1WspUwFGZVZaKPGl7IIneqbBMhinBwCeXzryahmM9CIr",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "a6d5615aa413239d98dff0c455bf2a58",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ZCO43zwiJSzQjXcSqJt8UQIGTXcI4FPFzAaR33hjdAx",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f79d11fd4f39b72e2151abc36c7869ec",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MY5OL1u1cEHBniBtU0k9WTHbqgzFIWjCHXSL4yzIbsM",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1UYbaU3bK5tEbbXwTH3YPzU1jCc6qsOWrCfZ4W85SNyt",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1uiQopUiUx70MZJhJGZpFtYfg2QMf0SjbVz1oYn79Vjw",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "85e1b98782415b553dd46d736fc104f6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1lv9IaTaH4qi6krNHiK4V9M4X7XJ4knfgUp7pqcHbnvT",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "19lo5ZKGhejzgENe6R3fBeUEqiUJBsu4p50OhSD8zJ8W",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1o8SxswrdqvXfO2eVpAFG0keEVIacnxUo1Pyd1NDR0Vj",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "3e5329e310c8a2d63d7c79fa09fd1591",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
