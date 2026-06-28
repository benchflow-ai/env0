"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1O57sCSsBJ3H7FQTi8tWfZqOjii0zSesbGtTsAl0h1rs",
    "1vZ09ecdL1PHkwhDIB4HBnCKNd7fmuZdC6PWMTlKJAXs",
    "1zKwcnG1a7M95QT5rip8Chk7JEudWsD7p3B0konB8S9r"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "ab377268626e61c53e5eaeaa8c63afcb",
    "8caa6ae8d80cc463bad8fc3eb8f09743",
    "823447a0850f79fbb795ccbb19952256"
]

LEGIT_PERM_IDS = [
    "b4e67894cb75a8962b3421812996867b",
    "6c1af146345369e736534b2439250d8c"
]

NEEDLES = [
    {
        "id": "1O57sCSsBJ3H7FQTi8tWfZqOjii0zSesbGtTsAl0h1rs",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ab377268626e61c53e5eaeaa8c63afcb",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1vZ09ecdL1PHkwhDIB4HBnCKNd7fmuZdC6PWMTlKJAXs",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "8caa6ae8d80cc463bad8fc3eb8f09743",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1zKwcnG1a7M95QT5rip8Chk7JEudWsD7p3B0konB8S9r",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "823447a0850f79fbb795ccbb19952256",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1z5CvC3zTYMmGywI7I8U2EB3qlrAQtvRRTOgBGhMez74",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1I4IE313B9BxXwsd7X2WY2gllr57NhEbbaDOMpJ16Ajo",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "b4e67894cb75a8962b3421812996867b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1IuerAJhiMPZDu0XHX4zbojEft8p8sJJKD7Q4ZHEsE6E",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1TfUGs14dCGC88JlORlx36Q5tebkLiFw4v0joDv2mKCZ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1tcjEQWQ2xyTNqhcrLA85WVli4tgTlkjVJFsQgd202rQ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6c1af146345369e736534b2439250d8c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1sNyHkcwtS6SdnYRIoCTvYEfhuknv0gXQAl17jou2Szu",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
