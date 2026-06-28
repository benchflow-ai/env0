"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1VY9819NHdBki1fO4lHrMNqR4k1hCRsLtyDVNp3mKSam",
    "1SgP0NAXj1BJ2otjAuc9gM1WOv10yPogzAbkbystaZ2q",
    "1WCkKPOZhls3i2fJhqjru9U2wOizmyEY2qHpKjRQdx3b",
    "1cfIZhtnfVZIlOELJmPs5BntI90VJcJbCHQL7eLylj1x",
    "1eOSXinm647sIKtmSdR9H2vUS5xmv5FbjpQrkkUtxpbn"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "4441c3df4869fe66004615c2cb82bc88",
    "0c7bbd504b87133a95776a28830a2b07",
    "1a17d95cfdfe7e4c16325e4bbbf2927f",
    "eed38655a4c2349e008c8fdec776ccbf",
    "f12555e674d955f34a319d92b7c7556f"
]

LEGIT_PERM_IDS = [
    "596c4387811332e53d3421e561a8e05f",
    "20e4e337445139474f9a3a8f8a1bac06",
    "300c2bb49503eb6c9fd660629fbcc7bf"
]

NEEDLES = [
    {
        "id": "1VY9819NHdBki1fO4lHrMNqR4k1hCRsLtyDVNp3mKSam",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "4441c3df4869fe66004615c2cb82bc88",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1SgP0NAXj1BJ2otjAuc9gM1WOv10yPogzAbkbystaZ2q",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "0c7bbd504b87133a95776a28830a2b07",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1WCkKPOZhls3i2fJhqjru9U2wOizmyEY2qHpKjRQdx3b",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "1a17d95cfdfe7e4c16325e4bbbf2927f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cfIZhtnfVZIlOELJmPs5BntI90VJcJbCHQL7eLylj1x",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "eed38655a4c2349e008c8fdec776ccbf",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1eOSXinm647sIKtmSdR9H2vUS5xmv5FbjpQrkkUtxpbn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f12555e674d955f34a319d92b7c7556f",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1R6dwQRAZFp1jffpF2WvLGVabE1vnSbKitKupD6wWcBp",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "596c4387811332e53d3421e561a8e05f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1w6eDyjME28B0UdaBOp0PwBdzF7rkgRTkzmeHfG4EGyw",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "20e4e337445139474f9a3a8f8a1bac06",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "11DM1cKy9XGDqreBA3JxPRg6RB32IccmMH1Cb4szu6Gg",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "300c2bb49503eb6c9fd660629fbcc7bf",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1EtStHM1t4GX7gxn4Taiw0EgAzORwC08M4ISwJJxRWeF",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
