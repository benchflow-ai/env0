"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1KHG84ErmfgX3VWSs5MRBb5pjIPXGcGCWmuSXmny88C3",
    "14BcGCBdtRqRAIYpT2jf1BqYy16MuNh0KBtijZMxeqeZ",
    "1wNDa4KVscZAsd0ReOo2weG2zd4Q5g0WYrlA42s9acwt",
    "1WHRDaqjOtnLMlJwJWaNYMoWF6I7TxT6Gezzo3WTDZTw",
    "13lvFNf0U9YSUqbAbjtzrZDq57KsKe1rwxaIbw4NGVe6"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "b7dc9166d7ae42721e58c1067cb829b9",
    "96f94560e56cf0f53325b2ca86695151",
    "c180d553755adda1362467dfc4bde2d5",
    "78d941831ea462ae170ced0ef15961c8",
    "55b0c786483bdbace780a2175474ec96"
]

LEGIT_PERM_IDS = [
    "a3114d6bda8b617b0dbc9b46f3e2aee6",
    "350f60a32f06a0e5262871074ff6178a"
]

NEEDLES = [
    {
        "id": "1KHG84ErmfgX3VWSs5MRBb5pjIPXGcGCWmuSXmny88C3",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "b7dc9166d7ae42721e58c1067cb829b9",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "14BcGCBdtRqRAIYpT2jf1BqYy16MuNh0KBtijZMxeqeZ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "96f94560e56cf0f53325b2ca86695151",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1wNDa4KVscZAsd0ReOo2weG2zd4Q5g0WYrlA42s9acwt",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "c180d553755adda1362467dfc4bde2d5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1WHRDaqjOtnLMlJwJWaNYMoWF6I7TxT6Gezzo3WTDZTw",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "78d941831ea462ae170ced0ef15961c8",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "13lvFNf0U9YSUqbAbjtzrZDq57KsKe1rwxaIbw4NGVe6",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "55b0c786483bdbace780a2175474ec96",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1cgmEmL1D1AKL0ZC2wX4PlONNO86btnDfTQbaHZj97I5",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a3114d6bda8b617b0dbc9b46f3e2aee6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1m5t0rt06iiZHWr4dxdn7tEnY67feymQAVWVfNF6r1W3",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1OTHAEGtHqSUUKOm7ZnL9ewZTs97nwuSQ1tCxdcnZIcw",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1bi072LxR8UgFG827ApJ0vLBVuBzDXIZWNDJhPCBVhhy",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "350f60a32f06a0e5262871074ff6178a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
