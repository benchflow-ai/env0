"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1qqER4T5qgNBLl5zJrzYXkm9I5Pwbs7DFEtKQ7QFW7Ow",
    "1kIn5zt74s9yc3t6DEJ3lhZUUOYG1cQOUC2FTfXoQ0Nx",
    "1pIGJUFjmPsem0VsewP8BzVpIgkSehYOdzejPCgqlmVw",
    "1kJghoNoBTjih31FW4vT4dppTsvjsmdq0maWQ4DvdwEJ",
    "1sRyQReGIR9gcpkSO35L4NroTzwJNpQQr0wodSGc7zAT"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "78caa55210a8ba1a3cc5154328357a48",
    "5cb0026dd1f3ba94b6817255b7db2cdd",
    "46572ddb8ceecde6cf4d5a3630ccda74",
    "55150afa2b7385c95d604dcbfeed5fc0",
    "ce22aaa95e4d236198453162ae2c15d8"
]

LEGIT_PERM_IDS = [
    "12931639bbe7ec300c1277b33c65c193",
    "aa5f97c73eac79c44cf5fa7ea48cf898"
]

NEEDLES = [
    {
        "id": "1qqER4T5qgNBLl5zJrzYXkm9I5Pwbs7DFEtKQ7QFW7Ow",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "78caa55210a8ba1a3cc5154328357a48",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1kIn5zt74s9yc3t6DEJ3lhZUUOYG1cQOUC2FTfXoQ0Nx",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "5cb0026dd1f3ba94b6817255b7db2cdd",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1pIGJUFjmPsem0VsewP8BzVpIgkSehYOdzejPCgqlmVw",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "46572ddb8ceecde6cf4d5a3630ccda74",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1kJghoNoBTjih31FW4vT4dppTsvjsmdq0maWQ4DvdwEJ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "55150afa2b7385c95d604dcbfeed5fc0",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1sRyQReGIR9gcpkSO35L4NroTzwJNpQQr0wodSGc7zAT",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ce22aaa95e4d236198453162ae2c15d8",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "16KExjOOMapt9zIQNhwCextAYIqR3xSZRE1LtqZ3srg3",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "12931639bbe7ec300c1277b33c65c193",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1Toe4FFb12FWYuuIzJURwzJZ8kBN6Bt01vyNZj1wQqQW",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1NOgcShEuxIO2loD0xOPQXzjO0oe0LvkRs4byA8sJ4RQ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1gCikN4EO8oFCgie24kF9CQBfYSHs6wcPKRuHBeZxfiD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "aa5f97c73eac79c44cf5fa7ea48cf898",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "18gR7Npzhgzo1x9kONhRH3zY553zsX2Y6nlanTRAKUzh",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
