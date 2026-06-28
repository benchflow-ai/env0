"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1aSY99dtoFjuvmHpl90GDXKPOHNIghQrc7M2N8X8q0QA",
    "15T5NxGRYCA00ePtNw1mA3yBDJOSm4u9EsuSOomH7D5u",
    "1RTJJCPywFvd27UcFmdm5NJKYiyPTX9BK0WKYZHbFHyf",
    "1J4xooJPCR0MtkkcPFQdp50gfm1MG4zGjbvlHiPN2Cri"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "2be86ba02752ef1f33b0bcfc686d8cab",
    "7c680882fd7e88394200894b56cb8ea8",
    "ab86053e2d9f8c371ec7287e74c31479",
    "1911d928c2583982cce07286ad41e3e2"
]

LEGIT_PERM_IDS = [
    "5c66e468afe0f676d91ec98ef136b14c",
    "77119971048fe733fb351e7d574ae634"
]

NEEDLES = [
    {
        "id": "1aSY99dtoFjuvmHpl90GDXKPOHNIghQrc7M2N8X8q0QA",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "2be86ba02752ef1f33b0bcfc686d8cab",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "15T5NxGRYCA00ePtNw1mA3yBDJOSm4u9EsuSOomH7D5u",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7c680882fd7e88394200894b56cb8ea8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1RTJJCPywFvd27UcFmdm5NJKYiyPTX9BK0WKYZHbFHyf",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "ab86053e2d9f8c371ec7287e74c31479",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1J4xooJPCR0MtkkcPFQdp50gfm1MG4zGjbvlHiPN2Cri",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "1911d928c2583982cce07286ad41e3e2",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1u8tH83mMnWw4yludCy5V047P9Y09zcoOADhTXHnP21x",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "5c66e468afe0f676d91ec98ef136b14c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1G4QcxDEnbMhVaNSmP0ctL9IHnT6UUaRWEIOHcssQkAv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "77119971048fe733fb351e7d574ae634",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "124nxQI6qBBEGvIIcPnvWWLk3hn8alhIkyfrVDTjggqp",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1CSpTPw2srxTEWOYd5N88c6q5FQffG7LsCiUOvQ5qded",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
