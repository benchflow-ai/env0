"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1STgcddm124mKeyqzrtW4TlvLJ0W7Rotslzfae39Lm1w",
    "1ozjOJECkZuOveXkWyyEfcLGe1GQPnvSbqqNuyagRHG1",
    "1zTKVlEIpt414AKmL6478SjD475UU22LvYja1T5V95Ax",
    "1v5h7GnEdNiajxrRDhblIuN5kbdBaPYCLem852zaIURK",
    "1Un1SMtEESqwmBrACKwd8wQdJAAOEJBJGHKIvDwux8zb"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "0b277359a46d9a932207897c9d809299",
    "2de5fc86681e2de2411aec8b2449b693",
    "7a0bf34205c34ddbbca106e18c9facf1",
    "4d9498ae62575e70a9ffdb0fdb903101",
    "83814711d5e0402e79c864984e5808e2"
]

LEGIT_PERM_IDS = []

NEEDLES = [
    {
        "id": "1STgcddm124mKeyqzrtW4TlvLJ0W7Rotslzfae39Lm1w",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "0b277359a46d9a932207897c9d809299",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1ozjOJECkZuOveXkWyyEfcLGe1GQPnvSbqqNuyagRHG1",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "2de5fc86681e2de2411aec8b2449b693",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1zTKVlEIpt414AKmL6478SjD475UU22LvYja1T5V95Ax",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7a0bf34205c34ddbbca106e18c9facf1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1v5h7GnEdNiajxrRDhblIuN5kbdBaPYCLem852zaIURK",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "4d9498ae62575e70a9ffdb0fdb903101",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Un1SMtEESqwmBrACKwd8wQdJAAOEJBJGHKIvDwux8zb",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "83814711d5e0402e79c864984e5808e2",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1mjXRwXJhqbiwBviBrfZC6Dab4ZedoAAmr2IfaDLszMo",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1cjNzlbpzK1k06SmV9WOv5N9HueS6cRfmaDJTRIAy7Ag",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "16ZzZXOpPPQOJ0DPoee4GFgLDd8Fy9V6z74ZIGPUc195",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1b65EbqJBddhs13v2suSdjxsGj1PWmB5YuX9ExRwVWzJ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
