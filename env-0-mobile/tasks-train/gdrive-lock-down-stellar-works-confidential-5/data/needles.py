"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1QW4MqVI7Zbs1YnNHP5hmxJdgIj7WPYZqEfMjHx7lRQt",
    "14PKMlncvZ6jIbhRfiGzfdyTX1gXUNJDThhMMyfwdgvj",
    "1dtgQmJ6FtlZTNZ5hT2BzgZvwlHW06YzFfHaC1Yxlacy",
    "1dORHFObzlDREhBUT3DHVdugWn7vQzD08iUqbNtjbkxp",
    "1nQWlXlxgN6pt8NTa9f4drHPnNvXnGc9hG0aE8luhbEU"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "f1b232e6a1eb47d58ca83ca09aaccabc",
    "fe654fd327ce754a7b79ca9d4d9d8478",
    "b03ba3c0c15bfcc9ab956b1b5e7bc818",
    "cd5b5fcf08f18e42d66bf3062cd39d9c",
    "fb01999f96a430ca7ab6fa8eee3f3620"
]

LEGIT_PERM_IDS = [
    "3c94af87b38173d264f6527248983765",
    "aab5d006098170c76bc580b315d83167"
]

NEEDLES = [
    {
        "id": "1QW4MqVI7Zbs1YnNHP5hmxJdgIj7WPYZqEfMjHx7lRQt",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "f1b232e6a1eb47d58ca83ca09aaccabc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "14PKMlncvZ6jIbhRfiGzfdyTX1gXUNJDThhMMyfwdgvj",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "fe654fd327ce754a7b79ca9d4d9d8478",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1dtgQmJ6FtlZTNZ5hT2BzgZvwlHW06YzFfHaC1Yxlacy",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "b03ba3c0c15bfcc9ab956b1b5e7bc818",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1dORHFObzlDREhBUT3DHVdugWn7vQzD08iUqbNtjbkxp",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "cd5b5fcf08f18e42d66bf3062cd39d9c",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1nQWlXlxgN6pt8NTa9f4drHPnNvXnGc9hG0aE8luhbEU",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "fb01999f96a430ca7ab6fa8eee3f3620",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1rvyy89wI238wfdHRfryVMxWsLJuKZgoONbl8mmDnflQ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1HulBGt75e0rOLoJ4jtXrCT1YBvzbZVTWfVJWoCMC0F0",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1v8J5PPSOrGJar4EAnIQl75urVtuxuagN8XBe48Og9LS",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "3c94af87b38173d264f6527248983765",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1czXqWH0QDGJx389aUc3vVyiOGLe6y6kvhyqgai9loq0",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1POip1hjrHbuxwQlxbbBOUVyCHoxefq1qtAGkFQT1Wke",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "aab5d006098170c76bc580b315d83167",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
