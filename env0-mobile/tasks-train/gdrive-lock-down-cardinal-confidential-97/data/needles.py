"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "10pfqylBh3xAbXyEqrVzpaHbftSvN8gkF78XG2o0TsCi",
    "1sXX8ucpyvYODSX9J8cI5zKQ8QWa45tHluOR1XgNTzx1",
    "1gimkTjNDEw21qsAo6tyZmlvBnRlBjBf4vrUq7GWIYz7",
    "12B3t9tzFSJ0pn7HI2cDp35VbXHvc4wYWb2CDiJUir0a"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "8ff5b51a8e5b13f2f7758dc71ab101ae",
    "3dc2a51e74c9ba6ab6a2735b91ec8fec",
    "9aac3d9d6ad58ce60516c57e8821fe09",
    "02ecf00083eaa4a913a793f618d7a9da"
]

LEGIT_PERM_IDS = [
    "f267a92a11e1c59902f3f36966ecbd1d",
    "a9222f7d3aee3ee5eef4f24a2feffbaa"
]

NEEDLES = [
    {
        "id": "10pfqylBh3xAbXyEqrVzpaHbftSvN8gkF78XG2o0TsCi",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "8ff5b51a8e5b13f2f7758dc71ab101ae",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1sXX8ucpyvYODSX9J8cI5zKQ8QWa45tHluOR1XgNTzx1",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3dc2a51e74c9ba6ab6a2735b91ec8fec",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gimkTjNDEw21qsAo6tyZmlvBnRlBjBf4vrUq7GWIYz7",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "9aac3d9d6ad58ce60516c57e8821fe09",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12B3t9tzFSJ0pn7HI2cDp35VbXHvc4wYWb2CDiJUir0a",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "02ecf00083eaa4a913a793f618d7a9da",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "19TPW3qvsVfmOXCnqljJfgjfH6HKXMJGwqt9MBGnAkmM",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f267a92a11e1c59902f3f36966ecbd1d",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1xkA0HcI3KYfvRguCOWa0vyPBKOeTPolDVUJmHsMeWSt",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "11gaorXXlHl9QLw4TlavOBvFQMlPphg6aVlZ9KdDamEd",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1TZyyDhTg90Vxwr96bl6eYaUWVGEwLTfR5uJMMSbUvoz",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a9222f7d3aee3ee5eef4f24a2feffbaa",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
