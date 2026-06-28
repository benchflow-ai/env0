"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1GTLVqNsljOBIvgOlk5MjwaD0cSOaUdR8UccwYlqg1UV",
    "1Cc0kWntbl6WiDICGUdSL6bIvz6eu6GlD3TSwbA7ycjm",
    "1cjzmA2zRDFWmPJAzr4NGT3ZKofWQ0zvdkyoJvmDn8Ws"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "486738632a0a4e5b4fedf3d2cd76861d",
    "54d5a8ba89a4d16cb44ecb37d019b7fc",
    "eaf850460c4600d3b6f6295ae00228ce"
]

LEGIT_PERM_IDS = [
    "2423e9add9c493bb4b7984bda5b2677d",
    "6bbd8f5d370bebf007fcecaea05b2ce9",
    "99c62e9b2cbaa4c3ff9778934ad4bbe4"
]

NEEDLES = [
    {
        "id": "1GTLVqNsljOBIvgOlk5MjwaD0cSOaUdR8UccwYlqg1UV",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "486738632a0a4e5b4fedf3d2cd76861d",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Cc0kWntbl6WiDICGUdSL6bIvz6eu6GlD3TSwbA7ycjm",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "54d5a8ba89a4d16cb44ecb37d019b7fc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cjzmA2zRDFWmPJAzr4NGT3ZKofWQ0zvdkyoJvmDn8Ws",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "eaf850460c4600d3b6f6295ae00228ce",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1KO4H8hWBIoYZZmPnNOmOL32eOxuYEjt3gfSPSLaz28i",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "17gUafc2q2TJ6KoEhaIKEJvvFvwabGJEkFB8t8hRXOfC",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "14Mv1CbokmSvmEUQcgTepseXigTrlGd3cCzGpYY72XcJ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1AaYHpqph0IMdHmeP8d1lw62X9BxjA3YEXllCsBktcgh",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "2423e9add9c493bb4b7984bda5b2677d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1zzR4bIMgIbqd4uxWANk0cPl8gq69MB67nsKx2XvswGp",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6bbd8f5d370bebf007fcecaea05b2ce9",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1v76UxiPGbsh9EwSibGoKOlHXX613UcpdZmRSZ3RYioP",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "99c62e9b2cbaa4c3ff9778934ad4bbe4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
