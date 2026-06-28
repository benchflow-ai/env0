"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1saGacN90LGQQsOe6a8TF7M6zv8Y2UDNgmTIZF57sdql",
    "1GUe3tQp2VVH4Tno7AhV34TObanZpPMoNdlPFEpcvuL9",
    "1POB7qNbLdMQGL6ucf75nf5LMieDPg9oWB0E8ZnXrKHd",
    "1MNYmuvcqbVqhBlJz9AFzn9pALmAD1PXB52idwSvEZUl",
    "127BEHrrTV3LtDZBuqzvwUJAqwvlkwgdTwEyEZhhWgjN"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "336b2142fa2d967ef1c1f3f575d5393c",
    "adc0ab37133414dd24c46d37b6f3095d",
    "2bd6df41eda090c71949b08cae023094",
    "df1d19362d12cc323396812a6d919b5e",
    "cf1d33fda3b8db59286f1f6339722374"
]

LEGIT_PERM_IDS = [
    "86d053bfe0ff8b1d8f68c013b695fe81",
    "59e51191033cac1b2a4662ca88a48859"
]

NEEDLES = [
    {
        "id": "1saGacN90LGQQsOe6a8TF7M6zv8Y2UDNgmTIZF57sdql",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "336b2142fa2d967ef1c1f3f575d5393c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1GUe3tQp2VVH4Tno7AhV34TObanZpPMoNdlPFEpcvuL9",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "adc0ab37133414dd24c46d37b6f3095d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1POB7qNbLdMQGL6ucf75nf5LMieDPg9oWB0E8ZnXrKHd",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "2bd6df41eda090c71949b08cae023094",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1MNYmuvcqbVqhBlJz9AFzn9pALmAD1PXB52idwSvEZUl",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "df1d19362d12cc323396812a6d919b5e",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "127BEHrrTV3LtDZBuqzvwUJAqwvlkwgdTwEyEZhhWgjN",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "cf1d33fda3b8db59286f1f6339722374",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1EVEvNFZNSTeq0p15ztgDwNWFGNBbWQD77aPPJOlpgVH",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1RjwXBRVNLoHWNtJoKCPQDV7l0N8xH5Wyy31XKLzaSGd",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "86d053bfe0ff8b1d8f68c013b695fe81",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1DTUDzHRkWFBjX8WHe0CeItLCwJEQiEw405EghG3KsZD",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1xzDUAv4kffIYv3VJcjL1TEw5Wx3iASuVCEI8opLAthS",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1EbPQhQxE1YhUTjIfSEnEZHy1XW7ESTdyjTtwvwP27Ex",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "59e51191033cac1b2a4662ca88a48859",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
