"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1y1GciTDLTEOPuREkqzA5u3nnO1gx8hQ9SLKredMG61d",
    "1eEsJlPSf3o4bConzXGXgjf3Sbsj0K4oP7OOFqpkfjoc",
    "1sjP2wG5ROGgkDoycbTfgfRE7pjNqnjab8x87Iqx946q"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "b2566bea0d9b0427ceae5ef335a70434",
    "92998271f93e9f6ca898402f4a3d1458",
    "89b46a3a9c47d8dbfa18061f44c0f598"
]

LEGIT_PERM_IDS = [
    "26f1c258e37fd52f3c8e9ddbf1493d44",
    "8acd2e5598193e6fb30c53bf82cc6954"
]

NEEDLES = [
    {
        "id": "1y1GciTDLTEOPuREkqzA5u3nnO1gx8hQ9SLKredMG61d",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "b2566bea0d9b0427ceae5ef335a70434",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1eEsJlPSf3o4bConzXGXgjf3Sbsj0K4oP7OOFqpkfjoc",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "92998271f93e9f6ca898402f4a3d1458",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1sjP2wG5ROGgkDoycbTfgfRE7pjNqnjab8x87Iqx946q",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "89b46a3a9c47d8dbfa18061f44c0f598",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ga87sMrexxlxuPmXaZhXUeNpappTYlEk3g2ohATvBvZ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1RyLgxeZ0rH9QqFlDj3LsCBxmDbAn04smJzlkAEoQ01w",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "26f1c258e37fd52f3c8e9ddbf1493d44",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1nbzyU5cpKJ7QgipvMkw4JA61KNskUML2lecJS4Ud572",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "15Ryh44rcFUT8hvbp8ohSmFpkWc1GMj4r7CnkNYxpYtP",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "8acd2e5598193e6fb30c53bf82cc6954",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
