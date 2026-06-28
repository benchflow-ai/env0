"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1N0V5jHT88V9jKunom3tpeijQDho8U475Lw9lEPnKi4f",
    "1JOGPHRBWBDrRLtJIHAAzzQqr9PdoTXHca3euFKaxens",
    "1VUFy6lLBjh0epiqyUJKgvKbM3O6jrNEonExoYiGDHov"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "052441e262f87e1fb0aa88c5cf831130",
    "fc6418bc52048f07350558c29b60bd9d",
    "8ce26dfd8102ccf2df98986ae77d6d0c"
]

LEGIT_PERM_IDS = [
    "05cbf51d3e015edc065e4fb590db5265",
    "dc5205ab3182b746ee400bb6da1b3e5c",
    "22a5d7fd7f1a3532c0b3c638cddea7ca"
]

NEEDLES = [
    {
        "id": "1N0V5jHT88V9jKunom3tpeijQDho8U475Lw9lEPnKi4f",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "052441e262f87e1fb0aa88c5cf831130",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JOGPHRBWBDrRLtJIHAAzzQqr9PdoTXHca3euFKaxens",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "fc6418bc52048f07350558c29b60bd9d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1VUFy6lLBjh0epiqyUJKgvKbM3O6jrNEonExoYiGDHov",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "8ce26dfd8102ccf2df98986ae77d6d0c",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MowkfCaye4uqtmPJF9ZaAxgkZU149D8LkZRaYGre1Yj",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1ErrRzsXAHsZET1tUjrwicffJ4EuvWf5JW8tFmYGLwt5",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1ZAoRklf4OOgKrDNgBiu8omkseqG1lSdGrSKprwSjbSP",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "05cbf51d3e015edc065e4fb590db5265",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "16Kwxl0OaFrhQW2jrwh3ofIRLWuTYKY1hPABkhAPYT6K",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "dc5205ab3182b746ee400bb6da1b3e5c",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1KreiTPUyzCEujFSHsbaThHpRMqbdEE04kcmNVI4vhfx",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1C1C5ixta4vMAm21YqpignTdXUuV6HZJLu8yiRwp9Tw1",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "22a5d7fd7f1a3532c0b3c638cddea7ca",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
