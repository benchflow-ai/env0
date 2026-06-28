"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "16hX0uqJsr1XhxS4I9GW4meqXWhq4ccsOy5572e4Pjfo",
    "1QvOohU3WLzKrrKnqaCCD7VI2B11Eb8VJYq8omcD1uvI",
    "1tqNdjLKdzgyV5HyFnwIpfAcT4lzh2cnYdvejVdH084v",
    "1ITg7qbxxTRzqJgQMastcd7BFZoNuTCugrUJIFxK9KKm"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "f46d59051554caadddc94fa6ca0bcb23",
    "10364d0f61e2ae6823216acf8336ae9f",
    "4c15cca5ba3789eb71b392c0abaf1aba",
    "f52d934bdb30fd6e0e7863dfa2915edc"
]

LEGIT_PERM_IDS = [
    "3f7652a5fa94f339f57d07662f35d615",
    "5228d6c3feeb6b691f7b075ef71660c0",
    "0369833be6c35ca85a65943ccfe04fb1"
]

NEEDLES = [
    {
        "id": "16hX0uqJsr1XhxS4I9GW4meqXWhq4ccsOy5572e4Pjfo",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "f46d59051554caadddc94fa6ca0bcb23",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QvOohU3WLzKrrKnqaCCD7VI2B11Eb8VJYq8omcD1uvI",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "10364d0f61e2ae6823216acf8336ae9f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tqNdjLKdzgyV5HyFnwIpfAcT4lzh2cnYdvejVdH084v",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "4c15cca5ba3789eb71b392c0abaf1aba",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1ITg7qbxxTRzqJgQMastcd7BFZoNuTCugrUJIFxK9KKm",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "f52d934bdb30fd6e0e7863dfa2915edc",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "192zJ0Uje5j5Qq2kHNjNoRH8cE31PiglTMrXBgmKfdA5",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "3f7652a5fa94f339f57d07662f35d615",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1N3aTirtdjSXisoiSLS7e7zqcrKVPXDV7UwptVbjwPDw",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1wLavi13WthoVlvZw0w9cbHhGuqT2clpafACKIlKm7sA",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "5228d6c3feeb6b691f7b075ef71660c0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LVZn41OouFGbj7RLJpddsnYjokSnywWkNk2lfKubZFa",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0369833be6c35ca85a65943ccfe04fb1",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1OZXA4vLT2CgFJqNSAQiksJbiBwf5OegVn5qadeYxlas",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
