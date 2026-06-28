"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1osh0dEJBQqRfpto4oOv74AilmTFrMw7yaYQFP80M0bX",
    "17sL5MZiZHVhmR4Mweqj8215ZoC5Vq1Zvp6j25D1wpfn",
    "1Qrz7oBTlt3nErov8QWEVe7u7yaoUpSxyUBTr2V5fdYl",
    "1bgg7kZUMZ7h13P3JGk3twLJmwwfakF6yHXCR5NKvl6o"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "e132329137b505083aa836e5e677261f",
    "e1b23f815bd479e98286cf0a402cf000",
    "69599afaf8644d170095ea3fa7716856",
    "2065f87809979a6314e602ca1f77c39b"
]

LEGIT_PERM_IDS = [
    "244a46bd3c90425f68c08b7295426a41",
    "47390b1ee5c8f74832afbf0ce24dc896",
    "0d2ad44464424a673265cf261b5d6cea"
]

NEEDLES = [
    {
        "id": "1osh0dEJBQqRfpto4oOv74AilmTFrMw7yaYQFP80M0bX",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "e132329137b505083aa836e5e677261f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "17sL5MZiZHVhmR4Mweqj8215ZoC5Vq1Zvp6j25D1wpfn",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "e1b23f815bd479e98286cf0a402cf000",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Qrz7oBTlt3nErov8QWEVe7u7yaoUpSxyUBTr2V5fdYl",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "69599afaf8644d170095ea3fa7716856",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1bgg7kZUMZ7h13P3JGk3twLJmwwfakF6yHXCR5NKvl6o",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "2065f87809979a6314e602ca1f77c39b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Tg7l8ZazFlE4qQhttqcZ6TG94OIwwNe1QT3o2vtwnt0",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1R62MUenWmlHG1QyE04KZhrAzO1o82sLEqzDO5VSnasu",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "244a46bd3c90425f68c08b7295426a41",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1sDFSgvl9ZIiie5L6npb5F6W8XJksEsmuhw0WfBNan8k",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "47390b1ee5c8f74832afbf0ce24dc896",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1eHaFqj0z5D9nEBzt19kcfoOxKby6en6HGFsiiegj0z6",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1SGg38aXyeSTyhD14I8AvavyhtBv5uKV4c1p25L5jvS5",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "0d2ad44464424a673265cf261b5d6cea",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
