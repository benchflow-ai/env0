"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1duq4oBtMQliUn63B7l7tVJFnsZenekbjhgm9Qc6h5a2",
    "1apiRhKg39hZ7q9IMku0051diilCkVcWYYSnaWb3OmoF",
    "1YLpGv29X1G0OFyF0LyoRHemJpsJinyLxf2VaPWltv5m"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "9493c5471988a8ae2b3dd7b9f1c0bf33",
    "47c9e4a4a665636ca6dceb241e7d3fea",
    "b523430d2a5011d3562f99dfc22a0dc3"
]

LEGIT_PERM_IDS = [
    "7a0daefb99d65de4e4e8cf7e3e4a7856"
]

NEEDLES = [
    {
        "id": "1duq4oBtMQliUn63B7l7tVJFnsZenekbjhgm9Qc6h5a2",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "9493c5471988a8ae2b3dd7b9f1c0bf33",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1apiRhKg39hZ7q9IMku0051diilCkVcWYYSnaWb3OmoF",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "47c9e4a4a665636ca6dceb241e7d3fea",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1YLpGv29X1G0OFyF0LyoRHemJpsJinyLxf2VaPWltv5m",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b523430d2a5011d3562f99dfc22a0dc3",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Ml0ooymXrXJhZcssZtziTzlySOoL7t0uneuQd59ctEP",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7a0daefb99d65de4e4e8cf7e3e4a7856",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1stw0bDCdrwHvz7cEMrIKP16hTg962KCG0WQBIOaPWJK",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1Cq0PGfNDMUaPOmc34IXtC3VR5cOwSLz7Eau4yJKLFo7",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1T8SbxBQriVQ16Z20tRNhAoB58xFdQSvvCB65TaiP4OU",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "14tbmpVHM0KE74dSMaQ7dQyow0pFBFaJ3x5SPmSrda3Y",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
