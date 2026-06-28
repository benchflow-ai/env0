"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1JawqVz3Xm9jjZR71rFzH8uXSnmOURHorrGfzjlCUGzn",
    "1vDEhsjh8vPj4ytu8m118CVnUd3bfqGvbMlU876xOCOp",
    "1fD9WcewZzHFkntSnmoXEqXtim3sqAKWayW4pMa69qoh"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "7d8ba8181ecf4dac21b4863269711b48",
    "b5268f42050a5565fe6fb339bc816516",
    "2d521d5386e25d269b2db1bd6191bcf1"
]

LEGIT_PERM_IDS = [
    "a86a85f49d232241b867dc0fcf4d7e58",
    "e088eb833e06bad0a9d5cfcd97f8561c",
    "f20d1ef74842f4f4361423c5a109e67b"
]

NEEDLES = [
    {
        "id": "1JawqVz3Xm9jjZR71rFzH8uXSnmOURHorrGfzjlCUGzn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "7d8ba8181ecf4dac21b4863269711b48",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1vDEhsjh8vPj4ytu8m118CVnUd3bfqGvbMlU876xOCOp",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b5268f42050a5565fe6fb339bc816516",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1fD9WcewZzHFkntSnmoXEqXtim3sqAKWayW4pMa69qoh",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "2d521d5386e25d269b2db1bd6191bcf1",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "183NOMMn0hrE2qnddiM2JDs89y879E598WHH3oV9zoLL",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a86a85f49d232241b867dc0fcf4d7e58",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1U2e6yLBdnD5Pgj2fiDCUNPkNdedSqR2buGgjxe3lo2d",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "e088eb833e06bad0a9d5cfcd97f8561c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "15PbthoHzEVevDlPAhFg9FZHrpmyXj1ds30nODyAptai",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1FXYwAonDJtWo5MKnsRSYHSQPrqACSGrbXzoscIT7eWt",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1jn6QWW3zpZjg5vj45uZIBaVbkPWnD9T8gb4cYL2BOXb",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f20d1ef74842f4f4361423c5a109e67b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1itf5uY3QbqSmCQxYd8ueFoGq0KtMHnQjl001eql2oTt",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
