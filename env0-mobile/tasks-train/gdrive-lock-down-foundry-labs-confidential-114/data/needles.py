"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1AknakkTXKBwC8uw4iq18nmsQLrzWCzcavidHDhaFHxo",
    "1Gf41sxYrCLzSLDZt24xdLCeGfvKW3RawyVAdXXG8Bvh",
    "1OGNWbwDZlR33fN4VuDALZrnAZ1LPmK2cs4S3hBfp7s6",
    "1A9Lqf1F94IVQhAPcuhlV3FQnzsfECmpoht1HDwF5k5p",
    "1ieSg89TJyYNlq6SP0QJ7keUdbCle5DNBFGw6dUvNYpc"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "319329936e73ec4472435d9836200d83",
    "c59ade0c9ac176077b4f0d3c2b89085b",
    "601a3071b1de89be22261cf9cc53483a",
    "436f27ee1ef3b260e50bdf19d92e9066",
    "2eaf724f3f79eb67af28eff6700b7a25"
]

LEGIT_PERM_IDS = [
    "f4d41c622b882d960b6c19e780591a91",
    "1c7480e3411498cded563e91c3ef7049",
    "73330c55151ead22b5d7aa33f86b7860"
]

NEEDLES = [
    {
        "id": "1AknakkTXKBwC8uw4iq18nmsQLrzWCzcavidHDhaFHxo",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "319329936e73ec4472435d9836200d83",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1Gf41sxYrCLzSLDZt24xdLCeGfvKW3RawyVAdXXG8Bvh",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c59ade0c9ac176077b4f0d3c2b89085b",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1OGNWbwDZlR33fN4VuDALZrnAZ1LPmK2cs4S3hBfp7s6",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "601a3071b1de89be22261cf9cc53483a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1A9Lqf1F94IVQhAPcuhlV3FQnzsfECmpoht1HDwF5k5p",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "436f27ee1ef3b260e50bdf19d92e9066",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1ieSg89TJyYNlq6SP0QJ7keUdbCle5DNBFGw6dUvNYpc",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "2eaf724f3f79eb67af28eff6700b7a25",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1dl1nWeCA6RUuzsbdO6nwk1SZofHY3ksM4cBkpzU9ekl",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1BJooKeIN2tDPh9RqU4bQXJYVl0x1f8YW064UAa6stu4",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1tU6cwlwL7mscYXY5rStftxNCYObk5Qf7eJKBMNFVUdU",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1wAQnYICkJpcxY8810wzxGkrUOkcz3lJ9EkSrNLQ2z14",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f4d41c622b882d960b6c19e780591a91",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1omu5AzlfInRtXQ6crnskosBCYLmgUu9afth7GQ9Ijw8",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "1c7480e3411498cded563e91c3ef7049",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "11WlN8NZwIUah2PNq9NaQddrUshwuWnebjqKxJFzV9RI",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "73330c55151ead22b5d7aa33f86b7860",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
