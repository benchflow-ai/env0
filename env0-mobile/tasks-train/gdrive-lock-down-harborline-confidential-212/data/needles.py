"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1LYeYqi8FjcF71x1j8btA2AvDyuShIHfyZbxJJEwfQhv",
    "1vz6M8pwJGdYjusUSnsprwh2WC0IH5TXJ0U7CbOW97U2",
    "1JSOHIXwDsji73acsCxnqQOZxclBSxIFBpzZGDjc3SKu",
    "13AF7KYNtdMOhwiNR8Dm7GE85sKVQ2X5MhdRiXz1U8Dd",
    "1ip6IHrCamqONznsJxpv7GXK9puFHFhoj6OUeTm0Opyz"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "75c34bbcacf83e710aba01b37ef9c06a",
    "524e6487c6999e4022ae24fe377b422f",
    "9b718a5a6aa5cd499eb36cf2989f2bc4",
    "742645155f27ea78f3d3b5e8fd59d709",
    "1fc01cf0c4439f3d592b3bbbc5e6e2bd"
]

LEGIT_PERM_IDS = [
    "8349ccaa8d952899c2fda1e2311627b5",
    "35361ab2b811a699eddfe19f49df54b5"
]

NEEDLES = [
    {
        "id": "1LYeYqi8FjcF71x1j8btA2AvDyuShIHfyZbxJJEwfQhv",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "75c34bbcacf83e710aba01b37ef9c06a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vz6M8pwJGdYjusUSnsprwh2WC0IH5TXJ0U7CbOW97U2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "524e6487c6999e4022ae24fe377b422f",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1JSOHIXwDsji73acsCxnqQOZxclBSxIFBpzZGDjc3SKu",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "9b718a5a6aa5cd499eb36cf2989f2bc4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13AF7KYNtdMOhwiNR8Dm7GE85sKVQ2X5MhdRiXz1U8Dd",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "742645155f27ea78f3d3b5e8fd59d709",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1ip6IHrCamqONznsJxpv7GXK9puFHFhoj6OUeTm0Opyz",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1fc01cf0c4439f3d592b3bbbc5e6e2bd",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1WwxDEt9Hi1xBE1LQOEY7bIeYQNUwJdgYLFvp5afcYzk",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "8349ccaa8d952899c2fda1e2311627b5",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1dx8hdIjzxneZxSMmvsH6vbKBphtxSaNqUoQpetlb5HH",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1l77bKLy4J2juWmZv3J48eVslrYwlOetvpmJ6yVeEeVL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "35361ab2b811a699eddfe19f49df54b5",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1qV2sww3ggExriPqLGXliezUvf44oQeH3ro3X2jjtVKP",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
