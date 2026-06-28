"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1OsgpVesdve1ol9u2LzFKpIN9w82NCedXldZuq0RIGkC",
    "19caehagNYdA09sLgToHI5Fc4JNrOKBCT4iCVKQy7dvR",
    "1X6I8Th2vf6mHIs7UFq4l4G0oJ7f6sqnDtc3O1lDPedl"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "97ac6ef0fc13a42e3f80965dda694399",
    "2ab5ff6ac7179474070d363709f6c95f",
    "fdd00a9d3a59b40227526e0a69eacb1f"
]

LEGIT_PERM_IDS = [
    "d0c4f88c077fbe203f880fac9f4c20ce",
    "939e03640cff9e06f84beebb9f486e85",
    "6e075967d5aef48b66d6ac1dc8aa2b15"
]

NEEDLES = [
    {
        "id": "1OsgpVesdve1ol9u2LzFKpIN9w82NCedXldZuq0RIGkC",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "97ac6ef0fc13a42e3f80965dda694399",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "19caehagNYdA09sLgToHI5Fc4JNrOKBCT4iCVKQy7dvR",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "2ab5ff6ac7179474070d363709f6c95f",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1X6I8Th2vf6mHIs7UFq4l4G0oJ7f6sqnDtc3O1lDPedl",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "fdd00a9d3a59b40227526e0a69eacb1f",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1VG4YkygzL6QFwY00kOPfvWZINNvDFqK6P4utC2ppZaN",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d0c4f88c077fbe203f880fac9f4c20ce",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "10KdIbImhSDAzDDyLXKfYC62TdDynhmNJjNQdywlOQXn",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1h0FeZaWzFxzGWEpzx13V6HOElzcjnWrnqDSycdEr7C2",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "939e03640cff9e06f84beebb9f486e85",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1vgtZ6px1iyAjycbRqEIQjayxrlukJAOWp9la4dvWpRS",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6e075967d5aef48b66d6ac1dc8aa2b15",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1k7uI8VUtPIyGIzugSlCSBYfreeVHV6pG8rOr3mY4vyv",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
