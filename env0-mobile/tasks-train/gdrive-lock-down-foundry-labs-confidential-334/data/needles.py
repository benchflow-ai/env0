"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1rpQEFPIirNSel8ogCjaqf1vgpcMRAi6l74v5gGk0IF2",
    "1kAlOoz3w11aMQQKISIWoU6fR2xvSZgAzZKbeBkL0hrl",
    "1XUgE78GDaem3iRKpzHmWHhhuIh9P6BOQWnFHKoQERPg",
    "1KxWllvNDE1YbtJWGXo83ax5IA4jtGq685lIf9V4lQX4",
    "1Jjr3NAxzP8wNunDGxiQ17ujvlALbBHkHdWfArk20i6c"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "8176ecad126671f3a33862b440daeb15",
    "70a5c0a76eb7a2ef38ff50a0bc9834ca",
    "0e6af27f2736d1277d473230b779ae8c",
    "84b6a34ed1f087360c681c3492ab6b5d",
    "bba1e787cd4f70501c8a10a0fec4738a"
]

LEGIT_PERM_IDS = [
    "7f154a139ffa760d3beaf78e5adb03b7",
    "bbd7310d10b2a611133b962787b38bc1",
    "6e584feb5663f46fc42ba85f4419bdb4"
]

NEEDLES = [
    {
        "id": "1rpQEFPIirNSel8ogCjaqf1vgpcMRAi6l74v5gGk0IF2",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "8176ecad126671f3a33862b440daeb15",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1kAlOoz3w11aMQQKISIWoU6fR2xvSZgAzZKbeBkL0hrl",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "70a5c0a76eb7a2ef38ff50a0bc9834ca",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1XUgE78GDaem3iRKpzHmWHhhuIh9P6BOQWnFHKoQERPg",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0e6af27f2736d1277d473230b779ae8c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1KxWllvNDE1YbtJWGXo83ax5IA4jtGq685lIf9V4lQX4",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "84b6a34ed1f087360c681c3492ab6b5d",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1Jjr3NAxzP8wNunDGxiQ17ujvlALbBHkHdWfArk20i6c",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "bba1e787cd4f70501c8a10a0fec4738a",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1v9HTWGuCENQjI4hgCf42N7kmS1f1u3q3BC6xAhiDYKv",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7f154a139ffa760d3beaf78e5adb03b7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "13b84lde3bu0Df6QdUzAb6eJHaQTMr100DigU7e8JgOp",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1BvhV3etI6pjttfaxdRjCge54KTqcJx4pRoanrj41rHd",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "17dA1NikL3GpP2q7MKiNfJmgQaJ15ARe1f3MSD84ybiS",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1VPxEhBz3XqnlrFwAg0skzv8PEoPsR3h8LzxmC5VoIB3",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "bbd7310d10b2a611133b962787b38bc1",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "13aJetsCDaWlgpWhKBW1XD5ZkJzOR9kUVyi9PW2MjDSg",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "6e584feb5663f46fc42ba85f4419bdb4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
