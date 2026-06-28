"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1WAxNCNgqn48Ntiz2nqsCC56vEURjMWUrf5dHrX6qs3e",
    "12BrBAvwUJE7kg9mPYIN8DvzC312JZvBzgbSD0YpxV4B",
    "1QFTXioyg3RxVJRzLfXNWvW64BUG82ZYrbuRzu0ELgP9"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "44d33ef1776b73debdd70bd6e1844997",
    "d6e158beffa405d10179a04bffce2264",
    "d2c9415918a706c6d570bbe56018eb6f"
]

LEGIT_PERM_IDS = [
    "56e33c781a9f9e78b7252a64ce32eada"
]

NEEDLES = [
    {
        "id": "1WAxNCNgqn48Ntiz2nqsCC56vEURjMWUrf5dHrX6qs3e",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "44d33ef1776b73debdd70bd6e1844997",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "12BrBAvwUJE7kg9mPYIN8DvzC312JZvBzgbSD0YpxV4B",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "d6e158beffa405d10179a04bffce2264",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1QFTXioyg3RxVJRzLfXNWvW64BUG82ZYrbuRzu0ELgP9",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "d2c9415918a706c6d570bbe56018eb6f",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1QPy6vLLdHyJhBQJrl3AemVXM6gR3hphok00H4KaG1Xv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "56e33c781a9f9e78b7252a64ce32eada",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1DVnf5nC6AaEG7roVoguxTLdx89xcXyColEmAg0GVeza",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1ny0w1ySqYYQXj4B8hvc9pVgxeWZSw4tTjBcGiqdGgCD",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1baEs3WKViSTKDq25DQXlK1cRp2jx6PKloZodwJSRXeN",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
