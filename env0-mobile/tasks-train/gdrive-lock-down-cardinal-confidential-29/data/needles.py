"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1EacBIegRhDkqVnzLdFX9rXS6Y4FdrZ6j4lFqVyAH9B0",
    "1kYcBOOxG9TX1XNamhpuJRvKhVjRYTvDwskJxKbAn6uz",
    "1OV0d7IX4Iit6Xa8S99GM98ynP0MDNjYyquo7H8cvjhM"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "358869087bca5b8b9483a790f0f16b5a",
    "73d1e8b7a97e58a8c7b128c7be5c4a6f",
    "7c189d9fe084c4329c33ddb7c0763a32"
]

LEGIT_PERM_IDS = [
    "ede70118472bcb32786346e307ded0b7",
    "f4a72a1cfb2ade13b0d15b5766ae821e",
    "19fe074dc078b1dacd09ff3512f7bd76"
]

NEEDLES = [
    {
        "id": "1EacBIegRhDkqVnzLdFX9rXS6Y4FdrZ6j4lFqVyAH9B0",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "358869087bca5b8b9483a790f0f16b5a",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1kYcBOOxG9TX1XNamhpuJRvKhVjRYTvDwskJxKbAn6uz",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "73d1e8b7a97e58a8c7b128c7be5c4a6f",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1OV0d7IX4Iit6Xa8S99GM98ynP0MDNjYyquo7H8cvjhM",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "7c189d9fe084c4329c33ddb7c0763a32",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1HwmX2EoPT4JdZKaG68am4ra1AmQiPJRtdAy4GGbFhwP",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "11TAobQjy1zdoOC40N9V5XjQApxmeb3VNCH6zQTvxxeQ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1srmOIMvotw4AMigFPmFwwMhDdqxwEFYT2jc8r84u5Dv",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ede70118472bcb32786346e307ded0b7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1wbKhBZlXmnGpWRL469uuNccZ28fktqp2SrBDDtqe3Bz",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f4a72a1cfb2ade13b0d15b5766ae821e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1R9QAz1gBYJPV5fRQA6F0KBrbDzRQ8KgcOqGh7sPNYR6",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "19fe074dc078b1dacd09ff3512f7bd76",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "16YvRk8uzMgPV9s5d9M5PVqktaMTP20uXcZIjGWYBTbU",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
