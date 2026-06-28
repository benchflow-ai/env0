"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "18rVjpVEDSlvs8ZEYDdHoGUbh0rUFoqePFNslfqBMJye",
    "13ju0wktsH5ZYv4JYNVuRhQ1x8UR9LxRqCdsmXXxNXGG",
    "1tW4q2BUMpk2RbvRHyYUOZufwTzR1vbWJHQWQzBz5vuz",
    "1IvlkvtLqdH7Jb2i7GXHocNdZyPdoL20hse2Kv3VpfbQ",
    "1vTDdAqLdjOJFeyvpK9SaexqZCGbYtHS6dGvftFDUhi2"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "5792837b52aca899897c4b1a1dc5837c",
    "0518d988107ce448b76bc216b2fd8c42",
    "5beaa0d6c4f72e0aefe9f0eeefc90126",
    "e2d5a1382ba38dd3e8c3ef6f90acb164",
    "5ae0aaf8de47d3dc9421d7fd01573d13"
]

LEGIT_PERM_IDS = [
    "8e1203ec70cc70e0f8c6d42fd57371ec",
    "9994816293bf5d91bd4afdc5cbbc9319"
]

NEEDLES = [
    {
        "id": "18rVjpVEDSlvs8ZEYDdHoGUbh0rUFoqePFNslfqBMJye",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "5792837b52aca899897c4b1a1dc5837c",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "13ju0wktsH5ZYv4JYNVuRhQ1x8UR9LxRqCdsmXXxNXGG",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "0518d988107ce448b76bc216b2fd8c42",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1tW4q2BUMpk2RbvRHyYUOZufwTzR1vbWJHQWQzBz5vuz",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "5beaa0d6c4f72e0aefe9f0eeefc90126",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1IvlkvtLqdH7Jb2i7GXHocNdZyPdoL20hse2Kv3VpfbQ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "e2d5a1382ba38dd3e8c3ef6f90acb164",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vTDdAqLdjOJFeyvpK9SaexqZCGbYtHS6dGvftFDUhi2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5ae0aaf8de47d3dc9421d7fd01573d13",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1yLocBNNgTsE8EX4k77zK0wWs4DeMSAOEwvoS9DsPukL",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "8e1203ec70cc70e0f8c6d42fd57371ec",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "16mYgPk06G5hm0zr9lYEFPRMS2E2yNkmrgzMg3Sv3pCO",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "17thyo9oMxj7sibKUqU34VoitpqWZWOcx623D0qr9OXP",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "9994816293bf5d91bd4afdc5cbbc9319",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1uMZN4ELHTjGtBtMKM7J4HaSciO0HicRwbfKB5OH2ZQ3",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1Cdw8w5zgvzM4ziNTdiSiBWjpkLyzXtnz3ceIZraMhNq",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
