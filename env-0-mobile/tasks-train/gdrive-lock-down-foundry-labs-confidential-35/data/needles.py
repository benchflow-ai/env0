"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1hSIkKh74qLDuKRWLm8LJTUjqV86KjgRepgbMZLZxuEP",
    "1DVHd8v6EVfsi21nDyRyuCcOc6SGId9Hx5YkW4j5DkUw",
    "1IEJe7PyPMAmQEV8QthJjg92u8B5nRq4NECcdIWAdjcY",
    "1ZsvIVLXFTlZDWkm2MuKroFk3bgVp6qqdTnMFchJPjRI"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "713e651c3e2d6b287cd5247c9a196e84",
    "da8bffab7aaf8241feb9d19f197514f3",
    "a4b122a0212025897b78496d625a1dd2",
    "a047284aee631a3c396be457577e61a3"
]

LEGIT_PERM_IDS = [
    "e54ccd21a08784032c72eb5e5b262571",
    "893d1ff2a11305eab2e201a2a8346b11"
]

NEEDLES = [
    {
        "id": "1hSIkKh74qLDuKRWLm8LJTUjqV86KjgRepgbMZLZxuEP",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "713e651c3e2d6b287cd5247c9a196e84",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1DVHd8v6EVfsi21nDyRyuCcOc6SGId9Hx5YkW4j5DkUw",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "da8bffab7aaf8241feb9d19f197514f3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1IEJe7PyPMAmQEV8QthJjg92u8B5nRq4NECcdIWAdjcY",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a4b122a0212025897b78496d625a1dd2",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1ZsvIVLXFTlZDWkm2MuKroFk3bgVp6qqdTnMFchJPjRI",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "a047284aee631a3c396be457577e61a3",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "15A1pCHpT8wv6be8Hu1mGfVCtu7IOTLyGqmvFtaL8zOl",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "18oayMhoDvLkL9wywslmrfQm188hwqpozwFNzbprpgyV",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e54ccd21a08784032c72eb5e5b262571",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1lnFDxGAvchpFaMmSEDATOCi2BPmtYzVIGcpnjpfy8f3",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1kJaO7jgB0I2c9Vp7KmxDQaRtGQPMibSZzzovy5Q5jot",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "893d1ff2a11305eab2e201a2a8346b11",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
