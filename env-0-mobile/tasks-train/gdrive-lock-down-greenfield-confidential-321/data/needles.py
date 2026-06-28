"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1CzdGavhUjpDzU2nG4zfyRYKQdk0s5bguk3Le08NRWO9",
    "1650Mbt4fqUnzVDx9mJ0wx4qD3RrO4dbBLNXnXZVh7sX",
    "15N3whTsLCkBJawqDrcjQvfAQBlZxyOQFBa13BGO8a99",
    "10Vgwh6ZaHxgJ7tyOmOgQ9EI6LZS3UV5YR8L4wVb8BR1"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "0df9c0c1e849061351b1f6f2d9fa7154",
    "79ec1d7a8dafca1f2888b538b19eac76",
    "f76a21f43393c2f879ecc51c3b04de16",
    "0a0b326e4c7d802fa34a0bfb80eeab4c"
]

LEGIT_PERM_IDS = [
    "e1a80934974496bde5f24a317f1429a4",
    "f2bf91c52e2a304f05a153e9e0885a49",
    "0e7a166f4ebf9ac74cdf19af764a1666"
]

NEEDLES = [
    {
        "id": "1CzdGavhUjpDzU2nG4zfyRYKQdk0s5bguk3Le08NRWO9",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "0df9c0c1e849061351b1f6f2d9fa7154",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1650Mbt4fqUnzVDx9mJ0wx4qD3RrO4dbBLNXnXZVh7sX",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "79ec1d7a8dafca1f2888b538b19eac76",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15N3whTsLCkBJawqDrcjQvfAQBlZxyOQFBa13BGO8a99",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "f76a21f43393c2f879ecc51c3b04de16",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "10Vgwh6ZaHxgJ7tyOmOgQ9EI6LZS3UV5YR8L4wVb8BR1",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "0a0b326e4c7d802fa34a0bfb80eeab4c",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "16ufAT5V5QsWRyOAZkRQkQu0olvchVWnP6HEfZaRvtwc",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e1a80934974496bde5f24a317f1429a4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ktlq0AV9m9AuIaAx8E0K0lmW3vEjJYDZurkj3WB4T9O",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f2bf91c52e2a304f05a153e9e0885a49",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1K0jEJkXgfdCowEpVgzEqarUaz4BvbvzAtIvDX2TfaVL",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1BwVvui3ZVnQ13V47pNsKQU6BaxbFwrgBjuoodd4nbIC",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "0e7a166f4ebf9ac74cdf19af764a1666",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1T76QBar3hBDZrH0OV8MbAPG60rC9wvMq7Dwb56yQjQJ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
