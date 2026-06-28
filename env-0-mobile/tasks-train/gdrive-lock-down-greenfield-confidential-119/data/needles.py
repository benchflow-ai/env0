"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1idvVk8pEz41GGeRJsyNurgS3zF0yOgOXqDSzzz3XaCj",
    "110Mu79kgoZEtG0suSLV0wOZSS0Hcx8HFpBLL3pmUkGm",
    "1rCQK6zspfegBGQxOQHds8mUwYxFRoLtqAs2Ob4vDlCe",
    "1xBpPR7erTsaDMwvQxvROqgr4R9ZbdXcEiQnk0OSg2Xd",
    "1fow92OAaDfQS3llo5eWatSHKJSDlMl2PpNFtz9la7bB"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "c783d1df70cd3ce11d6f4b439d6094c4",
    "c91a548e5b19548b3880e90ca4fc7b0e",
    "fc58e521b10581ff620f04545ea7ab41",
    "2990aa2048af997243b7a2b47965dda3",
    "29374d61a1678e6e7f7a54f5f77f4af1"
]

LEGIT_PERM_IDS = [
    "74274d46dff4f178f87bb630cec321c2",
    "f3c92f70258b45a5baba994493970fee",
    "33f2dd6604ae0170be7e335c4dba4343"
]

NEEDLES = [
    {
        "id": "1idvVk8pEz41GGeRJsyNurgS3zF0yOgOXqDSzzz3XaCj",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "c783d1df70cd3ce11d6f4b439d6094c4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "110Mu79kgoZEtG0suSLV0wOZSS0Hcx8HFpBLL3pmUkGm",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c91a548e5b19548b3880e90ca4fc7b0e",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1rCQK6zspfegBGQxOQHds8mUwYxFRoLtqAs2Ob4vDlCe",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "fc58e521b10581ff620f04545ea7ab41",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xBpPR7erTsaDMwvQxvROqgr4R9ZbdXcEiQnk0OSg2Xd",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "2990aa2048af997243b7a2b47965dda3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1fow92OAaDfQS3llo5eWatSHKJSDlMl2PpNFtz9la7bB",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "29374d61a1678e6e7f7a54f5f77f4af1",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Zr3pYlA5TfaO5JZC6gyHZyayMncAcNrAo6hJgogqn85",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1Etz3Z3FKs0Ys2lrxPAVZ2aBDpIerur53S1POlAIpF08",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "74274d46dff4f178f87bb630cec321c2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ArZqTuufVlnsDPy0m1GdYhpTkc1I6eV6zUP30yziiXN",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f3c92f70258b45a5baba994493970fee",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1kuOIXU1iwM8hjrHQwvkednG36RcjemR4bLcGlOjWbOF",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1Ix99Qcb0OC8eWIUz1EDWXem8yEQMvmUOzssSmhHa7xJ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "33f2dd6604ae0170be7e335c4dba4343",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
