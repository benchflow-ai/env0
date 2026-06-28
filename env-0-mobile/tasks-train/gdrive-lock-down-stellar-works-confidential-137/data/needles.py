"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1mgcgOdVmuE73AJbvRFjRX9FgsRQugJnzt0QPGlKWPLX",
    "1aRVAi3mET279pbRzkGqiGm9VwXuMLbNG2PmAA9kMECs",
    "1vEIstSWhcp8QVtQyNGSy9BNys47JxYKydcrtKgakEIU",
    "1xufWIWLDvB9A8dH8pVwsCFY2KPz4fnKTUXUhfki93Zd"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "b4da125fc54b838cd2b511b20a451f09",
    "6438a747497be488b030a00bbc9593f4",
    "70f2121c60451c44af130397a90c4fd8",
    "793738b62be13cab02f729cd265c0c8f"
]

LEGIT_PERM_IDS = [
    "26697b29dcfd9b590dd45556726fd014",
    "a043fd71b8a4767cfc07351ac7556493"
]

NEEDLES = [
    {
        "id": "1mgcgOdVmuE73AJbvRFjRX9FgsRQugJnzt0QPGlKWPLX",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "b4da125fc54b838cd2b511b20a451f09",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1aRVAi3mET279pbRzkGqiGm9VwXuMLbNG2PmAA9kMECs",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6438a747497be488b030a00bbc9593f4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vEIstSWhcp8QVtQyNGSy9BNys47JxYKydcrtKgakEIU",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "70f2121c60451c44af130397a90c4fd8",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1xufWIWLDvB9A8dH8pVwsCFY2KPz4fnKTUXUhfki93Zd",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "793738b62be13cab02f729cd265c0c8f",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1UXN0V0B75pzubFQBmcs0W8qzEH0wjDN1QOhQnlf5tCq",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1x2wPffWlWeWKxPRhleimeXJuwCJlv8AudKj272qXKwg",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "26697b29dcfd9b590dd45556726fd014",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1k0lY5ei4URRGXAw5nMKeXnnm1ecJKbNpXhK0JPXxW3p",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a043fd71b8a4767cfc07351ac7556493",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1MnlAXY8j9WXUDUVsCD94hadiwJJDwNktnphvdvqTwn9",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1tgv8fJxHZfWihBSjuFaBLBTAZ24SbqoXLr74ZCnIMCC",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1dQ7ri9uBe0YDV1BqVsPD3ZhZa5421GedKaR5tL0anU2",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
