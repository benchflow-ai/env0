"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "14mW64dTJbgqbtAfERrSyRfSzDPUH9DlSjSuj65sMq4e",
    "1puycfexVaKUk0pWnHR6eHB2dJisxZGzqgLzZHcjsxfJ",
    "1IHmGUTm0BLlmyk7Y2pqVkdONGtHUpYDdHEQOnkcbZTg"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "46ad6dabbe4ec94a0122c123c704fff1",
    "4bde6c3c5d2824e62274603509656250",
    "542ea5fd900709fe87833f8f44dc0da7"
]

LEGIT_PERM_IDS = [
    "85d6fb27b41e851aacd1489658ec8ba7",
    "ab28b771adf3535deaa8fa06bd52595c",
    "7e41440275f68ad6f89fd903e21d66cf"
]

NEEDLES = [
    {
        "id": "14mW64dTJbgqbtAfERrSyRfSzDPUH9DlSjSuj65sMq4e",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "46ad6dabbe4ec94a0122c123c704fff1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1puycfexVaKUk0pWnHR6eHB2dJisxZGzqgLzZHcjsxfJ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "4bde6c3c5d2824e62274603509656250",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1IHmGUTm0BLlmyk7Y2pqVkdONGtHUpYDdHEQOnkcbZTg",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "542ea5fd900709fe87833f8f44dc0da7",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1tp8rbrMB5c6bzzD3VL0Tsa1Pdofe4c2uUYuHh4XohAx",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "85d6fb27b41e851aacd1489658ec8ba7",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1v5ZC6VdMqlnRlJUPkw95yEfdLwVYrIzOpI5ZHOYy5OI",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ab28b771adf3535deaa8fa06bd52595c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "10qDLKKtA8TJTSoqbiZ3VicMAhrlzZtNIfK2hv6Gds8j",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1AVGeY8tJASOc1dVkylWoBFBcCSeWotFdMVnzQN0uGiP",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7e41440275f68ad6f89fd903e21d66cf",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
