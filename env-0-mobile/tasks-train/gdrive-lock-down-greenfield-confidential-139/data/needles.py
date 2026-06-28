"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1W6SWfXenI0j1KT3xnzIGd8BDozzcS9T8HjnewJA85JW",
    "1ML5149Xv6Y58YwzpbnG23ceTLsJhZPjwkGn9neNw5ni",
    "1bFf9TVAIW7B1DwaKqj0o6FCyRPO6dJhL3VUDruLxoi4",
    "1352DLVBsd8LwjCUQFx44mJLOAFEmOMtzB6Q0JAtbGcA",
    "17DR7BWodSfPFKg9yN14SSQUVZv543YJERviAxXiVPJt"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "814dc8eabdbc8641053add434e002daa",
    "8c04ba0095a93147134cdd274c0f4b12",
    "56f709de5e742580d83f3f30d9371102",
    "14b058704d59a425b3fdcad22a745f76",
    "8e65a9968945cf8a66e618eb38ccc27e"
]

LEGIT_PERM_IDS = [
    "7dff70d125a7b748b514dc9fcb684c68",
    "25a3cce42fbb974e527eb5e149064aef",
    "38ce33462f5cd8218150d650d0705b4e"
]

NEEDLES = [
    {
        "id": "1W6SWfXenI0j1KT3xnzIGd8BDozzcS9T8HjnewJA85JW",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "814dc8eabdbc8641053add434e002daa",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1ML5149Xv6Y58YwzpbnG23ceTLsJhZPjwkGn9neNw5ni",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "8c04ba0095a93147134cdd274c0f4b12",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1bFf9TVAIW7B1DwaKqj0o6FCyRPO6dJhL3VUDruLxoi4",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "56f709de5e742580d83f3f30d9371102",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1352DLVBsd8LwjCUQFx44mJLOAFEmOMtzB6Q0JAtbGcA",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "14b058704d59a425b3fdcad22a745f76",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "17DR7BWodSfPFKg9yN14SSQUVZv543YJERviAxXiVPJt",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "8e65a9968945cf8a66e618eb38ccc27e",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1gTn8vimZdv2HngnxUjeiLvRg5jYJlZMk93buCxPi0xG",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7dff70d125a7b748b514dc9fcb684c68",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1RqPCBmAxJxqCnBVf1Kj6hcTsq5mIK9t5dgZdPN0Yyxv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "25a3cce42fbb974e527eb5e149064aef",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1pAlWPYGZtd7cI451XduUw24wTJXYB5FIWQk8x2hD1uB",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "38ce33462f5cd8218150d650d0705b4e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1PhtFwMIwKuF5Y7e9qYqrVv5Ty4SbaGx54TfK05P40bv",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1DwZ556ik0Pf19koXD285LDEAhmEsx74xslZHkafyoMr",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1bud17xxhcJunK543LH4CiMtW030sckSCh8cllMQzNf7",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
