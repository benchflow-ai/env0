"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "15HM3lnQVuksYkhDy38356dd27jpTZlsoRSux0bSAfNt",
    "1sKSESpVzuAHUHQGCJA3ajD4ZAOB5AZbPS2tndwTMoQn",
    "1p9wU7Y3uf5Ezo5vxTuaibLRYCWYLrJS0ZInY7PRhBNX",
    "1Vt0awVOmIOKUoAw4d3VwRUTfb0xoPFy0nD7X1U8JMe3"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "f37751ea10fdb1a19859fec3ff87dae9",
    "2934940ab639ec7bb03a14d2ede77c0c",
    "5a39e6f5e8cd1472319f044a90ac7f9e",
    "a5ec6f5f84c20b1c80ff5966f4c305a3"
]

LEGIT_PERM_IDS = [
    "41e79371ed6ef894c7b0d33dda60e8dc",
    "14092012ff3d5a1b0be350b8a9b9938b"
]

NEEDLES = [
    {
        "id": "15HM3lnQVuksYkhDy38356dd27jpTZlsoRSux0bSAfNt",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f37751ea10fdb1a19859fec3ff87dae9",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1sKSESpVzuAHUHQGCJA3ajD4ZAOB5AZbPS2tndwTMoQn",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "2934940ab639ec7bb03a14d2ede77c0c",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1p9wU7Y3uf5Ezo5vxTuaibLRYCWYLrJS0ZInY7PRhBNX",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "5a39e6f5e8cd1472319f044a90ac7f9e",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1Vt0awVOmIOKUoAw4d3VwRUTfb0xoPFy0nD7X1U8JMe3",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "a5ec6f5f84c20b1c80ff5966f4c305a3",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ck7BcH5uTrXVx083fPK0zF4IYNwv1mAjBA95eXoHoeQ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1g98mPV5GO0Zw6EvPk9dPjR5sevuEh1bWH2RXQ0Ww0jK",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1zX0q74mn1M4611kjyWN9rN1d2pVyZHT9UUJW3GyTzTJ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "41e79371ed6ef894c7b0d33dda60e8dc",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1HuoLUL2zVqMnB8nUtKmy48CnfefBmhoLEpIfgNqea9I",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1KzIlec4vowBxk2Kyw2nCB47K9tuXDhmNDAAdwXOsS91",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "14092012ff3d5a1b0be350b8a9b9938b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
