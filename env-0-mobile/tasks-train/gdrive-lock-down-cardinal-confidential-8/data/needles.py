"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1YBL8B9XPB2x1WSdENmJb9IHW3hPnVNUUw9yyhdwMr6r",
    "1ehu6dGkVvPxpRWkh8TPcspjWYEMLALP9rVA9Irc3MTF",
    "1ZfMA0ogh1luK6uaZYC1EBoj7rW4YL2Fnkh2CceKsDEi",
    "1wYJX7A66A07msxFjV0ZUBG8c41WnJMmdICTPi0bxvTD",
    "1PTVzcoMxpKA4MbSUxoaQYCom9nav0YlylRCj8DR6PYc"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "6b34cbc64133c12d025af71ff2d38c21",
    "ee11bd6b4d1f9c85e1e96ca202d4749b",
    "cb64ef286f5471361507f5b3535f2d4e",
    "25367c2a548290c737f9e3b2c3c0acc0",
    "883785085ccdba6ba503e2456555f287"
]

LEGIT_PERM_IDS = [
    "97b302e8ef42706e57dd5717a5d30c2a",
    "65edc7e76243480ec47991951ef0402d"
]

NEEDLES = [
    {
        "id": "1YBL8B9XPB2x1WSdENmJb9IHW3hPnVNUUw9yyhdwMr6r",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "6b34cbc64133c12d025af71ff2d38c21",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ehu6dGkVvPxpRWkh8TPcspjWYEMLALP9rVA9Irc3MTF",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "ee11bd6b4d1f9c85e1e96ca202d4749b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ZfMA0ogh1luK6uaZYC1EBoj7rW4YL2Fnkh2CceKsDEi",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "cb64ef286f5471361507f5b3535f2d4e",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1wYJX7A66A07msxFjV0ZUBG8c41WnJMmdICTPi0bxvTD",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "25367c2a548290c737f9e3b2c3c0acc0",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1PTVzcoMxpKA4MbSUxoaQYCom9nav0YlylRCj8DR6PYc",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "883785085ccdba6ba503e2456555f287",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1r3opOqlIK5I5kN7SFSYjE2XVDYrkOxDkN4UKZygJ79K",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1nTuQhblRg5riwkevSHbQqbsDb7oBcjbZTTVShcSFzul",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "97b302e8ef42706e57dd5717a5d30c2a",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1PVRUUGOsbgf7KRRKZTy7qtc28E5j8aup30nvEsae2Mk",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "65edc7e76243480ec47991951ef0402d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1h5qaPMknHatAWH6M9FdVYDOjA4tJ0P1zbQSeEbfWyS2",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
