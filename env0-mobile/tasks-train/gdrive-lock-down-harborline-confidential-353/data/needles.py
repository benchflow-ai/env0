"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "19bUcsEwpenJZsrPMu8BUIRucn5CWJ3IiUxWgFKNSxdH",
    "1kTXDvZw7te5vuo7oXAY9UCWTf0rE3Efke1gNANJBLhc",
    "1QQIouPF1JP2LnyEw0dDSlFxZfhzjo1hCSiDdjwtvTQO",
    "18mGDngJjCLevDYfrijojITrcaNjU60uVvFglUqMZw6O",
    "1k05OqsyywuDo5tQUyykgvCTbeVAmnsFmcz2vNr1qcn5"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "b8e288a51e0a35aed9d7d7a3e65221b0",
    "0e99e7a01e0c2cfbc47eb18dd8ffc84a",
    "cc4c703907967db7df3c36b512ab1411",
    "f98956b9ed67001859fa9e467ad2c19d",
    "3f6d883c909b1600e751e421466b30e0"
]

LEGIT_PERM_IDS = [
    "c71e52e9485fc09871f9544cfc45f2fa",
    "599002a575b0f7d762c9a43a86321e9b"
]

NEEDLES = [
    {
        "id": "19bUcsEwpenJZsrPMu8BUIRucn5CWJ3IiUxWgFKNSxdH",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "b8e288a51e0a35aed9d7d7a3e65221b0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1kTXDvZw7te5vuo7oXAY9UCWTf0rE3Efke1gNANJBLhc",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "0e99e7a01e0c2cfbc47eb18dd8ffc84a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QQIouPF1JP2LnyEw0dDSlFxZfhzjo1hCSiDdjwtvTQO",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "cc4c703907967db7df3c36b512ab1411",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "18mGDngJjCLevDYfrijojITrcaNjU60uVvFglUqMZw6O",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "f98956b9ed67001859fa9e467ad2c19d",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1k05OqsyywuDo5tQUyykgvCTbeVAmnsFmcz2vNr1qcn5",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "3f6d883c909b1600e751e421466b30e0",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1VN0ALwgcADuY6N28YpuEV44P1ZsogfOarRE6aSr4bvA",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1WyvwIdZV9fFsgWyrycVZJbZjrFCQ9Ajia464bMWwrB7",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1POVcRavZ9bdLyoLMdoQXH64eW3s4bibI2Nh3rnmjBYg",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c71e52e9485fc09871f9544cfc45f2fa",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1xj8TPT7f27lzdsiwlPcpZCFRV6JDJ2nwUfGHL3cH0bx",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "599002a575b0f7d762c9a43a86321e9b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
