"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1LkYOLwSb3uaN7XSA1FUckiMBq4RS1hF91151tGq5tlE",
    "1OhpF0iyaRpxvGvZDne0lNeGet4FfdJm28eLhDfx46N1",
    "1S8rosyOYT7TVXUqVF1inLvN2cbUl3VDkV8GlVIYCSYt",
    "1xXYG9pjSKiFkR5lQ0u0Sv4UlUnLUfD6h8milGjB7Vzw",
    "16zwZdIg2j3lXqdXG67CPyTbxTxtmeFUmqdujd4CkSpy"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "86492c71ee3e4568f6eebb0a125cc9ff",
    "36d2a01803a3d9ba07104b44ab63ed7f",
    "859083527fc020b9b2ce4125686945fc",
    "534b55e3a276e0fe679f295e3fd63865",
    "d267253f2f9962534d15373131a444ae"
]

LEGIT_PERM_IDS = [
    "462eb0589e9c8d65d37f3bb40f5ce977",
    "c4205aef8b63a42dc7dcb38a0e9ec629"
]

NEEDLES = [
    {
        "id": "1LkYOLwSb3uaN7XSA1FUckiMBq4RS1hF91151tGq5tlE",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "86492c71ee3e4568f6eebb0a125cc9ff",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1OhpF0iyaRpxvGvZDne0lNeGet4FfdJm28eLhDfx46N1",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "36d2a01803a3d9ba07104b44ab63ed7f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1S8rosyOYT7TVXUqVF1inLvN2cbUl3VDkV8GlVIYCSYt",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "859083527fc020b9b2ce4125686945fc",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1xXYG9pjSKiFkR5lQ0u0Sv4UlUnLUfD6h8milGjB7Vzw",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "534b55e3a276e0fe679f295e3fd63865",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "16zwZdIg2j3lXqdXG67CPyTbxTxtmeFUmqdujd4CkSpy",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "d267253f2f9962534d15373131a444ae",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1UldGdRvIhYUDLRMzg7npln6dPf5vcFQZ0PC8PVRQj1f",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "462eb0589e9c8d65d37f3bb40f5ce977",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1mlTQNwUfn1a9kKjFOiWdc1ig10upeXIG6TYFPRV2SxJ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1S1tD4fePWP7T4fBa7z38P7KGgfe36HGEfOWTtnlqtgQ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c4205aef8b63a42dc7dcb38a0e9ec629",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1USzEKt7BKZDQHrJTjRwgdlVQ6EN3eNb4LUyze7eJiIN",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1i66F2VXmbOGTehubI7F5Vhlv5Dw1UaW2NEU1THZ8TPe",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
