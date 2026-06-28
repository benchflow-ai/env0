"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1Id57RZii7YjbH67HcxCX66txCFnq5lK6ZyfU2ztN3Mi",
    "14II5AaDsEvUg7pE6Ppzc8YxSlDsJZ7OJjRqoMtlnicn",
    "1nsE3GIWAdL67W2WP7vD1GhkWKYqTmontnmsMK5aMD13"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "591b6559e028a1b8eef037444e79a6a9",
    "3cefd65b8f2ac0d3a7a428d46e1b5c0d",
    "0f2bbee70f149510647c5aa4f3710ee8"
]

LEGIT_PERM_IDS = [
    "d03279cef179c127805ef1f0115373d3",
    "2f8a6a142b7ffcea5dc7ac923397981a"
]

NEEDLES = [
    {
        "id": "1Id57RZii7YjbH67HcxCX66txCFnq5lK6ZyfU2ztN3Mi",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "591b6559e028a1b8eef037444e79a6a9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "14II5AaDsEvUg7pE6Ppzc8YxSlDsJZ7OJjRqoMtlnicn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3cefd65b8f2ac0d3a7a428d46e1b5c0d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1nsE3GIWAdL67W2WP7vD1GhkWKYqTmontnmsMK5aMD13",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "0f2bbee70f149510647c5aa4f3710ee8",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1AnSoxkSSV8iW6ZTP6gjadTxx9NCFKmzlrp90Sm4Kc8k",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1JxqtKFLHQXTo846FfokHTAsvx3izy7dcCAW94lJnzZT",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1zDou5eGnb7kwvQJmOuV6JubWLFshSS7tYHcRygFCu2n",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d03279cef179c127805ef1f0115373d3",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1Ydd3Syd3RCTtBXWzZxfDiYYPE2ZmnwPur5ynJp0cc94",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "2f8a6a142b7ffcea5dc7ac923397981a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
