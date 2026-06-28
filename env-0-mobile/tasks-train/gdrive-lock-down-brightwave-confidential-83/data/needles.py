"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1ERLHDNY5rCnlAOQlC3p9VmMoGwjxmQXQ3UXsQU1A4IL",
    "1zLw9KhUvyW25MB7RcPZ1V5djGufcmqR6pEcISL41NxO",
    "1nNDpv4FbUKbjTI0pxyYTuTuVA0YbZK5mLWQ1c5yWQ2t",
    "12Apb6WvZRDwX3OLUmfXERu7Wgj3jbqVfSuZLWdf1L8d"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "0bdd5ac3343989497ce18e4d5b4565eb",
    "4fefc51c8572d23830e127435b7bc4e4",
    "bdc76ca70d7d4b0a5a43d854440bf13b",
    "6299ec393e342e06748b3e4edd1cca3e"
]

LEGIT_PERM_IDS = [
    "162b9f62c9a6a9f9835156d6d4b50948",
    "7344f71c476877284c05f504353d72d3",
    "b48fdf548c831015d9890dec06349961"
]

NEEDLES = [
    {
        "id": "1ERLHDNY5rCnlAOQlC3p9VmMoGwjxmQXQ3UXsQU1A4IL",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "0bdd5ac3343989497ce18e4d5b4565eb",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1zLw9KhUvyW25MB7RcPZ1V5djGufcmqR6pEcISL41NxO",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "4fefc51c8572d23830e127435b7bc4e4",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1nNDpv4FbUKbjTI0pxyYTuTuVA0YbZK5mLWQ1c5yWQ2t",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "bdc76ca70d7d4b0a5a43d854440bf13b",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "12Apb6WvZRDwX3OLUmfXERu7Wgj3jbqVfSuZLWdf1L8d",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "6299ec393e342e06748b3e4edd1cca3e",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1R881b1QgOck8Rehuknpw1g5gZk7hfNMoQ1tepw8m2nJ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1G3eIYD8TmPcw8c7pOec1DzJddtSpWBWxBHClsXkWClu",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "162b9f62c9a6a9f9835156d6d4b50948",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1sD8luP9EYuMv47JiMDILJYH1ws6NBbTNuKxVuiRO5qj",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1dI4n379XHeapdbHNk4vu1ecOY4lf8rzyHNCZrvNMaar",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1YhlESNkPs7zNH0Z9hrRSt14njZPqVWX8Y1bKQXPachn",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7344f71c476877284c05f504353d72d3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1X1ycXwDfUcITTmRIoJy4lj2smqa1ZUH1Z9KCpNvphtu",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "b48fdf548c831015d9890dec06349961",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
