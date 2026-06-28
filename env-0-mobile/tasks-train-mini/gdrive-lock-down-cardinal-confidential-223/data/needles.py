"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1cjcgZJf7CQ1P3K0r7yS8q6xvar7eZM8Y0lSt4ZjbxYf",
    "1UXx9ioayuJQmM86BJ5TsJx2jZ0nOuxdr3hPgjwfenXs",
    "1YEKzuWtpF5FVRoxgjSvngDBL7S8DyiizzbkFNVfeNFU"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "84945bd4c73005257cf6c31e6a11fed0",
    "64f93dc20de8eb7e55b1216997975642",
    "0a26948cc68b7b2a639b180f5e901fe5"
]

LEGIT_PERM_IDS = [
    "3f8e326ee18c56e6ea8b9c7a1f390c21",
    "a9abf925258dd57444f137e9b34add36",
    "d85bd041a1b49881e0ff6439ebec7671"
]

NEEDLES = [
    {
        "id": "1cjcgZJf7CQ1P3K0r7yS8q6xvar7eZM8Y0lSt4ZjbxYf",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "84945bd4c73005257cf6c31e6a11fed0",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1UXx9ioayuJQmM86BJ5TsJx2jZ0nOuxdr3hPgjwfenXs",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "64f93dc20de8eb7e55b1216997975642",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1YEKzuWtpF5FVRoxgjSvngDBL7S8DyiizzbkFNVfeNFU",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "0a26948cc68b7b2a639b180f5e901fe5",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1QiktHf965wsHL4ssjPI8lwxqWV25VL0o2rHhcBUgHTb",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "3f8e326ee18c56e6ea8b9c7a1f390c21",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1VyRp2QwR2CLEOI97H0jupzxMG57UmL0NEbFQYfJa60y",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1lKM02nfdI5toQDnDjmlYFfRyOBHvcptEoK6aJEVmvU7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1YU2Mk8IfotmuRJqzK0QzA4TNQCqtmcb67bos1GH5T6B",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a9abf925258dd57444f137e9b34add36",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1jpjXwK1giu0YqfoUwnVck4hQr8eB25CbMs93mfxC5o0",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d85bd041a1b49881e0ff6439ebec7671",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1HWnI7he9XERBYfnpvZfiHnmdV6DDNB8O5J8x7ZxaYhA",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
