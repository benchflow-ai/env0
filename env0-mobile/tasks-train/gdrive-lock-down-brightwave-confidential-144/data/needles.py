"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1H8A0rd0NMmoAGmMki25tBErR6a3JOKK38SmnD8qOaHk",
    "1gm3FbkWPpqbaJxZWZbfGZdFQyJjJbQJg7s0QBQIr8jC",
    "1L9bUZ4qGVmhu1NplM1qJMbEHshjrLSIw7aFu1TIuKX9"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "a1087a3b53120451db610f53ee4c5e32",
    "d9872b370732203a5c9d7b5eb16cea28",
    "a73249f9ca11cbe8e6cd6d485627176f"
]

LEGIT_PERM_IDS = [
    "ff2538a0e5806c76b259f2c49d2f6d6a",
    "1c43bad8f0e767127c04f1bb7080cf55",
    "cc8617389f09cee8c95bcc1a145662a3"
]

NEEDLES = [
    {
        "id": "1H8A0rd0NMmoAGmMki25tBErR6a3JOKK38SmnD8qOaHk",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a1087a3b53120451db610f53ee4c5e32",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1gm3FbkWPpqbaJxZWZbfGZdFQyJjJbQJg7s0QBQIr8jC",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "d9872b370732203a5c9d7b5eb16cea28",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1L9bUZ4qGVmhu1NplM1qJMbEHshjrLSIw7aFu1TIuKX9",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "a73249f9ca11cbe8e6cd6d485627176f",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1CdxbS2R2kbK4bHasmI4XLacAwo0osCiPR567qbgK81R",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1UdNQzzen998j97ODmobYs3RZrViQwxS2RzPOjPcCct1",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ff2538a0e5806c76b259f2c49d2f6d6a",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1IQrdwuG1jxMY410Ek0kkyB7G2KDPlTpvF103w87WpPm",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "1c43bad8f0e767127c04f1bb7080cf55",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1bzWKcWuOQf7qYxfKZRU9vkoPhNXBmPXy1pfaOC5LviT",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "cc8617389f09cee8c95bcc1a145662a3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1823aIr9n9wvxkSRShr6VoUfvNQ3P2LtQgAG75iNtRke",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
