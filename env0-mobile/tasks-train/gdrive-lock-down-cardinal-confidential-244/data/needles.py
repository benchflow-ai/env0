"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1o1HyRWqcDHR3BYZDEwyr0joj6MEKsJOwD5rYzYjIyLG",
    "1j8JwZWpJfx7IsslBszTfxfj3lAp0ePWV1kED7NVcJfY",
    "1St3rMZlrrJalVop61YLJv92BANq5sS6zV6puo2xQ4yh"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "a4e23a2bd5ba000e73d0850749601238",
    "7dd0e6fac20eff1a3ff8b01a4c5c7cfc",
    "186b472c93e85e5c450c8229a414ba05"
]

LEGIT_PERM_IDS = [
    "ee7739ab3987cbf9c4ea7aeb358e471c"
]

NEEDLES = [
    {
        "id": "1o1HyRWqcDHR3BYZDEwyr0joj6MEKsJOwD5rYzYjIyLG",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "a4e23a2bd5ba000e73d0850749601238",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1j8JwZWpJfx7IsslBszTfxfj3lAp0ePWV1kED7NVcJfY",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "7dd0e6fac20eff1a3ff8b01a4c5c7cfc",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1St3rMZlrrJalVop61YLJv92BANq5sS6zV6puo2xQ4yh",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "186b472c93e85e5c450c8229a414ba05",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "184Axepzql30WuZuTWyFzdhNjy7Ncwrqi0TqxRq8j9aR",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1268WjAb3mcjgDF23IIq7xDpoPfTkK69xoLOUYfDUXaL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "ee7739ab3987cbf9c4ea7aeb358e471c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "19AluKTZ2hIdIhD9Gq2snw3RpttqPwsYjOLoUpYeExAx",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1dxIGXUAjkHYPP64xDrh8vFY1O4Dp0XrVt9vGzwGP4HE",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1QSuXSptZbkAmFOv9jhHoTXzPWvwjRnF9KTBHqMzZTmv",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
