"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1lfhvEg40hPFSQnRmVbGNCy4dcUQmGjT5AXhMHKHlptI",
    "15qTPY2t9Lmnr2BQFXCyl7V0cJSZOBvtMQtiPfm27oNh",
    "1J9zs1ESNYJmj1bgPBpmgp8HPPWpv4A0DhOmXn6w3ObY",
    "1bvmODwVtoPOeQo1pZ1cQgF1C8HSX6XAIrjQrKsf1LAR",
    "1Kj8XzAvqn2MkHiaO7rIbGoAJsP5CNvMOUJEKqwD8Yl1"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "f95af8e95000d0d64b43fe43e018ec95",
    "0f7f81ea8c88c6464ec69b43e5c51d14",
    "2b905b7728091dde0d5a88a859754f81",
    "721d333865d5c8f8f5b70071f5b9c522",
    "84b79349ef2fb5915faba5160ad55724"
]

LEGIT_PERM_IDS = [
    "b190c0cab02444ec8a6f10bc2a441fad",
    "35c433946230f4aecff7a2a4ea6923c2"
]

NEEDLES = [
    {
        "id": "1lfhvEg40hPFSQnRmVbGNCy4dcUQmGjT5AXhMHKHlptI",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "f95af8e95000d0d64b43fe43e018ec95",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "15qTPY2t9Lmnr2BQFXCyl7V0cJSZOBvtMQtiPfm27oNh",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0f7f81ea8c88c6464ec69b43e5c51d14",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1J9zs1ESNYJmj1bgPBpmgp8HPPWpv4A0DhOmXn6w3ObY",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "2b905b7728091dde0d5a88a859754f81",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1bvmODwVtoPOeQo1pZ1cQgF1C8HSX6XAIrjQrKsf1LAR",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "721d333865d5c8f8f5b70071f5b9c522",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Kj8XzAvqn2MkHiaO7rIbGoAJsP5CNvMOUJEKqwD8Yl1",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "84b79349ef2fb5915faba5160ad55724",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1VzaXSKTKszV7vRiAhTg59GRV6T1tqgLT7coIAec2zBf",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1JM23kLXiasOSvD9PkALHSBMUj9kpVXCAv7S48Zf94t5",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b190c0cab02444ec8a6f10bc2a441fad",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1HQf4rDEtCnNWY5FKi3wGQdUDgFZzgCsOZq3IJegtxjq",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "35c433946230f4aecff7a2a4ea6923c2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1EPQyEruUlKyUsytdodw3I8UnNxtZll9iV9oqyAPF3j2",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
