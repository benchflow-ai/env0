"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1PK2CHRQqnmoqQ0csENNQfy6VxAkZRdPbcyL5leo48aQ",
    "1sE4KLDmm7q5WTSBWA9yYf3pGEhI0AEjC64N9X1z5vNS",
    "1AOw5p5yVFQlhxphcfjXDz00G2HIrqr6fyLIoFhuRlcK",
    "16ez573BuQcyLWU6PX7RlSL0izezoesQdckyFtslBbsh"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "f9dfc01c288319ba3aa4bb19f10cc3ac",
    "512b146c050ada535394f73cbf265408",
    "e8002f74c7f81c40a976eddead5163af",
    "041fdfd43fb6308a2cf0c315e7f1bf5d"
]

LEGIT_PERM_IDS = [
    "c251cbab005138402553716c5c064156"
]

NEEDLES = [
    {
        "id": "1PK2CHRQqnmoqQ0csENNQfy6VxAkZRdPbcyL5leo48aQ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f9dfc01c288319ba3aa4bb19f10cc3ac",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1sE4KLDmm7q5WTSBWA9yYf3pGEhI0AEjC64N9X1z5vNS",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "512b146c050ada535394f73cbf265408",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1AOw5p5yVFQlhxphcfjXDz00G2HIrqr6fyLIoFhuRlcK",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e8002f74c7f81c40a976eddead5163af",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "16ez573BuQcyLWU6PX7RlSL0izezoesQdckyFtslBbsh",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "041fdfd43fb6308a2cf0c315e7f1bf5d",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Zy956oebi5bsuorxA2beVcZNYb6ArJbzUhKUmystCUq",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c251cbab005138402553716c5c064156",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1xXCC4fb6glbaY8UkDTmaFy4XyM1kha5a6eWconIeDju",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1mxEP8B6JNYP9nhdy8FFgpLrzVBQqZHDGdrKZOBcIuV0",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "19cuOSx4mn7uHvoItRELirhC1jHfuF9kDtzBY8RRtzms",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
