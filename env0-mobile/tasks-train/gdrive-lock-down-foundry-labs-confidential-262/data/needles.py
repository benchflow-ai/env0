"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "10mRUjK0Ug3KJF3ylIMHKveH4P0Hyf7OADmUsS9ibs5k",
    "1qtHrxfDpPu2ho3LJF7lFosm0nzhssYj4Z3ZMXz0Hdx2",
    "1APBRjjOEsg7AURHRIGi6unDITfV3uwyIGnYjDaaxNeb",
    "13JubBIsz8vN9bptiYgLzRjCnuK0k6H3mO57hJglT4aq",
    "1nXH4pZTivczurcWm9dNLSoEnAoy95Ba4NuoFEpeN9wn"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "b7ca07146d9729878db8be9fe76e4efd",
    "e89d275c7732325f1ae803bfacc30a72",
    "68005a335fd128cf87ec19da755fe413",
    "ff13ed673f5724e5f13db24bfdf808cc",
    "040ea458e90e122a289b65a859e9f0c0"
]

LEGIT_PERM_IDS = [
    "6c846869d16ff9f161b1ea85f0f62cfc",
    "2c1e90f3db929cd3d557d7812eecd34e"
]

NEEDLES = [
    {
        "id": "10mRUjK0Ug3KJF3ylIMHKveH4P0Hyf7OADmUsS9ibs5k",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b7ca07146d9729878db8be9fe76e4efd",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1qtHrxfDpPu2ho3LJF7lFosm0nzhssYj4Z3ZMXz0Hdx2",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "e89d275c7732325f1ae803bfacc30a72",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1APBRjjOEsg7AURHRIGi6unDITfV3uwyIGnYjDaaxNeb",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "68005a335fd128cf87ec19da755fe413",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "13JubBIsz8vN9bptiYgLzRjCnuK0k6H3mO57hJglT4aq",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ff13ed673f5724e5f13db24bfdf808cc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1nXH4pZTivczurcWm9dNLSoEnAoy95Ba4NuoFEpeN9wn",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "040ea458e90e122a289b65a859e9f0c0",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YJtq8JTYPPvyL6VxWvH9Tn8gbC6IhmTkNO0Lc0EkqRZ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6c846869d16ff9f161b1ea85f0f62cfc",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ktPf0S6C2FwlqjyA5I0ZIZWQo8Ws1ZzFFRPKIvKE97t",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1KMCJ181dcscE1bSv02r7UsBLoLkYbS7zimJljBNdoXD",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1JyOQFx7zkeVn6rxB3IDvH3PmbX8LddPPfvCrvPkphxb",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "2c1e90f3db929cd3d557d7812eecd34e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1SUn3Y7kzj1Olzo5rGMCRGkFqcQFKTAFv4laxAQsZOuu",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1fF55XWeWKc6ZUrnjb4zKc6NnsVuoBTyypNOZRSZkKGJ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
