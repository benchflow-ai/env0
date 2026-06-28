"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1dQB7zL4zRI1udmQybGXihCsLV6U3tO6PbOgxEvTFhqN",
    "1yqiBOLRtKJCK5pHuJmjqESGgfV0FQSYKIrKxAgfavMR",
    "1MHPhQeOS47bjKtR1tFp8QTH8IpDz5Tduj4PUH8SYQ4d"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "1d5a12a8b4094071112cd555c28471aa",
    "ee9a9eafd436e8e0aa443adae250b738",
    "bcddfeb594befa6095f92c61a31bfbdb"
]

LEGIT_PERM_IDS = [
    "6a119b5c0dc3e1ddc233840c9ce87856",
    "b511bd9bdd61447b85f0970a64131cf3",
    "342701cdf6d97f279e5e3ceb6d9b58dd"
]

NEEDLES = [
    {
        "id": "1dQB7zL4zRI1udmQybGXihCsLV6U3tO6PbOgxEvTFhqN",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "1d5a12a8b4094071112cd555c28471aa",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1yqiBOLRtKJCK5pHuJmjqESGgfV0FQSYKIrKxAgfavMR",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "ee9a9eafd436e8e0aa443adae250b738",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1MHPhQeOS47bjKtR1tFp8QTH8IpDz5Tduj4PUH8SYQ4d",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "bcddfeb594befa6095f92c61a31bfbdb",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1AFjMD3TtlldLC7EQZQndupS1ityHlx3wOgcv7qcA1pa",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6a119b5c0dc3e1ddc233840c9ce87856",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1liGMzp7frAKLbpsEhp3DXCZqPcwaDMFwWfKqDUk1GlJ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b511bd9bdd61447b85f0970a64131cf3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1QKMc0GlJosdHyA8PyaKzvPAXycQmDKR1zHQsJA8yOk9",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1mY3y1kirkziXrbd2NKkzC9IIU9IAmqdm668tlobtoiL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1WZW4sSp16p68ZveMFk2atWsKBF9FTYzm7KteZaA71Re",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1XZe3htFecXc0nDHsqljLQuGqMNhK1YNzmpyi79MoNOr",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "342701cdf6d97f279e5e3ceb6d9b58dd",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
