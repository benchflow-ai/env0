"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1x60zynNTICzz2jO5cGwBOALYjiQvLSIh5MYldRE385R",
    "1LaFDVOcYGjwQA90x8tTmOUmycFvebTqqPODuTHDvW4X",
    "19vIuChSAlwZYnervtUp2g79Zp7DHAgQevESGSHk2QKQ",
    "12HIJgYwu2lgbtDyvfgD8KUYBORtJhma6N5aDtd4E1xL",
    "1kEMPo25ixEL9UqK8fiEd4zG26dtPziX2OhULx377ZYb"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "5033353c3d66856f378bd255d121667f",
    "fc3f3f1d45d521898225aef3230d2814",
    "6f3918c9412cb4016020d5d062e0ff1b",
    "47caccb9fcae65cde7a01f948eb8096d",
    "92b2602fcc50ebde749bcb8f97f1f938"
]

LEGIT_PERM_IDS = [
    "16168bd5dffbc43ab974e7706d370405"
]

NEEDLES = [
    {
        "id": "1x60zynNTICzz2jO5cGwBOALYjiQvLSIh5MYldRE385R",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "5033353c3d66856f378bd255d121667f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LaFDVOcYGjwQA90x8tTmOUmycFvebTqqPODuTHDvW4X",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "fc3f3f1d45d521898225aef3230d2814",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "19vIuChSAlwZYnervtUp2g79Zp7DHAgQevESGSHk2QKQ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "6f3918c9412cb4016020d5d062e0ff1b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12HIJgYwu2lgbtDyvfgD8KUYBORtJhma6N5aDtd4E1xL",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "47caccb9fcae65cde7a01f948eb8096d",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1kEMPo25ixEL9UqK8fiEd4zG26dtPziX2OhULx377ZYb",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "92b2602fcc50ebde749bcb8f97f1f938",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1SDoAUzD2JBHdw7Svl47wCHhqb4gFbHUes31ICYPHKf0",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1NHbzvDzPLWdUx5cv1nKngCKA4usWtlAxSJeD6ahVTCy",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1eVA4V0jvimrcldIvxEBcUhrpgWSVmctLwOM4ADtDAWH",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "16168bd5dffbc43ab974e7706d370405",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1xXq9H2rKNTlVR650ulveOiZCEmsaUlhGa1Yb5VyPkjo",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1wcOC3Xx5mYbg5WGG1zqOPVfacspI96AAQU35YY5qWqN",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
