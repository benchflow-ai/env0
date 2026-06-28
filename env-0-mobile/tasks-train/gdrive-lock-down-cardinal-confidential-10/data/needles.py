"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "149GGPTpKyATAFsALc6EqFrYCZkiiirckzuSHQA1ARnu",
    "1QOA9djgAY6U96NjiG1Qvsu9cwWxGsgyBboEHRd355i0",
    "123VlrQkCh0rscjNOdN53TXtlhiakeEn198X333XtfwA",
    "1b6sglvSy9atfJkWAX6iPbLXH5kK4UAH5QGSNL1aWXvR"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "6a260b597b3e7a72cc7a3f82c4a60961",
    "4eb40ade66dd297e68ce78d77719f24a",
    "e59f12e90e0ddd353e6024862f53a84a",
    "7da31604650ade0965712a80c18d4a98"
]

LEGIT_PERM_IDS = [
    "273bb5e7323b5bebf1e7716bd692a952",
    "c83466d07a4f946715661f5ded197f7e",
    "b897dd32e563bb0a47f3cca6387eca83"
]

NEEDLES = [
    {
        "id": "149GGPTpKyATAFsALc6EqFrYCZkiiirckzuSHQA1ARnu",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "6a260b597b3e7a72cc7a3f82c4a60961",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QOA9djgAY6U96NjiG1Qvsu9cwWxGsgyBboEHRd355i0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "4eb40ade66dd297e68ce78d77719f24a",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "123VlrQkCh0rscjNOdN53TXtlhiakeEn198X333XtfwA",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "e59f12e90e0ddd353e6024862f53a84a",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1b6sglvSy9atfJkWAX6iPbLXH5kK4UAH5QGSNL1aWXvR",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "7da31604650ade0965712a80c18d4a98",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1qgZOoYMfGElEIGsnN7HUF8PdSD2Taia7o6JE5Pgzjuy",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "273bb5e7323b5bebf1e7716bd692a952",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1qX70DiXXIFjRlIZPLdTzemWNRezgBS7dEC1XhJOWzwo",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1EFrxppW2sIuB2qO9Z06aFSvG9Ir9JI4MDp4F2pIlUdG",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1VsPBtdqntwX69wlEy2qZIvXzWfSx2lNymzP9OTyWkrn",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c83466d07a4f946715661f5ded197f7e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Tjl87cH5rwzbaZvmq5Tg6f60GkKLtIyuBg3yacbvxjE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1vWJVx2zP347JZBthxNR07aaJzG8ekzwmcFqAfDxBPpC",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b897dd32e563bb0a47f3cca6387eca83",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
