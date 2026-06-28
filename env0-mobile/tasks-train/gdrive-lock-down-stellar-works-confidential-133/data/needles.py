"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1Y7AFx30hlyxVdicJ8jcxqxcEFGp9dU5LcJEIjuUNMmZ",
    "1bFKXIsg1HG2Kp7svlsZr7ID37TsbP8KOQjmXbTgeZLG",
    "1FmxqIN561DCJJDlDwAV7wgHK7qlg8u7rlI8Au8T4lyk",
    "1CF0GMFRAKDmu6fNHUCBLqupndwEwFiZRNY6dLKqZnHm",
    "1jXF9cTnjyFHPiZyXqQDL9iVYaU1EewodSZnpQsxXOnv"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "5011a8b5cd17e19363eb84288f36fb30",
    "b07d81a97033768dd7cc821af700976c",
    "54a1e4df25a6273be4a681af0d2c7953",
    "47cd54a7362d8fdfa37cf824de4fbcd4",
    "e519f298b9dde7ff7eb811022343196a"
]

LEGIT_PERM_IDS = [
    "b6e20d4cc31745521ce1c7be60f59753",
    "965f65f5c969be59e35700c343d9dc05"
]

NEEDLES = [
    {
        "id": "1Y7AFx30hlyxVdicJ8jcxqxcEFGp9dU5LcJEIjuUNMmZ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "5011a8b5cd17e19363eb84288f36fb30",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bFKXIsg1HG2Kp7svlsZr7ID37TsbP8KOQjmXbTgeZLG",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "b07d81a97033768dd7cc821af700976c",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1FmxqIN561DCJJDlDwAV7wgHK7qlg8u7rlI8Au8T4lyk",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "54a1e4df25a6273be4a681af0d2c7953",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1CF0GMFRAKDmu6fNHUCBLqupndwEwFiZRNY6dLKqZnHm",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "47cd54a7362d8fdfa37cf824de4fbcd4",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1jXF9cTnjyFHPiZyXqQDL9iVYaU1EewodSZnpQsxXOnv",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "e519f298b9dde7ff7eb811022343196a",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1dQHqJ4aTKPz2la7NrLnccmLr200dPUJvfMxvTEkp62H",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "b6e20d4cc31745521ce1c7be60f59753",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1YYRIOV59rDTEbesfuYD4V4eocNqZCSfF8KHCs0Zt5mr",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1NFVoJHzMtmz3ixFdR1UujZRSJK3BuGmTZhzuWEGSb8Q",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "19WzjsvET3nw0ICLbB4E6cPpM2OBQtrSA1MqDLwBq2n0",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "965f65f5c969be59e35700c343d9dc05",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1wqvPrVuNl9Gk6OYU0r0aulazuTFw5rh9SLi9e4XKdhf",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1Nd1yks9jYovoWLGrB6GkLHCcfLaXPkXu5YhgPGgnf9x",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
