"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1qWcPjmvGtnzzauBfvPi7x4z2Vyyo5AH99fpeI3B7cop",
    "1bn9js2kmVtWoIBnBgOoVjYdhS14UlXHWa0S4xg2eVzX",
    "1E0IzRpWFm49qA5UUTObgcfauw4MEYMs5O5ejlmTOquR"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "ed2812137936952fab1568d181538494",
    "a47464a2b82089492b77d358c9234dea",
    "8020b6e40ad094b3fea34b83cd558ac7"
]

LEGIT_PERM_IDS = [
    "4696d0a2627bdaab2f4ecc795fb21160",
    "4c26b828f8dd93a8de265e4bc184a72a",
    "58b79752b05c2926d0106cbe8ccd4c7a"
]

NEEDLES = [
    {
        "id": "1qWcPjmvGtnzzauBfvPi7x4z2Vyyo5AH99fpeI3B7cop",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ed2812137936952fab1568d181538494",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bn9js2kmVtWoIBnBgOoVjYdhS14UlXHWa0S4xg2eVzX",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a47464a2b82089492b77d358c9234dea",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1E0IzRpWFm49qA5UUTObgcfauw4MEYMs5O5ejlmTOquR",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "8020b6e40ad094b3fea34b83cd558ac7",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YLAHcpibOMe2xhlkllqleVI3mBHMIJ0GPdCyxU6xAwN",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "4696d0a2627bdaab2f4ecc795fb21160",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1Mo4otPGw8SZfmac5fLGqctCPw22IWWzSHGU6AjmJF39",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1I7W33MMhq2Bbk9X7f5ErB5Pt5OvwD2bn1FGdKRM8lI3",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1zb0kNdmHvnHcTrMGXsz3Nfdq9U6dJ42xICZuRXJr4OS",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "4c26b828f8dd93a8de265e4bc184a72a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Wh0NFYaDIZnN8byk0XBEpUx9C1ERR05vsLwAcevY3Qc",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "58b79752b05c2926d0106cbe8ccd4c7a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "13COIZgl4E77e0bz0TQNKETTLnEGAiD8hI0vvn0TBSiH",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
