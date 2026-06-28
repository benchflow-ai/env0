"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1rsD3qbMyJzt1tWtBtnJLJynk4wL4em4334Ux9jGvW30",
    "1d9F8yL7ZXae5C9EONcEQua0SNDs19DODYywCvqKzpLE",
    "1hVIwSMAQJaGn5OxKOjHWWjhZZb0zPapNQOXPd1URIj2",
    "1dcQqBvCyTfvxJqV875XsF7Ah1AahprHhJtekbolG3w7"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "f5bcc45258138e9c02a1e3d8a3f07cf0",
    "4bc570a9857b812f0b7e6f8f738ca5c5",
    "232c5e115275ee7f086b3e14c04b33ec",
    "a84556b3b51be063c7396f827624ea80"
]

LEGIT_PERM_IDS = [
    "dcdeefa666e7ec78cc505af5dbfda447",
    "c304bae7e64fdc7e383894fc06b49659"
]

NEEDLES = [
    {
        "id": "1rsD3qbMyJzt1tWtBtnJLJynk4wL4em4334Ux9jGvW30",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f5bcc45258138e9c02a1e3d8a3f07cf0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1d9F8yL7ZXae5C9EONcEQua0SNDs19DODYywCvqKzpLE",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "4bc570a9857b812f0b7e6f8f738ca5c5",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1hVIwSMAQJaGn5OxKOjHWWjhZZb0zPapNQOXPd1URIj2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "232c5e115275ee7f086b3e14c04b33ec",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1dcQqBvCyTfvxJqV875XsF7Ah1AahprHhJtekbolG3w7",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "a84556b3b51be063c7396f827624ea80",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YxBGjuplDV9gN2n5sib4yL0zF4IQKvxQuHm0Ku9jLQI",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "dcdeefa666e7ec78cc505af5dbfda447",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1YJuCLt7DTIOA6Jyb7bkQwBIWyRcxogjWFpOyZpp5HTA",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1KNdWjkaq5k4H2yOXmfgLhraHPLHcZYsU1HihL9Ig1mg",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1xa5Uh9mM2H4dERH1SQVf8UOF7zMsknheXvZ3qBCPraM",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1rxBxM0XcHsWHPIE6b2XbGenzYfnFQ1w8DkbdaVaNnq0",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c304bae7e64fdc7e383894fc06b49659",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
