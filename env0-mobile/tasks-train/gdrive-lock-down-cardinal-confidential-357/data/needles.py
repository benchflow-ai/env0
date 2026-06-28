"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1Ia12VAbIDHzzYYVLGsa7ztBinoLg9ZN9Pmy0jsSSzcc",
    "14u6LBykSFtSRjGnmIAzQGXdT3XxqKn0GwFCwkPtnd2x",
    "1fYn5nvjCrUrJyYsE9Ddmqoy0FVmhZxtYrQOFW7z6R4i",
    "1LgzXW9KATcdcKtg4tiztk1XLMzHynjWv4BiGVlxcdWj",
    "13NCz7IxVxL52pP9ELkEvbND9pd676BEt8uiJCNa8W4z"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "be9350fe9561f52c17c0113d1d8e3f42",
    "f790828d5dec61e91985c997ce94f03d",
    "e06cac717a83df2c8258287c6c121b4e",
    "676c020cad01c401ebf95db3be0da11c",
    "b354d5bb7832f4c67599487876221628"
]

LEGIT_PERM_IDS = [
    "1080c822801133b78402eee05889ce6f",
    "c269ac6572b372de4034219cc782d205"
]

NEEDLES = [
    {
        "id": "1Ia12VAbIDHzzYYVLGsa7ztBinoLg9ZN9Pmy0jsSSzcc",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "be9350fe9561f52c17c0113d1d8e3f42",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "14u6LBykSFtSRjGnmIAzQGXdT3XxqKn0GwFCwkPtnd2x",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "f790828d5dec61e91985c997ce94f03d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1fYn5nvjCrUrJyYsE9Ddmqoy0FVmhZxtYrQOFW7z6R4i",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e06cac717a83df2c8258287c6c121b4e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LgzXW9KATcdcKtg4tiztk1XLMzHynjWv4BiGVlxcdWj",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "676c020cad01c401ebf95db3be0da11c",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "13NCz7IxVxL52pP9ELkEvbND9pd676BEt8uiJCNa8W4z",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b354d5bb7832f4c67599487876221628",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "161dHkVZQF7B7gS40czs8x0zFeu3DUqGxOrXG26KdQvx",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "1080c822801133b78402eee05889ce6f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fY0NVYkDgkMMnegi0J6LXA6M3kSyFg3waikwQQvM94V",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1HF4rJiTDlExPVc73TluiDe1DaAw3azd1CrQuLpkFTyV",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1dmYhiyJQwMzdnlOaeUEdEzse0Fco4OLBRGhlIYevRMK",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c269ac6572b372de4034219cc782d205",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
