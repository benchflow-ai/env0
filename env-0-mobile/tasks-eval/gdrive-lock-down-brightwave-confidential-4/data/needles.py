"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1KIXpdTbGNsE5DijMlDbzpIf8qDAfzHiDYJduBhAMM2p",
    "1txNCRi8ElnpGCx0DmyW5Cur8JGgD15wjgtogfRFFwlG",
    "17wab0ZO6FCmncmAz17nhLt614MczWeEzyBAdS2hKTgt",
    "14vmwiAPaG5cuTJepRzom2fcrgmItlMpdXS2N11h4fPD",
    "1xMzgIBnXvUoHcc8zS2FPyWwU797dqYnKvfSKqPQjv31"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "0f01b954330227f903a6997084bca820",
    "93bd28b2d824c513dd8af35cf8be5430",
    "e2023b377eb59e9514590afc4889a231",
    "df1423d58e775d6c928ca4c1c6ba9f2f",
    "4e25899de0516cb07d73f2e3dffe0b63"
]

LEGIT_PERM_IDS = [
    "b29750d190a6404300fb0a807cef0071"
]

NEEDLES = [
    {
        "id": "1KIXpdTbGNsE5DijMlDbzpIf8qDAfzHiDYJduBhAMM2p",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "0f01b954330227f903a6997084bca820",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1txNCRi8ElnpGCx0DmyW5Cur8JGgD15wjgtogfRFFwlG",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "93bd28b2d824c513dd8af35cf8be5430",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "17wab0ZO6FCmncmAz17nhLt614MczWeEzyBAdS2hKTgt",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e2023b377eb59e9514590afc4889a231",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "14vmwiAPaG5cuTJepRzom2fcrgmItlMpdXS2N11h4fPD",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "df1423d58e775d6c928ca4c1c6ba9f2f",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1xMzgIBnXvUoHcc8zS2FPyWwU797dqYnKvfSKqPQjv31",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "4e25899de0516cb07d73f2e3dffe0b63",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1o0oJcx8DOvnkBsFyHHSzjzmcMSwKECZZFQ19HYNqCgB",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1Cg1nwvcSeHDcP4y8mRBz4GLyKDLhE58QTqcwRUfpFiL",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1udoywFaP1sZwNqQdznElTofKlAJ6fVgOoXgyyS2IauL",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "15k8WlAETarouA5YHskjwOxDUEliEZePtZAwY9sYOUEx",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b29750d190a6404300fb0a807cef0071",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
