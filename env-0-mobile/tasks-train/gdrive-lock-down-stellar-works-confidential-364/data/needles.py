"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1pPTUxZs0COLrFnjil9IqWRexuifg1sbfuQrpzBma4io",
    "1h7WRMjuwZPXkFsPqDfwoq8uBbfF4odS256x0Kl4rx1X",
    "1hI4XPbSgKoBpGwKh5yBeA9dqbuX5yqrsiVoVwyGKm3k"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "c74f8494245a74da231a84b0bbfb6608",
    "a9583697786579336fbadb56b05f6e1f",
    "45fbcf731863d02612b0ac5ef5824b60"
]

LEGIT_PERM_IDS = [
    "bf434806b3504fc4e84cb607e67d9fe7",
    "e5d2116fdd5a3a881988fd4716f9afcc"
]

NEEDLES = [
    {
        "id": "1pPTUxZs0COLrFnjil9IqWRexuifg1sbfuQrpzBma4io",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c74f8494245a74da231a84b0bbfb6608",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1h7WRMjuwZPXkFsPqDfwoq8uBbfF4odS256x0Kl4rx1X",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "a9583697786579336fbadb56b05f6e1f",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1hI4XPbSgKoBpGwKh5yBeA9dqbuX5yqrsiVoVwyGKm3k",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "45fbcf731863d02612b0ac5ef5824b60",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1AWayw0OSdYNE39aVDqtLLgROJyJF63zFbwlKRDsclEU",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "bf434806b3504fc4e84cb607e67d9fe7",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1mfNEZK3rkBJlLmxW5lhStFljIjIzUOFtIVnWwpPmAU0",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "18gOibxGVem3ymNmJAWgJ0ZpJKIpmFUyPz07vydyxC3o",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1TzUa2TcdVAMikW2RxrTGpgLHZousWuBAxeAicc0VgiL",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1UkqoLHoVOSQxJ4NJYq30mrDKUCos3gNavddAMoa0zIf",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1DAFlqszbm9YEe9DdT6yIkgWhaytRvtIYBnWQ3vbcw8r",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e5d2116fdd5a3a881988fd4716f9afcc",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
