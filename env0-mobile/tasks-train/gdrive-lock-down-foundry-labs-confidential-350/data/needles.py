"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1RXo5b1zyXziFAZQr4f7dmCvuuXwXXpUFhs2hioICB4O",
    "1FOoNO1mTIjXpNf2gVD9exqqfQqZSlwEAbqT1QFrHL5j",
    "1tYv81MoN1X9weMOtQAN3hDzvtGKyARtEfIqghw2bW5k",
    "1M16YcfDaONZp5EPYSWjaJyPJLL5PuKkiU7K5VLUXwVS"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "0ee315b16207a9fe88743552d1713fbd",
    "c0b1f50db3dd6716e0c51a34fbb1ae4d",
    "f820763f9ebd329b9e87464a04de14f8",
    "1835a6cce8bdbb5931cd3a61d9fadb01"
]

LEGIT_PERM_IDS = [
    "a35aaef4f07853b4c2028fc504862029",
    "1724515725ed7013898710feb7393231",
    "74c57db138aec3e2863f3ecd815ae2d9"
]

NEEDLES = [
    {
        "id": "1RXo5b1zyXziFAZQr4f7dmCvuuXwXXpUFhs2hioICB4O",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "0ee315b16207a9fe88743552d1713fbd",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1FOoNO1mTIjXpNf2gVD9exqqfQqZSlwEAbqT1QFrHL5j",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c0b1f50db3dd6716e0c51a34fbb1ae4d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tYv81MoN1X9weMOtQAN3hDzvtGKyARtEfIqghw2bW5k",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "f820763f9ebd329b9e87464a04de14f8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1M16YcfDaONZp5EPYSWjaJyPJLL5PuKkiU7K5VLUXwVS",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1835a6cce8bdbb5931cd3a61d9fadb01",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1WUiyOLcwBozuY5vdtWV13KcRKzrmDg0RcxaDOI1V6n7",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1X3YfUmaeMhRFFQc5LDNkCVMdB77HGM60MEiJKYo25Zj",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a35aaef4f07853b4c2028fc504862029",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "164QgDFlUIIiPAn39fJUrCN5zJk5GQZycJoqj8GuLp0U",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1ddxvLl8x1oG9psVl8D1MnDQbpKUX6fCz9KNCLIXmajv",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "1724515725ed7013898710feb7393231",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1IzZhwScby0PpPnpTDOC4gxtVOTsSCKUUtsdNlPksI3r",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "74c57db138aec3e2863f3ecd815ae2d9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
