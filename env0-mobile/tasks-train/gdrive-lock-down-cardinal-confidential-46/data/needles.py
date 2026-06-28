"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1PHx7lqF0bAplj2qfnX4bJJLgf97aUkHfHSrMy4CZIIm",
    "1FfmJcu6KqgIr1WrU8BWWd7FwihqvW96IyVC4jBBBhXP",
    "1Fpp1XCOp6da7nCk9KrAdpvOlLhmgK5LgahuU56DzGNK",
    "1ID6zETTxXldRE9Qwg7YQUskz4zQJV3S0NKq8V6gEyNn"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "a65f85a9b2211867b56dc5e4e6bfdb9c",
    "e3dec5943f8bfb572970e5ef29b45a86",
    "2f136c7ea4ffb6491592f3d83041fd5e",
    "9375a441f9eb350f486babdf68bf398b"
]

LEGIT_PERM_IDS = [
    "6397848b07bbb0097c2a0d7446cf52f3",
    "a075a1f8dda6e6437711fc2df67f4547"
]

NEEDLES = [
    {
        "id": "1PHx7lqF0bAplj2qfnX4bJJLgf97aUkHfHSrMy4CZIIm",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "a65f85a9b2211867b56dc5e4e6bfdb9c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FfmJcu6KqgIr1WrU8BWWd7FwihqvW96IyVC4jBBBhXP",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "e3dec5943f8bfb572970e5ef29b45a86",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Fpp1XCOp6da7nCk9KrAdpvOlLhmgK5LgahuU56DzGNK",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "2f136c7ea4ffb6491592f3d83041fd5e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ID6zETTxXldRE9Qwg7YQUskz4zQJV3S0NKq8V6gEyNn",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "9375a441f9eb350f486babdf68bf398b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "11OHnSpHLf9K7xMzBGkjarmouEG5h9NfHURSWrOle8RO",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "6397848b07bbb0097c2a0d7446cf52f3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1jj5NNCq3qRNwuG6p0qkOMspTUpdzsRynjWRtBk7PyUH",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1LELRqXJp9eUlTucKzB3iza9K0te3wIswv5SzdO8xNuS",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a075a1f8dda6e6437711fc2df67f4547",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1Obolf9VnRqwub4jpcSrojxyeZ5rhcWFSaYQWfWVVuRZ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1NeL203UPIrY4SYo3MsGXZ3uSbzveO4l1zNYDOn1kq2K",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1cxwEHBHZgLQqK812I1gqR4vSnEaJs2Z6DnY6tuem42B",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
