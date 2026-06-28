"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1fk1CksvTbtRoQ4yvb9ou7BkI8IZvxHc6JehM7XZxZJJ",
    "1dzfEshWZYRJqBP8Fpq9f4WbjQt8Cf7uwzlKJpPao8WK",
    "1IyrClvSypXrp7O9IceBxi61LwCGUtS4SagVQnheTvqO",
    "1U9zwlmfoTFDrXZWcqzsu0bq37ltvk26Yv07Pl8X7Ssk"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "d4080e6283421c2754e887f3247f2953",
    "b2f4763bcb2bfc03bb8484c064aea9fd",
    "58d442284c2bcf737b16943c2c653390",
    "a5f19008d87f8f8ad0314a33c32ac5be"
]

LEGIT_PERM_IDS = [
    "e2392d2014577d9ca8ccfe4c5b386637",
    "da8503ae147f0ca5ca1bc7dcfcb681ae",
    "818d7ccd1fe4e18f309df5ef241fd2b4"
]

NEEDLES = [
    {
        "id": "1fk1CksvTbtRoQ4yvb9ou7BkI8IZvxHc6JehM7XZxZJJ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "d4080e6283421c2754e887f3247f2953",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1dzfEshWZYRJqBP8Fpq9f4WbjQt8Cf7uwzlKJpPao8WK",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b2f4763bcb2bfc03bb8484c064aea9fd",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1IyrClvSypXrp7O9IceBxi61LwCGUtS4SagVQnheTvqO",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "58d442284c2bcf737b16943c2c653390",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1U9zwlmfoTFDrXZWcqzsu0bq37ltvk26Yv07Pl8X7Ssk",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "a5f19008d87f8f8ad0314a33c32ac5be",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ZFrnf7CP50m2Lpgruh6Spi5pRLdDBXCOkbca7SM8Wjt",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1EU1HCq4VGINiMyJ6I7xgQwDIUD3iEvQgrE2EBNNkoke",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e2392d2014577d9ca8ccfe4c5b386637",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LJay8oT4W5oxg3evwrWCVqFpNJDXRYpzLE71NMqhtYo",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1Ge1mOsivRGOTrldJCAzHatFL8Yzk7JnOWb3rGQ8qpu1",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "da8503ae147f0ca5ca1bc7dcfcb681ae",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1T6BsNUd18DxUTZqDWVw6q4VgBN5WbFgXpbfzPHvCzZU",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "818d7ccd1fe4e18f309df5ef241fd2b4",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
