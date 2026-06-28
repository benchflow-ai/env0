"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1dUXaSjUwKQlPARof6t5qWDc2LjXnSrimhmujW9jsufo",
    "1AvuqI9ZcNEyO2I6WNDO7PUXeJ2pPSq20OdH1y9F7C9q",
    "1Ha6cUzZ7gxXL1FI3sWgrfAeQDn78wqMSLo627Y88m1e",
    "187DFcvcsMx7oakjKO8aLW4t4hC06kZyuYnkEozqwOgC",
    "1djUSth6RJZrNDGFSKbVEs6j2gNsNVQInrbUoaPnyPHU"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "643bad73529fcc2e7f62f91d6b960dea",
    "ec72c844ad7c7c749e90b10716347d55",
    "67cf97a1bffc960d9668b68f8bf006aa",
    "fe21d69eaebf3f94f6cbb940330201e3",
    "51e6c1771c28bcd32fa6927ca198e9d0"
]

LEGIT_PERM_IDS = [
    "3217684523d8a9a4c1890ac22c413807",
    "c73ba459d4c33cc56543703b3a5b3a4f",
    "f86ddf06f669da0ba77be9ba9ec1978c"
]

NEEDLES = [
    {
        "id": "1dUXaSjUwKQlPARof6t5qWDc2LjXnSrimhmujW9jsufo",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "643bad73529fcc2e7f62f91d6b960dea",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1AvuqI9ZcNEyO2I6WNDO7PUXeJ2pPSq20OdH1y9F7C9q",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "ec72c844ad7c7c749e90b10716347d55",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Ha6cUzZ7gxXL1FI3sWgrfAeQDn78wqMSLo627Y88m1e",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "67cf97a1bffc960d9668b68f8bf006aa",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "187DFcvcsMx7oakjKO8aLW4t4hC06kZyuYnkEozqwOgC",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "fe21d69eaebf3f94f6cbb940330201e3",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1djUSth6RJZrNDGFSKbVEs6j2gNsNVQInrbUoaPnyPHU",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "51e6c1771c28bcd32fa6927ca198e9d0",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1AWrxU7VfVKzFZCQhWfdBICQVKe2IB0uMQuAReBpiMJe",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "3217684523d8a9a4c1890ac22c413807",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1t7l9F2mqZCqdN2TN1GQcKz7ne9cUWZoCUjxMhChzNsx",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c73ba459d4c33cc56543703b3a5b3a4f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1oOsBXHuPwLu0mtDZsYAJb5HWPqbLdYHq9KkYRXwhgUp",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1xRV0UXkdZ4leo8xnyw15D9sdHetT7iLWrXkPr4RD3ri",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f86ddf06f669da0ba77be9ba9ec1978c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
