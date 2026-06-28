"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1WnM4B8xi2f2ZfHb1qDOVJCZrDWWjzPA9ognAtvkvt6v",
    "16E0Y6XzlcfwOpQnFKZHZUTf48ONyBcZ7ni0N2oNizwO",
    "1nw2Fyw6NRDhgWRotVF6MMwPMnJgHP9Q0HaeiIEMHJEt",
    "1FkLgk0kjTJpniW5ZNBicFllbIL8T1k2eYWLnZbdQFLt"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "c399ced01a3e3ddfb9ed1aedd5f4b382",
    "12a6ed20c9e9cc098a966ccd709a89e8",
    "f6945802f8b86aae66cfe2fbb9a11fd3",
    "dea7615edfa68b2898448319b4090dd2"
]

LEGIT_PERM_IDS = [
    "577aa5811c5ee1277f18466ee318213c",
    "135912eb9372a7b177077745a79760ab"
]

NEEDLES = [
    {
        "id": "1WnM4B8xi2f2ZfHb1qDOVJCZrDWWjzPA9ognAtvkvt6v",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "c399ced01a3e3ddfb9ed1aedd5f4b382",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "16E0Y6XzlcfwOpQnFKZHZUTf48ONyBcZ7ni0N2oNizwO",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "12a6ed20c9e9cc098a966ccd709a89e8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1nw2Fyw6NRDhgWRotVF6MMwPMnJgHP9Q0HaeiIEMHJEt",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "f6945802f8b86aae66cfe2fbb9a11fd3",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1FkLgk0kjTJpniW5ZNBicFllbIL8T1k2eYWLnZbdQFLt",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "dea7615edfa68b2898448319b4090dd2",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1evAUPF9hdrLuFGgVtBwXAjiRABerp4YRKYkkeR24avD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "577aa5811c5ee1277f18466ee318213c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "19bRXK2qpRuhN9KPvjfM3Z0Wveru3uHntGIGUN8zoslg",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "12NDVd5FDV1pvxuhQSO4hRpoPCAgWKpyWiPhRlRuvicJ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "135912eb9372a7b177077745a79760ab",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1xNByxc5Zz62CoNabKTRu3Ddte7uSjGvAJ4MDGxqqHro",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1MnsMBlMMo0KkQ1Vz1kOM8eqSOC7wj6yQkuXOQjkGCmr",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1IyyVZorfXk89o2ny4gghL8f44ShXVjYx5OwBH1x9lIt",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
