"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1mgE8CqlvPHNAFRruaxFomlSLyZn6JWfg7l6Q2s83wmC",
    "1aHT92eIUuNZakWmbDRYwJRwlV17779z8u5uCpralEYl",
    "1G2K01iiouYRvSJYTm3OqC8thHpe1p7sFqLoSyP7EGFf",
    "1ln6j28NxBajHfSUCPC2B5k375UVpyY1mNticWNlqwwW"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "6ac4c28946a73ad7ec770c0776a67b69",
    "0253922a09528de08035a12e128d346b",
    "9c512ba5f6548ee690c91ac6943ddf1b",
    "704a13ba7022b79a9fe2e24036cd2c5f"
]

LEGIT_PERM_IDS = [
    "1ea1b02d78e0faa4ec2a0fc527d275fd",
    "45180178c6c75d81135cc310d15637dd",
    "0b3bed60a058ef68322e52a9a37d05e4"
]

NEEDLES = [
    {
        "id": "1mgE8CqlvPHNAFRruaxFomlSLyZn6JWfg7l6Q2s83wmC",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "6ac4c28946a73ad7ec770c0776a67b69",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1aHT92eIUuNZakWmbDRYwJRwlV17779z8u5uCpralEYl",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "0253922a09528de08035a12e128d346b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1G2K01iiouYRvSJYTm3OqC8thHpe1p7sFqLoSyP7EGFf",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "9c512ba5f6548ee690c91ac6943ddf1b",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1ln6j28NxBajHfSUCPC2B5k375UVpyY1mNticWNlqwwW",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "704a13ba7022b79a9fe2e24036cd2c5f",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1GLie3f6CGd09ox7DWhWUT3Fb9Og5RZVLu3tI6HtP3O6",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "1ea1b02d78e0faa4ec2a0fc527d275fd",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Myp68wzriBIjFSl0Yxmvitvt6VvSy6CSgOlRScYyVk6",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1mX6IPlj4Mwl9KqL7hIJt7uU7hokh8uvE0TbAvHwEsyb",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "45180178c6c75d81135cc310d15637dd",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1UwAufKIjKDaJK0Q2IW2PxmBqnBEf9chLc0WCpPf61LJ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1Pb6IboOTFqZDiLAOHSSB2PgeJpiUSNqlHK4AZmHurIX",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0b3bed60a058ef68322e52a9a37d05e4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
