"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1A3jsNxklh325i0PIdOSvouVg7C3LIskIk5RNfCeYknc",
    "1uDTOK1itYzNZnGuEzEVOFlbRlz31x5lGGJCbyCnwByR",
    "1TBAFqWmFjFPmEWd8MH2kGRCRZbddab9DmWBSrElJboH",
    "1m2uDvzDmSZlsipWvlXGrmMox8vrpIvEcC5KlArmLjuT"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "6ce90c07924b1757e7acc8c89a1b9985",
    "5df045cad23db28745ad42e53b93d4ca",
    "84918eb12073aff9437c7f73c8168a0b",
    "3419dad2c421a9fa619a400c619d07eb"
]

LEGIT_PERM_IDS = [
    "6b957c740fab8f56ed112718e4187c81",
    "e17e36e17b22e978ca96e961c3c9319b"
]

NEEDLES = [
    {
        "id": "1A3jsNxklh325i0PIdOSvouVg7C3LIskIk5RNfCeYknc",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "6ce90c07924b1757e7acc8c89a1b9985",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1uDTOK1itYzNZnGuEzEVOFlbRlz31x5lGGJCbyCnwByR",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "5df045cad23db28745ad42e53b93d4ca",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1TBAFqWmFjFPmEWd8MH2kGRCRZbddab9DmWBSrElJboH",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "84918eb12073aff9437c7f73c8168a0b",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1m2uDvzDmSZlsipWvlXGrmMox8vrpIvEcC5KlArmLjuT",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3419dad2c421a9fa619a400c619d07eb",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1wUFzBZwC7bVKJPJSAJShWdH9SnMYZvkrgFsnwUWzegG",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6b957c740fab8f56ed112718e4187c81",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1iy6IHF3mxcuZxPzDi8yDVEkejyjGDkiWdNVoHr96Nxp",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1TBznuvq7re6xMsWsjEfeOSz0YAIoe3CWJrrUMH5jjNZ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e17e36e17b22e978ca96e961c3c9319b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "16Ror5CIVoHa0WPrhj7peDPmNGRI70aVKRzOJE8JsKCl",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1JEcx1LVrKWVcspZkVusXN5AB6etUejJ4yhrAw8g8zfo",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
