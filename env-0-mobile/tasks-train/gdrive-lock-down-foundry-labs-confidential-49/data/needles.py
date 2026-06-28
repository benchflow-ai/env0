"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1B7AtldEQqa1OeGCjdbMhLPabVxtuVUFXvsxsWTd7D6O",
    "1l8nZT1VlKQAFKcu6Os5oMUDSgeKf6tqkUSkq5Plhsb1",
    "1FHr7cBtCgzZ08YwVY9NHs9YKMDm4Fvu3358Qfy69pgV",
    "1wKOdFlJCgYqZyyWyce9CS02xCzD4OE7y6dyMVOnEI0r"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "533d375a304bc1a08ba6e7ac24de3be1",
    "6c4b0e679ed92ebdeae88d88bba3e49c",
    "bf9cbd27e0a6328d8318800613c0f0b4",
    "6668cb3e519aeb256e21483c5595cd58"
]

LEGIT_PERM_IDS = [
    "a63c1a0c525449387f31e41452e83ef8",
    "40b7d97b7eefc2a1b373e3e8a960df1b"
]

NEEDLES = [
    {
        "id": "1B7AtldEQqa1OeGCjdbMhLPabVxtuVUFXvsxsWTd7D6O",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "533d375a304bc1a08ba6e7ac24de3be1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1l8nZT1VlKQAFKcu6Os5oMUDSgeKf6tqkUSkq5Plhsb1",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6c4b0e679ed92ebdeae88d88bba3e49c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FHr7cBtCgzZ08YwVY9NHs9YKMDm4Fvu3358Qfy69pgV",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "bf9cbd27e0a6328d8318800613c0f0b4",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1wKOdFlJCgYqZyyWyce9CS02xCzD4OE7y6dyMVOnEI0r",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "6668cb3e519aeb256e21483c5595cd58",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "15sDMxDXd2k47WKcxytHYcUv4Q9Wv0FVYSA1MHs9EJrq",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1AVXbXoBVJdHG4ram9UNyTsq0KQmEyCMuV6pKDxQJ48o",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1hGjzcBzPYP1pMtmExv54KEs4cBqGQ9px10f1ffkTlmw",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a63c1a0c525449387f31e41452e83ef8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1WRsHl0L6Rb8YPcySLlBPExH4zb6OFpJNzXOgv43lBlT",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1uta6BRN4dLAw9VTDmAkWYVu2WwoEQRJswxt9C7jfh8O",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "40b7d97b7eefc2a1b373e3e8a960df1b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
