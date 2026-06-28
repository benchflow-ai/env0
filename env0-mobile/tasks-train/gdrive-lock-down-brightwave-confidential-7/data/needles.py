"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "15x9dRhR2Tn6wj0xPZ4XWqlsDNaOrlIu6aROuOH3t2QH",
    "1JQGESd7P71uJqSV3GCAJHMjwU6ztSMHHU6QD0u83nwL",
    "1sw3zJ9hVstStC6znQHFqtOzhUueyQCquVdiOTbCSQyR"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "540509cac43ec94a29c0bfa349943b4e",
    "ec1ee94fe305bbad0123e9a277fe9e98",
    "3a92ec3472d408d3ea78cb714772455a"
]

LEGIT_PERM_IDS = []

NEEDLES = [
    {
        "id": "15x9dRhR2Tn6wj0xPZ4XWqlsDNaOrlIu6aROuOH3t2QH",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "540509cac43ec94a29c0bfa349943b4e",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1JQGESd7P71uJqSV3GCAJHMjwU6ztSMHHU6QD0u83nwL",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "ec1ee94fe305bbad0123e9a277fe9e98",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1sw3zJ9hVstStC6znQHFqtOzhUueyQCquVdiOTbCSQyR",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "3a92ec3472d408d3ea78cb714772455a",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1RQ78NVYqvi6A7rEZIZAqRfq7TG1KUrXBXC8v8fWOLYb",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1iyxYF5eKzQbejBzw1kDJEb31Gc5g86YvVySfqBCG6JZ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1HNNdbmgoDvU2CUCHyzaZD1I8UQbWcYtJ13At6GOXbwF",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1PU3Mh6pLG9PVLHkaVdI0ohGblgRBz9w4wLmG9bNOMVK",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
