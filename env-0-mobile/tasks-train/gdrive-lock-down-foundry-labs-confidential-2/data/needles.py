"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1GCC297IOgZf4dZn7GF5JBLeVZoQErVV1pk9xCS50QDe",
    "19s4PwuooNSLNTpzPwL1Mv7pJcGzs7CgCWIqPzaKf8xi",
    "1iY3ZgjEZcXOjjKAi7nSfwNgRfbHFuZgWJxJ9hsbD5aw",
    "11ZDuxTFOqfra4XHs6VJXhvTT5etLHuqhVbsmwNPv3bm",
    "1QMkdpq4PVvI1cOMq04CD1A4SuOMioY1mWSFo5qos0aK"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "229115195224e05c3dd7b13c5585cfe7",
    "f41d5cf57e0b9982f83767b489e4cbb7",
    "dc944632e1ff5e5fc41100df0e2cb356",
    "f28b8c5b1aa90f42820bfb25b6d4a2db",
    "339537c7a49889ce5d520e7ab5677959"
]

LEGIT_PERM_IDS = [
    "66e567a549a044320818441aa781299d",
    "33e391a0d57fc8d476765bff83fe8b5c"
]

NEEDLES = [
    {
        "id": "1GCC297IOgZf4dZn7GF5JBLeVZoQErVV1pk9xCS50QDe",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "229115195224e05c3dd7b13c5585cfe7",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "19s4PwuooNSLNTpzPwL1Mv7pJcGzs7CgCWIqPzaKf8xi",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "f41d5cf57e0b9982f83767b489e4cbb7",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1iY3ZgjEZcXOjjKAi7nSfwNgRfbHFuZgWJxJ9hsbD5aw",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "dc944632e1ff5e5fc41100df0e2cb356",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "11ZDuxTFOqfra4XHs6VJXhvTT5etLHuqhVbsmwNPv3bm",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "f28b8c5b1aa90f42820bfb25b6d4a2db",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1QMkdpq4PVvI1cOMq04CD1A4SuOMioY1mWSFo5qos0aK",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "339537c7a49889ce5d520e7ab5677959",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1odbvcBP7fA8QkPRpx7jleXIztGTKedBqHgzqC1LCUg9",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "66e567a549a044320818441aa781299d",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "10f8oYnvVgb6JwkbxgvoKckjI7QI356vvrJtbr3hwC69",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1TvfxENqfVp4sC0dwRPlLC3gjUZ2QwaOaw2ua0pUoawf",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1Blv4wYGpdjTwSaObrZemvzXff3eCgefT749aI0HYeb1",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1bbqM5xNaLeIPS9AAR1n1yYENSxl25WG844ABD6bW0yV",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "33e391a0d57fc8d476765bff83fe8b5c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1eFw9vblRNxohyhn78UzJescnYHBq5TZqiTPbTcEXoVo",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
