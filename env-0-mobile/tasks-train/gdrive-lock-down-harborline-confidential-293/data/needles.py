"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1OxpV9eiWqOZZuMLBR8eCY6h8sytLbhOfVoqvh6tgiYb",
    "1bj8viaAZRn8UWxerCguzZd61L6UBW2OfY7R6QBvo0qa",
    "15D9DYeVrZnCUJmrwWvLmjan5jMSFzbeXb0my191Jkhi",
    "1Q1xvzL0lPlWI5vCGmkawkZZp2uRPcU1kCm20mBLB0dV",
    "1z9SGBmYSbHJX7RB845sYVU9zWfTvcOwDyn5aNTFqu72"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "5736a4bcea69b44e252a4c4ca9b2e3f2",
    "4bd680563eb8b1404549eb111e113c38",
    "6a01ce753acd5f0b6dcbb123f3409e29",
    "be83c98cda65694a6eb321f5826e4c2e",
    "6785f84a0932928a3fb5e1a04984a9d7"
]

LEGIT_PERM_IDS = [
    "82075768b56b89f05e803a24a4b7f21e",
    "4d698055d7ce748415bf48b2c21c00a9"
]

NEEDLES = [
    {
        "id": "1OxpV9eiWqOZZuMLBR8eCY6h8sytLbhOfVoqvh6tgiYb",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "5736a4bcea69b44e252a4c4ca9b2e3f2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bj8viaAZRn8UWxerCguzZd61L6UBW2OfY7R6QBvo0qa",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "4bd680563eb8b1404549eb111e113c38",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15D9DYeVrZnCUJmrwWvLmjan5jMSFzbeXb0my191Jkhi",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6a01ce753acd5f0b6dcbb123f3409e29",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1Q1xvzL0lPlWI5vCGmkawkZZp2uRPcU1kCm20mBLB0dV",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "be83c98cda65694a6eb321f5826e4c2e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1z9SGBmYSbHJX7RB845sYVU9zWfTvcOwDyn5aNTFqu72",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "6785f84a0932928a3fb5e1a04984a9d7",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1VaRQzOtRxYJ3ioBZIPYYTatgpxndlyT363wUzOcKLch",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1t3xjEk2j64lGgisTaAWggpiWvmgtwWYYkLbKAL6sKsT",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1LBA1UTnOPZs8Lw3oMQbE0e9hGaDrTjPztfrgzwj0fZl",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "82075768b56b89f05e803a24a4b7f21e",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1t4Kn6jWtyr6glBIz1Zx0EvfjgY4ahCrCWnjLWxqUtfA",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1jk5U6mApIxJccRSWw4TdRkQ1ExhYXnzFJNVp5prGFkI",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4d698055d7ce748415bf48b2c21c00a9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
