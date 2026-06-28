"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1iU5cKe2vLjUPYmrQqGXDTVK3OjoStU5owqLvZ7bS9Wd",
    "1L5TWoZWrNXoP7Iw8Tw0PSPYxoc8UilwleUzYIBY2fgX",
    "1jDNOSmdRGDOgLsGJsxI7N5iWzFgx9g3lDcU1qkLReel",
    "1gFajFVzYS2GgjewLvRGlsnx4zNUVAMH7enchOG4QOa5"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "dcacacb119379d12d1d4006f88c35e8b",
    "74b767c23145daa6437e558ceedb614a",
    "212fd6c83af47c384b76b517e13cc259",
    "110e97fc84813554f52bd596657a1ad3"
]

LEGIT_PERM_IDS = [
    "46a43ea39d5d5e81beed8b446211b4cb"
]

NEEDLES = [
    {
        "id": "1iU5cKe2vLjUPYmrQqGXDTVK3OjoStU5owqLvZ7bS9Wd",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "dcacacb119379d12d1d4006f88c35e8b",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1L5TWoZWrNXoP7Iw8Tw0PSPYxoc8UilwleUzYIBY2fgX",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "74b767c23145daa6437e558ceedb614a",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1jDNOSmdRGDOgLsGJsxI7N5iWzFgx9g3lDcU1qkLReel",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "212fd6c83af47c384b76b517e13cc259",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gFajFVzYS2GgjewLvRGlsnx4zNUVAMH7enchOG4QOa5",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "110e97fc84813554f52bd596657a1ad3",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1em2cdNsP4YCOCnLYFCewPsMwX8R61te6SDnI7dbn1Np",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "46a43ea39d5d5e81beed8b446211b4cb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1FMCE9yq9DuFsCJw2Xy0PdVWJXnCqlxZARMCslBQHSt6",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "16OrhTlZPliJN21LLBfZk1LEQNYqdLPIG47lGrUNCFIU",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1Bi5Z7tph7ozBnSGSQBwbrnRqAZc3SCe9021Zk7Km7Gm",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
