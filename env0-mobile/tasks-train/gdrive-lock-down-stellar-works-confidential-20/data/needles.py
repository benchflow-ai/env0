"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1BX6SB1oQZRhy3ZurZ0ZkWdmctHqWIONepmRSGgbyCCn",
    "1XAChvscveonwRqXYgUoHWmwWBqEdPamHFLk3upwSBdk",
    "1PLtnQBDXVOzINeNJVSHm5RO15vliMdB7Ak5CAh4Jp85",
    "1k9zxjKkApkoWLyooA0q8wJO4dbaHeapkbPDpr8DG0LR",
    "1LjGHctQV7IbdBV8V28hCq0XDMCn7fS7NqCLXbOgXFJ1"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "9b98cc56ec27c74486ef7b2245f77e62",
    "6fe617b1477fec07ab2be6a24d74517e",
    "61985527b0b597dd994d374bda073a32",
    "5f3ba04c39e80d30b92712d9e647833c",
    "497c912f25e28b5bf4105e18911d1779"
]

LEGIT_PERM_IDS = [
    "24e1bfde7f2e08be8e8da454d071f76a",
    "88fd434fea3cd327c27216a51b9fdef0",
    "fe40abc6cc1ef41a334f820cef42711b"
]

NEEDLES = [
    {
        "id": "1BX6SB1oQZRhy3ZurZ0ZkWdmctHqWIONepmRSGgbyCCn",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "9b98cc56ec27c74486ef7b2245f77e62",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1XAChvscveonwRqXYgUoHWmwWBqEdPamHFLk3upwSBdk",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "6fe617b1477fec07ab2be6a24d74517e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1PLtnQBDXVOzINeNJVSHm5RO15vliMdB7Ak5CAh4Jp85",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "61985527b0b597dd994d374bda073a32",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1k9zxjKkApkoWLyooA0q8wJO4dbaHeapkbPDpr8DG0LR",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "5f3ba04c39e80d30b92712d9e647833c",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1LjGHctQV7IbdBV8V28hCq0XDMCn7fS7NqCLXbOgXFJ1",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "497c912f25e28b5bf4105e18911d1779",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ZwSJZJnHDTAI1cwaoTZMWLueii2VhtTllVhR8seUKeT",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1mfpHw3DtD9dUNWQTUih6bk4mJl5NCw1vckcj3IdRsBF",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "24e1bfde7f2e08be8e8da454d071f76a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1YfAR0DL5KQi4M1psdeHJT5FP7UjhjrdLd48Si83OECj",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1mp6edP1CKIo2JxwXQHWoVNl67dhs2FR1iCB33bsa61I",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "88fd434fea3cd327c27216a51b9fdef0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1INxTOe4HZLwOkyre0ZJzmFq7eG7YYmiu75f4EV10f6W",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fe40abc6cc1ef41a334f820cef42711b",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
