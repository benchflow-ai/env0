"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1R0GzmwDhK2wTTrn5dd9r1eHNJHVQBLmGtQ9CZKup4Pp",
    "1Vc9LJQdMCYW1tQVeY0iVk9tRpgjI71N5jSnhLbR7uQZ",
    "1upZUWtLQIIc2nEY4kCys6jXyV6nEdIVeflPSRFUUH4s"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "255bc4b7af63eadef3a836942c5cdb7c",
    "df62cea90765a5ceebe26faee12865cd",
    "7457d6ac3d750b96eb9b8cc4e36bf0c2"
]

LEGIT_PERM_IDS = [
    "fac3a995a6a9a951cd928096ac9e65a4",
    "43dc6051dfae2fe5b2511af602b33fc0",
    "86468f844861641c744769ec1852ffd9"
]

NEEDLES = [
    {
        "id": "1R0GzmwDhK2wTTrn5dd9r1eHNJHVQBLmGtQ9CZKup4Pp",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "255bc4b7af63eadef3a836942c5cdb7c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Vc9LJQdMCYW1tQVeY0iVk9tRpgjI71N5jSnhLbR7uQZ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "df62cea90765a5ceebe26faee12865cd",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1upZUWtLQIIc2nEY4kCys6jXyV6nEdIVeflPSRFUUH4s",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7457d6ac3d750b96eb9b8cc4e36bf0c2",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1jigWSXjsYh6o6WDRcmWcQOs6UfG53cwTLNdF9m8Uj2T",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fac3a995a6a9a951cd928096ac9e65a4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "15ljJ4X8jAyvdzp8uEdlNuyambKk1FChK6AWAnP1sdx0",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1yvlLya6932DxzKIZjeVGLzWcH9fZbWn7eik4t1vUTre",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1mWo2GCs9SPYDpcfo54NebPQCjqoCRlYuBQMZPivsvuf",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1Nph4CBUlH5iaLxrOXb8dpnzP0JDG3eF4SZ8u4IG1XUh",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "43dc6051dfae2fe5b2511af602b33fc0",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "18vYGGFxTtYUrO2iIPQBRejrB6dX6BUJ5aNhrnC2XNuD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "86468f844861641c744769ec1852ffd9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
