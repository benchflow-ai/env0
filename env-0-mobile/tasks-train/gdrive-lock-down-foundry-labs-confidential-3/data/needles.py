"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1QWerfRt2Hnkt8uDpIfBCo33zwoZqDUGDLBY7E68vyVN",
    "1beXLaxir7e3oSBoCRzJofKHBhZNalwlBCi5OzQcoSGW",
    "1mNVvBp39C8dGPPvQnwl8GqtlTDOVeMFqfENw4RkaxdA",
    "1sBOi9dxDuekUZD81ybbQDTX25Qg1AQukAqIHp3SiMy7",
    "1RQTac7i3VY8OUG9noYPVGtVOz3JQL9ZJSmubfUFAhSv"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "bdca0a3bbe83c619484125f90e14c40b",
    "6aef46c14130abf9a21345e815df634d",
    "9b07708156d2e5dc3367b15c0726d7aa",
    "f0b0836820b63b556170df600f283838",
    "694f440e9dc8ff7eb49d06c3bf3616d0"
]

LEGIT_PERM_IDS = [
    "6021722c7a826720ae3ff8d86be3cb80",
    "81fe7f985e80e02418703b57ee2d27e1"
]

NEEDLES = [
    {
        "id": "1QWerfRt2Hnkt8uDpIfBCo33zwoZqDUGDLBY7E68vyVN",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "bdca0a3bbe83c619484125f90e14c40b",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1beXLaxir7e3oSBoCRzJofKHBhZNalwlBCi5OzQcoSGW",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "6aef46c14130abf9a21345e815df634d",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1mNVvBp39C8dGPPvQnwl8GqtlTDOVeMFqfENw4RkaxdA",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "9b07708156d2e5dc3367b15c0726d7aa",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1sBOi9dxDuekUZD81ybbQDTX25Qg1AQukAqIHp3SiMy7",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f0b0836820b63b556170df600f283838",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1RQTac7i3VY8OUG9noYPVGtVOz3JQL9ZJSmubfUFAhSv",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "694f440e9dc8ff7eb49d06c3bf3616d0",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1xYxxRHlKQ8FNrcWB7SjNVQPoB3j5U6xLJE6obrkgxNY",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1F4AWXw4GMWgqvnFPvTPgBtlgJ2Y6QYJNJHTjpR4U6CR",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1NiBm1UxhfSnPAbzL1jwGTOnQWGBZxQ4KdyRHdVqbiPO",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1hEH3W6K27ZJTpqZA2v1FWlZG0W5KctNrfbroKV9pTjU",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "13bScNTCHk62vfjJSEzwhG5CWp1UDyLDBT2kMhQyzVN1",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "6021722c7a826720ae3ff8d86be3cb80",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1MloI7EtPBmwRBJquNHUfywpP9xRasBF6nH5Tczo4y6z",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "81fe7f985e80e02418703b57ee2d27e1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
