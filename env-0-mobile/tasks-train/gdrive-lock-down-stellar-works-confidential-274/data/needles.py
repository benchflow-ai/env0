"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1cCnKmkADwoNPHvtNhCDWVFxc74K3rzMmw0RJRHO5E8a",
    "197HlIsfkw6q8rQYsJxQPxJDHp2UpDFOvKnuIC6TtKj3",
    "1NkpZvuqW92scrIjudiY8HUCMTPAIZQEcclxJ8EOhlG5",
    "1hxpEquK0kLuY8qA71Aewr8RfvtJtaQYwqJwu8cI6q5T"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "1f69a24459ee391f756a0e41aeb9a44a",
    "486a8798a9faf4a94e4ea2da7d974228",
    "f476dec5720a57f26c9f862013cdb8c8",
    "52262a362966e1169ddd04ffbba0e631"
]

LEGIT_PERM_IDS = [
    "6ded43248c4d7c2009685bdd9c715a58",
    "714bdccf2186b01178bf4ba7022f0ccc"
]

NEEDLES = [
    {
        "id": "1cCnKmkADwoNPHvtNhCDWVFxc74K3rzMmw0RJRHO5E8a",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "1f69a24459ee391f756a0e41aeb9a44a",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "197HlIsfkw6q8rQYsJxQPxJDHp2UpDFOvKnuIC6TtKj3",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "486a8798a9faf4a94e4ea2da7d974228",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1NkpZvuqW92scrIjudiY8HUCMTPAIZQEcclxJ8EOhlG5",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f476dec5720a57f26c9f862013cdb8c8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1hxpEquK0kLuY8qA71Aewr8RfvtJtaQYwqJwu8cI6q5T",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "52262a362966e1169ddd04ffbba0e631",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1R1msi1mC1r7EqecePC0k2oYDfOwEYAq9tqIVE7uXF4J",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1jzXnc1ZHlJuZFzPmwjlIA0UtvZZbk7dFe7IpwP1LXfx",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "19NNVIdUje8jtVmDzLlrqUlO028Smt5gpq31kC6qbPh4",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1GeFUZRSYHFCa9DVDQ2paL0UEjCy7B3UYVrFTBnk11Az",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "17Dx5rb9i2pirE4tKJv5HqIzyypgvcBtKy1gjMZehmzx",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6ded43248c4d7c2009685bdd9c715a58",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1iKeAWctGAswwnmsFX62ffwsnXcfQ71tRoQm9sjHoGW2",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "714bdccf2186b01178bf4ba7022f0ccc",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
