"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1aR8Z9dHpI84uwRcFoTY811hfY8fPgjPpKuDwfturgII",
    "1xQfx7ItmqupomIgavwCp5mZmykjoyhnuNkiGuRUpnH7",
    "1xagGqhPTiEfey8JHWrMyYIj9NvvAHCAZZisaY06UvA4"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "f588a7d4c9afafced8bdf4bda802aecc",
    "5f4053fd4611209d758f9cd694cd9092",
    "0b25ff5d53b5cad7343c90201e7a30b8"
]

LEGIT_PERM_IDS = [
    "a05dde2f70ad10a1a3fa8fd34f1d87e7",
    "2fdbcb2a03138c706ec1239bd3d9cf27",
    "650581df4e0daa946f937bae76e44e7a"
]

NEEDLES = [
    {
        "id": "1aR8Z9dHpI84uwRcFoTY811hfY8fPgjPpKuDwfturgII",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "f588a7d4c9afafced8bdf4bda802aecc",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1xQfx7ItmqupomIgavwCp5mZmykjoyhnuNkiGuRUpnH7",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "5f4053fd4611209d758f9cd694cd9092",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xagGqhPTiEfey8JHWrMyYIj9NvvAHCAZZisaY06UvA4",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "0b25ff5d53b5cad7343c90201e7a30b8",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1kGUF5hnkcSvVKLYjREyGseNMkERlOFljbfkdJXR5DYl",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1mRzmp3NwImaoJNTyJqUi7DiafpDx2kXXciw3zCLgyRV",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a05dde2f70ad10a1a3fa8fd34f1d87e7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1uMEiifEHctyjbKiuFclXIVn0AJd26qKdnxAOGbFAxSH",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1xnfZa1p3Z1MZA1JKONT9TgYvYFMN2LQcDbVZK8bO2FO",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1Jo4Xs6Syqxgw6bssokDwI0xbOusf8o2RDkG1KxVahgb",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "2fdbcb2a03138c706ec1239bd3d9cf27",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1IyoKt3KKWoaCIsJccS7PHWCJZ2jBE6vW6VhxWKOF1nh",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "650581df4e0daa946f937bae76e44e7a",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
