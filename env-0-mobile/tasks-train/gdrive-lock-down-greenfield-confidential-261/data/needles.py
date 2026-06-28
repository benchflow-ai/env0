"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1Js7nIoXPTaDUduaErWadxZX2f3clzaIH5eym3uM5vA3",
    "1O3LPz2UmF9A378JMB7g0fNwikRO0WqRogeEDnYoHyOU",
    "1INkD8RxWvHbSoT5XYZZ3tcHZLU0ZOa8NdsYry3tvGK9",
    "1bXsnkIOiXJPZRMhX7eKRAGSGGDTpKbsxPpZHXGVUHAr",
    "1Qdgbjk3524IvEVIDjQkhQXnsBthufqAoCG7wZI724bN"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "6c0c31190be672534ede4429e85e32be",
    "c706aac5d160261b112ca45cbc732af3",
    "2a85eb8eb4c38559f345514baae2ca61",
    "9715c7becb756a815966b8336a7eff1d",
    "19bfc24aac8d32dee0a1342486ec94a3"
]

LEGIT_PERM_IDS = [
    "7cef33d0972d77d286c027b7385a6f37"
]

NEEDLES = [
    {
        "id": "1Js7nIoXPTaDUduaErWadxZX2f3clzaIH5eym3uM5vA3",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "6c0c31190be672534ede4429e85e32be",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1O3LPz2UmF9A378JMB7g0fNwikRO0WqRogeEDnYoHyOU",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c706aac5d160261b112ca45cbc732af3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1INkD8RxWvHbSoT5XYZZ3tcHZLU0ZOa8NdsYry3tvGK9",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "2a85eb8eb4c38559f345514baae2ca61",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bXsnkIOiXJPZRMhX7eKRAGSGGDTpKbsxPpZHXGVUHAr",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "9715c7becb756a815966b8336a7eff1d",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1Qdgbjk3524IvEVIDjQkhQXnsBthufqAoCG7wZI724bN",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "19bfc24aac8d32dee0a1342486ec94a3",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ahPHkODaVqnXwCAlDKQDr20sDhCQjU1ANhtYgcbYeEW",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1EUmK3r1RDT5fA5kvkKp5O7tMMUIYfA4EeSyOD1kKpWv",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1iAU9x3MAEqhzv6Ci6pNsm85kr5b0jdimcKvZvvgpOJA",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7cef33d0972d77d286c027b7385a6f37",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1KILdCDv5hYdtjSLfajtxntvkJtv0OyVJAkY77kJx9Un",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1kIK1JCY547kxbErkUkDsllydFsn4NIxA1RHJu3DL1p9",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
