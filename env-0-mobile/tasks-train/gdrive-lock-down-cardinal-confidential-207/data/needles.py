"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1wle2VcX7VV7NeAKAVVxFT281bZPWyaW5DMBe2bDrqry",
    "1rJeDytrvErKWreYFhCZTltRU24xS2NFbsy496Vx9Z9g",
    "1dR6YKdeO9UehBBDw2th1KxKksYadMpxZc7DclcKwr9W"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "e901a7b18c59cada91b49ac4d49435e8",
    "5633cdb5592bd42a7b1086c468e89194",
    "e86479d933d8871d6e34fe7ebc142be5"
]

LEGIT_PERM_IDS = [
    "a823ad75ab2831648e7000dfb64ef098",
    "7f3fbfdd78fe13244e682784e6146df6"
]

NEEDLES = [
    {
        "id": "1wle2VcX7VV7NeAKAVVxFT281bZPWyaW5DMBe2bDrqry",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e901a7b18c59cada91b49ac4d49435e8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1rJeDytrvErKWreYFhCZTltRU24xS2NFbsy496Vx9Z9g",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "5633cdb5592bd42a7b1086c468e89194",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1dR6YKdeO9UehBBDw2th1KxKksYadMpxZc7DclcKwr9W",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "e86479d933d8871d6e34fe7ebc142be5",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1uP748iNxXwLPHXRSwVRvp2kcVa4S1D9Bz0I2ZD7kxa2",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a823ad75ab2831648e7000dfb64ef098",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1jTjCrEAG4LC5r3dd9DEg0l7PnDr8LZdq0dWBIDIcVIu",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7f3fbfdd78fe13244e682784e6146df6",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1Tbvdr1RAE89y0uomQqXb2fQ2nhGMvQ3USXP9MXgVAlM",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1uoAXLKV3CVqnGF4idwAC6BhxROZFrfRioimyroQlwOo",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1Xl6VPLOcTsTdwRnZoY28CxUPHvlL9wNkLdrFUpEIGkZ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
