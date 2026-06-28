"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1thoVhEOzPnD90zF4bkLcEhw7HDTXMfLXFrU95TDweIs",
    "16Vl79gn2AMsRsCK6VSKiQ0OSjxViMsJ7781PdkOXgWW",
    "1RHRCoDPOxz1FsezOzAbNsWJuZLa5fDwpqlfYEVtjDPj",
    "1N7k2X0XCBvJshrrBF5yBsPMiDnTGdFyTLhd0Mxz0ecs"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "b6dd31784bdcc32f7ba4848dbcf2aaa5",
    "4e20120202f229e26dcbc8dbe48fbffb",
    "d7415c4651a2112f1edd0ce169f6b9c2",
    "052a7f569c5c49bad52ec748f86f970d"
]

LEGIT_PERM_IDS = [
    "a691bbc9fcb6fc838a64f5bb1c347ab4",
    "498643018896f4d082ca1bdc47933804"
]

NEEDLES = [
    {
        "id": "1thoVhEOzPnD90zF4bkLcEhw7HDTXMfLXFrU95TDweIs",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b6dd31784bdcc32f7ba4848dbcf2aaa5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "16Vl79gn2AMsRsCK6VSKiQ0OSjxViMsJ7781PdkOXgWW",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "4e20120202f229e26dcbc8dbe48fbffb",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1RHRCoDPOxz1FsezOzAbNsWJuZLa5fDwpqlfYEVtjDPj",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "d7415c4651a2112f1edd0ce169f6b9c2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1N7k2X0XCBvJshrrBF5yBsPMiDnTGdFyTLhd0Mxz0ecs",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "052a7f569c5c49bad52ec748f86f970d",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "134YS3IVbkWYe8WjbRGlClD59VlSYkk6dSOd3vihob9g",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1gT6h95iEwv0Ko0z04gNVHN0MqfijXDcq35CpBKYaTcL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1d7onsQq37DhCw5YFmr47pQ0xvzkEGuagQfTotj8pi48",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1LMQOkSDLMzPTj3B4LLepCIFG3iUDwKKzbxxCWOXLbbl",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a691bbc9fcb6fc838a64f5bb1c347ab4",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1OOUIfaw2IGejVyU9lKa4LfE4joCHDPgnPqetVg8FQN2",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1SIVWhmwzg71l6RLag83J4kKD9UoxDsxnigCACVdYUFa",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "498643018896f4d082ca1bdc47933804",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
