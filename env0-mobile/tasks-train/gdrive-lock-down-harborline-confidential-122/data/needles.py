"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1Ng6iVIaKzI6YTEkF6rbucJXCZT27ubu0Z2mEN7v6jf2",
    "1tr0jAJ9li8TE5lABZjXdMrTTkg2dcbIUiTl6YrtU79o",
    "1mxQI55yCtmg1CSaYcrrLg0Z9OxTPYkzzbw07ngfvtf9"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "9654ef631eee73e0c012eab5e95530bf",
    "1c57c0d5287a3222ba456ebc1fc516a0",
    "72d45ad5fcfb143d5abb10158ff3f9e4"
]

LEGIT_PERM_IDS = [
    "49741db67785e780dd9ef71d699421d6",
    "b521b43b86e2ac070858db63bb42020c",
    "85e4cc8c513c413ecef4aa6e0a3d3ed1"
]

NEEDLES = [
    {
        "id": "1Ng6iVIaKzI6YTEkF6rbucJXCZT27ubu0Z2mEN7v6jf2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "9654ef631eee73e0c012eab5e95530bf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tr0jAJ9li8TE5lABZjXdMrTTkg2dcbIUiTl6YrtU79o",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1c57c0d5287a3222ba456ebc1fc516a0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1mxQI55yCtmg1CSaYcrrLg0Z9OxTPYkzzbw07ngfvtf9",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "72d45ad5fcfb143d5abb10158ff3f9e4",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1EibOqvw8ILntLrplFYy9oA17kPOHF2dobAVLCQwLRjh",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "49741db67785e780dd9ef71d699421d6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1MpRuW4kXpHVBCHqKqGHaTpNAKBX2g9DsBg0K1lo5IBK",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1Hw0Hlz08WheSNuSx8LmdkIwNgalGSoodJUp4aZapNPP",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b521b43b86e2ac070858db63bb42020c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1d0jAFuIlljonD1vz7HW7xCerQtMFMe6WTmnuz7oF1Kt",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "85e4cc8c513c413ecef4aa6e0a3d3ed1",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1yzAyFZ6wrOmusFfPuC4qmfSNlXzWrJ7clxa8wfktjxi",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
