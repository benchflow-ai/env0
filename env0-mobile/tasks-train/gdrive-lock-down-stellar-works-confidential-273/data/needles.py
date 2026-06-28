"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "10Rnwc6tGQsvC0R9j9TJkWyl9jTmIu2RlAXiROcmZXnr",
    "1qOiOuASbbsJ7QE7OQZtKv2q637yuLbZCdVeJCIqlDZP",
    "1GpbcNK7PVaunUaoM8YGZ0CcxekaV9rKiq4d8JydLO5H",
    "1oqFWsVANLt7SArTKpmeHXTASDL4poii4OAepaxOo6Qp"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "9d26b4d22ffea6af3d1e5a41da4258ed",
    "57d14a040f438e91086b677adc46caaf",
    "8e9b6ed359e009bf23a9dece2db60232",
    "794028ad28763c4a6d0e94c376724636"
]

LEGIT_PERM_IDS = [
    "76cf9103f22771bc087707362d0673a5",
    "6e883cc5bba93ae348e09ce00c9fbb2e"
]

NEEDLES = [
    {
        "id": "10Rnwc6tGQsvC0R9j9TJkWyl9jTmIu2RlAXiROcmZXnr",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "9d26b4d22ffea6af3d1e5a41da4258ed",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1qOiOuASbbsJ7QE7OQZtKv2q637yuLbZCdVeJCIqlDZP",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "57d14a040f438e91086b677adc46caaf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1GpbcNK7PVaunUaoM8YGZ0CcxekaV9rKiq4d8JydLO5H",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "8e9b6ed359e009bf23a9dece2db60232",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1oqFWsVANLt7SArTKpmeHXTASDL4poii4OAepaxOo6Qp",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "794028ad28763c4a6d0e94c376724636",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1CqoFBaD2kqRhS8xzd30kHx28kqOrmUBPilKzEu4FL9e",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1CUZPCOBanLh57rDBVFw60PzUAYIHirVFuULYxNIJHoC",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1tWbl4I9nuLuPBvaLwgYixluzz9jjM4GnSkEgrXiVr1r",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1UmYuMStFqyNb90vngElbBmKCCpawwoEpglSGgXgAwF9",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "76cf9103f22771bc087707362d0673a5",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1WMJZLPGbcyORH8FbSixwi55BsERoeZ2BnoYr7sLIwbf",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1gk7OhVrGMCKEwq33h3JOd5MXFcJiclDAlWL48p4pewV",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "6e883cc5bba93ae348e09ce00c9fbb2e",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
