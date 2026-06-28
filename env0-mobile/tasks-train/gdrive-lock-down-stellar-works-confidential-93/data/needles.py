"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1yozUkwzvTxHBo2aDcPG5RDuTk9d3x2NjNnHwteYFBQQ",
    "1cvSnzaNOrtkDvKSMwcpGSC4kQuWzEt1j3lAr1fQfVcK",
    "1FlBa66zRnh79v1slIX1zLjSiydCjwP9uGWbjGW5Zpyc"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "17a61635e54fa9b32377400d0929c6e7",
    "a9d11ca74c94e7edfa03b495cefa638c",
    "4874ec0a44cbc052469944f99fb37885"
]

LEGIT_PERM_IDS = [
    "d586bb7c92f5808b3808f7da012afb42",
    "f35044d5e427fd7804ced6641a2aab31",
    "94b776bf0004e6e9dbc179197a179e1f"
]

NEEDLES = [
    {
        "id": "1yozUkwzvTxHBo2aDcPG5RDuTk9d3x2NjNnHwteYFBQQ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "17a61635e54fa9b32377400d0929c6e7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cvSnzaNOrtkDvKSMwcpGSC4kQuWzEt1j3lAr1fQfVcK",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a9d11ca74c94e7edfa03b495cefa638c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FlBa66zRnh79v1slIX1zLjSiydCjwP9uGWbjGW5Zpyc",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "4874ec0a44cbc052469944f99fb37885",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1NGDoNJyud1r3t7ADlOlU0JZ6UcivEqROPJNcPj1KqBM",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "d586bb7c92f5808b3808f7da012afb42",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1H5OmBGpKefFXc2EdBBAMEVFtWn96aj0rwCmbztcMj7S",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f35044d5e427fd7804ced6641a2aab31",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1zzcd6eY6P6GzVZgp0vJUOo13KVoJIGdRxS5YbEpKuKu",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1c4Pv5MIWRHhJBustHGZPFqbNYN0vK5s4HIyH6tWiXPb",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "94b776bf0004e6e9dbc179197a179e1f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1kutzir5OsAG9gwJ75N4AXAyH0BwuKnCjQE39Mnuyw5e",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
