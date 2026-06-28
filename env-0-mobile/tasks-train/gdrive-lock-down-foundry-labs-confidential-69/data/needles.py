"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1L9Y1SuGv2bfQvzm86VDpBUwbpvqBs2muFY3Xe20dzE5",
    "1Jd9zApkpJzYRkm5zihnENbRY75ZyUC6WnQDDlqnQaEN",
    "1WZH8YQ0uU7khZK0WSVdpjuCk8Onsnz0bpgabdRgPHJt",
    "13VXoFGAFHjCDBSqXoDBxNrMDmndFsQCBYJ3OmeNmdZJ"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "4a7207d0710f001c6cdee75a41dd621a",
    "f41d53ea511b223505423d809abf16d7",
    "29d583a34d07dbc05704c2f83181d9b4",
    "84291e9629896345d6a88c4eb1766b33"
]

LEGIT_PERM_IDS = [
    "53aadd569d33c22b958e1e813ea11df3"
]

NEEDLES = [
    {
        "id": "1L9Y1SuGv2bfQvzm86VDpBUwbpvqBs2muFY3Xe20dzE5",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "4a7207d0710f001c6cdee75a41dd621a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Jd9zApkpJzYRkm5zihnENbRY75ZyUC6WnQDDlqnQaEN",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "f41d53ea511b223505423d809abf16d7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1WZH8YQ0uU7khZK0WSVdpjuCk8Onsnz0bpgabdRgPHJt",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "29d583a34d07dbc05704c2f83181d9b4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13VXoFGAFHjCDBSqXoDBxNrMDmndFsQCBYJ3OmeNmdZJ",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "84291e9629896345d6a88c4eb1766b33",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Zrc3d4WyNm9UnwOKb34xPLnjPMs1U7YOuUg2FH6bt9X",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1j3FyS5K1imT1jmFCnvRN4BDiVhvcAah7uSL8XBMg5Ax",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1H0VUNc9FefPvxcY3lUeUCYTFRi0W3chtO9LzYgoE1oy",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "53aadd569d33c22b958e1e813ea11df3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1GjNSiIZdp7wTDUWqdkcXj6Nix2wLQvRpQX1JKtcV14S",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1GlaCvpFL0KJrQMWkCHHauhhPGoBa0KfhcU274Cm88hW",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
