"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1QLNfuRezEsrJrgq3IyVtzyFZiE6jTifgqbdW0q3QZ2k",
    "1tWk2poVh1WdXthMHUJCjMtPsBJ8jji5wJZOapHD5NUd",
    "1PalfDrLIlGbN9ESheiT4MKoLoMoMOgEpIUSc1k10AbQ"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "149cd70d184ddb200620f8d426f6030a",
    "3e904458636f065842b93caf6eb0a816",
    "329939415d2a292a1f31aa607c9cedec"
]

LEGIT_PERM_IDS = [
    "3d03daeb1c8d5feb1efcc8568bd9b98a",
    "365fb3d1459a24de51a72c0d4921e003"
]

NEEDLES = [
    {
        "id": "1QLNfuRezEsrJrgq3IyVtzyFZiE6jTifgqbdW0q3QZ2k",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "149cd70d184ddb200620f8d426f6030a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tWk2poVh1WdXthMHUJCjMtPsBJ8jji5wJZOapHD5NUd",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3e904458636f065842b93caf6eb0a816",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1PalfDrLIlGbN9ESheiT4MKoLoMoMOgEpIUSc1k10AbQ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "329939415d2a292a1f31aa607c9cedec",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1tGDuzFAf7HAubGMI6dheh7KCXgSVFWyTurd63rL296R",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1RRyFkZLA7u31fd9cqN7dLaKu1QTubHUKWVJx6cQDT3p",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1g5YkWyWHbTXwUI2DmrvZPPE5bwldgmFCzujmyyvnq1x",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "16mJBRrhdhnxrspyIfyrF1aU7rPPmEXWVJfhSbHHgvDc",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "3d03daeb1c8d5feb1efcc8568bd9b98a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1nddujXMfV6cWQEChoJK2UCS2RWouJIHlLp3glZLu6sO",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "365fb3d1459a24de51a72c0d4921e003",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1t3GPJfdTjWUbIbRrOABz0AhyTPUp6MtyYaWbCsRQX82",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
