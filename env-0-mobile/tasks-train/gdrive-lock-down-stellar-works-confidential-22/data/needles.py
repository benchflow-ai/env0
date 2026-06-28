"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1pai7CBlah7J43kloPPkZDhwNgmGgQR8oBN4N4IopC4R",
    "1v3ObSduDR0T3FgOqZBK5CCXkhyf6oirEOcP97wugVIo",
    "1Eyvm8wFqt0o9inNN106hyG1ndVslLJoEb0gWX9RPvwr"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "b93499873b58bbabb5cdc7274775c82b",
    "de65a2e475f757865965764a14d4c321",
    "3e5afd46f22581768895cfbe91d3e784"
]

LEGIT_PERM_IDS = [
    "e85a4277547e307b0131a92ce912aeeb",
    "4c1dee695301d36216f4f89b2efb78af"
]

NEEDLES = [
    {
        "id": "1pai7CBlah7J43kloPPkZDhwNgmGgQR8oBN4N4IopC4R",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b93499873b58bbabb5cdc7274775c82b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1v3ObSduDR0T3FgOqZBK5CCXkhyf6oirEOcP97wugVIo",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "de65a2e475f757865965764a14d4c321",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1Eyvm8wFqt0o9inNN106hyG1ndVslLJoEb0gWX9RPvwr",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3e5afd46f22581768895cfbe91d3e784",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Z39MqnhZuNf6dLplZg8FUJ71BdK5N0hKwCjyqOPewO3",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1rwuWPrJrnbFlLSpxadvRbpyvCi4rGWSFSMsF2GUdkw5",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1J2jqi1J9u2Nn0DGx5PCWs4015UAXcgtLuQajBh9mhFg",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e85a4277547e307b0131a92ce912aeeb",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1roLfLP3HXMze5iGlZdfadn31RVIQj5FmQ4nHDhulK0t",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "4c1dee695301d36216f4f89b2efb78af",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
