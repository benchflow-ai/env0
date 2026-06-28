"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1WDrVkhBYClkqoBdcVelP6WGM7gLEcC0neaDHEIbEIYp",
    "1ov5XXYdT8kL3BQ3xpnOqRnCQplAaYA8EBE8yqbIM5i6",
    "1ET4ianJZL8hhqNixBfkckqWr8eS0Kbf2Jvqzu8vd0Wy"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "69d01129df721aa972c4ff67410ee747",
    "ed590deafb25129c55cfee56369903eb",
    "46ad3cb9186178aa97e7d338433b33af"
]

LEGIT_PERM_IDS = [
    "7314227c86ce13cc5b09999e42339b96"
]

NEEDLES = [
    {
        "id": "1WDrVkhBYClkqoBdcVelP6WGM7gLEcC0neaDHEIbEIYp",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "69d01129df721aa972c4ff67410ee747",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1ov5XXYdT8kL3BQ3xpnOqRnCQplAaYA8EBE8yqbIM5i6",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ed590deafb25129c55cfee56369903eb",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1ET4ianJZL8hhqNixBfkckqWr8eS0Kbf2Jvqzu8vd0Wy",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "46ad3cb9186178aa97e7d338433b33af",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1UmaRDuCIZBhU8vQXJlTzwxcemnBDa76Ykygm92edclB",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7314227c86ce13cc5b09999e42339b96",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1Nz5q1EpritMzmzhy72foMAn7Iq3SFtHXIy7CSJ5J4KO",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1eDvgPS7qscLlTvgrklHzG47C1Os1xNjizO2bsPgSloe",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1W822ZWefmk0j2JdOF5heOe1qlfGRpidimTWuaLN7g0v",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
