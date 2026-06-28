"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1TDlJxjlr6nZwlMRp0LOSS5eAe4V4cC2GBsTbuepce94",
    "1bW9QHbvXnN1CC3KMCviDrvM3po8lPw9s8rvpcv8ldVF",
    "1yq5UdT44rz2uvR0WLT7SiVFPlxr1iiwGTPYJgTQAndX"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "1bce62edcc85b1f5ba548e368ee7f64b",
    "9225ebb3b0b9d5fc50de3f4172f9c1fb",
    "a552d12dc908907fedef37f246ae4669"
]

LEGIT_PERM_IDS = [
    "97b033af14c0a388908e079fad51cb6f",
    "2877f4ce3c1e27b6cd4277ca7c3b800e"
]

NEEDLES = [
    {
        "id": "1TDlJxjlr6nZwlMRp0LOSS5eAe4V4cC2GBsTbuepce94",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "1bce62edcc85b1f5ba548e368ee7f64b",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1bW9QHbvXnN1CC3KMCviDrvM3po8lPw9s8rvpcv8ldVF",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "9225ebb3b0b9d5fc50de3f4172f9c1fb",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1yq5UdT44rz2uvR0WLT7SiVFPlxr1iiwGTPYJgTQAndX",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "a552d12dc908907fedef37f246ae4669",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1VEryU3pwFiKh2M3UQearFIlaERhHKxHqeWaNkIMS4Jt",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1X8RSubp8iHlSRNzBsowfLf0sOWbnUMFcc8eI77AkzBe",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "97b033af14c0a388908e079fad51cb6f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Pon3IUqs6qKdckSBgrBONTBbOz7BD4QubooiXKoJWZL",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1PkxssF2AuCW33s7BDu7xlKoOxUVcVAMpqU8mDioXBAv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "2877f4ce3c1e27b6cd4277ca7c3b800e",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1Msdrta7bSuUEX7H3Q4d6oZXMz2cBqe9avFsfMdq2HYI",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1OB5gvOJZxw38kkq5SIE1ogbh3GfS0p504v2XWJqQn4U",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
