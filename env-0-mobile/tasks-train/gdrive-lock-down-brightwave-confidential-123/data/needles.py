"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1BgcW5PNpigvfpjAg2IkdlvNpYBLpwes289cX8FfDrZs",
    "13omwo286JuprwlngQQeThEDfaYVlmUMCkT9MALCjciB",
    "11k8Yh0Il2N39QDs3zEm8PgH9Al5hJUiwubvTlHQl6CD"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "cc46cfa70b0112ad3066d9f10fa62e5d",
    "28861e5fada9dfa1832b60458bea68af",
    "3fbfb2272bd017361064794458c65a94"
]

LEGIT_PERM_IDS = [
    "a7a6ea08d07e27e9ab8a62f11e69f60a",
    "608544620bf91efeba507d3c82f48d05"
]

NEEDLES = [
    {
        "id": "1BgcW5PNpigvfpjAg2IkdlvNpYBLpwes289cX8FfDrZs",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "cc46cfa70b0112ad3066d9f10fa62e5d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13omwo286JuprwlngQQeThEDfaYVlmUMCkT9MALCjciB",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "28861e5fada9dfa1832b60458bea68af",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "11k8Yh0Il2N39QDs3zEm8PgH9Al5hJUiwubvTlHQl6CD",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "3fbfb2272bd017361064794458c65a94",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1pt2Wok8Xyp674CUXUbHiNM8yidHIMeWWYHxiZDthYfm",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1tLGm5vvgYYcjPEEuHng4Z8vn4iSiuhzwYYh0Bm6zJV5",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1xnbogYQCZyHSajYLk9kRnZpjYLRfzbH28Ku6YQK2Pl5",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a7a6ea08d07e27e9ab8a62f11e69f60a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1rDfzFkbHBkBzWgX9jtbgUbU9rWzCmfq9TbtflulRFeb",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "608544620bf91efeba507d3c82f48d05",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1K2HPFLnWFZMERnzCWlxJOMGh6ruCLBw1Td4BYBwByTV",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
