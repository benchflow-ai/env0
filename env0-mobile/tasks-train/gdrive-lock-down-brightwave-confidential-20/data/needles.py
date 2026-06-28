"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1XFfhXP4t9vmpwxtW0vzr0yKyLbe6JSRfxvCfkWHbS16",
    "110cwiMmgni3MNSAuxw1im4suirV70RoQc4HYFHMv20Q",
    "1uIBRU5xcaA8R3GTAiI7sJZbOgjOfit2SUBbOHma69J5",
    "1Up3ruDY8xX1GLcxdrZtqAmhIrkTnIMedKwwLGBKzjZl"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "19e6cab0e04def84167cc2c74393a695",
    "800fc7d3292e26f11faac27ad7ddf9af",
    "3e7a6a66c35f248f39711a46a2fa2354",
    "18d9823e534eed3242c744335b298043"
]

LEGIT_PERM_IDS = [
    "281a344c96abb23cddb2cda0271b5531",
    "339073aa5a4af2159f01d5862e2cf4f0"
]

NEEDLES = [
    {
        "id": "1XFfhXP4t9vmpwxtW0vzr0yKyLbe6JSRfxvCfkWHbS16",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "19e6cab0e04def84167cc2c74393a695",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "110cwiMmgni3MNSAuxw1im4suirV70RoQc4HYFHMv20Q",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "800fc7d3292e26f11faac27ad7ddf9af",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1uIBRU5xcaA8R3GTAiI7sJZbOgjOfit2SUBbOHma69J5",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "3e7a6a66c35f248f39711a46a2fa2354",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Up3ruDY8xX1GLcxdrZtqAmhIrkTnIMedKwwLGBKzjZl",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "18d9823e534eed3242c744335b298043",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1XVL8o9Q3NvhEUw8J2z9QLa2tpW9ve4SN69obX9PyiFj",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1rE3VYMAq2kEbS74lg7bMf9EjoWMcEyOb6VkpfpFP7Td",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "281a344c96abb23cddb2cda0271b5531",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1N1xxQURI5ABZ9c9EOXIGWbxQWFUxjxm7M20UbLgSDRS",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "339073aa5a4af2159f01d5862e2cf4f0",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1akPWECBrR55MiWt64SO3tzs7ZaNhzDPk81JcOti0QSW",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
