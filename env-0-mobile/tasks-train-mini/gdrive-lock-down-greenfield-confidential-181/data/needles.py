"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1EyLRCO5VCUwNMykKJwJ78SHLD6wT2nDUVY5vW7JPDus",
    "1KqCZR1Bu09h5z347OElzOCt0oNIpB12RgjIU1weBB6P",
    "1DT0krlJUeDbNBsboAuDHw0MHhfCEu7xMJtofGrWnkd5",
    "1FCPVT52TEBbXsEM0a8bFGlYEhPSso4C5EAmm632PdQd"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "662fa7bf708415b5e22d19c982d23ca2",
    "3400eae959f822968c441fb0c14166be",
    "a2b31e6a268779cef09f1018ef69bdf9",
    "2af39f99f69e758dc7b01962f2059934"
]

LEGIT_PERM_IDS = [
    "75430b6481a74f43510d3cdd2ae74f79",
    "07b7bac7fc54dc50bd72a211851ce846",
    "9161f43efa8a16a3d284c325104d84f4"
]

NEEDLES = [
    {
        "id": "1EyLRCO5VCUwNMykKJwJ78SHLD6wT2nDUVY5vW7JPDus",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "662fa7bf708415b5e22d19c982d23ca2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1KqCZR1Bu09h5z347OElzOCt0oNIpB12RgjIU1weBB6P",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3400eae959f822968c441fb0c14166be",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1DT0krlJUeDbNBsboAuDHw0MHhfCEu7xMJtofGrWnkd5",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "a2b31e6a268779cef09f1018ef69bdf9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FCPVT52TEBbXsEM0a8bFGlYEhPSso4C5EAmm632PdQd",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "2af39f99f69e758dc7b01962f2059934",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1y9Y8mmtrRub1Bw3QRAspZ0yeRFjQbVkzGPs0mHNnMFk",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1Lbq1yDl7a1rRHEPJQg5X4mGuHNAjclUkA1rhE2f2Opt",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "75430b6481a74f43510d3cdd2ae74f79",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1h1kNZnPvPRRyEV2GjG7jyRog4i7tNKlUgMQaf3dDkc0",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1jv3IAMvEIe1X1smdkqBnj1Akw2JcuwUq3ki1Bc6CeOI",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "07b7bac7fc54dc50bd72a211851ce846",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1BnLU7rzprdATAGNFrIiZy5VsRIxvotJj3tE2kvL2rgZ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "9161f43efa8a16a3d284c325104d84f4",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
