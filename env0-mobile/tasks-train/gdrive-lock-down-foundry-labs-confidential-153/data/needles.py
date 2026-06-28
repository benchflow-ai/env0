"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1KiKXVfc4L49tEDyZDeggZZtxme2Hz0Ojgsq0RwcvdHb",
    "1gCjvR19Lr2uPFaiwOCB0rsSlaZLUlf7ff3PDs5GHvoY",
    "1mhiWvpwX48ZV12Xquim2DA54NakMVMFaWT4ZqZaHOj8",
    "1FfCsJIH1iqcLG1MWPSMmz8i3cqargYiES4btj8bsfSN"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "127f617781280eba45044651b0512ccf",
    "eccb45e2877ffd66fabb30493ca68bdf",
    "a94b3aeeb6560a6e1d61ac505cb7bf8f",
    "58c072c6f8c4ea0600a68d95c7eaeb6e"
]

LEGIT_PERM_IDS = [
    "fe9fd37e3890913ec65fd43c13e2ab3c",
    "086d5fd935bc9ed23c4102fd637d3126"
]

NEEDLES = [
    {
        "id": "1KiKXVfc4L49tEDyZDeggZZtxme2Hz0Ojgsq0RwcvdHb",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "127f617781280eba45044651b0512ccf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gCjvR19Lr2uPFaiwOCB0rsSlaZLUlf7ff3PDs5GHvoY",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "eccb45e2877ffd66fabb30493ca68bdf",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1mhiWvpwX48ZV12Xquim2DA54NakMVMFaWT4ZqZaHOj8",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "a94b3aeeb6560a6e1d61ac505cb7bf8f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FfCsJIH1iqcLG1MWPSMmz8i3cqargYiES4btj8bsfSN",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "58c072c6f8c4ea0600a68d95c7eaeb6e",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1hurmnJBUQqebOrKDdVorb89fr2upgMxA1KTZ609yjuF",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "fe9fd37e3890913ec65fd43c13e2ab3c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1PMQi5wRs97c2dSJsyj9Mlw2mIU7Yl54VkaOF4xVl6cG",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1tObgg5N5ebddGkmwMAXncxbl900RJkItmXpZX6BvZO9",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "086d5fd935bc9ed23c4102fd637d3126",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1a9w3TWd20vczOa88NaJaP4GdhdGm7hSSX04u4Nl1uJ1",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
