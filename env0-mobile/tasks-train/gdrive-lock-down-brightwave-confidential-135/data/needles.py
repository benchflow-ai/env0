"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1GpR7ywvKu8Nthiuyk1VmlLxMHE2Q4nHIXoZxcZ77tIJ",
    "1miv3Buqi0uMpyr32JakUIEfFlfDfa6wxhyas0BebnCp",
    "1EAs4jejYIR8Pe91oPO1zEkScgr8xDSnMhIQKXbcItV3",
    "1a3zM8jLEORRtJ30ry0OrWbVO4aZijcdmx6mypYSK2e8",
    "1F1U2xKOCliLwLQm1mexMT7N3yekC0bDsGGdVyFtNJhh"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "16bd53116798176c435c4771be702262",
    "dc98a07fdf9f14f40de311355845df83",
    "33d77cf86620fa8627b3060ece4fe3ff",
    "480a667d934e69f26c12ee654f78aebf",
    "281969ef9ab6ad6fc71118af58667854"
]

LEGIT_PERM_IDS = [
    "c2ae7695f63c9d73cad01f144d5a3e43",
    "eee0455972124ae803191f5723a6fa13"
]

NEEDLES = [
    {
        "id": "1GpR7ywvKu8Nthiuyk1VmlLxMHE2Q4nHIXoZxcZ77tIJ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "16bd53116798176c435c4771be702262",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1miv3Buqi0uMpyr32JakUIEfFlfDfa6wxhyas0BebnCp",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "dc98a07fdf9f14f40de311355845df83",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1EAs4jejYIR8Pe91oPO1zEkScgr8xDSnMhIQKXbcItV3",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "33d77cf86620fa8627b3060ece4fe3ff",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1a3zM8jLEORRtJ30ry0OrWbVO4aZijcdmx6mypYSK2e8",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "480a667d934e69f26c12ee654f78aebf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1F1U2xKOCliLwLQm1mexMT7N3yekC0bDsGGdVyFtNJhh",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "281969ef9ab6ad6fc71118af58667854",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1kEm8H2tuSb6F3kP95eJPV3os2HfaZjBnywwNHBAxs65",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c2ae7695f63c9d73cad01f144d5a3e43",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1rurt5f8yS8UYZMLGGjNVujlnEXnWLUjo3Mbw0sRG7A8",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "eee0455972124ae803191f5723a6fa13",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "18iXQAP1x8NVLGb6dTFNfv70ltt0FDSewfskgvwbItQ6",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1Pdbz372id8oPiZc7exOSlm2gt3EBNBHoDNsutMdvM5s",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1DUPVzvS2qhVrVnt3cALeBmCZscRYOqI4ZZwDGNg9caZ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
