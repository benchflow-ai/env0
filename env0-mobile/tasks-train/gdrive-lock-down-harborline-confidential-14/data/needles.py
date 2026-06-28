"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1cBWwpII5I9Y4YHjrbEzpNzngdQsOcGjcWkZuOjJKBYD",
    "1lbFOqcLRtLdl4mI47GigoEToNthcHbYHcaeppELGWug",
    "1t16aaqdvTg5clCiSakVa1mpFXoSJdAgEhJkWIUVFzAy",
    "1Q4pv5tCqsLFsPpLe6bqApf2HnsTkUkUBiuFtA1vxZ1R"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "6be09c16947c7c59018f9b15e48ee7ee",
    "67ce6ea8d643c5809a088fb15f84db13",
    "b2109a291138159f89c5ac71eb54315f",
    "6c7635674fefd0e563721c22903d6087"
]

LEGIT_PERM_IDS = [
    "fa338380859256175cf9f37331b50e53",
    "1bfa14566e36d30799b6ab1938f06b20"
]

NEEDLES = [
    {
        "id": "1cBWwpII5I9Y4YHjrbEzpNzngdQsOcGjcWkZuOjJKBYD",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6be09c16947c7c59018f9b15e48ee7ee",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1lbFOqcLRtLdl4mI47GigoEToNthcHbYHcaeppELGWug",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "67ce6ea8d643c5809a088fb15f84db13",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1t16aaqdvTg5clCiSakVa1mpFXoSJdAgEhJkWIUVFzAy",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "b2109a291138159f89c5ac71eb54315f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Q4pv5tCqsLFsPpLe6bqApf2HnsTkUkUBiuFtA1vxZ1R",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "6c7635674fefd0e563721c22903d6087",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "16YD9nIlQVgOjGZPaq249WmvwEUL4V22hcN4UPn3hXd2",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fa338380859256175cf9f37331b50e53",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "13pfr4cH4FxXF8fa93vNL1l5ULdXmXfvhlYvdCsU8tZa",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1cCKwMeClA4JT5U4Zu7GVq1WxtgvVTjHcouU0KF98z66",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "1bfa14566e36d30799b6ab1938f06b20",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "11Vltzxw4gCtHivDt0da36FX82KcDxwX1tiSQ2YBX5GV",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1aTJElkSGWW1J965x9F1c7MngZahJtjplAYtXp2tNjEN",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
