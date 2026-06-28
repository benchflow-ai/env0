"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1qJgyEI1KaX4uMMdQA0ATzuedvjyooiFIqTrXOx3fbWJ",
    "1dYkaXyZqpH58UGahUBKrqHoxpiiLR7IKH7ZByboZMrD",
    "1mJmW9nR8z8DUpjoVW8RfMkdUiSwR4xb7RNio7dLru83"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "3a17fb10c07d876fca39d4198a776d67",
    "af6037c4f3529fd90fbd17ab40d6d1a2",
    "c171bd0ba2795590c1d65e984e64d957"
]

LEGIT_PERM_IDS = [
    "0adf971aa2063473f18889fd1ac2a70a",
    "1dd937af31ddfe594763ec478c9a20d3"
]

NEEDLES = [
    {
        "id": "1qJgyEI1KaX4uMMdQA0ATzuedvjyooiFIqTrXOx3fbWJ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "3a17fb10c07d876fca39d4198a776d67",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1dYkaXyZqpH58UGahUBKrqHoxpiiLR7IKH7ZByboZMrD",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "af6037c4f3529fd90fbd17ab40d6d1a2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1mJmW9nR8z8DUpjoVW8RfMkdUiSwR4xb7RNio7dLru83",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "c171bd0ba2795590c1d65e984e64d957",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1XraJe8YqjMHNdJt9aq6h2fk8dxLQjRTG25MsX25kK1k",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1XhmJC8iKRwNaDBfp7UjuP0EXSyLuuOfWmOWTWyaZD60",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0adf971aa2063473f18889fd1ac2a70a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1jlHyZqPRqnMOLEh7AMy6f0MwOmgoxuQqo18NzKoFR5Q",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "1dd937af31ddfe594763ec478c9a20d3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1nxGK3iUeaLU3cuUq2OjjOsvutMme0FPbgo1v4mUJYK6",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1geLBLk5LZpXBlHdlLYxXuazT96lBhEATHmlTyjLefBb",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
