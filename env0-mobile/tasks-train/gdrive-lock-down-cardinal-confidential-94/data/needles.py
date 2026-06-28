"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1dAw5OpqtJ8x7OIRcJ9N0IjmVU71nxDwXhKN3G7g2mu7",
    "1FcfIoQPLmQTCvfb4q8vKchKUtZ3WzWVc31eNaIA6TAo",
    "1t9wskfoDmar24aLM0a4e0ILVyZoc2z3IwdlyNytPZyF"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "6e102c8fb9edc599f1d9e1082e479499",
    "e487a9e5357ab58dc83aa25d1de724e3",
    "6b13ef5465e05133f78bb7cd54c2710b"
]

LEGIT_PERM_IDS = [
    "13a154450216eee8beadf858c00b101a"
]

NEEDLES = [
    {
        "id": "1dAw5OpqtJ8x7OIRcJ9N0IjmVU71nxDwXhKN3G7g2mu7",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "6e102c8fb9edc599f1d9e1082e479499",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FcfIoQPLmQTCvfb4q8vKchKUtZ3WzWVc31eNaIA6TAo",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e487a9e5357ab58dc83aa25d1de724e3",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1t9wskfoDmar24aLM0a4e0ILVyZoc2z3IwdlyNytPZyF",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6b13ef5465e05133f78bb7cd54c2710b",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "10tBQe4iwl1lw94uPybbGNDx1XJFxgW2Fwy6f0RPANng",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "13a154450216eee8beadf858c00b101a",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1H8mHz3Ix8mLRgQQVpOCdkTonUu8BF0o5xN5Dn4O6kWe",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1xPE9S8Rm1ZNsT6J8bUOmGK7XyFo9OKCqhgqs3q34tZy",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1kHRiJgHJdwbo1Z1DlQWf1061pht8GC8ZaEVXpSMUM3l",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
