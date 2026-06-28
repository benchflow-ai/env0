"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1qHUmacbaWqKNgX0nY770xO5ufbkbMsA09NlwctngPqu",
    "1rUJzeF8gK1Ti0LIkbvwjXsvqw5avM7H7Vxnqs5ulUZp",
    "1AOAwnZPqPfm4U15EmHxgNoUt35LwP5czfCW3rdYdDB9",
    "1sy8hK6biyDEObIOJ64tcRk0M1EdtjwaAlSU1MTz2GK3"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "3c5526ec9b686d8173f19c30c5090328",
    "bc69ee5326df2e284093c03fa4785822",
    "3de5f9a6011e679fed2ba1cb1f873666",
    "4af4e6d1749a3aa79facd46aa0180d30"
]

LEGIT_PERM_IDS = [
    "8b5e7e27c66d3f38498668dbe22dabe2",
    "7b48291ff1888fb065d604efe912341a",
    "ed0003f12533d6265467f6c8de3d4823"
]

NEEDLES = [
    {
        "id": "1qHUmacbaWqKNgX0nY770xO5ufbkbMsA09NlwctngPqu",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3c5526ec9b686d8173f19c30c5090328",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1rUJzeF8gK1Ti0LIkbvwjXsvqw5avM7H7Vxnqs5ulUZp",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "bc69ee5326df2e284093c03fa4785822",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1AOAwnZPqPfm4U15EmHxgNoUt35LwP5czfCW3rdYdDB9",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "3de5f9a6011e679fed2ba1cb1f873666",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1sy8hK6biyDEObIOJ64tcRk0M1EdtjwaAlSU1MTz2GK3",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "4af4e6d1749a3aa79facd46aa0180d30",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1JBVU1lNFd97BsiTlAUm2SlRfQ9IJynFQGpPZrznadg9",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1T1iISqhONSlaGQd5oInHuzdPMZ4wnNToEXMoHYfWsC5",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "8b5e7e27c66d3f38498668dbe22dabe2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "10fhm7HVocedRwADq9XIwXcYTBhOymg7dynq27gv4PLr",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1wdXXNp0pzZoYGZ8jGKxUG220crAyM868WQSDqIuvDgQ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1EskrBZbMKlwsxOFnQyoE9E10CVkL7XDOIP8gt1ax9AZ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7b48291ff1888fb065d604efe912341a",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1lS65m8HcFUrQEAyzP3kaxGM9EkSEqxGOmwyHllqAUPO",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ed0003f12533d6265467f6c8de3d4823",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
