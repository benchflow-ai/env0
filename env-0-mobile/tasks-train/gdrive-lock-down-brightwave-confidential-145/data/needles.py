"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1yK9xMkMOSACNSovWthN62An0NI3guDvIlxgrTTptOSO",
    "11PHX9L9waoRC4wjJYiNF7jQk5NVRS7jpQnwK2C7HI4X",
    "1f5FuNPtyUaO2575AkK76p0FHcD2MxkFhnLkLa3N0NRN",
    "1dgrTkrv7rtpuyOneZ6Cn4rJZIxfOkRSd84aFuuhemtY"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "be1c891373eac2e377420b129c39dd82",
    "a80f8f739ff70339e76114c7b865ed0a",
    "9a8b9f9f5dc07618888d7a332d86a6a7",
    "34e30833aece04fec7ea407d4b46e202"
]

LEGIT_PERM_IDS = [
    "3cd40e100f61dc406de105d241713ce5",
    "7e15ed036a6daacccd163d43683566b1",
    "8aaa637404397a79c4af46dd66f1df4a"
]

NEEDLES = [
    {
        "id": "1yK9xMkMOSACNSovWthN62An0NI3guDvIlxgrTTptOSO",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "be1c891373eac2e377420b129c39dd82",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "11PHX9L9waoRC4wjJYiNF7jQk5NVRS7jpQnwK2C7HI4X",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "a80f8f739ff70339e76114c7b865ed0a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1f5FuNPtyUaO2575AkK76p0FHcD2MxkFhnLkLa3N0NRN",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "9a8b9f9f5dc07618888d7a332d86a6a7",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1dgrTkrv7rtpuyOneZ6Cn4rJZIxfOkRSd84aFuuhemtY",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "34e30833aece04fec7ea407d4b46e202",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1zGfqPgiRErahmiw3WSvj26IuM7a6yDWPHnY0zxGaQUP",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1YYDxDJPJwuN7nFO0CJWBpxmCMVl0JJ5Xur254fZbDGK",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1LTW1UxNt36h57mKHEbCU2VkTbOUxCslgxHkvuM229X7",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "3cd40e100f61dc406de105d241713ce5",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Im8CJXXiuyQ5J65sihalVnlXgf20UcjYGbwQ1xOciB2",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7e15ed036a6daacccd163d43683566b1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1SrNLZHX0OHQ1tuwITHef3gY36jnRZFcas1dXNPzO4lX",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "8aaa637404397a79c4af46dd66f1df4a",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1iCgo6mOl2zYB96Vy9oAgZqKqtATy2T5XX9Agx1a6Ttj",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
