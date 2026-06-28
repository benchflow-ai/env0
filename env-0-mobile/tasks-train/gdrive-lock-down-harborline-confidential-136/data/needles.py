"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1jO6IAVNVoLNSegPOqrL3lljlzYR7RLHPYqU9O4qpkAK",
    "1bN5HduAenVEdvmUmAzynoZRVXn6OVEBw7EarwKE3ri5",
    "1gN8C2MlfGAAOMnrZdM2OxSSzPgMTi4CZpVWXrOBamuH",
    "1j0t1mAGMK2LgZmf3ZrlPmVMSAZm4zGa3XkTnpTtleKl"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "3c8bd8b9fe1fdb33a3093519263a7155",
    "1a8ae31a83b7c4d3e6fdece9001e641c",
    "ba295dae56dd9d0c1fe705ccbaed37ad",
    "db47b68e3da409a73d3fe625409ea4a7"
]

LEGIT_PERM_IDS = [
    "0477e80144fc3988827006efea774364",
    "55089bd445de72a29f7b4ece2ac2b7a1",
    "1183c96ce5f1c77af56c1a28e9ba9327"
]

NEEDLES = [
    {
        "id": "1jO6IAVNVoLNSegPOqrL3lljlzYR7RLHPYqU9O4qpkAK",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "3c8bd8b9fe1fdb33a3093519263a7155",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1bN5HduAenVEdvmUmAzynoZRVXn6OVEBw7EarwKE3ri5",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1a8ae31a83b7c4d3e6fdece9001e641c",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1gN8C2MlfGAAOMnrZdM2OxSSzPgMTi4CZpVWXrOBamuH",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "ba295dae56dd9d0c1fe705ccbaed37ad",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1j0t1mAGMK2LgZmf3ZrlPmVMSAZm4zGa3XkTnpTtleKl",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "db47b68e3da409a73d3fe625409ea4a7",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1SNblujsRszKMpK0KLbuXzNxXwRYXEFTdcg9ilSTERpM",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0477e80144fc3988827006efea774364",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1NfTTmm8bCOgVUtKTKCOpPGJQem7Z1Y5RtIKkgm8G8XF",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1298IyocCC3Q8W8dZNH2BIAl96O9Sjakg6ETWurMXWiy",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "55089bd445de72a29f7b4ece2ac2b7a1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1X0W38ert6ACPyCFG2JxHT8Q2quCY7VtUOqcKA1IFpHY",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1pEbdR4IXe8oMgwP6yqnUns4Yn3He7eQF0d7hiiTNVXm",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1mExcrkpU7SYuLtFW7suyoPTuJ6sO0f52ygnjg2PWQiZ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "1183c96ce5f1c77af56c1a28e9ba9327",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
