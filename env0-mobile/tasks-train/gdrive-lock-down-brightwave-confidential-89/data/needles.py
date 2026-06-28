"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1YGdQb9Cr33ly9XGXwAYXMQnhkMvOnDMVoitfoty6SRX",
    "12n0E6U5XpN2jdE2KMjhJ1fiYXpDMv7XqdLnG7wn7wqP",
    "1suuNA8FDRwxHfYd3KoUu6upgJ4TElPNmh2EaS1Ko1k9",
    "1ZfBj2N5rcyAL54FB6Tju3qpezLzbCTEddotu8sr4viP",
    "1g1gBBzLtGQIjIfEwGYVYBms5BMU0yliFFEOmHVyHb2s"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "4085006f21362f3e5401add73e2ef190",
    "1154a0587d32b12dc1288850f232a82f",
    "458e574075a64cdaf3163a0449278561",
    "f51baaff468f41c8d42df0b00f00488b",
    "5acd37d8ad20d81b5c15dbc34f478ab4"
]

LEGIT_PERM_IDS = [
    "d1af70d1498f9c961f0cab80b5b3310f",
    "a6645a730c8ef97d17bac846c23b2e29",
    "07d7bad91cf527cd321219d9ec79e99f"
]

NEEDLES = [
    {
        "id": "1YGdQb9Cr33ly9XGXwAYXMQnhkMvOnDMVoitfoty6SRX",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "4085006f21362f3e5401add73e2ef190",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "12n0E6U5XpN2jdE2KMjhJ1fiYXpDMv7XqdLnG7wn7wqP",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "1154a0587d32b12dc1288850f232a82f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1suuNA8FDRwxHfYd3KoUu6upgJ4TElPNmh2EaS1Ko1k9",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "458e574075a64cdaf3163a0449278561",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ZfBj2N5rcyAL54FB6Tju3qpezLzbCTEddotu8sr4viP",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "f51baaff468f41c8d42df0b00f00488b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1g1gBBzLtGQIjIfEwGYVYBms5BMU0yliFFEOmHVyHb2s",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5acd37d8ad20d81b5c15dbc34f478ab4",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1byldQO65eD8i8YzlLWWc2I3kltHvieLotReK8T2NubC",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d1af70d1498f9c961f0cab80b5b3310f",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1FV95FwWqHKCgcYOGmMMBoPQfcNK349kMmK3nE9SUhIu",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a6645a730c8ef97d17bac846c23b2e29",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1YvLlJvK8kjHaDTj72HkfyydYmPH2fAcdzbrdyzQTnyO",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "07d7bad91cf527cd321219d9ec79e99f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1gDQZwN6SouJZBc3hdYeuyDfd4x1TlDblYGzaBOj7D6B",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1tSDKyYbHCKWMMgbNqgygRFHZMKcrSCDVEXqSDXK2dP3",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
