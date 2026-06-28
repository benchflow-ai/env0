"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1jFjTSEjz1i6yDpnAG1fpisUlGWwmLSlTbaXipircFgQ",
    "1cYkZV8HuOBDLwi2uglg8Q7FjMQt0eOxg65CCrTXU7N8",
    "1MdQJ2solz9LqJjtVGqCFoeolfmzk5arMqfgFfaCqZYM",
    "1F8iv4skBmRg6NJjJzOfNR4yqEEAOa4hvmvKqS1QBRHr"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "7cb9004d8f66010719cffdeb3b2cedab",
    "d2b2cd946681b4e59278c4455b6ec440",
    "c94707b1c70c521d8209e32412e13633",
    "587de399a1391c690e677cc1080ac277"
]

LEGIT_PERM_IDS = [
    "d16e43ee9f43e7dfb857e57660daefc2",
    "c9bbf6142f1ff45bba72a4fc6a58e833"
]

NEEDLES = [
    {
        "id": "1jFjTSEjz1i6yDpnAG1fpisUlGWwmLSlTbaXipircFgQ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7cb9004d8f66010719cffdeb3b2cedab",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cYkZV8HuOBDLwi2uglg8Q7FjMQt0eOxg65CCrTXU7N8",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "d2b2cd946681b4e59278c4455b6ec440",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1MdQJ2solz9LqJjtVGqCFoeolfmzk5arMqfgFfaCqZYM",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "c94707b1c70c521d8209e32412e13633",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1F8iv4skBmRg6NJjJzOfNR4yqEEAOa4hvmvKqS1QBRHr",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "587de399a1391c690e677cc1080ac277",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ST2S1t8MPxAAAeAtBWusgk8LNrFGT7CfIZlV5ep8AGK",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d16e43ee9f43e7dfb857e57660daefc2",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1wBrV9pbiR0GeRtx2oPQAzjC1X7OCHdNo6KYyqU3FpdP",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c9bbf6142f1ff45bba72a4fc6a58e833",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1a5ULJbwhIaGhqXZiYegl6fuVmhY05quAP9Mf0885ERR",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1VQsad3nDmr3Hs6EVEAeAiy1nZDrgRSh1hOaZyYZ8CR0",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1ePsesZ0YXmNlXFo8hpcqFRmrOWsb3NJHgDUd0VCgTaM",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
