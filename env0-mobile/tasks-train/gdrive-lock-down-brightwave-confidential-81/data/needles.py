"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1pgUBDOf63q1ETZ4aITJgJlCkGnPL1R132v2M8JU6N1i",
    "1ViblvGMmMgc7NKYw6JT66xSpIWPCaflaU14VpTwGu8W",
    "1NZ73pdn60HXp0YgYGj6VV8l6ELU3s57kmsgIUgmtLMw",
    "1dPBl7XX5ij97JG93ZbzqRKLfBrQngfPlfm565UIqiZQ"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "a1eaefeb287a89482aafd5ee51125640",
    "bcdb77bac8518f94205f30128d894d34",
    "5d9fd2e44c2da4275675696ff282ea07",
    "8f90c770ea87aac540b79beae4472ef0"
]

LEGIT_PERM_IDS = [
    "ff7735385ff6edc86f7b7ccd395377dc"
]

NEEDLES = [
    {
        "id": "1pgUBDOf63q1ETZ4aITJgJlCkGnPL1R132v2M8JU6N1i",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "a1eaefeb287a89482aafd5ee51125640",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1ViblvGMmMgc7NKYw6JT66xSpIWPCaflaU14VpTwGu8W",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "bcdb77bac8518f94205f30128d894d34",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NZ73pdn60HXp0YgYGj6VV8l6ELU3s57kmsgIUgmtLMw",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "5d9fd2e44c2da4275675696ff282ea07",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1dPBl7XX5ij97JG93ZbzqRKLfBrQngfPlfm565UIqiZQ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "8f90c770ea87aac540b79beae4472ef0",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1uw6v5q4bj5gPqUZzLQ45SxKHBGGsLjB4ZeREQPtZ8eD",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1uCSbGX9mcDTOfnd8bONbFGCmMCoKL1HBhbIxCRszbQz",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ff7735385ff6edc86f7b7ccd395377dc",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1M0ZS54468cWjcuYIVMLpxtv41gEistlNm1mm8ctAmMk",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1ci29ClCJ2cRiyW5C4IOPzRqDQuA0tuWZiKKhLpCTNzv",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1Prq8CfPBA1Jd9Q3QtI8GfW5JPjJd3h2XziDOWHoGPTB",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
