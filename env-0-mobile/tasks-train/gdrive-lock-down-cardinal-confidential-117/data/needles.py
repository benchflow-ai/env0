"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "13HTDvRRjgUNWDaXCgrvqJAyngpKZmaggFe339DijpW0",
    "1huwmKR8BQcblJjTOer9cp8Lt6o8QqzpXPLSxhl0DZ0a",
    "1jqF8897fR9iz0PuKYSSsPkCMD0IkqQ1iDxCID5ekkHP"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "0189d1daf3a4583aa89ba748d4acb1a8",
    "0c9c3067186cb22fae4a1f158dd7e4e6",
    "f58f04ea450cff286ab61c9b01e77e0f"
]

LEGIT_PERM_IDS = [
    "5c93360677bd5852e9adcb2c89cde7a1",
    "a0807502c2f2feadcc72c8a180ba7f52",
    "7f723fb9a6fad201f6040cf88345be20"
]

NEEDLES = [
    {
        "id": "13HTDvRRjgUNWDaXCgrvqJAyngpKZmaggFe339DijpW0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0189d1daf3a4583aa89ba748d4acb1a8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1huwmKR8BQcblJjTOer9cp8Lt6o8QqzpXPLSxhl0DZ0a",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "0c9c3067186cb22fae4a1f158dd7e4e6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1jqF8897fR9iz0PuKYSSsPkCMD0IkqQ1iDxCID5ekkHP",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "f58f04ea450cff286ab61c9b01e77e0f",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "16nCGgA7FqUm4foLxZ0ZprZSax1JEVKLatPd344ptose",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1XG6trSZ6Fyzq3zIXDIyjuNot0MANpNUVHxixdCVvtf1",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "5c93360677bd5852e9adcb2c89cde7a1",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "15RfhigOwnuIvfJGsfkGv0Ck2QP8h3NUqh0rBWmMMixJ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a0807502c2f2feadcc72c8a180ba7f52",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1eHxlhguxlv0nA3s2HnDxTKsjEbk3AV8NSrMbBdHDgib",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1RVLfsORns24zfeJVR8NZRCxqX4ym8bgvFWR22VY0D0y",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "15345ghWNNUXrvwwcNzcTFYr3oiNbHyKF1xbJAzoFHqG",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7f723fb9a6fad201f6040cf88345be20",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
