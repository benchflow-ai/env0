"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1OoYfTzTiF8GGzqEhjctj6Yq4W4jxkWpZDauwjCPyCaI",
    "1ugacpvJWZqUwYo3D8ck9zRx6iSspFBeNv9XGwpY6Gmc",
    "1dFuqYz2AOpprxLT4iMqfvlXAFRBIlTiKvH8jOh8oaR5"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "e62f6973fa04cc592c738112fd4e7ab8",
    "0bb94e9d0c39cb59d9312ab48ce527a2",
    "6a69a7407c5980934b456946bec80c3e"
]

LEGIT_PERM_IDS = [
    "d11fd9bd7001f79bb484c8ed923ed831",
    "a5e4d36d45e646e611d81da1bffedf62"
]

NEEDLES = [
    {
        "id": "1OoYfTzTiF8GGzqEhjctj6Yq4W4jxkWpZDauwjCPyCaI",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "e62f6973fa04cc592c738112fd4e7ab8",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1ugacpvJWZqUwYo3D8ck9zRx6iSspFBeNv9XGwpY6Gmc",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "0bb94e9d0c39cb59d9312ab48ce527a2",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1dFuqYz2AOpprxLT4iMqfvlXAFRBIlTiKvH8jOh8oaR5",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "6a69a7407c5980934b456946bec80c3e",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1qDySbRhgyDwPfL8v5sYiEH1URkvADqhVhSVI8tL5UvL",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "19F9KMAkZZ5ncWyAubHsMZwRaldHinZbsQ7BFMfQOa8z",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d11fd9bd7001f79bb484c8ed923ed831",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1OPK0D1j26Ns9Pbc5ubqrBqfH85gGzLEkUJy7wwZUkWh",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1NwEJEFaoVgdy6IPco22Au18tcrCQGCgFq7VxohqOyAC",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a5e4d36d45e646e611d81da1bffedf62",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1J09MlPH6LjvncQD52L61QqSkgmArobhyXj0N6eKtDtA",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
