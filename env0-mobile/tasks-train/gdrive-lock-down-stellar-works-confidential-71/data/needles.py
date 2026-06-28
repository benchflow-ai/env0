"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1wVUfuCtyOXRKqSvIbQ2BqxJmzJVSLam7bGMqGuQT5ay",
    "1xe3NQcKAzuWixQNedo4cjpLKhlgN2srd3Ux9w8NcnNW",
    "1Q2E7Fdq9xi4e89YnwwhnroVUSXdeYcslIILeeaIKq6w",
    "1k5KcoZ2EEp2YrbUZrSnlNUcilFyoKuxjscGdUxyq3xG"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "17fa4e133b182ea97d2d92b5fc80e9c9",
    "78f6bdb42ae0392cfa9d61d4d5e0d07d",
    "92dcffefacc1d774bfe05f6376612e4a",
    "22853dd6bc1150adfbb1d3a2069265b7"
]

LEGIT_PERM_IDS = [
    "8465e1ac5c9324a16a17b325257ba3f0",
    "58bfd84b79ae46c859ff21665118de22",
    "58abfabf3efa6d024f48e40899fb0e83"
]

NEEDLES = [
    {
        "id": "1wVUfuCtyOXRKqSvIbQ2BqxJmzJVSLam7bGMqGuQT5ay",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "17fa4e133b182ea97d2d92b5fc80e9c9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xe3NQcKAzuWixQNedo4cjpLKhlgN2srd3Ux9w8NcnNW",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "78f6bdb42ae0392cfa9d61d4d5e0d07d",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Q2E7Fdq9xi4e89YnwwhnroVUSXdeYcslIILeeaIKq6w",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "92dcffefacc1d774bfe05f6376612e4a",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1k5KcoZ2EEp2YrbUZrSnlNUcilFyoKuxjscGdUxyq3xG",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "22853dd6bc1150adfbb1d3a2069265b7",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1DdCSx3e7UZqFfIPp4c5eyWuEVptHTUv1l3pzimIMCqM",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "8465e1ac5c9324a16a17b325257ba3f0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1rTPYnJLQjJCkvkglelCBiJfMVfPCxn1396PmE5yKara",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "58bfd84b79ae46c859ff21665118de22",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1rKCeBAYi1m8YaXHiEKMmY33r1fPQNNErP5On7rq4ZMG",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1mZzcSrTIkq2tdlTNgfcP1PgvAw65FagwauFIiphAuK4",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1v3w5vfBtAiwwno5nnaOODO5bGGKQsnOFmLO2n69AAYO",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "58abfabf3efa6d024f48e40899fb0e83",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1jqXu48a2nUdqz3KfQU7WtgfIeyfqYo8ingHJTjuISGe",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
