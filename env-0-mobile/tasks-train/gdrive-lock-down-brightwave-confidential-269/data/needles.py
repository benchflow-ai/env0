"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1SyM1oUfihK4pnzkZlInJ3f0pDlex39GJEsKMTnrG7xe",
    "1gqkbBS4xoFvo0vsr0WmkOPQD6xdHGV8bMftSW6XNPL3",
    "1ahE7wdJP1ocMJl3ZhGmcoeuxGyzEqtuPUvzSIK8s1AX",
    "11aOkJsx3BgE3IeGvccyJld3DSmHxWqDu6YrzE88sfdD",
    "1osnOgLok13QztewIlDnbZAQmnr9UUZOobAqrgtVwPRm"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "926d50b7bfd55b8ac0ae6e4448fd95e7",
    "4feb4dcff8eb436ac2038ab8d8343154",
    "ecd19c7d608e4e20792bf963e3d68e29",
    "96fcf4093e3b53d41239d91e9cef6f8b",
    "ebe2ba3423f9d609cb26cd5ff604ac92"
]

LEGIT_PERM_IDS = [
    "c51e7bb0b55a81a31eb19d3a17fd57a9",
    "275f7d6b24f26b85a652a302e18d3ac9",
    "5ac4174a4456c28ece89f0f255f479db"
]

NEEDLES = [
    {
        "id": "1SyM1oUfihK4pnzkZlInJ3f0pDlex39GJEsKMTnrG7xe",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "926d50b7bfd55b8ac0ae6e4448fd95e7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gqkbBS4xoFvo0vsr0WmkOPQD6xdHGV8bMftSW6XNPL3",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "4feb4dcff8eb436ac2038ab8d8343154",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ahE7wdJP1ocMJl3ZhGmcoeuxGyzEqtuPUvzSIK8s1AX",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ecd19c7d608e4e20792bf963e3d68e29",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "11aOkJsx3BgE3IeGvccyJld3DSmHxWqDu6YrzE88sfdD",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "96fcf4093e3b53d41239d91e9cef6f8b",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1osnOgLok13QztewIlDnbZAQmnr9UUZOobAqrgtVwPRm",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "ebe2ba3423f9d609cb26cd5ff604ac92",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1mpekwRzPSDMeVPvEG9lvjrUi4KwCZrVsspeENgcNixp",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1C9gf6H7wGXL2FG9MpDDBw6hYKH08ZwBG1I5KlQpnX7r",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c51e7bb0b55a81a31eb19d3a17fd57a9",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "112loS8aEyzNepXjPKAfXlPRH64yf2Q8RHwbTjuTsNFC",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "275f7d6b24f26b85a652a302e18d3ac9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1MuuxtUN7XEUBSe8K7ucnYFeCjHS5E4LOtTv6mxzS1JC",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "17d3NbLmOSNCXjlVqAsheWkq0ssMIZWdzagj52sLDWe5",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1mySdxBhRZ8A3uK0LaQBTctGd9q0noTZjHy5ot0qNuPD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "5ac4174a4456c28ece89f0f255f479db",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
