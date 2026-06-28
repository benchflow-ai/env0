"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1rpIo9M0CEYQ9ya6H6MkeRhp3heBue6bbuKQuuGxslhR",
    "1dljzEuClkkdZwcXg9lubHJQdTgmFeRbNA2WT6tsAEvk",
    "1XptlKKbqChAjIqdwwaXEb2lue1x9k43ZXl8sSxs1jzX"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "8c9995c1ffc9b48d7388eadd7bb4f29a",
    "ef5786af117f0a11e4af11b41ad70b5b",
    "7c6eeea7fc199381c4121a02c2ba6392"
]

LEGIT_PERM_IDS = [
    "ac3b15aa4790d0c7a31d86b43785c3d4",
    "cdcce32264cb42781a9726d7aa177810"
]

NEEDLES = [
    {
        "id": "1rpIo9M0CEYQ9ya6H6MkeRhp3heBue6bbuKQuuGxslhR",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "8c9995c1ffc9b48d7388eadd7bb4f29a",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1dljzEuClkkdZwcXg9lubHJQdTgmFeRbNA2WT6tsAEvk",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "ef5786af117f0a11e4af11b41ad70b5b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1XptlKKbqChAjIqdwwaXEb2lue1x9k43ZXl8sSxs1jzX",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "7c6eeea7fc199381c4121a02c2ba6392",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "19qYXdxdBLZuRO8hR93IGkRKgl0B2ADelpQmKg6hoqRv",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1FJlP22kYMPrUCTNqeTBFnlgHfu63hdAAvBY1Zqdm9DF",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ac3b15aa4790d0c7a31d86b43785c3d4",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1Hdk80yugCcYmWmDj3SXdhYTReM0Xj5OkwuUArAadtmD",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "cdcce32264cb42781a9726d7aa177810",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1vQzlcMawCtcUj16CkuOSxPbDHUYwwSlRIPPdiX9gY5U",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1uEjieSZX8UoXC0E1FUcVu3rm1UzVuEikdNZZO13Pkmh",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
