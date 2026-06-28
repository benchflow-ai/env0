"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1iqbEoxf3FpH9cWNK3rs1LODh0GOT5hatU4e2NE9YBHD",
    "1EmqLmyiiz6Q0ouxlczbMnMLEkTTyTn6zfnPXzj1DvGN",
    "1lp6rDqnZFUWC7UxIyo7sASlmSJnstmd1rAKztraLEL3",
    "1apKr7flT3JSRRdJ6Wj1soukUOTJMtQhAlUrCxaGb74T"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "3cb93c6b86786595fe31c8e2e1947fa8",
    "49ed8f5b74c5c0d682513a68337a0c16",
    "626b715383f6bd9ccfb2adac40544013",
    "806aa7b8835d2a2d8facc15bd0a9c857"
]

LEGIT_PERM_IDS = [
    "26c8b8b997b9a33d231ff0c6243b2f89",
    "08268bac84e4a599ed00690784888fea"
]

NEEDLES = [
    {
        "id": "1iqbEoxf3FpH9cWNK3rs1LODh0GOT5hatU4e2NE9YBHD",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3cb93c6b86786595fe31c8e2e1947fa8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1EmqLmyiiz6Q0ouxlczbMnMLEkTTyTn6zfnPXzj1DvGN",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "49ed8f5b74c5c0d682513a68337a0c16",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1lp6rDqnZFUWC7UxIyo7sASlmSJnstmd1rAKztraLEL3",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "626b715383f6bd9ccfb2adac40544013",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1apKr7flT3JSRRdJ6Wj1soukUOTJMtQhAlUrCxaGb74T",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "806aa7b8835d2a2d8facc15bd0a9c857",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1uVR8cO4VUdBfR2AsltW3mIB96wnJkNLYFtfljNKU9wx",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1L9Woll2UlCl3VaaF2X5QDFWz08BZGOQWDfoJXtNcWUJ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "26c8b8b997b9a33d231ff0c6243b2f89",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1yGl6NQRD5TTJHIsgPKe0vKfdnKLDdl11ffN3sIxNB9Q",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1wFYGH8MdaknB4JIne230TNzNJ57p3Hy6kComxGvaH9G",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1FTuQr2hvoJr6NQqZUBNKS3Y9y4D2h0LQ1sbNyI97nmY",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "08268bac84e4a599ed00690784888fea",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
