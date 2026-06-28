"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1jk3tfKOv191nTdYsWKwEycsOtxKid99wpylNAXkQCx1",
    "1gNoBYXfHE8lLwEWXoo30UTKupklC4o3wxZPVbTkOnau",
    "1rpVpXLBbTCEAyZvh5VXZuVEdD1NQUH2Yj5bzJ1lgD7d"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "d81a1a405d2dc97ea383e0684a7ca973",
    "efe90990efcfd310d54cdf3657218c24",
    "4c0f308bede4234b2141074e82ca514c"
]

LEGIT_PERM_IDS = [
    "02ee3703c7574cf11d63338d85839a5f",
    "07d028b914844027cc4fd8d75697d394",
    "688612b71a9ec1545f19feb67b61c16b"
]

NEEDLES = [
    {
        "id": "1jk3tfKOv191nTdYsWKwEycsOtxKid99wpylNAXkQCx1",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "d81a1a405d2dc97ea383e0684a7ca973",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gNoBYXfHE8lLwEWXoo30UTKupklC4o3wxZPVbTkOnau",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "efe90990efcfd310d54cdf3657218c24",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1rpVpXLBbTCEAyZvh5VXZuVEdD1NQUH2Yj5bzJ1lgD7d",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "4c0f308bede4234b2141074e82ca514c",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ntvEdms8hCktv50SUWfcuLGS5AIExuA3MkqzUxJfNHO",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1N688IkpYhxI4aW4SK5zdgiiHdv7Efs5M82k88RXMhXc",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "02ee3703c7574cf11d63338d85839a5f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1oowkLRMoeUBeNwLp0FMonbhn7hxrzFYN9tHfouojKf8",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "07d028b914844027cc4fd8d75697d394",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1t7iKHtwhundim42qbPHoD2ANNuAZW1JKR70IKXYB9Nn",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1r2eY9uhaWlosjy6e75NortF0PVatZzAta2W6nPK70tY",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "688612b71a9ec1545f19feb67b61c16b",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1XnsVtgkBMsqdUL7e2MpSWMlTV3W3omBgISgKUWSFVrS",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
