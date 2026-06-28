"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "16oMZRzU8vJ7DAOWJmAgjrvDHMZEf3tFPoLtKcn1hFvr",
    "108g5uQzGrcKEaHGUFnHIOtip6PMCqLLoo0rDMtY0Zqa",
    "1xJLL2CMb0Q6a8fIb9uZKUbfq1sEXOaepWnifMVuLTiW",
    "1k3uG13ail2j0UrIx30NOOVn0zi6hvuaLC0P41SCMKbn"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "f74351854b5dcdd99fa0b5f3f9700828",
    "7a2e1991bbd48549d3b8df121c24d9b7",
    "e60310eaa6588ebcb5a450adfee81dd5",
    "957478e2fc76361b0eb92a75835115e9"
]

LEGIT_PERM_IDS = [
    "ae31653095cd494acbdbad86fce1fb25",
    "4b6ec372a5426ebc4c916f981ccee7b1"
]

NEEDLES = [
    {
        "id": "16oMZRzU8vJ7DAOWJmAgjrvDHMZEf3tFPoLtKcn1hFvr",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "f74351854b5dcdd99fa0b5f3f9700828",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "108g5uQzGrcKEaHGUFnHIOtip6PMCqLLoo0rDMtY0Zqa",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "7a2e1991bbd48549d3b8df121c24d9b7",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1xJLL2CMb0Q6a8fIb9uZKUbfq1sEXOaepWnifMVuLTiW",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e60310eaa6588ebcb5a450adfee81dd5",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1k3uG13ail2j0UrIx30NOOVn0zi6hvuaLC0P41SCMKbn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "957478e2fc76361b0eb92a75835115e9",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1lh6AWk7KdCPUugsEPNFXjTJmqrvcNh6FBwUXlYVM6Et",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1xdPx96vKbeUP8FkAPIgyRGTpfCoehg4tPnsc6TwXfAC",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1d6FespZxMVqXiRBsaYrmCNklE26Z0w16OlPjRQGsoo8",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ae31653095cd494acbdbad86fce1fb25",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1EJDK6o7SWqKsnoTqIvCR31PiITK0TkpL2aQfu2zrvVO",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4b6ec372a5426ebc4c916f981ccee7b1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ElSZg1GgQqukxP2uJWjxgVXCvzIT9LRt9SgkM5KQFA7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
