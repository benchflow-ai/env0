"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1m4tGnaWOwuAJfeNFhvhZCwJFYnIROnhlwAfo9lz9T4w",
    "11lprhN9PgV5iIr5Fv79fwGnTU4A7AiKTDeBnYqWaeDW",
    "1Oz8ZnvS5dNyiWgN7fAmsM1SgHZGeQc6OHG9z6LibMvc"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "1f307cfd175fa4cf87e122888313b175",
    "b586e32ed608d076a6b36c4ff4ce0661",
    "7cb5eeb743c1767979fc9c157e3574e8"
]

LEGIT_PERM_IDS = [
    "7da1afa5bea3effea4783755bbf432c4",
    "49615d902b47a997361d1ac055562f55",
    "6acd8567aea4cbf3d07463e3c6c56565"
]

NEEDLES = [
    {
        "id": "1m4tGnaWOwuAJfeNFhvhZCwJFYnIROnhlwAfo9lz9T4w",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "1f307cfd175fa4cf87e122888313b175",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "11lprhN9PgV5iIr5Fv79fwGnTU4A7AiKTDeBnYqWaeDW",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b586e32ed608d076a6b36c4ff4ce0661",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1Oz8ZnvS5dNyiWgN7fAmsM1SgHZGeQc6OHG9z6LibMvc",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "7cb5eeb743c1767979fc9c157e3574e8",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Ttc5dZJzbBUqINT3OKYr29nvp1QHnnO8Qmr707k5pkF",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1W8djkWkoKv7bp64kUu90RAW2X4CI5yXsH85Oq4nJkdH",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1wQV3iDk82ogGXxrWs7MUFZMKMZYFcMSbZRMgm3KwAsQ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7da1afa5bea3effea4783755bbf432c4",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "17G6Pd77JKlyBrWxvHkOMv9gS94coIoGQuXRpFFjJdGa",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "49615d902b47a997361d1ac055562f55",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1AXi9ATsyPN13HJd7RoYO87iIfSPfsLxUesZ3Uwq7Nd0",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1J5H5X7VG4GNZ8ZRDAa6sdOJmklzxQ005t6hazUcvvVp",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6acd8567aea4cbf3d07463e3c6c56565",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
