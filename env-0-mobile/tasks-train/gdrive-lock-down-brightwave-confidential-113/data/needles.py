"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1p9fEIdsUITi9b3f6OIRXtIKMSTnM08CXXljIAdg6lID",
    "1AS669lbruPeA1O8nO28M8VANIC0uV3LenwdHriwEPsk",
    "1geO8vXI0PLK0v6G5UNGvJGVn3v5EcQYLz8tYaVzQNUY"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "00abdfcab02c86e62087d2a97836b133",
    "49dcc9bfed3c589ef21617f7bc336e7d",
    "1e48a66ac01a4c1a4d59367a99bda362"
]

LEGIT_PERM_IDS = [
    "8c10734ae3299b54f68172d19fedf2a4",
    "b271495d0217c900e1348fb9b3bbcbc5"
]

NEEDLES = [
    {
        "id": "1p9fEIdsUITi9b3f6OIRXtIKMSTnM08CXXljIAdg6lID",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "00abdfcab02c86e62087d2a97836b133",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1AS669lbruPeA1O8nO28M8VANIC0uV3LenwdHriwEPsk",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "49dcc9bfed3c589ef21617f7bc336e7d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1geO8vXI0PLK0v6G5UNGvJGVn3v5EcQYLz8tYaVzQNUY",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "1e48a66ac01a4c1a4d59367a99bda362",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "135YtwOploeE7ykVvUFL6BdK6MoYYKwk21RVmpwI8HOF",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1hYYzcocJomtmS1aVzA5EjZM5Gatf7J3SLMbbOzLlmU4",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "8c10734ae3299b54f68172d19fedf2a4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1u3MuVjpE8LLeobilxAlL7a3QwL0J5XmEXXy9QLhhSQi",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1suBKBAjtPs1CcvdjkL5rDV4u4IgxOpMPt7CU9UYotod",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1YyslwTET1mKas9wneG3imkVTlodwn6zHKAnwq9LdTNk",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b271495d0217c900e1348fb9b3bbcbc5",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
