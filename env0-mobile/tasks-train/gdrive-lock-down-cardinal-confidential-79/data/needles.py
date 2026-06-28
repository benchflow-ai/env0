"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1y741xOW2ESxoqUYNQuyOtU4c3JpvXCReub52eJUj8g7",
    "1GVMzDQqK1WPLnnbvde8Nz4q5YhJDARY8spuZL72nN1l",
    "1Yrst6hosw0AKyuFMyVXK2uidd8RG3Kv5gukCuBJoiC6",
    "1EajufvWOc2X0TRHBkz8KJ0yuhtx9YjPLHXj4bnz9L8N"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "15048ce2e4632c99427565e8804abc21",
    "6c935209cabf67ea4714c55e057e5c36",
    "cac0025b90dbf196c703a4ac44167bbb",
    "3bbc150c133c69670686ca0301ca5aaf"
]

LEGIT_PERM_IDS = [
    "ff6dc6cfdada0f1e16727e8fa87d3a45",
    "0484ab02a2f5a229487b3228fe1b8823"
]

NEEDLES = [
    {
        "id": "1y741xOW2ESxoqUYNQuyOtU4c3JpvXCReub52eJUj8g7",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "15048ce2e4632c99427565e8804abc21",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1GVMzDQqK1WPLnnbvde8Nz4q5YhJDARY8spuZL72nN1l",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "6c935209cabf67ea4714c55e057e5c36",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1Yrst6hosw0AKyuFMyVXK2uidd8RG3Kv5gukCuBJoiC6",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "cac0025b90dbf196c703a4ac44167bbb",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1EajufvWOc2X0TRHBkz8KJ0yuhtx9YjPLHXj4bnz9L8N",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "3bbc150c133c69670686ca0301ca5aaf",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Tl9nqgqzc2LbpWvvNv03fxrLvE40s9Uf9EEq8inDtM4",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "10isf1AxDlfoyimtaE5mhbWDYdgl9eSlqHlKM1HX4y6x",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "10wIQcJDnZBRtk7MSAgLet8Ad9HFnA7RdvVmKHYDtBjm",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ff6dc6cfdada0f1e16727e8fa87d3a45",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1HgfvUCAP1KoHmc7aS8ZZts0oibGUcGLbrgjx9Lr7v6P",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "0484ab02a2f5a229487b3228fe1b8823",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
