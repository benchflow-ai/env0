"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "17oMv95hmWMqS59VrfOMAMli6u7cxE9x2WSP6UDQ3zpy",
    "1PsvhSkoAL0A9gwiTgwmzfp4maEzCAuhr0Ys27oBGNfD",
    "1e81IQclFrapqeJP9VR9iXbXqQKSxPIkUPIvQqY8f4nD"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "daa683c9c96e7fec66a86b70bd47dc45",
    "cf10d6408d920c24f784fdea5d7c383c",
    "b3389d459341baaf9cc2cf679d44d0d6"
]

LEGIT_PERM_IDS = [
    "25808908dc88ba6c8e84808c18bb7965",
    "03c1ec0ef29142e26f18c6230f98f3ab",
    "058521dcd8904cd2f24d63093221f89c"
]

NEEDLES = [
    {
        "id": "17oMv95hmWMqS59VrfOMAMli6u7cxE9x2WSP6UDQ3zpy",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "daa683c9c96e7fec66a86b70bd47dc45",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1PsvhSkoAL0A9gwiTgwmzfp4maEzCAuhr0Ys27oBGNfD",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "cf10d6408d920c24f784fdea5d7c383c",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1e81IQclFrapqeJP9VR9iXbXqQKSxPIkUPIvQqY8f4nD",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "b3389d459341baaf9cc2cf679d44d0d6",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1D1zDWelytGM5Lv16KXQoIk8UkiLw0fglCZG1Uu9z7Ss",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "25808908dc88ba6c8e84808c18bb7965",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "10xYgqZW7sQdiGn9lpQGtMeSS6kb6UBY3BpWin7XoZyx",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1nyaoTcIWIENxaiUerG6gSX12HyXh4X6ApIPZPKl5etd",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1sDMv7PgW8QzZkeonVre51EQ0BoDQbaJvsuvAtm64Sm9",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "03c1ec0ef29142e26f18c6230f98f3ab",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1lXc1RVLpiLxP65ghfu7fqH2WKuePbDbclV2DHipx603",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1VATyfPeoJJWt3bEhBsgGcb9ONjrYY9PCOjYEFNv560p",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "058521dcd8904cd2f24d63093221f89c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
