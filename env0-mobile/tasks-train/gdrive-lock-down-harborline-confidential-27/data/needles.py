"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "11MQ2Qn0sUM2vpZVZTntgKBWFWqW3OHlIDpUo9KbPTb1",
    "1BHwhScn3CN0dIbfqxVArmDKdcFghlwjGbNVmdxXpbl4",
    "16r1IL7Ri0Jz1vtO6CLREHH9Kbc3DN6pLy9FIgxgSIT6",
    "1JYI9Ufa0J39Hy4NdbRPKTd9AVV5ZmnoVZaxO0TWslE7"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "2ab6a81d544d65be4e9398d4715e89bc",
    "985ca4beb20bfc4a74f2d56a502ce33c",
    "a99ee4411348ec1f14f2aca71175d75f",
    "991074b8f1dd8299b5739a3172f334b6"
]

LEGIT_PERM_IDS = [
    "b3d5599aeccd9de09df81c3ee053504d",
    "ab87195bcade235a62f414a770d27c11",
    "9144ad7febbbc7609f1bb3eb0e0ac4c6"
]

NEEDLES = [
    {
        "id": "11MQ2Qn0sUM2vpZVZTntgKBWFWqW3OHlIDpUo9KbPTb1",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "2ab6a81d544d65be4e9398d4715e89bc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1BHwhScn3CN0dIbfqxVArmDKdcFghlwjGbNVmdxXpbl4",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "985ca4beb20bfc4a74f2d56a502ce33c",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "16r1IL7Ri0Jz1vtO6CLREHH9Kbc3DN6pLy9FIgxgSIT6",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "a99ee4411348ec1f14f2aca71175d75f",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1JYI9Ufa0J39Hy4NdbRPKTd9AVV5ZmnoVZaxO0TWslE7",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "991074b8f1dd8299b5739a3172f334b6",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1wGJrbmgIR96uscUNbfyz9oDq5itYimyPIwdR68nk1fr",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1MnGDwKuh7EsqFP1ze3Z5Vi87GRyyHp8oGIKn9K7fXwh",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1NAqa5LIT6xPdmyJMCz2WfpJ0iVXK0gLwDFjvZ7qOhjO",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b3d5599aeccd9de09df81c3ee053504d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Dw15m5DmnkD1UJZoF5k3OwEULRB0zftJsceB4DncT6w",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "ab87195bcade235a62f414a770d27c11",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1WBSbdjowRGd4TWvIqONDDVtQDua2xtvAqNjXxgbnljP",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1VlugWMAv5C4GBrmalAgSlVaFEwnlzdz3VAN7pKwZX4H",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9144ad7febbbc7609f1bb3eb0e0ac4c6",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
