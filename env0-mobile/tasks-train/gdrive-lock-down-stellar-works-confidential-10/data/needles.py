"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1qsZgmSQjdJAVLeX7W8AzMomF7qtTOhLDVZIkPvshfix",
    "1fKxjalnRi0TCXfJDq1FGw2CIlXEyEpUjBdlMHsVUQsZ",
    "1MEJ92r5ARefJjJ33m48XALNZKYLAZsNhKwL0bCLauzi"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "6c3573a28d37620fd2cc1e68a5e6e652",
    "ab498cd521309a12093bb04904a1f365",
    "d8ef719caaec576dde0eb01efd6b5c6b"
]

LEGIT_PERM_IDS = [
    "bb5f3319c8d2a68a5d487fd6c10939e0",
    "c590b026b6b377bb8d9ebcf7eb3f4019"
]

NEEDLES = [
    {
        "id": "1qsZgmSQjdJAVLeX7W8AzMomF7qtTOhLDVZIkPvshfix",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "6c3573a28d37620fd2cc1e68a5e6e652",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1fKxjalnRi0TCXfJDq1FGw2CIlXEyEpUjBdlMHsVUQsZ",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "ab498cd521309a12093bb04904a1f365",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1MEJ92r5ARefJjJ33m48XALNZKYLAZsNhKwL0bCLauzi",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "d8ef719caaec576dde0eb01efd6b5c6b",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1d9YS23JIZNTa5yoBJKP8lQ1On16hOQyOaNpVdDdXuRM",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bb5f3319c8d2a68a5d487fd6c10939e0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1gTJGmWcHSUrqeVpqaIGXzxl5R0T46ait8QzVnX9wkSy",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c590b026b6b377bb8d9ebcf7eb3f4019",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "18ujjclIf1aq6KzSpIhpbW7OHgjBlfhgdKZJ96dJNUaN",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1Kdwr3Hd3uyCbyc0iIvatlA9K6xBAlbcokJ4sa9fm9aD",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
