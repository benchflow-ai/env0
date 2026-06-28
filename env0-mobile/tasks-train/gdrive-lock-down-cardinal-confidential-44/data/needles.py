"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1GyDVoprXqHWaUrET44UiVQxkhgpnwutlNl4xHcR4nEB",
    "1bzaGS0bslpvRL9Q5IjGl67IUl9dzssqqYQx27NU0qfj",
    "1UBXqthwZ0oJ9A8dVd1aXAERcCG8SEvZIMxHXSyRzZNE",
    "1kfog5DaYc7vFJzJtomSMkaUuLX71aDPlNXBTLC4c5hP"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "01314b6014d1e8b0d8f51826c465ec80",
    "b379fbaf2364431e893296c762c02a75",
    "e8748469783201d0c00bc879a50c2c2e",
    "f8a693ec79d4e1b51472debe2384f37f"
]

LEGIT_PERM_IDS = [
    "f84af914c18d5cc3e2c1f2549f88f40b",
    "4d045dd27752531a5d85e510ea48b8ab"
]

NEEDLES = [
    {
        "id": "1GyDVoprXqHWaUrET44UiVQxkhgpnwutlNl4xHcR4nEB",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "01314b6014d1e8b0d8f51826c465ec80",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bzaGS0bslpvRL9Q5IjGl67IUl9dzssqqYQx27NU0qfj",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "b379fbaf2364431e893296c762c02a75",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1UBXqthwZ0oJ9A8dVd1aXAERcCG8SEvZIMxHXSyRzZNE",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e8748469783201d0c00bc879a50c2c2e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1kfog5DaYc7vFJzJtomSMkaUuLX71aDPlNXBTLC4c5hP",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f8a693ec79d4e1b51472debe2384f37f",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1KGo8Z9w8QmUaHGZpGzvfI0iXapltuAlfnvlsXlt9WKX",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1LVcFEfHSYnLdJDmJf1EvG5z2rBAGZJY6SSpYdDXeOjd",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1iSCKcRmMnQAm8UJV8pI6lsdnZt4R2YGk3JUUBHk1xzq",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f84af914c18d5cc3e2c1f2549f88f40b",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1nDgaiWzMa8TLojAgMBlzpN23cWENK7PuOgUhrIqS2jW",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1fvjWGGhjt0sGf5aFV5ZygvtM7MLlgpEV55GKpn1rQCN",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4d045dd27752531a5d85e510ea48b8ab",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1OBoIqAfNBSQz9tHO5acY1KeComd7dUcXOCxZd5uvKG2",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
