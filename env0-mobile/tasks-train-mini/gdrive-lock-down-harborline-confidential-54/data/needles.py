"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1S0XDO8dGLo4JTl3k77GMfPvhoPGwwJoHecvponDUQJi",
    "18Mp4AkvlTLupFM3p8OhAyaFdqRrYDzahjjAYPOez3Z3",
    "1E8uq6yi30yT0CcPSPaovXqxoJWrhRkqjBqTPo7NzIjz",
    "1T1sRShRUsvApgFWAaFXptYsrwHJ9rpS8d32XmzxDADA",
    "1z7IYmk4hXzpcoV0iaiXIv6xNGFeGRF5Si21XGQwatkH"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "d1b308582fb7de7c7ecdd0ea8739d7cd",
    "6bd3e684f2a3d8a83f4c22a76d0448a4",
    "22144ea733c1053d9450b5ecf5fe6634",
    "a3a6b591bc731a38dfa84f4c052fb6ae",
    "6bc28205f523ac5b5543e5a58e997665"
]

LEGIT_PERM_IDS = [
    "ac72f5013e235c164a4c7a728586f6c9"
]

NEEDLES = [
    {
        "id": "1S0XDO8dGLo4JTl3k77GMfPvhoPGwwJoHecvponDUQJi",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "d1b308582fb7de7c7ecdd0ea8739d7cd",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "18Mp4AkvlTLupFM3p8OhAyaFdqRrYDzahjjAYPOez3Z3",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "6bd3e684f2a3d8a83f4c22a76d0448a4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1E8uq6yi30yT0CcPSPaovXqxoJWrhRkqjBqTPo7NzIjz",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "22144ea733c1053d9450b5ecf5fe6634",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1T1sRShRUsvApgFWAaFXptYsrwHJ9rpS8d32XmzxDADA",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "a3a6b591bc731a38dfa84f4c052fb6ae",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1z7IYmk4hXzpcoV0iaiXIv6xNGFeGRF5Si21XGQwatkH",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "6bc28205f523ac5b5543e5a58e997665",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1prOviXp0amrT36JCSH4Kz3RWuBMXxXS6jYYktl6VRUr",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1kWQ7WEQKwsLcT2wC0TMA9uXMldrQLyFLN91UrA5jqr7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1Oa8DKcJ4QcJ8RK7qrcAhlpEg9gSCz87k7YS2YnI66BD",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1Rr5H2S6VqDWb9xk7JVLinu9bNqMwFHfDQ6drQPpgici",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ac72f5013e235c164a4c7a728586f6c9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1iThhuD0Isjg2YXDunM2pmEaIGPLZXkR5p7aQAmBRbt2",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
