"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1t2j0BY4ZWOixz2FUH6WM3VP0ywmMvl7wf0w02tJv2Tn",
    "1stxIRXo8v7SFunw8NOXoPb1czl0aRun87VXNNg2bwO7",
    "1LTDAtm1y3hvM6GOJSkOqfJOD36qJEVzaxTFvhU5QPNQ"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "7624c8572402453ad80c9bb105b63164",
    "2badbfc5189874cf8b533ed0014072d7",
    "a690c8683c6ea2571c887ac32ee64fd0"
]

LEGIT_PERM_IDS = [
    "efe17d71bd2ff2451a3e001619a416e5",
    "09fc8be7250c8f3507ed1e7229e95d09",
    "1177c6c9534d5232fafcc3f2f9e6e0b9"
]

NEEDLES = [
    {
        "id": "1t2j0BY4ZWOixz2FUH6WM3VP0ywmMvl7wf0w02tJv2Tn",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "7624c8572402453ad80c9bb105b63164",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1stxIRXo8v7SFunw8NOXoPb1czl0aRun87VXNNg2bwO7",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "2badbfc5189874cf8b533ed0014072d7",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1LTDAtm1y3hvM6GOJSkOqfJOD36qJEVzaxTFvhU5QPNQ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a690c8683c6ea2571c887ac32ee64fd0",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1qdFcczwYO8QuHTTbdWS8jwGVgQkCv3TgFcTg7Wyc3NS",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "16bQl7y1BJwYbxfcebFEkaZVb61y3MpS6Jv3McL8UOQA",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "efe17d71bd2ff2451a3e001619a416e5",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1VbAtzLoT8nAcmrRNZf4R4oUMglw6g0dbQvGcQgsiJ0z",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1OkpUySltI04hK0KffIxhLYN7dKteWixT5Ivwvmy4pYB",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "09fc8be7250c8f3507ed1e7229e95d09",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ON3FeCi6m8v1oXVm5VXGlLCwXgyIkFktSb017Fd5Cth",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "1177c6c9534d5232fafcc3f2f9e6e0b9",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
