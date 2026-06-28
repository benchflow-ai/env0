"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1XeikbaslEEKWgHyVYtKqBDG1dSarjgFoCiakHpvDFCk",
    "1KwY0t3xKi9jwIkEZO3taxB9HCvFS3pRhBbJQzyvggzA",
    "1BnlH1Wwg28rwKuOzvyVRKhEjqTzVP3FUYXxOe0011Zm"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "ef2761c5543cf5c7da33b9233b74f68a",
    "7b956fea353aad024b9b364ef1831d78",
    "23a00627d2035d4452912ae98108f642"
]

LEGIT_PERM_IDS = [
    "8cdd19bfdc813a37d18bca37249912a9",
    "6129ca6de41383aa828c748bea877f6e"
]

NEEDLES = [
    {
        "id": "1XeikbaslEEKWgHyVYtKqBDG1dSarjgFoCiakHpvDFCk",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "ef2761c5543cf5c7da33b9233b74f68a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1KwY0t3xKi9jwIkEZO3taxB9HCvFS3pRhBbJQzyvggzA",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "7b956fea353aad024b9b364ef1831d78",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1BnlH1Wwg28rwKuOzvyVRKhEjqTzVP3FUYXxOe0011Zm",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "23a00627d2035d4452912ae98108f642",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1AxRK4R0Wd42lJKPb4tT5qIfsXlQfX2Ca0nfwNxrxfyp",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1njKKUq2hUb1V17nYTC2pkF5XKCZg7IgEsxSKXuYOc6o",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "8cdd19bfdc813a37d18bca37249912a9",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1hIAdhY1U9uFLskA4EkqHLLzz6FRIKob4SyatGRvdND0",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "6129ca6de41383aa828c748bea877f6e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1MO3MfoR4AkS7QhWFC8cVTF6pXsLGwdKTmLK85zhNAYL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1aPxzfA3ox8FDbbWlErES3MdqPrJOClpHydDlGdjfYl6",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1IuZIyu5SZqgTZbmIcR3loPpBeeOg0bChZZEuv8zh22N",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
