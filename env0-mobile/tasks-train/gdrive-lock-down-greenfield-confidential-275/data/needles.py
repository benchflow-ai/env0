"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1prGNs5j9RaVd4UedZLbnRxhOrY24bvez5aMe00Bu5bU",
    "1Zj6uDkSvMuX2Ap8bBrdzb4VOwuSi65UrStzUhQDy2vs",
    "1uE24KN4GJlx1PBVIJDTsnm06mYQlQigN2zD422Tkq4r",
    "1aF4r3RoRqYmHQUvXl4nYXbtOzOpvi28oYJEcB5Ozqim",
    "1otImzv3l2BQW7ybs6xf0JADsfXHlBNGPxE8VK3awwUj"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "7d300baf20599949eed5ad8d6c75d05e",
    "cc77599f2f189e4813b4b2545a8f2a60",
    "e3edee02154e6824419f53ec1fa60ebc",
    "aee7ba4017717b4e1d7dd91a22ba97f0",
    "3df54e7a66c4e4c07b3d20ec63d15b00"
]

LEGIT_PERM_IDS = [
    "d55bdb9bce7ea1d5a8e78d79fba03fc3",
    "4c37a2523f9b7cd5e1def312207f229d",
    "ff600a4291f618a9d7e86c4849725a9d"
]

NEEDLES = [
    {
        "id": "1prGNs5j9RaVd4UedZLbnRxhOrY24bvez5aMe00Bu5bU",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "7d300baf20599949eed5ad8d6c75d05e",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Zj6uDkSvMuX2Ap8bBrdzb4VOwuSi65UrStzUhQDy2vs",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "cc77599f2f189e4813b4b2545a8f2a60",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1uE24KN4GJlx1PBVIJDTsnm06mYQlQigN2zD422Tkq4r",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "e3edee02154e6824419f53ec1fa60ebc",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1aF4r3RoRqYmHQUvXl4nYXbtOzOpvi28oYJEcB5Ozqim",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "aee7ba4017717b4e1d7dd91a22ba97f0",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1otImzv3l2BQW7ybs6xf0JADsfXHlBNGPxE8VK3awwUj",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "3df54e7a66c4e4c07b3d20ec63d15b00",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1TFMGKTKRvxRvwHpNRCZg23rNhVrtU7AbdKhTFSkkxYw",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "d55bdb9bce7ea1d5a8e78d79fba03fc3",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1LRSfRvt1b25JDcNmvS9rIpr8n7Eki1MIlFCkvooDZFI",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1VHaP7iYwOVIcUnwvwH9RmgMxhgXyM0VAutF9gIG5hPg",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1cm4qdzhfTcnNN6VmB8dRdKG4cpgPIKvNT6bVescm9Jd",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4c37a2523f9b7cd5e1def312207f229d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ky657b9Rxp3AZOzJAyaHRMUAR0w9CRRmgD8WOL81Zla",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1XgZLIoGN9XU5G2gXWaRzHOuzAr3ZjFD4VcgHDgWxGEM",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ff600a4291f618a9d7e86c4849725a9d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
