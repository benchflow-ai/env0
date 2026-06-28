"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1OoJ80zzXJ76HwQafpsMahourCRqoVh77hYO3hEM3N91",
    "1845qSK7oRAsaonY5Xt0WawV0f9u3Tyo5Kv10lH78mGi",
    "1Zv7zcUkzthZqAU8XSJ0Ugp7eT5vyiDmIau0cwKb1Vv5",
    "1CDFbEeEc1etgu6EwymGNNKaS7RCWjpfWUPvoxcIlfEH"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "7d802355fcd95339f2cbcf4d7eb3d404",
    "a4e1fedf0dfefb2a8679f7bb010d92d7",
    "f4b4867659ac1f966dfddb158e3f883d",
    "c75d510654eebd36ca053e7b7bd71809"
]

LEGIT_PERM_IDS = [
    "63344f2b8ef88076e3c4f176f2e935f1",
    "7574b2fb3b75bd956ea99494ed95b963",
    "3fe58d60926c58436e74306fc46d9332"
]

NEEDLES = [
    {
        "id": "1OoJ80zzXJ76HwQafpsMahourCRqoVh77hYO3hEM3N91",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7d802355fcd95339f2cbcf4d7eb3d404",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1845qSK7oRAsaonY5Xt0WawV0f9u3Tyo5Kv10lH78mGi",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "a4e1fedf0dfefb2a8679f7bb010d92d7",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1Zv7zcUkzthZqAU8XSJ0Ugp7eT5vyiDmIau0cwKb1Vv5",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "f4b4867659ac1f966dfddb158e3f883d",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1CDFbEeEc1etgu6EwymGNNKaS7RCWjpfWUPvoxcIlfEH",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "c75d510654eebd36ca053e7b7bd71809",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1hCudYbbyyX64mYSWnGvjBMU52yhhEeeWXnjr8N8MbB8",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "63344f2b8ef88076e3c4f176f2e935f1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ytPbQnbYJrG6m0s37Ko5nlrTem1jClg3BhD9JW1iSbD",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1GIJBIIYhhBjsmxkV0AMCJoiUiMZXmvzq9YIkGkbWTsd",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7574b2fb3b75bd956ea99494ed95b963",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1nYk5xjotIZNOEC6WDTtT7ty44EHZlgwwxPWKw4fvWTj",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "3fe58d60926c58436e74306fc46d9332",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1SYR3WQiBUtu4qUKeXQ6Mj9S67dSSWAL8T33VSOFT5xt",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1yT9enUy1ixzwCkhgrcyE9ongRYetZgWTQGGktFbDUtN",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
