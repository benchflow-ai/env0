"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1sbY1viSw6lTOXxYDdc3QclVMZWTdarAHUDjA44t1x53",
    "1pt0u7ZtmSmVlo3OO95PQlhr9gLx1woLWS3buaVVvcUK",
    "1FzS1oydTC2pAM7MBOVx3eKsJKXPHWSg5zpuS5UBHe9Y",
    "1bFa6ea8rOEzFFsFFyHyq2ZIxQxoFGilyDhDGyUK4s5V"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "4e7157da1b8540027d34fdd6a59af5bc",
    "bc8ef315ebaab3f0af47ad723eb26064",
    "e55d52d0064c5dc2b9d00af8d04a77f2",
    "eddfec3f09b87b63827331b367b21e91"
]

LEGIT_PERM_IDS = [
    "9d97e1cb42c615531b440e04880855eb",
    "4306340d4837ac27c01ce2be869499b7"
]

NEEDLES = [
    {
        "id": "1sbY1viSw6lTOXxYDdc3QclVMZWTdarAHUDjA44t1x53",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "4e7157da1b8540027d34fdd6a59af5bc",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1pt0u7ZtmSmVlo3OO95PQlhr9gLx1woLWS3buaVVvcUK",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "bc8ef315ebaab3f0af47ad723eb26064",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FzS1oydTC2pAM7MBOVx3eKsJKXPHWSg5zpuS5UBHe9Y",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "e55d52d0064c5dc2b9d00af8d04a77f2",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1bFa6ea8rOEzFFsFFyHyq2ZIxQxoFGilyDhDGyUK4s5V",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "eddfec3f09b87b63827331b367b21e91",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "142HaD3LASh17zSP19j9KmYPhmqXc2o4USjqrrx3mSkS",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1riGYfL38s3o0QaS5RvyDf7FkqybQNi9pquGfcGDmPF5",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "9d97e1cb42c615531b440e04880855eb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1CHl2Nm5QAhrDiv0yikmrNenrYqnnE8AZwSsrgHt6zNK",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1KOh4xjVwLzgGuvR7tTOSks2frYyJLQ7qkWjRrSZBPvP",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4306340d4837ac27c01ce2be869499b7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
