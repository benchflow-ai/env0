"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1Ho50i9gihIEix9iPWaJNHXpboamPB2zjVI3XqPzuEnz",
    "1SRRK0NeESNNGC1CBmSDzdXJ4tvviPW6W1X2vjHSWZfm",
    "1RuGcZLTXBs0R7ycKVB0QXwOzIGCoUP9ShWxwr6N1Q6O"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "831f261ddf8f80aae74494e9a8a62106",
    "c5e4069ce04b02da4deb93a5828490fb",
    "958c43ef74fa372da39268cefff96bfb"
]

LEGIT_PERM_IDS = [
    "16dc71df25e04925f4b02357aae78ba8",
    "97478705813b7bfc4d22e5a0d86a23b9"
]

NEEDLES = [
    {
        "id": "1Ho50i9gihIEix9iPWaJNHXpboamPB2zjVI3XqPzuEnz",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "831f261ddf8f80aae74494e9a8a62106",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1SRRK0NeESNNGC1CBmSDzdXJ4tvviPW6W1X2vjHSWZfm",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "c5e4069ce04b02da4deb93a5828490fb",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1RuGcZLTXBs0R7ycKVB0QXwOzIGCoUP9ShWxwr6N1Q6O",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "958c43ef74fa372da39268cefff96bfb",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1mcYPQ2HluOc7oNka9GPBI6aTCe0Kqf7kQRU004DpFQn",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "16dc71df25e04925f4b02357aae78ba8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Sh4GdYUZsEo6BgM6pfGPBHw4nBLhUtYjZ60KKH7WJ9N",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "12fEiStM5CwWOigHm1PU2a8puuWw0Zae9HoV8JlwsFTj",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "97478705813b7bfc4d22e5a0d86a23b9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1D6Ww25WSVj2OUhf5JQcZHrWbkcz3qq0LlDw6YuDUJGG",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "16EHLQaJAlYhKBPgErSTRMEN3R6DQQs5viWEbuKckBcF",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
