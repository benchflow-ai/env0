"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1gB9zs0GBSou02iaHpmBO8mzF0xWWpV8uhymt85iPzRP",
    "1dXDpfk1fdoNWbKRsDPxbJHEgeLthClnLlDYpVa9sBPs",
    "12QwJtmjSHwY62ZG45N82ubR9Q0s0CEBV9xY6jG4U6JD",
    "1NoKpt3rUh9w5ZKLH60ZpeM3vz3tUbuf594aSCfygQOc"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "265ed20917d90d3c83286f93c15d424c",
    "b21e52131c2ed6173b7c3d7d978ba013",
    "3cad2c8bee4a2017e75d33d789ab18bd",
    "49b005ed26af6a3749315cf90bb64323"
]

LEGIT_PERM_IDS = [
    "5fc0d05cdb2c5a30b7e74b5fc19dce62",
    "d9f48a0a68cf443a1db178e06ab5a10e"
]

NEEDLES = [
    {
        "id": "1gB9zs0GBSou02iaHpmBO8mzF0xWWpV8uhymt85iPzRP",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "265ed20917d90d3c83286f93c15d424c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1dXDpfk1fdoNWbKRsDPxbJHEgeLthClnLlDYpVa9sBPs",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b21e52131c2ed6173b7c3d7d978ba013",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12QwJtmjSHwY62ZG45N82ubR9Q0s0CEBV9xY6jG4U6JD",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "3cad2c8bee4a2017e75d33d789ab18bd",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NoKpt3rUh9w5ZKLH60ZpeM3vz3tUbuf594aSCfygQOc",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "49b005ed26af6a3749315cf90bb64323",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1gzvVlu4HxXVFAtpOCSf5ymOd40kHLPR8UoiHkjs5eA2",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "5fc0d05cdb2c5a30b7e74b5fc19dce62",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1HKJNEAyLvJr1ngpeu0c41h361WvxmxWLzowiUXdY6Pi",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "19sQ0Datm9q4LwOJBXFm6oH2ZzLRmM1Ul8Rjl5ym74n2",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1OjnEPYJapY1tX9E6QDUAhLBmbLvZsGRH6rkrgq3f3He",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "13xnpWN6hCfYSfOhEEShxc8wjdtdfISoTNutEtgjynFc",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "11G13DY1rYvkSnx6Uv2ETD6qyITN02ILX5ZHl5DRL9bL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d9f48a0a68cf443a1db178e06ab5a10e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
