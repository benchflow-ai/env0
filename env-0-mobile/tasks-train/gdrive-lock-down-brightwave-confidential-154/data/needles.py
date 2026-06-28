"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1YcPrvzRRJaa9oKHYteqFGPq0i8JEpsJqbrG6KkomxoS",
    "1Ui2iTX6fEcsTuhrvUP32eqiQHGIkGbZj6MKCYVjqOlo",
    "1vfeDL3wZmIdkiXstrkWY39kepFmSTOo720MWKjEELLQ",
    "1h9eLVuXcljsm0CXTkcO6ApmDTxPyiZGav1yI8QnUo28",
    "1NFViFmDs9MfxfFAdazmL8e9gvKpcxiaVmPjyFsuZsN4"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "dade71ef0600bee7bdc82d9e64f56b81",
    "1cd2100bcced71030e00c8540e2514d9",
    "d6d41bcc655ad2d3e9f313766580ea92",
    "058606ef880a83fe92a8e525bba5fd08",
    "034ffc7ca2b07129ac4cabafda315ace"
]

LEGIT_PERM_IDS = [
    "83e0f044139a68537f2d79bef7d786f9",
    "17fb19af0c8e33c9227509a8871cca51"
]

NEEDLES = [
    {
        "id": "1YcPrvzRRJaa9oKHYteqFGPq0i8JEpsJqbrG6KkomxoS",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "dade71ef0600bee7bdc82d9e64f56b81",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Ui2iTX6fEcsTuhrvUP32eqiQHGIkGbZj6MKCYVjqOlo",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "1cd2100bcced71030e00c8540e2514d9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vfeDL3wZmIdkiXstrkWY39kepFmSTOo720MWKjEELLQ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d6d41bcc655ad2d3e9f313766580ea92",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1h9eLVuXcljsm0CXTkcO6ApmDTxPyiZGav1yI8QnUo28",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "058606ef880a83fe92a8e525bba5fd08",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NFViFmDs9MfxfFAdazmL8e9gvKpcxiaVmPjyFsuZsN4",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "034ffc7ca2b07129ac4cabafda315ace",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1kQoGYTco4qkJeBCR5h4Rw25GEXxGFRGzRLZamJPvA1k",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "83e0f044139a68537f2d79bef7d786f9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1I2Y5K1wLcrJUfzB5tvqdokEs1qhmiXEAOjiYCpL0dQa",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1HOeEb583sqeT8S6yXoVAteb7rFFHyoElX68hdkA4wju",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "17fb19af0c8e33c9227509a8871cca51",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1VqI3KHEm6sp6ZuUyMQWMgqzUHnipJUn9MVRqaBNOG3m",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
