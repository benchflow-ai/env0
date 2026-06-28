"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1dKFXxiZhKwbEdUg202KjJEFBjcKUum7Oy8XU6GWNtgW",
    "1x28PyeO3deaF6vW2ped9PsU2Wj95EScuWVqYVNjc5sm",
    "1tdCLKA1s7RRxoHlgzj8EzqNtBsx3jOJuorMJEqQv628"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "4f91a3f7038e542cd5b2847f31263b77",
    "2e11e2d2e96432de52f2e68c40ca03b3",
    "b78a06dcf314a92a46957a9cbc09e503"
]

LEGIT_PERM_IDS = [
    "7d5176e1ac7be4cfca697ffa29075d80",
    "79ae867a7110802472f8e44437698a3c"
]

NEEDLES = [
    {
        "id": "1dKFXxiZhKwbEdUg202KjJEFBjcKUum7Oy8XU6GWNtgW",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "4f91a3f7038e542cd5b2847f31263b77",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1x28PyeO3deaF6vW2ped9PsU2Wj95EScuWVqYVNjc5sm",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "2e11e2d2e96432de52f2e68c40ca03b3",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1tdCLKA1s7RRxoHlgzj8EzqNtBsx3jOJuorMJEqQv628",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "b78a06dcf314a92a46957a9cbc09e503",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1nGrinzLlimbaCgK56WHsVG2mREOVyyjxm3fI5S6S98L",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7d5176e1ac7be4cfca697ffa29075d80",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1Z8K8Rua8CY9rYzcDpMCgbOC0Dcx6PtnIOxsOlfgYgjH",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "79ae867a7110802472f8e44437698a3c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1KkIsp0lzfvjObC7tkLjgzzlmJQJNTUYjnYYxys5vX4w",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "17vuFzntT0froMFIqWSi1Ug2GoqSPIy6H8I3EVsAtZ4x",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1ZXLzx66PlmTAkZF1f0sdXv4cjlTkGRZvtSUJRxvxATg",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
