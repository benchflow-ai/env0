"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1OnX5eqevM95pDtyEmTRRzHWFRwlgL1TLpLQKvO1HFlI",
    "1oGlv3aO0D3Zfd8lpfx8oAvzEWf9jLCyYjq9JLyuBgfk",
    "1QPz4qTUscPrUHeJJZ89E3eNTyFJdr24nDDZUcfw8NRX",
    "1zfymy8vDwOmGLFeeEBOKXsyDx9cYjhoT4FRyuo1aVjD",
    "1KS52RD6s86RuSss9Iek8npRU2tKIw8dKtFOwbKGRCGO"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "ae079e284b727b8e934afa54511fdbaf",
    "9d23eefa50aeaa72c33f6cf558cba5a8",
    "de6f91cc12dcd5b2c99d86984196ba00",
    "2b3bee4627c6094298cad37eaca0c3f8",
    "00141c675ce7b2f577518ed429c446db"
]

LEGIT_PERM_IDS = [
    "7069c0ca59c789f93481f7658f962057",
    "4873ade53242f4e0608d6e466ef6d61b",
    "c7c300291885fcb1640f54672d701845"
]

NEEDLES = [
    {
        "id": "1OnX5eqevM95pDtyEmTRRzHWFRwlgL1TLpLQKvO1HFlI",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "ae079e284b727b8e934afa54511fdbaf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1oGlv3aO0D3Zfd8lpfx8oAvzEWf9jLCyYjq9JLyuBgfk",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "9d23eefa50aeaa72c33f6cf558cba5a8",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1QPz4qTUscPrUHeJJZ89E3eNTyFJdr24nDDZUcfw8NRX",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "de6f91cc12dcd5b2c99d86984196ba00",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1zfymy8vDwOmGLFeeEBOKXsyDx9cYjhoT4FRyuo1aVjD",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "2b3bee4627c6094298cad37eaca0c3f8",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1KS52RD6s86RuSss9Iek8npRU2tKIw8dKtFOwbKGRCGO",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "00141c675ce7b2f577518ed429c446db",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1FbxBFqe6DGxzj0ZS0j8wEJswUuVc4EZ5OHXRQJ1eWyp",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "188sXMcIpqslbpwHTacJFMaPgmLbgTPQeJ36ScDTdn23",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7069c0ca59c789f93481f7658f962057",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "17uCfd2ZYHESCHulI9KKlmrXaeemMTg9TUT0n6zAAaoR",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "4873ade53242f4e0608d6e466ef6d61b",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "15K8zp7zzqGrnjO7e4DeWnfFRjF3tzJgXqXQPmQfVEnH",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1r7ho5OQ0cgYNpXbBtuDPXDwrY4eG9nAtPTqU5qzEpGV",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1AiXQ4J8qOJRWluJIdsccbB7Z412kywTuGl5cm5wHZ2o",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c7c300291885fcb1640f54672d701845",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
