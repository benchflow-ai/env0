"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1EefPvBPPEVr1ivr8rpCB4myX0D1ANbNXxQlTSra48CL",
    "13qkodD9mAVLsORb04OqjECPIbZG0OGdHLaspfaHnsWA",
    "1QUtLKGCl37ukzLQVOe6xxc3uP5UauS3raT7pI6LOxc7"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "bbf8a990c77110ba5fc4070a247daf16",
    "b5ca557e9f1d86e647b0e196a64536ef",
    "cc01ec686869f4f0d6e6d9da7182c5b3"
]

LEGIT_PERM_IDS = [
    "fef0470dd2993eaad98391e921f3d1fe",
    "613a99d64cbd452cb07df67a19c2ba32",
    "813bbe1ae220b1551938856205a1e2be"
]

NEEDLES = [
    {
        "id": "1EefPvBPPEVr1ivr8rpCB4myX0D1ANbNXxQlTSra48CL",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "bbf8a990c77110ba5fc4070a247daf16",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "13qkodD9mAVLsORb04OqjECPIbZG0OGdHLaspfaHnsWA",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "b5ca557e9f1d86e647b0e196a64536ef",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QUtLKGCl37ukzLQVOe6xxc3uP5UauS3raT7pI6LOxc7",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "cc01ec686869f4f0d6e6d9da7182c5b3",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1RV2NGG4h7QgR1NU1ZgkpwuOJSHDOXH9uMiMAC2obZgD",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "fef0470dd2993eaad98391e921f3d1fe",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1QSiRYHEzeZUiFE4OyA1aXbBSyZPG9dr7ESuexLmRvJo",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1vX64hatjDQukabGHmiyNNsVzWOYeBBS8nW06snhmexK",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "613a99d64cbd452cb07df67a19c2ba32",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "17QpC7AbUDvZ17Oyp2oaOkrxLr1XuvqORLzogsB4Kfy9",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "813bbe1ae220b1551938856205a1e2be",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1N3gKYaMASZYEaii5LFvtL01kNrHqijtG7FfnCVQTJA4",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1Ezu4Nu5azNK64qurfrjHzB2k8o0oxWRc9HuNnZKFIjA",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
