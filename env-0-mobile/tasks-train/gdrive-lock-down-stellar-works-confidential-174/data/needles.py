"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1tcyenm7TmWbMpvAIkcRLyKdPNFgqBBuqGXLX0WTNUwj",
    "1IcRIHs9TJWnRKOD5KvufowKbXWCVIzenR6m4G5sDTX7",
    "11MjsyEaMGOv4De4WGOD2xVuHvWjADqC0araYFRNghLZ",
    "11ZAzKVVAgWbKesKlovHTz4OXotJDKveoJAuERbMMXJS",
    "1FlhZZTdvnTR7E1sLm62I4v4PwBFHdZ96Q8WdLPR9adm"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "13a926ec3953264ea52c6422b396b7a7",
    "bca069c950503db2b4dc518a4706c9a6",
    "2c7e9702c2679529cf97baa2e4ca9021",
    "94aa89e611352d17184905da1a3c05da",
    "f6a69c07813fb76bfd82cef9c7405a10"
]

LEGIT_PERM_IDS = [
    "087288a403130b2be9c2c8cb2004f643",
    "b1e1acc0f9428fcb0344bc7363236dab",
    "f187b1d821bf2867e4305c99b5493eb1"
]

NEEDLES = [
    {
        "id": "1tcyenm7TmWbMpvAIkcRLyKdPNFgqBBuqGXLX0WTNUwj",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "13a926ec3953264ea52c6422b396b7a7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1IcRIHs9TJWnRKOD5KvufowKbXWCVIzenR6m4G5sDTX7",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "bca069c950503db2b4dc518a4706c9a6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "11MjsyEaMGOv4De4WGOD2xVuHvWjADqC0araYFRNghLZ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "2c7e9702c2679529cf97baa2e4ca9021",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "11ZAzKVVAgWbKesKlovHTz4OXotJDKveoJAuERbMMXJS",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "94aa89e611352d17184905da1a3c05da",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FlhZZTdvnTR7E1sLm62I4v4PwBFHdZ96Q8WdLPR9adm",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "f6a69c07813fb76bfd82cef9c7405a10",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1kjQocoULOfLzlkdEX76KtnpWcANjliyLDicdWvcIU9k",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1x2Lf7832E4JdLIeiStuRQwad5p1EzCmJwmEXBG0OJia",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "087288a403130b2be9c2c8cb2004f643",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1oEtgzT5YaCtjJa2caBxEuCSvECef3ACFkVa7xc4DD04",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1favU2ztic8DbjHzBHXci5AZ2LwcdJsQBbhAF3f1IBwo",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b1e1acc0f9428fcb0344bc7363236dab",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "11lItJAO6T9rgCaw3QJriamVGLN40wTxgyqg9JXIQ4Rd",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f187b1d821bf2867e4305c99b5493eb1",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1Yfmw2amvPY3Dje1tdLKjkFeVFQPk8AT5wfeFHlikY5K",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
