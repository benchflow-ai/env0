"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1G2BLnNk97Yec38gc3kVftDKQqGhnPtN7inAHxNrASdL",
    "1zflEw2w9JjZAoPQY7DkVE7bqi0x7LSA0i1qkZJtI8bh",
    "10Ctr8ysowS9KzErUX6CtA6CSngkMKIFPgyYVtliR7EO",
    "1NLttIay2JvcwWDttm39DopkfgLQh5FVAEYkuWz2iHpx",
    "1HeYuMY0Cpo3ZVXvS5SommJNOcO6iL0q1sAHuEee00go"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "24fc6f19e51b7c2e37f4963a20de53a2",
    "2951853d413649fdb126d8fe54cd3725",
    "7e944082daf1a7c404ffaf2e8433888e",
    "32954c317d6d10c8608add355f88216b",
    "e050b98faf959fca12f151e9912adfdc"
]

LEGIT_PERM_IDS = [
    "70a9a172ad65bd52c52a68d8a340307a",
    "65eb346e0e19add598912f5557c36c40",
    "44ec37a75a717076255f5e09fcc9831c"
]

NEEDLES = [
    {
        "id": "1G2BLnNk97Yec38gc3kVftDKQqGhnPtN7inAHxNrASdL",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "24fc6f19e51b7c2e37f4963a20de53a2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1zflEw2w9JjZAoPQY7DkVE7bqi0x7LSA0i1qkZJtI8bh",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "2951853d413649fdb126d8fe54cd3725",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "10Ctr8ysowS9KzErUX6CtA6CSngkMKIFPgyYVtliR7EO",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "7e944082daf1a7c404ffaf2e8433888e",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1NLttIay2JvcwWDttm39DopkfgLQh5FVAEYkuWz2iHpx",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "32954c317d6d10c8608add355f88216b",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1HeYuMY0Cpo3ZVXvS5SommJNOcO6iL0q1sAHuEee00go",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "e050b98faf959fca12f151e9912adfdc",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1soSFkyIfHMzU1rQtMRPk36kwzz1tCHSvSPwMLW4CVnM",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "70a9a172ad65bd52c52a68d8a340307a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1dlixN4kNLsKayBlmZEHrP239ckuOFf7rbfXMtCk3XRO",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "65eb346e0e19add598912f5557c36c40",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1s2ITzRQTeQmznCvP9gcusc8A8IslFG6shIT5kdKNRLn",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "44ec37a75a717076255f5e09fcc9831c",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1Bg6PcwvtjNOkU9o5UdEkx5T8fnJfpJYI06t056m9Z3T",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
