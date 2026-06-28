"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "13y6fEXRg81yHzMcGIX3wJTpQR7lhvqEOG8pzjHcSOlR",
    "12wfETsc9JJdp1Dt5dZecPTunKLQig3VIxs7WJWIWxLN",
    "1ZzQXSYSsTs41a6xRqRVsbULmUjhvjuIrYOPtETnYXGF",
    "1Y8gFpU0IfPcwYyHrrtGgBjYdLpuqfHgT0WHG9HkQFDx"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "ea4ecb4101b5ff03c0967d55e18bca76",
    "b8268de04df78e73385f9ff0668c5d2f",
    "869a0c02cffef99d986ffbc788b57b99",
    "f00e5ef06026bc6ddb9abc2bf4f7c58f"
]

LEGIT_PERM_IDS = [
    "fa54ed120686b8130e748ec22e381ca2"
]

NEEDLES = [
    {
        "id": "13y6fEXRg81yHzMcGIX3wJTpQR7lhvqEOG8pzjHcSOlR",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ea4ecb4101b5ff03c0967d55e18bca76",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12wfETsc9JJdp1Dt5dZecPTunKLQig3VIxs7WJWIWxLN",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "b8268de04df78e73385f9ff0668c5d2f",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1ZzQXSYSsTs41a6xRqRVsbULmUjhvjuIrYOPtETnYXGF",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "869a0c02cffef99d986ffbc788b57b99",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Y8gFpU0IfPcwYyHrrtGgBjYdLpuqfHgT0WHG9HkQFDx",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "f00e5ef06026bc6ddb9abc2bf4f7c58f",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1nFsGRtkufsICicNcqBac7f2m0ABIj4USboyB3l4efvR",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "fa54ed120686b8130e748ec22e381ca2",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1vpoNvUy67lIypMp9DEkFbrlu25jEkTdZQJrw9O0g44s",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1ld0JfpYmTg6bL8Hdj697HaSkJbhboYp9KVLWkXHdpXz",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1ErwGo8pcoyy1lDIanGAk4JWYFnxvdAU06Hxp7ZqubXl",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "14jg2kfQHtOMsQBM26zwhhG9EgdnjaU3SPzJSOfWKoMN",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
