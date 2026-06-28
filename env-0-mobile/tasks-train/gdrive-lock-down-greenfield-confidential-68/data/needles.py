"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1DR5L1BuiDgTi1LLKkw4050TMpxPU56AyOZZLtfyjWi8",
    "1dTij5S7uU5ODDSSbzH1cSRDjsSatmc7nxyf6VSiame2",
    "1Ethz8WQ0na46ymfHt0Hi67Z1wCDd4DPgYxQjgr6Znc5",
    "14hDysr4sKjzD7JqVFW6qdQ5c0HZ1QNiEyeYk1ddW2Lz",
    "1im278w4uHCgRUocMfUQlRFUlA4dpM7i4ZIIHoP40SbN"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "58c6cdb54465dc0f91afcda862ad8a3b",
    "1906ed848977c4f0d9795725b7a95157",
    "0c28e7377600999c2db0d8ce0a86e4d4",
    "6f15bf499a25368de545a88e36da32bb",
    "cf8f79cbfc3659d018e8f2ad7d1ff6e3"
]

LEGIT_PERM_IDS = [
    "f8686aa5b592ee69a0d7be99307875f4",
    "985ddf14a72a88890d640ee8548a0e2e"
]

NEEDLES = [
    {
        "id": "1DR5L1BuiDgTi1LLKkw4050TMpxPU56AyOZZLtfyjWi8",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "58c6cdb54465dc0f91afcda862ad8a3b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1dTij5S7uU5ODDSSbzH1cSRDjsSatmc7nxyf6VSiame2",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "1906ed848977c4f0d9795725b7a95157",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1Ethz8WQ0na46ymfHt0Hi67Z1wCDd4DPgYxQjgr6Znc5",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "0c28e7377600999c2db0d8ce0a86e4d4",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "14hDysr4sKjzD7JqVFW6qdQ5c0HZ1QNiEyeYk1ddW2Lz",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "6f15bf499a25368de545a88e36da32bb",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1im278w4uHCgRUocMfUQlRFUlA4dpM7i4ZIIHoP40SbN",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "cf8f79cbfc3659d018e8f2ad7d1ff6e3",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "18zOrrSKFuRn21mIIDOL1bE3PWfTlyADxajyRGCltllB",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f8686aa5b592ee69a0d7be99307875f4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1kYAJNKHlvsWI4RXcL1FEbhk7XBfqPyy6VMjxEROocfh",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1kF2EGPNPrxaDDgGeeoCSauHZTkgWfxJrRAm91McK3jB",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "985ddf14a72a88890d640ee8548a0e2e",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1nXlGzSBBsSJUJHw4ONbAkw4C2QiaUWeRFlhTLTykaOA",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "14O1VyNKakrvMPkQDdvUYDCcjEbXOnkMmRqyod8xlafR",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
