"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "17iGBem3NINal515IjvkipKFQdAs6EiH7imqVKgkuUkg",
    "15Uq38yEH4cyGhXkD7agt55IS1tmnFcUiS9E9zwHZqy8",
    "1dPFbOQ1c6inUvHs8Kcia7Qcko0PI9VhLRdD6Q7Jq1tu"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "e0a0b47afb409a466604220d3f1c2053",
    "8f7bcfb7fd6527cf090a2f3a54cf0e5c",
    "48fc5f16d68e964cffd70d3f822c6c62"
]

LEGIT_PERM_IDS = [
    "fe480121305bc5aa53336b47ec2bb210",
    "c7a9cac22214b2b00ef641e1d24258cb",
    "44d9d44d93015193f72f32a8e08ab914"
]

NEEDLES = [
    {
        "id": "17iGBem3NINal515IjvkipKFQdAs6EiH7imqVKgkuUkg",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "e0a0b47afb409a466604220d3f1c2053",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15Uq38yEH4cyGhXkD7agt55IS1tmnFcUiS9E9zwHZqy8",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "8f7bcfb7fd6527cf090a2f3a54cf0e5c",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1dPFbOQ1c6inUvHs8Kcia7Qcko0PI9VhLRdD6Q7Jq1tu",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "48fc5f16d68e964cffd70d3f822c6c62",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1VHxzyjhNF1Lol3B3ooBixYpteo77hBp1lyVlNZ3eOmF",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "18QgATN12qkByoaz2o9RKHinZIGqOnkhgHpwm036gjyR",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1YbMCgjhv6Fqe8wqRlDukUXvB0WTkdtevLUWrBcGi5Gq",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "fe480121305bc5aa53336b47ec2bb210",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1UnmflSgo9YwlkWlqBrejTyjxEoQG24PHCX4EWRfnJrp",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c7a9cac22214b2b00ef641e1d24258cb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1qiIb6QuS1nYJBMop7XVllPGVdL5mbSdUs35NhCAlz23",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "44d9d44d93015193f72f32a8e08ab914",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1qhd62lzAWwFGxGScWdTmNiwr8Ni1ezZYCvJyCZNxQJg",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
