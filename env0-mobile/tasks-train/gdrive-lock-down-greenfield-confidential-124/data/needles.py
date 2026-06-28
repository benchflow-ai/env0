"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1b37GfZ17Q2nrSvUJhpvDxbObl12YJIbWlXYO6GG4GmT",
    "1MHzGcSuYjLZJtOcHREuXCqY6SP6EmvVkszGKas5X8vN",
    "1ajNsYswyocodAvqaIU1J3RGhkP40Y5vdiEaz4g1VIJ9",
    "1Oy8nCZRLLu0rfV70kZbwIis6w2C4CTX8gTnGnWGdGbf",
    "1BfxF1HSOiOOIgPLl4IrCD0yMGXSZw8P6F7jNacEbOhF"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "fcd9d0cd97fec156068f775c6b996cdc",
    "f8e8a31ff70a11daa68c4ba8afc32a89",
    "bb177855d126fc39fe71829aed7c3242",
    "eda80cb5f52360254bc8d556bdc58012",
    "0d4aebe51cb5aaaa43b697835a5928ca"
]

LEGIT_PERM_IDS = [
    "72dffff5ca774f2ac3af3272b81713a5",
    "e35249871cc6eec7e83168fc826d50a1",
    "c427ff90754a8357edb7526eea95ee58"
]

NEEDLES = [
    {
        "id": "1b37GfZ17Q2nrSvUJhpvDxbObl12YJIbWlXYO6GG4GmT",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "fcd9d0cd97fec156068f775c6b996cdc",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1MHzGcSuYjLZJtOcHREuXCqY6SP6EmvVkszGKas5X8vN",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "f8e8a31ff70a11daa68c4ba8afc32a89",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1ajNsYswyocodAvqaIU1J3RGhkP40Y5vdiEaz4g1VIJ9",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "bb177855d126fc39fe71829aed7c3242",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Oy8nCZRLLu0rfV70kZbwIis6w2C4CTX8gTnGnWGdGbf",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "eda80cb5f52360254bc8d556bdc58012",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1BfxF1HSOiOOIgPLl4IrCD0yMGXSZw8P6F7jNacEbOhF",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "0d4aebe51cb5aaaa43b697835a5928ca",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1lZ2WsvmxcrgFWfr8Uol9A0k44XOms7BsvN6WyF596Tu",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "72dffff5ca774f2ac3af3272b81713a5",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1r6WalKzGztBbVHaip7R7YWmpyPwypJ9suynnwGUoEPh",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e35249871cc6eec7e83168fc826d50a1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1892WGC1XyyJ5cXgQKY1Lnw2lnJisFrAAN8JfcwAD5MQ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1rIs53oWGtltxWpgIeoVWyMK5xJgZEFGOv7N4DhpJmIf",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c427ff90754a8357edb7526eea95ee58",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1QBiPsaIDqBQ4JaFLJAEDJmDQU3VQ8VutK2vozaKbVdX",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "10slvs9CcIOjmxp6p743VRwOTbRuB6QK4rgzyKRPzsuo",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
