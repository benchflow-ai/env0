"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1SkQkieOwwGJ3TOYJE6vGBYjBLkTd9CbpaUaG28zUA44",
    "1Kc281tjHCR5I1KxVzolpw1MHwEru5DKC4bcvS5jxI39",
    "1ia3eXMmPRH5N6JgqRXqlPuGBodPggsoezZtemZUhGD9",
    "16MsQgFJxs8CaCbiHsP34KVH5Nt6D7n786ymC0PdSgYN"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "c050f5043b2befd5bab7502afb4020bb",
    "2496665920324b4e4ea6b18a8dfe1e72",
    "d5bd25fb1883f6c9d62654a8925e67db",
    "066022033fff49d7538019d6aad74a2f"
]

LEGIT_PERM_IDS = [
    "9c7475592ff3f5007bf4939eda9e207b"
]

NEEDLES = [
    {
        "id": "1SkQkieOwwGJ3TOYJE6vGBYjBLkTd9CbpaUaG28zUA44",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c050f5043b2befd5bab7502afb4020bb",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1Kc281tjHCR5I1KxVzolpw1MHwEru5DKC4bcvS5jxI39",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "2496665920324b4e4ea6b18a8dfe1e72",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ia3eXMmPRH5N6JgqRXqlPuGBodPggsoezZtemZUhGD9",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "d5bd25fb1883f6c9d62654a8925e67db",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "16MsQgFJxs8CaCbiHsP34KVH5Nt6D7n786ymC0PdSgYN",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "066022033fff49d7538019d6aad74a2f",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1hnoaQD2zgX4HuYteiFdnYEWSVezPORt2ulqgJMWXHTe",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1iJAGGU83CxNuHIs2EppObF4DfZK8fRTXkva9rGk2Ybs",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1BASugThIZuMFyAxKFnrE3SQ2LHMa2Q4btEbHCLn9bSF",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9c7475592ff3f5007bf4939eda9e207b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1JJZZljzp1aNMoa6bYnItqy4Kyjw0ToF3EwiuvFjeh8J",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
