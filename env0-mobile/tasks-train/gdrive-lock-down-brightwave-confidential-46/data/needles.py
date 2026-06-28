"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1517JjbEP01GICiyOe9KFKCaG5gGlXDQItXkor4vbXp0",
    "190XPWIPvF1cxJgwYirLCK1hfMRlTkZjWISJQEA0oqZG",
    "1WuqJgKNc3Rqo8YWwVc244t31mYRyLFrIBREXKNFLUWd",
    "1x5FoMepZ6WTc47HBXtbtIiFzDYHBrRmTVgUtfDjtDRH",
    "1aGKN6CXzC3hAjMVJ0zLiqet3IaXg0LwznZ5A9hFaxt9"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "48a489f2a7b4d9dcb07a1d47bb2f8a3c",
    "26a2c468222880c0829a3754cade24f5",
    "8e51a9c9757ac4bda8ed5381a9b02f38",
    "e4ff709ccb58768409b4e6eca094c1fb",
    "6b113ee350d71d0d3656f642641cf9e2"
]

LEGIT_PERM_IDS = [
    "7b5aa4f7edaa845c5f6664afd6cc49c0",
    "f0428c1361dbb659494abdc8dc6cbba5",
    "c19920ff14e3e10644b2326d9993905a"
]

NEEDLES = [
    {
        "id": "1517JjbEP01GICiyOe9KFKCaG5gGlXDQItXkor4vbXp0",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "48a489f2a7b4d9dcb07a1d47bb2f8a3c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "190XPWIPvF1cxJgwYirLCK1hfMRlTkZjWISJQEA0oqZG",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "26a2c468222880c0829a3754cade24f5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1WuqJgKNc3Rqo8YWwVc244t31mYRyLFrIBREXKNFLUWd",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "8e51a9c9757ac4bda8ed5381a9b02f38",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1x5FoMepZ6WTc47HBXtbtIiFzDYHBrRmTVgUtfDjtDRH",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "e4ff709ccb58768409b4e6eca094c1fb",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1aGKN6CXzC3hAjMVJ0zLiqet3IaXg0LwznZ5A9hFaxt9",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6b113ee350d71d0d3656f642641cf9e2",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1bIqKem99h8tQdt9iCfwhtKqh7Sn0nxTIFGmiwlrM5Xt",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7b5aa4f7edaa845c5f6664afd6cc49c0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1cFJ1gX36pJzHccPGQPjRTwNxCqyUvbJAfdfcooyk4iA",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1lFOuUL8cFM4IoiGOGyuXGH5iRwqyBLp2vwpq1qaK8It",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f0428c1361dbb659494abdc8dc6cbba5",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "16kRt275ZhrgmkDY7Ilmpv97owoCg6kyhSSO0E9Njki7",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1VX5AI1HEOphMwxsz2lHd2aaCHLzD22x57Pm3vdLsZq8",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c19920ff14e3e10644b2326d9993905a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1q7XeOQgzvnQC8GC36oxIZ1dJ9LPZwdWcUIIA6dKxXfj",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
