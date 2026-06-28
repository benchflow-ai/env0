"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "11vX8AXv0Bm8oAO3IDWAmlfjpveoZ1Hg91gAlEZSw5sb",
    "16S06O8V3yDljRTBDGJvyf4AUFdQeBn726AkJGdVbKyb",
    "1YjQ0ic3Q3FOP2ybuPTSDQkcHi49E5qaQym6ZFoKYhRz",
    "1Gmz4UtjJ4g5vm5spjoc7INkYlecjOOEPWSppQh8jqAX"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "a892b6138942d86b54cfaa3bcad1bf00",
    "ec481de6d6ad95b2001848b8a2c392f2",
    "da8e72c82e7d16ef750ef90a91749e57",
    "71d79c468ac2fa3f737e5fb0325a9114"
]

LEGIT_PERM_IDS = [
    "0f28c848ebeb18119ba1535500251359",
    "0dda7ca863df51c6f664be55ead56619"
]

NEEDLES = [
    {
        "id": "11vX8AXv0Bm8oAO3IDWAmlfjpveoZ1Hg91gAlEZSw5sb",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "a892b6138942d86b54cfaa3bcad1bf00",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "16S06O8V3yDljRTBDGJvyf4AUFdQeBn726AkJGdVbKyb",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "ec481de6d6ad95b2001848b8a2c392f2",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1YjQ0ic3Q3FOP2ybuPTSDQkcHi49E5qaQym6ZFoKYhRz",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "da8e72c82e7d16ef750ef90a91749e57",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Gmz4UtjJ4g5vm5spjoc7INkYlecjOOEPWSppQh8jqAX",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "71d79c468ac2fa3f737e5fb0325a9114",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1iZrVk0ON4ZgF55JbiCxKhJA4fM0wPBpNHWrDvBSb2uH",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1PxcmA7SXyobkdIdlGbzCNgRhh8pB5MwWROmRyejgKlV",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1SUNc5yD91esNNpG9WhAPeoPJ3mJJeaVVUiJE2fvK22u",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0f28c848ebeb18119ba1535500251359",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1kM0GjUUOSuuqaNRrxxgxofz371GE31Q64NnsMfDImaH",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0dda7ca863df51c6f664be55ead56619",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
