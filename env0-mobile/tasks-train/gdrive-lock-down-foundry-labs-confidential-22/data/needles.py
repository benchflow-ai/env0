"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "14cuXmZ9gzFpaLu0E3fKCbKaMcOGtLWiHLTeUM1mYHqe",
    "15d2DI6PTmEsavmgQ0zOoVH4UvLKjEsV0ghDjj8NpSTX",
    "1zvV9cjpCirf5UW5kZaElkf8xNT1mG56DxpbDQNIGr6M"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "721332ea0ec29bef2c7a28fbeddd84af",
    "f703089716cae678367380a21a8b74dc",
    "778f9beab0a12ed2bcfe2ac3fb919737"
]

LEGIT_PERM_IDS = [
    "7edd14d524f33c63014dc05292fdb5fe",
    "6fbcff2258af6b508f8254fb499730e5",
    "915ea5d2f5313f7266269d760faf3ac2"
]

NEEDLES = [
    {
        "id": "14cuXmZ9gzFpaLu0E3fKCbKaMcOGtLWiHLTeUM1mYHqe",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "721332ea0ec29bef2c7a28fbeddd84af",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "15d2DI6PTmEsavmgQ0zOoVH4UvLKjEsV0ghDjj8NpSTX",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "f703089716cae678367380a21a8b74dc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1zvV9cjpCirf5UW5kZaElkf8xNT1mG56DxpbDQNIGr6M",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "778f9beab0a12ed2bcfe2ac3fb919737",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1IT5LbZlGPZ0G2IvdY1bqskiDRyaXX67B58LCLZfWtTN",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7edd14d524f33c63014dc05292fdb5fe",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1iG3ozxqrLAZbF29k7c8gRCpFooztgdyFWN4OW7u3AXf",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1SGPtQiBKtIPHyCpywFGrmxuHimy4a0pGThxw6oUYTKX",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1jEnPHvbMMZLWU5os2VzcqxcvbuIFL2iLz4H4Beqy2kx",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1DWZ0OjGxEr1u1IwYxdwRXGyVkvS4W061f4gW8GXKOgm",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "6fbcff2258af6b508f8254fb499730e5",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1YMncQM6NM3gf5J00bSdOnsL70fM3a42a31SKrNskuFf",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "915ea5d2f5313f7266269d760faf3ac2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
