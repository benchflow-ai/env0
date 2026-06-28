"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1bgCWdy4Aovr6XGvcxSLj36GX7SVf5rWGYceZGUDdqe6",
    "1uoHITz56qMDgLvRtdCvAt9RE6oRyed4X6fYxEV73qsR",
    "1yrRiuqIua8MYLg9d8YM3USdnHYow625NF7Czm3FAPuX"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "d9d9b2ef4ea613884e9503e5cb2f2122",
    "5bc71873aac71bb97f408d5cf1e5df3b",
    "51a43e23c828406f0a002e5b1946d45f"
]

LEGIT_PERM_IDS = [
    "01b68a03d570545cd8a9d13783a4fb12",
    "94993951426a1307e7c9c8f7f60abd03"
]

NEEDLES = [
    {
        "id": "1bgCWdy4Aovr6XGvcxSLj36GX7SVf5rWGYceZGUDdqe6",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "d9d9b2ef4ea613884e9503e5cb2f2122",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1uoHITz56qMDgLvRtdCvAt9RE6oRyed4X6fYxEV73qsR",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "5bc71873aac71bb97f408d5cf1e5df3b",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1yrRiuqIua8MYLg9d8YM3USdnHYow625NF7Czm3FAPuX",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "51a43e23c828406f0a002e5b1946d45f",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "110Um4fgTHR4NEvVDRkMn5UmXbv8qk9TbEYArXTw0dlC",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1ulzM69ecEiGZkrkliMV6Tgp9RiLveLEaEz7rQaxOJIU",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "01b68a03d570545cd8a9d13783a4fb12",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LXCXhu4IHRhoXaRALnIwffF9C6Pt2YAXWapOeVQhuuf",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "94993951426a1307e7c9c8f7f60abd03",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1VavIWZ3RzNPqm8tr70PCI9ZbvCu0Q31XXGQhJ8Fp6MN",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
