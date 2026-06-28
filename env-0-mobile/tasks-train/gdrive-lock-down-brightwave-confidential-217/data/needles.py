"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1FE0V7Xj2LU8lB94nioZFY71RwE3B3IQ0DsmmDyVtoEb",
    "1cWA5ZBbBMlhAtpskjNkoFbEo31weJJ9D1a3AblJIEGS",
    "1a17j5WVqGJvCeOYVn99wVYqzF5sgIF41vo0kzVKn5rn"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "1ae7cf88a6e7c3530843076e1b60e1a6",
    "7f29a79b7fba6ef2357f5064d9ce7cf1",
    "edc540cc97103162ec577e7ea744629c"
]

LEGIT_PERM_IDS = [
    "a6be4302be40298ac9dcb6aee8aba86e",
    "799891016950d8866c284f8c3bc9411e",
    "7878627b21cad16532ba59e003b4a9d9"
]

NEEDLES = [
    {
        "id": "1FE0V7Xj2LU8lB94nioZFY71RwE3B3IQ0DsmmDyVtoEb",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "1ae7cf88a6e7c3530843076e1b60e1a6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cWA5ZBbBMlhAtpskjNkoFbEo31weJJ9D1a3AblJIEGS",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7f29a79b7fba6ef2357f5064d9ce7cf1",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1a17j5WVqGJvCeOYVn99wVYqzF5sgIF41vo0kzVKn5rn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "edc540cc97103162ec577e7ea744629c",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1qo1K47EppZhBwLLfyQbhXdSWjBS1CT2AVwNDTQBxGaV",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1NLRYkYPyf0Gld0h7SNdZ9OGmt2UZ2f5TJdI3HNTLfwQ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a6be4302be40298ac9dcb6aee8aba86e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1IY4zuNttRgOs21fywWsqzxBezQNMp1TImolVKxnin1D",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "799891016950d8866c284f8c3bc9411e",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1eDiY1hadikfta4Y9A9TeALdCtXX7EoU8OStRFaB5omE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1nNZgKpXeP6fR4VFxaulL8x7evrqdLqbfKnAlMCx7SeL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7878627b21cad16532ba59e003b4a9d9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "12JF2TyurqMvG1yadz2uxSf9TgX7HmMEIhycF7ezYFtK",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
