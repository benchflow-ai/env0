"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1mzDI7gDvoZfRrp4265Eqv63Pb0h909ZSrLYJIyHGFJC",
    "1ZpWvnuLxlhE80EqGzChGRJCI3Skq9Z6o2s0WiQ6asGi",
    "14o1s5sXTFDoUlwOCVZza0boB5g9iW3he6AKGBsLQhnu",
    "1uIxf7PwUSMaokFqcedeH4vjz8yr0qWxXSTFfCBNT9pR"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "e0f585c418b06ed0195840caa4e7d28e",
    "7d5ca223e0f44a16778c3341bdb74185",
    "d369640e129874eec9ec1aa1eb7936ad",
    "8721803d69aca737083fc020011c70c7"
]

LEGIT_PERM_IDS = [
    "b380a4f776288dca0ee9b7e6305cefdd",
    "ed78c1226a52820baa06eab4814fff6d"
]

NEEDLES = [
    {
        "id": "1mzDI7gDvoZfRrp4265Eqv63Pb0h909ZSrLYJIyHGFJC",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "e0f585c418b06ed0195840caa4e7d28e",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1ZpWvnuLxlhE80EqGzChGRJCI3Skq9Z6o2s0WiQ6asGi",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "7d5ca223e0f44a16778c3341bdb74185",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "14o1s5sXTFDoUlwOCVZza0boB5g9iW3he6AKGBsLQhnu",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "d369640e129874eec9ec1aa1eb7936ad",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1uIxf7PwUSMaokFqcedeH4vjz8yr0qWxXSTFfCBNT9pR",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "8721803d69aca737083fc020011c70c7",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1PpFvodoypZ3uBNwL1lc1TOnf1EoOgNYToMPMdaeyf4b",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b380a4f776288dca0ee9b7e6305cefdd",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Rv2Vb3lgqLb6g8kaJtPNC2379VwGDyeEInR07FLLLeh",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1coLQvhqQnS6erK4NOIHwAbHIXBsOxZOfNXqwamHQ3FA",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ed78c1226a52820baa06eab4814fff6d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "19dPbT6isj6B58r3laM1j7XOZK6i7Q2eTtbo7TQd807f",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1cg9br7GHL8fkn51BCbDw77BhJzDPBPgUanO3Cs3Z34V",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1r49PAVrye904vvqoe9PJusbC9T4lqlxYCYW0c4jrwKT",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
