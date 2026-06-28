"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1JoqjC44a7zTZYe2lkgVTJ3wBBDnktPBuSAoZTYL4Eiw",
    "13IaWIFrDNA8uBeIhkSJPIbQll9LAaKBWNA0HA4KDRvl",
    "1tzelSNP6TiWJalKTzxjW0xfiq3hQUkzLcCtFBrB5KY7",
    "1G0EdBPpmSUTyGMvQu8qXtfYzo8QtdE9kphJRlzlTqf0"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "3b03f5a8da9e3154f6ba1beb573998f4",
    "a9263f9e277b94b07ac4e987eb2c3793",
    "71f36db6e000416701253a9db8b76844",
    "25a7cfd56df29660587ba6a69debf141"
]

LEGIT_PERM_IDS = [
    "c1bff73f6b3accbecc073189c7738d18",
    "5bbceaf0dbaf3ef00ec7db489ee72555"
]

NEEDLES = [
    {
        "id": "1JoqjC44a7zTZYe2lkgVTJ3wBBDnktPBuSAoZTYL4Eiw",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3b03f5a8da9e3154f6ba1beb573998f4",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "13IaWIFrDNA8uBeIhkSJPIbQll9LAaKBWNA0HA4KDRvl",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a9263f9e277b94b07ac4e987eb2c3793",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tzelSNP6TiWJalKTzxjW0xfiq3hQUkzLcCtFBrB5KY7",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "71f36db6e000416701253a9db8b76844",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1G0EdBPpmSUTyGMvQu8qXtfYzo8QtdE9kphJRlzlTqf0",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "25a7cfd56df29660587ba6a69debf141",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1SXAXPZCQaECPwBa283JWpL90RbYE7JaHDeU2MiS021P",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c1bff73f6b3accbecc073189c7738d18",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1saPQI3L8TsaOtCEtJbEbqJsmIsjHmWzC7OsdBn9rEbX",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "5bbceaf0dbaf3ef00ec7db489ee72555",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1gpGEy8ffjxxy4MiOTBS1L9STEKcNd233XdQy1weyplN",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1i0lLz7naVtVlZdWLpo41UgSzpPRtRrolrNTouaDMRGf",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1LpHERS2exQKoUwEpi4u7SEJbK7Bb56dq99wpWrCUAoS",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
