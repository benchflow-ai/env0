"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1acpnc2sPsOe4SS9hbkf6OMs8NtNfcDOHItKiqXXHlaD",
    "1oduAizyu2yhyIrtwWxAVFm4BON83aAkI23IK02oZfBR",
    "1fAIAX4gGXMyACs1rbhpkDGEtNvfFX1DFgtUaLBAXD5f",
    "1Ri26MInS8a78XCjPi8EtHWsbVunuMqnBdgOfeFRxOSY"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "4a8e786c2435153daf3e4faa8d8083a5",
    "32ad3e0f3909cfe6340067cff0619520",
    "d61ace592d49ef7f3d71a637b4cf7605",
    "41f60b265865a09e5f44b2016c5385af"
]

LEGIT_PERM_IDS = [
    "3742271877396ff44f374d7c4f5f94ec",
    "bff70fb5efd23288da9bb42f73261a36"
]

NEEDLES = [
    {
        "id": "1acpnc2sPsOe4SS9hbkf6OMs8NtNfcDOHItKiqXXHlaD",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "4a8e786c2435153daf3e4faa8d8083a5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1oduAizyu2yhyIrtwWxAVFm4BON83aAkI23IK02oZfBR",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "32ad3e0f3909cfe6340067cff0619520",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1fAIAX4gGXMyACs1rbhpkDGEtNvfFX1DFgtUaLBAXD5f",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "d61ace592d49ef7f3d71a637b4cf7605",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1Ri26MInS8a78XCjPi8EtHWsbVunuMqnBdgOfeFRxOSY",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "41f60b265865a09e5f44b2016c5385af",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1OILnsolKQSoJQFFAuOQZMdFk5jIOMnRi3w7HYhbR7Bd",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1xstYgOHtdAtKaipjfL9XBUvsu2cPIaNTV81wMyEVNgX",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1uhg9ZwYCtlshAsr8uEUYYB8BELAyetxHlrViFOLiOqH",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "3742271877396ff44f374d7c4f5f94ec",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1lFo5wxO8NtBHuIXy8vqyGxYYStK47lHezANJmkhSnry",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1PyQDMyjlX7Wt37vvdXWSsrJlvWS4GOMMe93B8xeBIyz",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bff70fb5efd23288da9bb42f73261a36",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1OKe1UxOhEY1vAHoyEGzL0q3QVedF7h7THXWjiNB3fFY",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
