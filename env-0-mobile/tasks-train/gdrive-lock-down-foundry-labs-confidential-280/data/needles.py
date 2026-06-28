"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1kMGT2bjqQslEAr1gGPo7t72yOhrtnfQDIBPF7hznIJy",
    "1xA8uXziYcMALK2ltdv5cIFdz0KYEVOJZuwwd7CNhgpF",
    "1VuFR55DzefGvazql2CDwxKdaTmmwJRGVc300t0mwvYK"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "ff9a6c86cb6f3557801a19f7d41aa747",
    "7d25964b8355d27a5a24983e073b0239",
    "82f6efacdf317410126ab3878f670225"
]

LEGIT_PERM_IDS = [
    "baaf9f9e7117d9eb8c0aefaeed1607c2",
    "6f595dc3d758fbea71152f4f986ea689"
]

NEEDLES = [
    {
        "id": "1kMGT2bjqQslEAr1gGPo7t72yOhrtnfQDIBPF7hznIJy",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "ff9a6c86cb6f3557801a19f7d41aa747",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xA8uXziYcMALK2ltdv5cIFdz0KYEVOJZuwwd7CNhgpF",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "7d25964b8355d27a5a24983e073b0239",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1VuFR55DzefGvazql2CDwxKdaTmmwJRGVc300t0mwvYK",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "82f6efacdf317410126ab3878f670225",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1jRNOOOtD1EwWNRfG3QdhQ0FiepV8V6rXDWUxqraDAP5",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1XB7KfZfVeLwTEHYTLIdUSLr4MeRTxlUiXUzR3PFw37U",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "baaf9f9e7117d9eb8c0aefaeed1607c2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1dnBR4eIqck3wxgHL2IMVFn3RWABLUCikn5h9cWbpFLN",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1rPDfLHrb9QeHhvC1sP32k9KLL9xfHWFOmbZWKk0IKzz",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "6f595dc3d758fbea71152f4f986ea689",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1uQegqYZzFObgrfFJlyxxlxuSEP2ZFm8aiXKy8gfpwWE",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
