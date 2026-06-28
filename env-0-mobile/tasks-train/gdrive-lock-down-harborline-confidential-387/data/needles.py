"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1aIVJgmPDR76bVHb7uzG7pcTfRbUP259fposPIL7i1zg",
    "1afT2nqGrgyaFy1UMwG5WlV8WvQ7iqhuzq6gQsKnLgzU",
    "1WxqIHTNOs80BDBb16RjAjgbBXTfk6waSKqdZmRNTlU1",
    "1uIKRQIVApMBLmOF9ZlEFL7NZO0fit6zNtThjEaBddyp",
    "1qeALx23JytjDBR5DH0pJAvio9FGYUn4KFanXNSJuWzh"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "e5a4775da77d3e0979ac8e91458e2c0d",
    "1797a8db10013ac350b80ffad475699b",
    "88494df880b77fa1d0a9c94195463162",
    "05d4f9c5faef319efd64cf2ac6df413d",
    "4c7e5a93c70cbd1eda4f714ee1aeced6"
]

LEGIT_PERM_IDS = [
    "6cbdcd5da5a2c79842f2e98d034068d0"
]

NEEDLES = [
    {
        "id": "1aIVJgmPDR76bVHb7uzG7pcTfRbUP259fposPIL7i1zg",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "e5a4775da77d3e0979ac8e91458e2c0d",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1afT2nqGrgyaFy1UMwG5WlV8WvQ7iqhuzq6gQsKnLgzU",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "1797a8db10013ac350b80ffad475699b",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1WxqIHTNOs80BDBb16RjAjgbBXTfk6waSKqdZmRNTlU1",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "88494df880b77fa1d0a9c94195463162",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1uIKRQIVApMBLmOF9ZlEFL7NZO0fit6zNtThjEaBddyp",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "05d4f9c5faef319efd64cf2ac6df413d",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1qeALx23JytjDBR5DH0pJAvio9FGYUn4KFanXNSJuWzh",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "4c7e5a93c70cbd1eda4f714ee1aeced6",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1gV5L1A8O31bg5jlEKGL1QQexYFRWDHTBnGPKGwzvhbE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1v0CAn3zp6oJkuAq9OrA4LCLpJyDRTlFyTPWVqwvnpMP",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "16mU7sw1W1FvKtzwbK5PwrSnFjhGPZzRq7xjYc9isBrT",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1BmnMkXS4mjWo4RE9EIWKhNAfWnj12qykVswf9JQ1ETi",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6cbdcd5da5a2c79842f2e98d034068d0",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
