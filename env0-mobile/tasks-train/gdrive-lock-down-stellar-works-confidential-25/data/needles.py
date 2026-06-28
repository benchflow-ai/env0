"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1ZgbSw56vlB6gNjg101XG3klHvowE1Ln1g1RUktgGHZS",
    "1epG8DbVYWn6rY422gFV50KVN7iMFvCheAEFN1Zh230k",
    "1ZBN5FVnclSi5VafOOpwVHVmvMoBrpsK1nAyNl4MMd6E",
    "1EdY8NXTGm5YSEvBsn9bqERglwTTyTgqBvEkSW0rXYgg",
    "1K60AdwPa7HnQEczP7DFdmOSyK47AdxxwEWiopuY5tcO"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "b9df116bebbec61ec043554600749f13",
    "f4a869fb9371323d405e7b5a7029b609",
    "eea9607e975a4413fd35f5805af9cde1",
    "42f13bb0ae313bed3c44c037ce09bebd",
    "f655ac200b05e19b87ce729a858bf469"
]

LEGIT_PERM_IDS = [
    "892e0935000a102cfee05f81e42caa27",
    "391321a7311c75eb4c1f1516a8e03f28"
]

NEEDLES = [
    {
        "id": "1ZgbSw56vlB6gNjg101XG3klHvowE1Ln1g1RUktgGHZS",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "b9df116bebbec61ec043554600749f13",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1epG8DbVYWn6rY422gFV50KVN7iMFvCheAEFN1Zh230k",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f4a869fb9371323d405e7b5a7029b609",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1ZBN5FVnclSi5VafOOpwVHVmvMoBrpsK1nAyNl4MMd6E",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "eea9607e975a4413fd35f5805af9cde1",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1EdY8NXTGm5YSEvBsn9bqERglwTTyTgqBvEkSW0rXYgg",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "42f13bb0ae313bed3c44c037ce09bebd",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1K60AdwPa7HnQEczP7DFdmOSyK47AdxxwEWiopuY5tcO",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "f655ac200b05e19b87ce729a858bf469",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1s63xMTCtEKClKJXtAcGp4sPLtKoIxNwcZKdoCpHvGIE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1q3kpsuirOgKAFyRH8CBmbmTs0NL0BwhZX6NXGQIfrkM",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1c2cQinfxL4gXwThun4qYiTo1izU80wnc6k3VT67Nr4C",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1OBs9bh00U7V9IxZMfK8Ty3KlLp9LAh3hVTZ9R3ti4nA",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "892e0935000a102cfee05f81e42caa27",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1f9TxiinBfUGjV0ofFxsi39R3wFyTzwUDQsjh3IW0fMz",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "391321a7311c75eb4c1f1516a8e03f28",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
