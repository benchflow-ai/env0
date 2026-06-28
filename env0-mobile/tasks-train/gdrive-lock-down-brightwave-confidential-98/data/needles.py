"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "15eQHnx7LkK2NG6l6TP5C9FIrg4MJnK490rj9TnvUKoC",
    "1dhM1dRyIuAGjTLyfhybB4a2ReUSurYU43qpKCIdQxCV",
    "1yqfDZum9wp3jy2EDX1M3SgSRC3JR9IfHlkIiwMI1IuG",
    "1IPSzYgjI5usVC6zkYw3pXP3Bl6Eo3k3sV71YmTE2ZNy"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "b7661ba1c58254e10131fa4cf0e4d1ca",
    "8abf9b9c9daff7ab802c057a37bac562",
    "80bd28979c921ca9d9c941d5105a67ec",
    "42e72dd2f305584f10214f99a3c4f01c"
]

LEGIT_PERM_IDS = [
    "cc2e2507a83be4eba544e69fc6719c89",
    "48457eff82fecdf0c71c1a859969d1cc"
]

NEEDLES = [
    {
        "id": "15eQHnx7LkK2NG6l6TP5C9FIrg4MJnK490rj9TnvUKoC",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "b7661ba1c58254e10131fa4cf0e4d1ca",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1dhM1dRyIuAGjTLyfhybB4a2ReUSurYU43qpKCIdQxCV",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "8abf9b9c9daff7ab802c057a37bac562",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1yqfDZum9wp3jy2EDX1M3SgSRC3JR9IfHlkIiwMI1IuG",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "80bd28979c921ca9d9c941d5105a67ec",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1IPSzYgjI5usVC6zkYw3pXP3Bl6Eo3k3sV71YmTE2ZNy",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "42e72dd2f305584f10214f99a3c4f01c",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1oFSjUb5TLYq5m2KE1Rs7FLGxS7cNOw8HgvMHckWYPLx",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "cc2e2507a83be4eba544e69fc6719c89",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1pQwF1izBcvCBIEFsamVUU9pB8qMr2rvoVvJbUyxXNfy",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "48457eff82fecdf0c71c1a859969d1cc",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1ZBt9nTEamKwWXCqFoybw687xJXN1yPdz3PlUAWXX9Ap",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1qDUBhzh8DbLZFsidkfdwm5JbouVeYXv11dkJZo90iiu",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1hZ0FJrCPvEvYoaW2tmKimgIs9zGj9CaF8XZ3rAf240o",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
