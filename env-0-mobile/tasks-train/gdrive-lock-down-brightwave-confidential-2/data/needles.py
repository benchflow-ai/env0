"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1mJrhyP5izCwhPcZ0TDmLosfbOzVJUzOdKEWGR3XtzTI",
    "1VDSHZltFu4unnQg5DngENPlMv9dspDnECTYUjWHnvw7",
    "1FBPUDGLuoyh7D4OI6bLxMs5QngLdiL07DtqSrc9v8JJ",
    "1PCYy3e0SxaBXzaK6Hl6IINsjfUMWWDY6ULmJHR6m5JZ",
    "1JUGFeC8cF1xY7V5IfyfOlbPVD6THL5IH1ag7gepfTPV"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "b09e60a31e7330d62f4de93d5845d483",
    "c8dc3696e004bfa5c4aa50d2095eaf55",
    "af7bb914d8c81128a936f9ef29833776",
    "82ebfc2e4cc6fec34d160c41d90fef6f",
    "a667b38e09608391a81d76eb87e09242"
]

LEGIT_PERM_IDS = [
    "55f27667268328e9f174e81054846984",
    "f7660f2591a5364eb4c27fa984d619ae"
]

NEEDLES = [
    {
        "id": "1mJrhyP5izCwhPcZ0TDmLosfbOzVJUzOdKEWGR3XtzTI",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b09e60a31e7330d62f4de93d5845d483",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1VDSHZltFu4unnQg5DngENPlMv9dspDnECTYUjWHnvw7",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "c8dc3696e004bfa5c4aa50d2095eaf55",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FBPUDGLuoyh7D4OI6bLxMs5QngLdiL07DtqSrc9v8JJ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "af7bb914d8c81128a936f9ef29833776",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1PCYy3e0SxaBXzaK6Hl6IINsjfUMWWDY6ULmJHR6m5JZ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "82ebfc2e4cc6fec34d160c41d90fef6f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JUGFeC8cF1xY7V5IfyfOlbPVD6THL5IH1ag7gepfTPV",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "a667b38e09608391a81d76eb87e09242",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1bo7FiIgJY5JnsgpkA4m8upkavesP2mtbLA8H8A6xLgH",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "55f27667268328e9f174e81054846984",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1oOAyJyAxOV1UZLMwJE2AnKs7TNWh8Km4FnGbNl8lONz",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "13rYGoDCvXEO7KUtKjPeonNX2o3KCIxcxc14ewXtT9bc",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f7660f2591a5364eb4c27fa984d619ae",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "173OUbKdpuepeIEkOHz5CutrrA0Wp33GBQRDxPUp6in2",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
