"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "17Gg5U5yfxwjj0j2AwOoXaKCKFRp7uLOkDrCCsnpXuXh",
    "1E0E4f0eNsStqSORtCRZSYlM2sweTLrBKhlfWaFy7816",
    "1m5Pvr1MYZ3dtv0tZSOUTRFfTsFgg8j0tDjomfjHKDuU",
    "1clkddKdq2Le1Z7cpmNyfrBxdZrza6wgvihOoHNt5ZCX"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "63ec6f9b6b6c490ac331a0029ca19af6",
    "c205e467122611515726db4b7b5b490e",
    "606d43c3f2392e2b001516f62cbabf47",
    "8d11629934190faf6f702584f5dbbb75"
]

LEGIT_PERM_IDS = [
    "cb69387cd8d2509f0dfb1f4a6c905d0d"
]

NEEDLES = [
    {
        "id": "17Gg5U5yfxwjj0j2AwOoXaKCKFRp7uLOkDrCCsnpXuXh",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "63ec6f9b6b6c490ac331a0029ca19af6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1E0E4f0eNsStqSORtCRZSYlM2sweTLrBKhlfWaFy7816",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c205e467122611515726db4b7b5b490e",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1m5Pvr1MYZ3dtv0tZSOUTRFfTsFgg8j0tDjomfjHKDuU",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "606d43c3f2392e2b001516f62cbabf47",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1clkddKdq2Le1Z7cpmNyfrBxdZrza6wgvihOoHNt5ZCX",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "8d11629934190faf6f702584f5dbbb75",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Fg2ETkeVgdSBoMnS8LMVUV8MkO54uvkUB6bLSoN3Dxs",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1rWSMRCM7oUYd3bUBl1wsGhAtQKOn4jiJ7YZJfQJYURU",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1jfGAYVqZR0Jeaw0GoMnpPDpsb1tBQCS5COF1a02Fi5U",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "13uTtBAWwBhIx1yXUWEy1rCwutS7J9QIfC6n7kaNWquT",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "cb69387cd8d2509f0dfb1f4a6c905d0d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
