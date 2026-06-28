"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "12rJxXXZvCqL8VV46tcXyDyCDpFNd67RCvwOKGrRllPs",
    "1Jy9iwNEVEF4g48YVmNJgoOJesfsjmay6ZHy3D9mETro",
    "1HKKj7EQyaB2MaOpaYLSOnNtsLGsw4uLVMA7mZkak820",
    "17ZpO3nSPp4c1qydvcMB2thuAG02pYj8WdBcqtsoOdr1"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "ac78e906c5f4e1e70fd6916aff3b61f5",
    "d677f815ca06158a1fd2f39a04d6c72d",
    "27dc53902dd5f413e0b25cbc1d9eb1a1",
    "04717f4ef89e92bedbd27f5d5cd17440"
]

LEGIT_PERM_IDS = [
    "c81a891e9cb0cdec96d35a975f82380d",
    "5f377da018eea44d803578da3948e3a8"
]

NEEDLES = [
    {
        "id": "12rJxXXZvCqL8VV46tcXyDyCDpFNd67RCvwOKGrRllPs",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ac78e906c5f4e1e70fd6916aff3b61f5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Jy9iwNEVEF4g48YVmNJgoOJesfsjmay6ZHy3D9mETro",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "d677f815ca06158a1fd2f39a04d6c72d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1HKKj7EQyaB2MaOpaYLSOnNtsLGsw4uLVMA7mZkak820",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "27dc53902dd5f413e0b25cbc1d9eb1a1",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "17ZpO3nSPp4c1qydvcMB2thuAG02pYj8WdBcqtsoOdr1",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "04717f4ef89e92bedbd27f5d5cd17440",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1NGsX813I2mYvbQUGlz3PXFaKaGsPTQ9cICVWDXrCKMZ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c81a891e9cb0cdec96d35a975f82380d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Y5HM6c149XS0l2NQistNHpgGBKofKxFk4jwz4IbRVwL",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1RZw1bohPNsWzGAIItyGSFRmcWHlwKW7ELqGposbeNr8",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1zWGP4c2JuU99T2EbAmETn70SUJAKJtPkydZgHjthqNJ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "5f377da018eea44d803578da3948e3a8",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
