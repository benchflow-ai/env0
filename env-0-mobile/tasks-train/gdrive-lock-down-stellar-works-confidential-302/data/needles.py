"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1pLFUmJLfVkzj9Wq0EDHfSkzVBikQJG5KXDHqgauGiz8",
    "1ufmpBGBeTxbOwaJMwqZiJchEsSCVAlhUmqeoDcyC859",
    "1hYrONlD54YXGVubSV1xc51iadR7xl3xDcCAOvv2bvQu",
    "1iefjpCNTHdkXiosN27V7CCQJD7Rg4xa9VciZjU5KN30"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "a555839870171e139c8fca4394dcb2d9",
    "792f2744e050be73179c3f153ff9a0cb",
    "48260cc11eda62a33211560361b81c7c",
    "5ecc7ae885d610ae3dc5f69bf0351d5c"
]

LEGIT_PERM_IDS = [
    "c8c85c50b721e34828675911ab31675f",
    "dff3d5fc18710da02a68e478c0613656",
    "4f4d4855ddf94f27e58b9916c90f7430"
]

NEEDLES = [
    {
        "id": "1pLFUmJLfVkzj9Wq0EDHfSkzVBikQJG5KXDHqgauGiz8",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "a555839870171e139c8fca4394dcb2d9",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1ufmpBGBeTxbOwaJMwqZiJchEsSCVAlhUmqeoDcyC859",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "792f2744e050be73179c3f153ff9a0cb",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1hYrONlD54YXGVubSV1xc51iadR7xl3xDcCAOvv2bvQu",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "48260cc11eda62a33211560361b81c7c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1iefjpCNTHdkXiosN27V7CCQJD7Rg4xa9VciZjU5KN30",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5ecc7ae885d610ae3dc5f69bf0351d5c",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1bSN7XeMhBwEO2k7HaytQdVLvy6PR9Wiw7VOcLv9tp1R",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1dOBD6T7FDsLV7xAs9c8LNPhBRMo22ZZ9SXt2pgpcLdz",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1pcsKW8iPrWWZbvp39REg6gYFxzKkNrKDkY6VW8xxKDB",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c8c85c50b721e34828675911ab31675f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1mb08A2T5WwzirPWH6FPcKQ7kTX6f7qw9Pod7A99gWjW",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "dff3d5fc18710da02a68e478c0613656",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1HxLQ3YYA65xHmQjTWlfIjAIp6QPFb7Sk0ppTj4HF8af",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "4f4d4855ddf94f27e58b9916c90f7430",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
