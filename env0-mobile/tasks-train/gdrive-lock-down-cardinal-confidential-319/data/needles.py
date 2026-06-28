"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1lRoCnwI2ALfHmcEBbMD2rNgieOs2oYhVFX1QUF9eXsi",
    "1ptz1DMttAC4dyuef6JAWJAzjH8s4m0z4RaHCuEeMfyD",
    "1zLa42i8ffZBYBao9Yp8meobDPvZR9NzVKxwflOoQ76h",
    "1LgUzK00bO0L9qma9tyDHVgi7g1HKSCwiYBYrSU4Fn9z"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "79611ce88e432a99301e443f6e3eb3b1",
    "40ad186c523ed7dc453dd7182257b2a4",
    "cb772d2e077f634d63e8eea4eed1303d",
    "0184e17abb37e62dffffc5df8bf89970"
]

LEGIT_PERM_IDS = [
    "936a3f93c0192f40b5d87894d831e496",
    "bbcaf097b5552b2c645055f8ce328db3",
    "d8e54ec2b07aadf13eef33b6031cb685"
]

NEEDLES = [
    {
        "id": "1lRoCnwI2ALfHmcEBbMD2rNgieOs2oYhVFX1QUF9eXsi",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "79611ce88e432a99301e443f6e3eb3b1",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1ptz1DMttAC4dyuef6JAWJAzjH8s4m0z4RaHCuEeMfyD",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "40ad186c523ed7dc453dd7182257b2a4",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1zLa42i8ffZBYBao9Yp8meobDPvZR9NzVKxwflOoQ76h",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "cb772d2e077f634d63e8eea4eed1303d",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1LgUzK00bO0L9qma9tyDHVgi7g1HKSCwiYBYrSU4Fn9z",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "0184e17abb37e62dffffc5df8bf89970",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1m1uG4pZ4tPfk02ycj8XIIadVCsFFZ6XiieJpoEvfkVv",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1p6h69B1Eebkze5okJpyPBMGZ6N9DnBrT3HIFBInKuxM",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1c8yxNHAAQZTgaPRVLs5z4yu5nnTurPyPozUY9z21jZ3",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "936a3f93c0192f40b5d87894d831e496",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1CFdRbIp1RyscbgwAmSiQbM7xJSrCDCz0x162SZrImS5",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "bbcaf097b5552b2c645055f8ce328db3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1jNRmjDq9LbGnVgNd6nOBAFEYx0C9g6zOjU4NaoN61ZF",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d8e54ec2b07aadf13eef33b6031cb685",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
