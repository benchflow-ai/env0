"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "17O9SZsE89CJeOeO5yHRGcnb293Ok3NSII8TkFlpMCKk",
    "18D706eklOy1zkxbFIKMLv06ThkTsQlDHMBgKYkXz0N6",
    "15TPTcLdtOrEgk0A3WT0zrgfrzlbvInVmsebtaXxKf3R",
    "12Bt2QWET6BkzBTkLYFXOdQUT1hcaXrdjAfJzqmlLaZo"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "73585fae5cd14d9a0f022c3076af8bb2",
    "bf2dcc5a25f8d3ac41250f0b6a55b59a",
    "8af0751072abc95154cadae279336d6c",
    "17f2204cb6f603507ec92fcb0fc544c7"
]

LEGIT_PERM_IDS = [
    "23bc524ebf0e1a36fc689e98191656ee"
]

NEEDLES = [
    {
        "id": "17O9SZsE89CJeOeO5yHRGcnb293Ok3NSII8TkFlpMCKk",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "73585fae5cd14d9a0f022c3076af8bb2",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "18D706eklOy1zkxbFIKMLv06ThkTsQlDHMBgKYkXz0N6",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "bf2dcc5a25f8d3ac41250f0b6a55b59a",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "15TPTcLdtOrEgk0A3WT0zrgfrzlbvInVmsebtaXxKf3R",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "8af0751072abc95154cadae279336d6c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12Bt2QWET6BkzBTkLYFXOdQUT1hcaXrdjAfJzqmlLaZo",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "17f2204cb6f603507ec92fcb0fc544c7",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Y1ZwGVm6BcGzJA4CKhJr4MJ8cwgic7FRhrj1R2WB2qH",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1f0fjtFonFYFXBF50m3mL6OfjGoiVI9K20z1cSmgb63N",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1CJseHEQr8lPZqg93ABqCIEinPVjHITovT8NRZE4TPGC",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1FYKIvKNfurhNk4K1sTPrUOdDHDYrQi8302X3QA0NwdH",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "23bc524ebf0e1a36fc689e98191656ee",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1QBK4NjMvXKAaD5utRdirqO3vEpnOmgXA0Kfgf6h1u0k",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
