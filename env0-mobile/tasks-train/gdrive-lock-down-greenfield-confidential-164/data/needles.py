"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1M3Pyp6UOGjYKwkgmKgfmmpyiI2C3ZnPJcVD4ttqrh2T",
    "1OTmoB3rGHvVkAJ9EeEtn0O1XOn7REYEgVhX1Qc9HsFZ",
    "143fRd8jmYc62eYje336JWZijnAyYUi8Ypi76DxI4fo0",
    "1LUjkmoSkTl7pA5ADaqd6gCNF36FcEl8nue6wkyBkUg4"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "fd5d489b7dd4f9b0c0229fd0a0120fab",
    "494f6f436511023c3c9f81d93dc04ea8",
    "f9003d1a1cf76fa9af961bbbb2e4134a",
    "45a77caaef1bc1a3546a47b87eedc243"
]

LEGIT_PERM_IDS = [
    "8b1f21f94074733642e4b17cdff94b96",
    "da1c8da6b12d1311ebf667895c0af74f"
]

NEEDLES = [
    {
        "id": "1M3Pyp6UOGjYKwkgmKgfmmpyiI2C3ZnPJcVD4ttqrh2T",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "fd5d489b7dd4f9b0c0229fd0a0120fab",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1OTmoB3rGHvVkAJ9EeEtn0O1XOn7REYEgVhX1Qc9HsFZ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "494f6f436511023c3c9f81d93dc04ea8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "143fRd8jmYc62eYje336JWZijnAyYUi8Ypi76DxI4fo0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f9003d1a1cf76fa9af961bbbb2e4134a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LUjkmoSkTl7pA5ADaqd6gCNF36FcEl8nue6wkyBkUg4",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "45a77caaef1bc1a3546a47b87eedc243",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YTYgWuukBDbMbF0ssEfMFWq2fpMXElWPQBwdXncLEf6",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1joiMYI5som9fuM6KY58kB49OivFDQ3hZTErblzoM4Lz",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1GoZgl6haFLFgclRk7N7LwdL3Vcg82JNz7bYO8rjmj4W",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "8b1f21f94074733642e4b17cdff94b96",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1nEI3TZwrRqmN1yULGvWPb6aS6hiwntNZXYCfCBUCZTz",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "da1c8da6b12d1311ebf667895c0af74f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
