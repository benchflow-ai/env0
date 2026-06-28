"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1TobojdH3iqfXuBqNPPazYDrIG4sDrhzuo39YIIIzkwm",
    "1bquDQ9n58VoR2lgbPKFRrpbfMwOgjV7k0brL8IpPBXU",
    "1umfHjKJqFw6z3OliIsoVM1l1RdDvBQ08gQg8pA0Vhs0",
    "1NGjSIPjmOvQ0QT3MDuM4fxbYm0NfReRj8ZJGqvbYAy5",
    "1MK5U4FRlVEHJ3x1LocDLEvrvP8matYLpgUjddewyGv4"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "3231a5725ddf44822c1558876f4d1147",
    "0962944a9d17894143a68d7983abc4bd",
    "ac2fa76289e9c7430f536d66316832ec",
    "1fec6b9c2abf176dfa4f7be02896cb4a",
    "fce4a3a179f4006ebb7547ef20d40211"
]

LEGIT_PERM_IDS = [
    "6af60a4fa93b23a62eebabbab787b817",
    "6e125fbfde9a4e56ec57d0e2cfc37f22"
]

NEEDLES = [
    {
        "id": "1TobojdH3iqfXuBqNPPazYDrIG4sDrhzuo39YIIIzkwm",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3231a5725ddf44822c1558876f4d1147",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bquDQ9n58VoR2lgbPKFRrpbfMwOgjV7k0brL8IpPBXU",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "0962944a9d17894143a68d7983abc4bd",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1umfHjKJqFw6z3OliIsoVM1l1RdDvBQ08gQg8pA0Vhs0",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ac2fa76289e9c7430f536d66316832ec",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NGjSIPjmOvQ0QT3MDuM4fxbYm0NfReRj8ZJGqvbYAy5",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "1fec6b9c2abf176dfa4f7be02896cb4a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1MK5U4FRlVEHJ3x1LocDLEvrvP8matYLpgUjddewyGv4",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "fce4a3a179f4006ebb7547ef20d40211",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "174VgXaqkwJvtT56djDS0HCypSEIPRLkYYC4GHyCDWq8",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6af60a4fa93b23a62eebabbab787b817",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1Mj3GrXSblK7Swudt6OBWbi1Od86OIn18V4utl7Rnb2p",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "116UfT470PKxfBC6rpoK6srQC69t4rUrTeTLXFXByc3o",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6e125fbfde9a4e56ec57d0e2cfc37f22",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1kMPM32wNG88da0RqY6vZWiE57wE5rE6pXcO5J7tSije",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
