"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1eHZRPJ6OT0oj6CaWjv6tJ2uftoysNdW0Qgj9HFdJY0E",
    "18dMf6YmCC13A2lGG5A1oLkf9OQ8y421iOaCyhbdl51h",
    "1YpZZeNOfB1z6qjGxdWPkRaDcgtQbsYMHEvrxIhXc4pA"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "47fb5ea80bf71617025644bc60736aad",
    "9db331418f4604cd67406367ef720ce8",
    "af0141f4e355a89485428cd36d986bb0"
]

LEGIT_PERM_IDS = [
    "3a2ae1e412f50f9022a30f7770101b6b",
    "437d944427b601d80d31636052f56ac8"
]

NEEDLES = [
    {
        "id": "1eHZRPJ6OT0oj6CaWjv6tJ2uftoysNdW0Qgj9HFdJY0E",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "47fb5ea80bf71617025644bc60736aad",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "18dMf6YmCC13A2lGG5A1oLkf9OQ8y421iOaCyhbdl51h",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "9db331418f4604cd67406367ef720ce8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1YpZZeNOfB1z6qjGxdWPkRaDcgtQbsYMHEvrxIhXc4pA",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "af0141f4e355a89485428cd36d986bb0",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1RJnS1jCq9nbLzoQYvxP9WLWQw3JkohMWeyNG93VlwyE",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "3a2ae1e412f50f9022a30f7770101b6b",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1xsQotrutU5ZAKweOKPkkxs8sfYWTaiGCfHaCeRWJkc9",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "437d944427b601d80d31636052f56ac8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1vf0ATQwwZFSQ0plkoRy8E09K6OrR1G0iUaHM7PfOX0L",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1zIsbznJdYroDU6qDuvUS0Vj67rqu2Foio67g4M8vxlL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
