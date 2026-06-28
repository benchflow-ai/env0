"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1mOawx7D14JL2B4wNoPM08rix14Yu61Ri2oHBVZYqby7",
    "1PULRajodJzwMR72bKVSd8KchW6br29DoCDbWu1j7O1j",
    "1JTtPQPqok7Jklnp0YB6W5uQGim7iA87YQtutHG8ZLt3",
    "1HXspaEAhKdQvLSIAQBICoZT8fhUjqbFOU0GtzP9teRb"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "c6529222e3e50bebfce5cebf403a3b1b",
    "730fd2dc76739923717cdfe3ea75bf61",
    "37f9b2330962e6b81917c0f170950202",
    "5d7adb7d4a074bb60e540893550b934f"
]

LEGIT_PERM_IDS = [
    "73fcd27aba2f0677678993d62a3b98ef",
    "31953faa8a43a4316a409c429650c3ea"
]

NEEDLES = [
    {
        "id": "1mOawx7D14JL2B4wNoPM08rix14Yu61Ri2oHBVZYqby7",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "c6529222e3e50bebfce5cebf403a3b1b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1PULRajodJzwMR72bKVSd8KchW6br29DoCDbWu1j7O1j",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "730fd2dc76739923717cdfe3ea75bf61",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JTtPQPqok7Jklnp0YB6W5uQGim7iA87YQtutHG8ZLt3",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "37f9b2330962e6b81917c0f170950202",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1HXspaEAhKdQvLSIAQBICoZT8fhUjqbFOU0GtzP9teRb",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "5d7adb7d4a074bb60e540893550b934f",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1SfQCkH2nPxLqSRXaI7qXVd8602vfykDsk1RJDNvivYZ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "73fcd27aba2f0677678993d62a3b98ef",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "10c98CcJyfx6l86G66e7GVndJqRBqPxtDcsEIeLHNBgf",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "13jtBllqaOYpJkgPFFPuJ3BFjcQavBiI8eAAqg7gnrLH",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "31953faa8a43a4316a409c429650c3ea",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1hhVV11ONsjmhcBPvE7lAvzRDoMZ5Rdw1hA5CJJb1k8L",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
