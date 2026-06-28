"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1IT08tDUrYXWxchPO2b4MEly3f8g8qXNf34VlYZtm0Ha",
    "1xE2e639udLvqR0Ay0ozV2FpsQVjP4TZLD3uH0mPtuPd",
    "1q5as1RPvFUvDkzlHttjTn0Qimk6XSHy6vahLOj86759",
    "148C75P4i9kEGXsKGtojBrIALrfJ62RwyF7H95TC1Utr"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "51b7397f87c03678d643ae827088c97a",
    "72d450f5c05fa9fb173b078ef1d2fb7d",
    "c3e1ccd61de4fb36d540f5dd35152789",
    "082f69838123964285439968a546d571"
]

LEGIT_PERM_IDS = [
    "7994e5b343ac6ca4583dd6650d6cd046",
    "11d317fbecb534dd2c7a5907b4f22fbb",
    "0827b0071c9ffc6674386496b55be8a7"
]

NEEDLES = [
    {
        "id": "1IT08tDUrYXWxchPO2b4MEly3f8g8qXNf34VlYZtm0Ha",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "51b7397f87c03678d643ae827088c97a",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1xE2e639udLvqR0Ay0ozV2FpsQVjP4TZLD3uH0mPtuPd",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "72d450f5c05fa9fb173b078ef1d2fb7d",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1q5as1RPvFUvDkzlHttjTn0Qimk6XSHy6vahLOj86759",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "c3e1ccd61de4fb36d540f5dd35152789",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "148C75P4i9kEGXsKGtojBrIALrfJ62RwyF7H95TC1Utr",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "082f69838123964285439968a546d571",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MRy0stV6QenQfohCijgiBeBbPwToE7w7XSl1sESS6ig",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1IECZwnVz3lmEqK4JLsGMoq49GrFM4VvzjIytdpxCkVS",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "155DgWavVvaLQt7qqEJwdow3C9UDlzqLnItX2buUFt75",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7994e5b343ac6ca4583dd6650d6cd046",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1PEnhxBFD3jSlDeA2RrK21pJIVE1ddv8Jk9l5i3pesEw",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "11d317fbecb534dd2c7a5907b4f22fbb",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1ISg6hq7WTXfzqhKlEhyWvB8kuVZWuY9qw2zDTubQ21D",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "0827b0071c9ffc6674386496b55be8a7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1V0CJ6dNOYjCm4t23LiWhOWhggxEjWyTxDmkAu12aXW5",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
