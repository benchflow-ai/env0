"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1RhKk6MDodHNxBbUg86QJyin3yrEZMS6SSqZeflcJWwP",
    "1E2C7wU2lrCXrMw77faIZZ7h6ACRq3SIWlPxqcfb5PVp",
    "1E0c4CAdwmAQBHzsuZSZK0ma4YO4ePMKMEBHfSdcUS02",
    "1WdQ3CYtLp6O8ITd0wRjb4GK5kAcI9q1WAlkqUapLcak"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "e8d9e615619d242daed15c2c74216933",
    "d65b103450993d79747acedc97a49947",
    "5d259687b8816bb305fdf681643d9f3c",
    "142ba994ed855dd04e29f3d21e1add4d"
]

LEGIT_PERM_IDS = [
    "243c6e3f376cdb16ca74201f11cd8425"
]

NEEDLES = [
    {
        "id": "1RhKk6MDodHNxBbUg86QJyin3yrEZMS6SSqZeflcJWwP",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "e8d9e615619d242daed15c2c74216933",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1E2C7wU2lrCXrMw77faIZZ7h6ACRq3SIWlPxqcfb5PVp",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d65b103450993d79747acedc97a49947",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1E0c4CAdwmAQBHzsuZSZK0ma4YO4ePMKMEBHfSdcUS02",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "5d259687b8816bb305fdf681643d9f3c",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1WdQ3CYtLp6O8ITd0wRjb4GK5kAcI9q1WAlkqUapLcak",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "142ba994ed855dd04e29f3d21e1add4d",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1oMF7U0SeOg0Sal1Bj8D0h8TNoCqKUstyVqSRzsizgRh",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "243c6e3f376cdb16ca74201f11cd8425",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1DEa5xiPrb49JRE6GBswnUlUTknwjT3AvzQhEacEKSQe",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "19aQZ4cRr4fLjo5sV0dKQj07IJEaF2fYU0ZXtwWAIEMV",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1JycTf3arhfASPuTwPaZkgDrdHvuqLuuW6Dr44UqdUjh",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "16vfplxXn2NcXyYgGuS6C6syZjCNm0hZHCGxofXLjIae",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
