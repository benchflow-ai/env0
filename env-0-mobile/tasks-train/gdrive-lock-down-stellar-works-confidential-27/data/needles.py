"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "113VGxFDJKBO9RU4ParqZWZtuMDBbE1PrU9X8VWbVZb9",
    "1OtDUH3zZRcwtoJz8cTePNsGsBSnF0Coy2Rmt91j0oqx",
    "11WydRTaeKDWBvsaOTknQcorNoQ2HKtkvGoBOJKfvxzb"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "3b0112e0056266fa4541aaf88aa982b6",
    "23565d65a2653e69603997a4c23f6cdd",
    "a7fa5d585a75575c831272aae74c939d"
]

LEGIT_PERM_IDS = [
    "01f3827cf62e5d8ad0cc0a4043de4cda",
    "22423fc6f7dfa7c5636626ca7617b5e8"
]

NEEDLES = [
    {
        "id": "113VGxFDJKBO9RU4ParqZWZtuMDBbE1PrU9X8VWbVZb9",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "3b0112e0056266fa4541aaf88aa982b6",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1OtDUH3zZRcwtoJz8cTePNsGsBSnF0Coy2Rmt91j0oqx",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "23565d65a2653e69603997a4c23f6cdd",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "11WydRTaeKDWBvsaOTknQcorNoQ2HKtkvGoBOJKfvxzb",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "a7fa5d585a75575c831272aae74c939d",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "147KLzsHEjXSMRk4y0UArVwYEDfVxwdGnnYdJJqOuGEu",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "01f3827cf62e5d8ad0cc0a4043de4cda",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "15V0mWHjpJRpqhK57CKDtN1LQCfQzsGTVub6KllfI27k",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1ltMMnYUh5kCFIH29mPJJ5wvSgSA98a2zRcPJGUNdnE0",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "22423fc6f7dfa7c5636626ca7617b5e8",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1K2oZGyCobSOQnXWPbPMYyNh7nUgvG0JYdYav5Y39IiI",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
