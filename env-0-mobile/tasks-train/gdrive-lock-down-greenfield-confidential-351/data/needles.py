"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1it241GxgldmFlild9X0oXrpnJtRZTJCeq3ivGTz5ya9",
    "1tciZP3A6u8bJGeLDizgpf1rIneWHi67HUnC3dMMjpRu",
    "13n7ut8RGnhdL82sc8GEYAbvzBzQhomqY2j0kfJyvaJo",
    "1mtUZLf124xdxVFHx26nFv1b7iPVCiPQKQdODQqAheQc",
    "1Kroem6r5B99KP7CBZjKche5dQUr0ios6htXd0CwRWkl"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "3d34bd72fed6bc0ed1a95b43a8d3db41",
    "dc1c45ab371e7ecc0f680531f8761c0a",
    "6669ad56d14862cfdd8e9ece895fdf6a",
    "3a3efe5e2e61228f6f6925d88fb38c83",
    "872e9a4d9ea320fe23edbbd22d379ed2"
]

LEGIT_PERM_IDS = [
    "19a4123a9cb92cc2f35e71ed82bf2c09",
    "359aa850ef451eae84fc824c34a0b4f1"
]

NEEDLES = [
    {
        "id": "1it241GxgldmFlild9X0oXrpnJtRZTJCeq3ivGTz5ya9",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "3d34bd72fed6bc0ed1a95b43a8d3db41",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tciZP3A6u8bJGeLDizgpf1rIneWHi67HUnC3dMMjpRu",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "dc1c45ab371e7ecc0f680531f8761c0a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13n7ut8RGnhdL82sc8GEYAbvzBzQhomqY2j0kfJyvaJo",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "6669ad56d14862cfdd8e9ece895fdf6a",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1mtUZLf124xdxVFHx26nFv1b7iPVCiPQKQdODQqAheQc",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3a3efe5e2e61228f6f6925d88fb38c83",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1Kroem6r5B99KP7CBZjKche5dQUr0ios6htXd0CwRWkl",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "872e9a4d9ea320fe23edbbd22d379ed2",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1gweJkah55CJbphMpHOj3SCnyqFXvGb45f0U9DVLJNKU",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "19a4123a9cb92cc2f35e71ed82bf2c09",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1p31oWG27ORKFX8JrwC7HrW5hP4lRRCz0yMrK5JzW86U",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1Glet12d83ub65VbcvcGxyyxWFn8jxTPC0QvLk0u3rus",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "359aa850ef451eae84fc824c34a0b4f1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1p8A6V2KRQSPkxUNEqI8YnvKRUGClcQQx1aNHrib3hzO",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
