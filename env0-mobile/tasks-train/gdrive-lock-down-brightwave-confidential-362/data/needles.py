"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1ArWWDM9rcZLjwJ6iitiST8I24rEILf59rqKRWhOnFCP",
    "1EjqBto5pOhDkRI9reTxYohU54DPdcJjSEIfwg95X5MV",
    "1teaYMwOmJdGsvxwtHQtTY21MUVAJUxJGPruaVKwPo4p",
    "1w3aBjSPfHINcfNhkbaxvBc4IcPiYpOMks2SAFi4amTj",
    "1kENTQEopq3vpIhqDuOoBgdmaLKynWNseHNyUPvJIsRN"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "3d28a6fc03a00f182d3dfa481b16226f",
    "695655c5fafc6ca4a372d7b49d5e037f",
    "7490d6d74eb824cec1bee847be4b18f8",
    "2bb987e6cf9e834b81afd0c543ded9f6",
    "5d90b6e933f81c8cbd9625c828889cf4"
]

LEGIT_PERM_IDS = [
    "7173e673b16a8e01ee02053f37304b03",
    "2e19ece8b1483f521b49155c3713017a"
]

NEEDLES = [
    {
        "id": "1ArWWDM9rcZLjwJ6iitiST8I24rEILf59rqKRWhOnFCP",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "3d28a6fc03a00f182d3dfa481b16226f",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1EjqBto5pOhDkRI9reTxYohU54DPdcJjSEIfwg95X5MV",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "695655c5fafc6ca4a372d7b49d5e037f",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1teaYMwOmJdGsvxwtHQtTY21MUVAJUxJGPruaVKwPo4p",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "7490d6d74eb824cec1bee847be4b18f8",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1w3aBjSPfHINcfNhkbaxvBc4IcPiYpOMks2SAFi4amTj",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "2bb987e6cf9e834b81afd0c543ded9f6",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1kENTQEopq3vpIhqDuOoBgdmaLKynWNseHNyUPvJIsRN",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "5d90b6e933f81c8cbd9625c828889cf4",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YaP3uugv0uyWeSFUQNaPDzqG2BYLQxha6i8UoasuGG9",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "18mVGpHasfDIrU3Qhrr5a926mZhyeCNShSr3z1VW0tsU",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1rcTlm0qt21robH6WU25I1U9Hk2Es4JYRAJfKEMViwmK",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7173e673b16a8e01ee02053f37304b03",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1QPUgdntN2ZrPjA4wK2u5kfzELurZvyvnqZVKNkfHGOu",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "2e19ece8b1483f521b49155c3713017a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1JXHP273ff639QGtWpJF0Jnptf5G9tfpTs8gg5HaH558",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
