"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1t1HTvTIePB2i7pYW2s710ShaFdIzM6Q3Z4efFTdAeLQ",
    "1nW5Y1UciigI77cE16jVTqpinbSPcCYXsym4Urlc1oWH",
    "1Vm0GhcleykRIgduDz5K6CMHIQf3nvzfTJ8i9sf4lqx2"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "0f6ac17581c1c7ba59cadb9b1a1dc1c3",
    "8f78128066eace624d909056b740826e",
    "51e2972bd9612b2b2a5bc2363c226514"
]

LEGIT_PERM_IDS = [
    "7b909ef752c58f6e809ba17ffc952063",
    "b2b2c89d74bc50f35eda21948d7a5257"
]

NEEDLES = [
    {
        "id": "1t1HTvTIePB2i7pYW2s710ShaFdIzM6Q3Z4efFTdAeLQ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "0f6ac17581c1c7ba59cadb9b1a1dc1c3",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1nW5Y1UciigI77cE16jVTqpinbSPcCYXsym4Urlc1oWH",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "8f78128066eace624d909056b740826e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Vm0GhcleykRIgduDz5K6CMHIQf3nvzfTJ8i9sf4lqx2",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "51e2972bd9612b2b2a5bc2363c226514",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1aIQMBQTByqNmJDu1jXuXWOAmCFPSi9IlGWDl1LodE7w",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7b909ef752c58f6e809ba17ffc952063",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1eJXYq7K8oyqWkpPw6knf2Urc7xwaUMAT5KC3N1Jy9h9",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1quyVHNYBzQSd0AhRxEMYj7NnTveBE02MSKPMUt2xHKg",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "11zgj6jtIfItFlLDp9Js3zl2HQKkLoQCHY4bJJIM2q3Y",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b2b2c89d74bc50f35eda21948d7a5257",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
