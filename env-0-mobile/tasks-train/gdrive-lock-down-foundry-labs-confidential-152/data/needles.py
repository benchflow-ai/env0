"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1RsTrCmwx8iBUycMfRy7F41KFzHOPZssZtVIRxBAmATU",
    "1TKxMuoFcRyRvot8dD0y8jmTSn8LebL9fuuxOHQszaLS",
    "14tYsHvvYEu0e5BgU2ioOQZEpUYvQS4fa82uMibEOJYu",
    "1o9oCT2adUZ62U17ma5QR2D1yBOpR69312LVOYZFLY7n",
    "1UZiAQ5O1rkUBdXJ55Y3Tb4ZwmUjC9e7NjJ0LkBaeIXU"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "a1ca55d3a9f5453d7f3d52075253b399",
    "f3f4b1a301ff9385ea3f370fabecc261",
    "0476ff46f261716d5adf60db9cf56d08",
    "2fdaabb79e384e5e77710b9ce2452025",
    "6ecf51a9114348cdec08719f845e740a"
]

LEGIT_PERM_IDS = [
    "c3a8ab7c2b4a3b77bbbb8119b14caa42",
    "9028c6757a8e2e7af441f0188bd185ea"
]

NEEDLES = [
    {
        "id": "1RsTrCmwx8iBUycMfRy7F41KFzHOPZssZtVIRxBAmATU",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a1ca55d3a9f5453d7f3d52075253b399",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1TKxMuoFcRyRvot8dD0y8jmTSn8LebL9fuuxOHQszaLS",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f3f4b1a301ff9385ea3f370fabecc261",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "14tYsHvvYEu0e5BgU2ioOQZEpUYvQS4fa82uMibEOJYu",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0476ff46f261716d5adf60db9cf56d08",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1o9oCT2adUZ62U17ma5QR2D1yBOpR69312LVOYZFLY7n",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "2fdaabb79e384e5e77710b9ce2452025",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1UZiAQ5O1rkUBdXJ55Y3Tb4ZwmUjC9e7NjJ0LkBaeIXU",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "6ecf51a9114348cdec08719f845e740a",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ccJnzC7a8RTpZ1xxAKhtX8vU4bZIVo5gLZeGMf2I2Cs",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1tup1dXU5KMnoKgQ7FuR2xJxL914erSNGJ4kyv5oVJtI",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c3a8ab7c2b4a3b77bbbb8119b14caa42",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1Ehp4vWw4K9Z5tCDJHAThfMnPoINDsbc4TRDO7umcUsc",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "9028c6757a8e2e7af441f0188bd185ea",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1FgpIwnL9PaNI37mZOtZrm8yBzCKgLpsdEl2L8F5gBFp",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
