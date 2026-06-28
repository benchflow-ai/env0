"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1wZ9LrYlGYpmHneag0crfttRf5hMv5lB9GzjmgERl7bW",
    "1Olo1SdRNfbrWejYw3IXkwHQo0U660lWnPNCI8Donrb9",
    "1gZpEgNa3bvGhimCNPLqgmMjl390gwOfVDCT4YOSK4NB"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "0c444bd3fba89132a832a1da0f137127",
    "e54d1eee45e9d1e044af8bf6b238636d",
    "a2d533af7553f15a59ddae789e8624f9"
]

LEGIT_PERM_IDS = [
    "c1724d8dde415ead7b1c9f17b4292af7",
    "1e96eeaa030c068fe60774f1fe580aeb",
    "101ca1b6f176ef060ace7bd232e076b4"
]

NEEDLES = [
    {
        "id": "1wZ9LrYlGYpmHneag0crfttRf5hMv5lB9GzjmgERl7bW",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "0c444bd3fba89132a832a1da0f137127",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1Olo1SdRNfbrWejYw3IXkwHQo0U660lWnPNCI8Donrb9",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "e54d1eee45e9d1e044af8bf6b238636d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gZpEgNa3bvGhimCNPLqgmMjl390gwOfVDCT4YOSK4NB",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a2d533af7553f15a59ddae789e8624f9",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1mHux64hQIT11suvedzb5bwZduPfYEHbrj8cUivrxcey",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1GHRvnxmwUuAMVCwrecJJHBwaFyye29SB5bCIW16Xko2",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c1724d8dde415ead7b1c9f17b4292af7",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "17RQuXyUX63ryDZYsre9uJD2v99Zc7PIfqNUCpmzPkUJ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "1e96eeaa030c068fe60774f1fe580aeb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "16Qus2PzloBVaix7nUdAEA7S2FnJRKa5oxfQG8c8FJuq",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "101ca1b6f176ef060ace7bd232e076b4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
