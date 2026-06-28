"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1YMcRbPBJvZImTgLKeWQcEuC4TxuLHefv7JctiWMm0pt",
    "13aavSgxmTA8pO8Ld15J8Cq9di9WcbsRkQHTC4kohMLy",
    "1GYQx9FIFOwdY8UgGNnxp6QWZvwEz8IYEfRDYwEQKfZr",
    "1Ya9XHOQaD3eW0s1D3Kt7NoKr0TxQrF9LgG8pG2ep2jy"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "a11ab4917c1470a4c72d1b12fd5c40b4",
    "82d4e79319a965b0084678936432ca92",
    "e21c9c959108ec75784f64c1a6f08b29",
    "1a1ae8d5d256992c43afb6c921724e08"
]

LEGIT_PERM_IDS = [
    "389b0da4d6af927ee96f2ba0ccd8ec5d"
]

NEEDLES = [
    {
        "id": "1YMcRbPBJvZImTgLKeWQcEuC4TxuLHefv7JctiWMm0pt",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a11ab4917c1470a4c72d1b12fd5c40b4",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "13aavSgxmTA8pO8Ld15J8Cq9di9WcbsRkQHTC4kohMLy",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "82d4e79319a965b0084678936432ca92",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1GYQx9FIFOwdY8UgGNnxp6QWZvwEz8IYEfRDYwEQKfZr",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "e21c9c959108ec75784f64c1a6f08b29",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Ya9XHOQaD3eW0s1D3Kt7NoKr0TxQrF9LgG8pG2ep2jy",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "1a1ae8d5d256992c43afb6c921724e08",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Hjfbegbb1syUfJudDHAPKHSAAmFXz10ajyr3vPNuOhL",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1JBmklONEviD4EvvsepldIVtLb0SNHTd7CGtXmyMBnC0",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1qtwiX91HPW87oqTiKqfQ0kFGJLWWhnyBAqAfuKE5yrr",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "389b0da4d6af927ee96f2ba0ccd8ec5d",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1MySTzSNtzUsn61OsrSZCizHnDR5ITU45xs60NpjlNow",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "11Zdlv4UlAHXt2erVQp0fTzgdgQVrpj0agRNhWlKeLue",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
