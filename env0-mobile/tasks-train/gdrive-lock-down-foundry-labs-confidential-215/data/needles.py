"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1uFTHjEcyye9C3QRmNO4gyuyPVWSTpptzuWcHBW1KWVv",
    "1pzU9kTEYWgMBI8KwiuUEz9YHEXbpcbfWBr3Y7YcVQTe",
    "1c3h7TaYzfcZTlIp9Os2JQK3RaJniThBZ6aW5v1avVip"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "d1955cf227bb74a20f71441daa57546c",
    "8f4e432e15bd3094eca693140475b0af",
    "a9d7f3115199494d6d837b9d2e405007"
]

LEGIT_PERM_IDS = [
    "edf88912a034c9a0b7723a6eba0a897b",
    "dd6274f0c98250e50f5bedb7efd94abc",
    "0506e89b2d76a3312b4c0e8c9dcfc77d"
]

NEEDLES = [
    {
        "id": "1uFTHjEcyye9C3QRmNO4gyuyPVWSTpptzuWcHBW1KWVv",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "d1955cf227bb74a20f71441daa57546c",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1pzU9kTEYWgMBI8KwiuUEz9YHEXbpcbfWBr3Y7YcVQTe",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "8f4e432e15bd3094eca693140475b0af",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1c3h7TaYzfcZTlIp9Os2JQK3RaJniThBZ6aW5v1avVip",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "a9d7f3115199494d6d837b9d2e405007",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ZX5XhORU4npMUlJymDLAvhJwM1D2AJY96ynGeE0dY0W",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1yIztUHa1I7uCwvLZ9PR5nieVllX9eD05VszFXUXJggd",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1ep8Yao72k5XX8tmGC3PhePy0JGrOJ8jWgDLKgS9HJ9J",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "edf88912a034c9a0b7723a6eba0a897b",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1c9TMI6tTPVE7Jx5B2v06qVln8cwqxE16S1FA6EWtKJV",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "dd6274f0c98250e50f5bedb7efd94abc",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1z4kxoEYEhx0a5MRbyqDFXn99tfUAvxswUKxojrDO5QU",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1GOqa5DHjJqZjWQajU9yA5yok4h3BTSEAyPnEtN4NJjM",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0506e89b2d76a3312b4c0e8c9dcfc77d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
