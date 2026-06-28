"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1lZzEYzsYMtKO7jjNGX33rvMArC0IXvmNpISblCg15WV",
    "1YjFsugCpHVscTV5VErbMybhbJ1dSsvOb4yswhqZLaKk",
    "1yeViHLJ6Fc1Hbvrx3hUYANUVWHjvajqyLaeIf1lupBl",
    "1QGP9W23UAkyVOgPztQQm2T91oArABhnLVTEKj8re8D6"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "32c35920175e9a927293bcf2c452edf6",
    "aca4d79d2283800d08b5d57df36aa942",
    "8a53c03a44417a70ed7884633bde47f9",
    "c43c8ae038de9e4d7fd5dbbe1c18ad8b"
]

LEGIT_PERM_IDS = [
    "437e063c111d911036e252b3cc96d61c",
    "142362574057099f5af004f01980a5fe",
    "b825425fe529e8c2831cc23f8b34de15"
]

NEEDLES = [
    {
        "id": "1lZzEYzsYMtKO7jjNGX33rvMArC0IXvmNpISblCg15WV",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "32c35920175e9a927293bcf2c452edf6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1YjFsugCpHVscTV5VErbMybhbJ1dSsvOb4yswhqZLaKk",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "aca4d79d2283800d08b5d57df36aa942",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1yeViHLJ6Fc1Hbvrx3hUYANUVWHjvajqyLaeIf1lupBl",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "8a53c03a44417a70ed7884633bde47f9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QGP9W23UAkyVOgPztQQm2T91oArABhnLVTEKj8re8D6",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c43c8ae038de9e4d7fd5dbbe1c18ad8b",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1rSB2IzF5PjrK69SoC13wuvR0fEnjTCi0uiZxl0LtkrU",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1sjeeab7vWR4P6ZqLRTTl8dqwaLvEYQRYC0MV28OgSON",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "437e063c111d911036e252b3cc96d61c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fVySlmfRQOHBxHSIWjrhG9phWFQH9zscfgRDvHuk0I9",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1FCa0IU7kb1VSZAhttaBk8aFtA9lf7kKmSukY5jmQcxe",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "142362574057099f5af004f01980a5fe",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1C97LECO9JjSejFi4FZ0zObkeeEAzu1JcTBtw7sl1keg",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1D3I1pUDLweD5T4kjvaUixYUgI38rl7wXMI4sVwFnBTQ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b825425fe529e8c2831cc23f8b34de15",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
