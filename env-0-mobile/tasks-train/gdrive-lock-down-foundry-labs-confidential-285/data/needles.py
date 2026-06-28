"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1Bw8Hzl63YhuKaYEJ6QlO2L1moNWKTbij00SpDNDgg1m",
    "1y68j8xAMt3POy02kU7TZHJ4PjVGbmZji97pi3uiA2xn",
    "1HsBB5DUia3qWIGPNJ3aMr6tEjICx3GOg38dmXkhELFN",
    "1Ib1Ur87v3uIASOoEt3EQPeC7PKWk56J4lFEX6mXqkf8",
    "1tDrYQFxAnGvuWyWrf58Vwta48CRadrQnweuN3U1YdF9"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "7c4c5ff2f59b0d20e2a3946d72346d5e",
    "bb5b7846f7c81091cc144220dfe23302",
    "428293f02d82ecd729e653612ad8212d",
    "fad15fc1d4a1470b6d3cdb1388841663",
    "ac2218a432d001f010cc6b119f6254d4"
]

LEGIT_PERM_IDS = [
    "8c3c351b18222f3c68a25b42a354fe87",
    "8af87ab8a1251d13353baa64933fff23",
    "d21fa3a29df4de529b56d23e0df25522"
]

NEEDLES = [
    {
        "id": "1Bw8Hzl63YhuKaYEJ6QlO2L1moNWKTbij00SpDNDgg1m",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7c4c5ff2f59b0d20e2a3946d72346d5e",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1y68j8xAMt3POy02kU7TZHJ4PjVGbmZji97pi3uiA2xn",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "bb5b7846f7c81091cc144220dfe23302",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1HsBB5DUia3qWIGPNJ3aMr6tEjICx3GOg38dmXkhELFN",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "428293f02d82ecd729e653612ad8212d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Ib1Ur87v3uIASOoEt3EQPeC7PKWk56J4lFEX6mXqkf8",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "fad15fc1d4a1470b6d3cdb1388841663",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tDrYQFxAnGvuWyWrf58Vwta48CRadrQnweuN3U1YdF9",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ac2218a432d001f010cc6b119f6254d4",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1sQgL6s1PMpvO09cZNe4dXt7fhy7bEU01XA0YWPbbzzl",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "8c3c351b18222f3c68a25b42a354fe87",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1tnBvuK7Ah32RgsDaKVE8xTgeI6WmurzLSXn5VgfS0r2",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "8af87ab8a1251d13353baa64933fff23",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Rvn09OMoMME50Zk333wySKDcnZGan6ygw8Sko3UjCDO",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d21fa3a29df4de529b56d23e0df25522",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1yJMCwi5zeeQEt8MFpVMDOxEaiIwz3UdeNrnvPjkjOiM",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
