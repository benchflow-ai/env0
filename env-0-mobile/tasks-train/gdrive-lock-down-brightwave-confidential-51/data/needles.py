"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1mYJJkdon94vbbXyUukniyhhb9Foz4GAVLNEscTbwC6j",
    "1tlwKvisxvIoHcb3gTiCgEzwtSElLO8mc4PGBVr9DOO9",
    "1sXiyDqdYTEStyaF7mA84h3K7dNgG5zSSOht9WNSEwvT"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "83e160eaff30ed73ba4245aa77766270",
    "bb7950b3a9f56c56c2b29d6ee8d5c5e2",
    "7faad608855cef8eef78b2b0908507aa"
]

LEGIT_PERM_IDS = [
    "8bd1327cc5debf63d517771437bef6b0",
    "4244dae6ca05f99a9a15cf9c1a032276"
]

NEEDLES = [
    {
        "id": "1mYJJkdon94vbbXyUukniyhhb9Foz4GAVLNEscTbwC6j",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "83e160eaff30ed73ba4245aa77766270",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1tlwKvisxvIoHcb3gTiCgEzwtSElLO8mc4PGBVr9DOO9",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "bb7950b3a9f56c56c2b29d6ee8d5c5e2",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1sXiyDqdYTEStyaF7mA84h3K7dNgG5zSSOht9WNSEwvT",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "7faad608855cef8eef78b2b0908507aa",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1eJFuGh74UaJ3lWkIWJAOogZF7Bo443FOpwgIom1Ouab",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1I7mM41ZqJSayZL9TMvOFrIf7X0AIdVLQg4U1UaO51cV",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "8bd1327cc5debf63d517771437bef6b0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1zzWJz64UlbdSXdjdmU5HlwFvI83Q769CtFgMs1Ah3Nl",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "4244dae6ca05f99a9a15cf9c1a032276",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1jjqQyJ657Z4NsVjMOeSH2gRxg8APUQEBVPPMmgTWTz5",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1k1Bcy2lKeNCtxo2gSWd2Vc190Jd0qONtPYbw2Ma0oUp",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1sMc1YzPKgdfnUtWrkmF2ClgY16C4pEpdiaqsSfBoY2Q",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
