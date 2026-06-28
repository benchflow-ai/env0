"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1ZB8ZFXTkfUAu77YLYa6dWjPWJkR3HSqmnNrt3P00lML",
    "1LJESLIw74UPxqzZh3b0V38uPSzZjUW8Gx6pe5sy3NeS",
    "15Pjpcgil65KuUDaTojPhWYwBosd6h6PJMP9oTtfS5SJ",
    "1l4HY0eqOliar2kLoaq0UQXL2nT0LCWe57eFjX89sSUn"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "e34122e8141236efba7aa2299a679162",
    "6a79e5e19e05c4bbd7b843d085181966",
    "9a218a07d4e90d3dbe5c138bad26383d",
    "13b4b329f78f9715db7c1d6d1e149894"
]

LEGIT_PERM_IDS = [
    "31532812ece810a8461a5bdd54e9b720",
    "1ef068ac25027ca48fe28c1e1604fbd8"
]

NEEDLES = [
    {
        "id": "1ZB8ZFXTkfUAu77YLYa6dWjPWJkR3HSqmnNrt3P00lML",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "e34122e8141236efba7aa2299a679162",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1LJESLIw74UPxqzZh3b0V38uPSzZjUW8Gx6pe5sy3NeS",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6a79e5e19e05c4bbd7b843d085181966",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15Pjpcgil65KuUDaTojPhWYwBosd6h6PJMP9oTtfS5SJ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "9a218a07d4e90d3dbe5c138bad26383d",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1l4HY0eqOliar2kLoaq0UQXL2nT0LCWe57eFjX89sSUn",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "13b4b329f78f9715db7c1d6d1e149894",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1C9Zekyxhw9ykLWQYUIRpjoPyARv7D1RAbs6rESCKQDi",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1LnUrFTFnwETlq0YuePgTdsBPq0CZOnghyfWtOQ9Ctg1",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1QyhLKnSRgHztdLM13kU8yFhe6RVbC7HFUUJaanXUg7t",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "31532812ece810a8461a5bdd54e9b720",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1RXaAxbiRVjIkw5ztVGZlXs4Y7VgJY2eQltORu45vrwD",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "1ef068ac25027ca48fe28c1e1604fbd8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1mQYdU2kASD9nhw6iS4zQBfTv8sVEgR2ZoERLLMIjp7k",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1SCXcuotX85uvqTxrerEDk1zothlEYEHvOiH0JxkQlAF",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
