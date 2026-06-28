"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "17KYdRGst3PoTrA2ahtvcRsWVVvNGtfWll77ra9kNfUg",
    "1qN3XqicOK6vFmaZF7yRUKEalVpnPQVRYhwFs7l87Mgj",
    "1iGCnVk1wVZEOkv81CAnId1Y1XFo1pZWuNlPACAyfkDs",
    "1BHN4NlE91umy1QdCdkZQgXvNRWTfYqdyzI1RJ80DbWj"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "9df67381da80a965a971860738bb63b1",
    "1cc75b788a710e839c0b9ebd81d51b3e",
    "18ae91d967d289d046a32cbb58ba7c72",
    "0c638174515f415bbdb06a3d5b7ef1ea"
]

LEGIT_PERM_IDS = [
    "4061ae4769950665f2e810b0db9d1ef0",
    "9e5763d110ed766ed4448535aecd50f4",
    "9db22cfc3af81c11cd14d338b5df9376"
]

NEEDLES = [
    {
        "id": "17KYdRGst3PoTrA2ahtvcRsWVVvNGtfWll77ra9kNfUg",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "9df67381da80a965a971860738bb63b1",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1qN3XqicOK6vFmaZF7yRUKEalVpnPQVRYhwFs7l87Mgj",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "1cc75b788a710e839c0b9ebd81d51b3e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1iGCnVk1wVZEOkv81CAnId1Y1XFo1pZWuNlPACAyfkDs",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "18ae91d967d289d046a32cbb58ba7c72",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1BHN4NlE91umy1QdCdkZQgXvNRWTfYqdyzI1RJ80DbWj",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "0c638174515f415bbdb06a3d5b7ef1ea",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1EO3kYZydoSxk2pDzPy2f85YIzakIZrXBqtzyPQrZrNj",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "19mEHN5rtN2ARPN6sIsFQPfhuJP4sR40fqEs2bV0o5bf",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "4061ae4769950665f2e810b0db9d1ef0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "12h2cvDMCOuJ02vQlcmcxPpoiLdjImVelYxUuvuDSPKH",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9e5763d110ed766ed4448535aecd50f4",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1pF1PvB7dYpg46sqWp5f0bGcLSOhWuYbhqz8m4TGZ3HB",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1ETwWVmauV9w4wogk8rL9NiKx1Y8PNxfmPSNMXXs4nuE",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "9db22cfc3af81c11cd14d338b5df9376",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Jzo7BwFUXjQFETC087GzuPqWK5qSMJdxKJK40ZPYTRn",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
