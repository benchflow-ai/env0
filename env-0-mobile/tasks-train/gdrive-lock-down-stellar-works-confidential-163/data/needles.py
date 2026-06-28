"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1YL3pcyDtqVlY9190YB2xjmG9mIP6zk1h7gjTB42ARYC",
    "1VKsNTJZRHVfWhbw6gzVCC3PzipIrkOwhDv0PQn7KhZu",
    "1H70NTzRMXqRQZdcQXjjbSrAHewMFCnpridjaa5B4Nxj"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "71b8b0fb13e727a94685b717baa864f2",
    "d1feea2bac3394c51a095298ea231212",
    "cfbd12480a90b325afcc99f7d4f09ac3"
]

LEGIT_PERM_IDS = [
    "480aa4022b5e5c5837218d575eef45d7",
    "60cb703343fac8173b0ee3880557fc12",
    "5db71c045c40c5bb64e926dfffff7da7"
]

NEEDLES = [
    {
        "id": "1YL3pcyDtqVlY9190YB2xjmG9mIP6zk1h7gjTB42ARYC",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "71b8b0fb13e727a94685b717baa864f2",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1VKsNTJZRHVfWhbw6gzVCC3PzipIrkOwhDv0PQn7KhZu",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "d1feea2bac3394c51a095298ea231212",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1H70NTzRMXqRQZdcQXjjbSrAHewMFCnpridjaa5B4Nxj",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "cfbd12480a90b325afcc99f7d4f09ac3",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "11ECjO18T4LoWifIGErWXcZbr6AKLPQNUzLgw7fJXZBx",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "480aa4022b5e5c5837218d575eef45d7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1KR8KuIk9VpiDSb4j0AIV1lMJYZMhsb3m7KmGMiYdsQx",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1lV356509vppyLOxTqhdHkPJ5aMsWTMBFKlc1IH8LooF",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "13ufqguFS9dOdk7drlb1YFP61SnpyVWJiFkxHOA7DGcP",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "60cb703343fac8173b0ee3880557fc12",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1Kl8zb2DxeHbUnmPRMlDV2egktEd5LHVvsgcPin63u32",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "5db71c045c40c5bb64e926dfffff7da7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
