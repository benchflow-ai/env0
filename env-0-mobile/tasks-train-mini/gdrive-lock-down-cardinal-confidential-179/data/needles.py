"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1qJEc1YNM8T4wZwkMF1YVKY6DN6ApNLSIhAJEqZBJoIE",
    "1ttinqOj2rPbVV4jNoOgGqZzvwm0DxPnxIWRY9OUHDxG",
    "1zHGvxTUyFlQRgHw1ugwKBgANKHVZgcCVk4ufY5fKP3k",
    "1soJuxAjm9Npcfrnr2vIvUwkSXpPv1WWMJb87BNi712K",
    "1atPyNHQKFNpGnMQesScWqQ1qP7NHkMJ2UKIG7AxK65i"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "d5c0d9396b759a326a82cc00a670eabb",
    "7e9e25d9166e932245de1eb594d394f8",
    "c86c72b9624cdfef1fc736a5161ff361",
    "cbb211028a606ee0adcf5c577ca87c34",
    "218b5647ca97c067ddda264b776215d6"
]

LEGIT_PERM_IDS = [
    "135cde8549440440a6080cfcd0f8695e",
    "e341417c51cc3be51c577f01783ff9c0"
]

NEEDLES = [
    {
        "id": "1qJEc1YNM8T4wZwkMF1YVKY6DN6ApNLSIhAJEqZBJoIE",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "d5c0d9396b759a326a82cc00a670eabb",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1ttinqOj2rPbVV4jNoOgGqZzvwm0DxPnxIWRY9OUHDxG",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "7e9e25d9166e932245de1eb594d394f8",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1zHGvxTUyFlQRgHw1ugwKBgANKHVZgcCVk4ufY5fKP3k",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "c86c72b9624cdfef1fc736a5161ff361",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1soJuxAjm9Npcfrnr2vIvUwkSXpPv1WWMJb87BNi712K",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "cbb211028a606ee0adcf5c577ca87c34",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1atPyNHQKFNpGnMQesScWqQ1qP7NHkMJ2UKIG7AxK65i",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "218b5647ca97c067ddda264b776215d6",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Ao6Vy6O8pUBeK58daSABm4GTDJZW2mOEIbNF7mLtoUG",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1d82JloVqbjKtmfNMTgGqMamSJM9lC5KUbik1Sq1cEnH",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "135cde8549440440a6080cfcd0f8695e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1c0hpdNaybzqn1FyGkC9Qq3K3YxJOzoFwEYwKaG0qQ1r",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "17X2xBmYyrIxeoR7d9OTx8xZJr2YKey9TRgkrIA9HgGs",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1ypER2nmacrHDEb4yoo7HcxX89Kx3cqoMAv3PCku7OFg",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "e341417c51cc3be51c577f01783ff9c0",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
