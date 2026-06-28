"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1bYstvoUkWcRWbUR5nJF0d3dMjeBORQK1Zegq7wZHqra",
    "1rbrqkmdHVsOsgxDLHK2pDZRxbxOytHOWwLU1VPanMTL",
    "1bkrn3zqZvSXdvoBY2LIqsIda8fCrlEkNx6cCATBIvIe"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "dfd201f85a6257db68530f1991e85f26",
    "33c693ce0eff0a332d291246ff897d4e",
    "1407aef3d54c5b7455575b13550a2ad8"
]

LEGIT_PERM_IDS = [
    "47a814f1d22d31e3a9b2c872522c040d",
    "4fad0321f58a0489155a101aa9cd903a"
]

NEEDLES = [
    {
        "id": "1bYstvoUkWcRWbUR5nJF0d3dMjeBORQK1Zegq7wZHqra",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "dfd201f85a6257db68530f1991e85f26",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1rbrqkmdHVsOsgxDLHK2pDZRxbxOytHOWwLU1VPanMTL",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "33c693ce0eff0a332d291246ff897d4e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bkrn3zqZvSXdvoBY2LIqsIda8fCrlEkNx6cCATBIvIe",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1407aef3d54c5b7455575b13550a2ad8",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1jNSj1NB7OMtlWCQjx6GNFvXseCX0shFfFV4TCDwx1T8",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1hhM0Y1dWK3dauoWdvuhv8wHkXNGSCyELucbeFgzGOhN",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "47a814f1d22d31e3a9b2c872522c040d",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1AKhhpCopigm85iXqggi921BA0ho55O57mMhB0Ts0WPJ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4fad0321f58a0489155a101aa9cd903a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1xywAdOp8XUSM4JcY87ATO3cVtTQGWFUXZpjQOqja6Ii",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1t4wpKZLDVNAHuh3O3UFGDRHGnWy7LBR0o1y248gqb8Q",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
