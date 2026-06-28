"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "19eipsxQdfTwXu3PVOlvRsNqoVnD3E6iXDHyxdXlJ0v9",
    "1NiCURmZCSOScnCVftvS6shDbgnpWI6kdmEL659bjxqc",
    "12LJiXiFbHLxKN0KxN90TjiWdxTJpkXRlXgnc1BCkWJ9"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "933383f83d675ab700885925578e2275",
    "86dfb189e6a3f916d1972d5d3cd9e752",
    "d1cdfc51b37e42e3efae02867a96b525"
]

LEGIT_PERM_IDS = [
    "48bf759108a58d973aecbb2c08e6b5c1",
    "2724365346ac01a935207e553e784019",
    "74827ca87848c93f035fa2cad38afe47"
]

NEEDLES = [
    {
        "id": "19eipsxQdfTwXu3PVOlvRsNqoVnD3E6iXDHyxdXlJ0v9",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "933383f83d675ab700885925578e2275",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NiCURmZCSOScnCVftvS6shDbgnpWI6kdmEL659bjxqc",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "86dfb189e6a3f916d1972d5d3cd9e752",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12LJiXiFbHLxKN0KxN90TjiWdxTJpkXRlXgnc1BCkWJ9",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "d1cdfc51b37e42e3efae02867a96b525",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1HzphM3HCe1IyctvoolFQVM1nO4qehhUdQuE6VIg1sYY",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1wvnAqjz9b8rqZZhOojhpBWkjT9tSvbt4wbVt1qwyyW0",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "48bf759108a58d973aecbb2c08e6b5c1",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1z008GuKWwadQibWTrXpSkEYpVY04PCaKvIpwviohWWw",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "2724365346ac01a935207e553e784019",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "19ciz8pHP5vyPlJjxtyFgx1AqpTl8tdanXxprEZeIRrg",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1eJs7PYzy5SMTjB814CdnnHZZ1z2NuZDRxARTjO8sfo1",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1y1SJaXF7LapgvcBntXCMTRlj5j1d3MDIfdAYT9yirvj",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "74827ca87848c93f035fa2cad38afe47",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
