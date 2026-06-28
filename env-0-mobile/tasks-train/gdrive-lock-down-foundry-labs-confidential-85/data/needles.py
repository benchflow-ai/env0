"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1q76ORqPlWCl1Kih8jmb9pjSGEgeghgwRH9DGGORX3Ur",
    "13CQLN8oGu2OVTOwlBQHa6c6HDO8dgJD77hiXC4Dnryg",
    "1lwt5xi8ai0g5NdlXmFtHOOCG8XLJmokHYwJFr89qNZb"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "173a84d315cd2d10b2fb37f9af066bd4",
    "d517f9c7bee16a2bfc8cbe43485cce26",
    "464c2207f0d1f2feb327ceb071475d3e"
]

LEGIT_PERM_IDS = [
    "f2d533fa5e8aebc4192b143e282582f2",
    "45b4f11dd5d9636ac9e48dfd46c11529"
]

NEEDLES = [
    {
        "id": "1q76ORqPlWCl1Kih8jmb9pjSGEgeghgwRH9DGGORX3Ur",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "173a84d315cd2d10b2fb37f9af066bd4",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "13CQLN8oGu2OVTOwlBQHa6c6HDO8dgJD77hiXC4Dnryg",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d517f9c7bee16a2bfc8cbe43485cce26",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1lwt5xi8ai0g5NdlXmFtHOOCG8XLJmokHYwJFr89qNZb",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "464c2207f0d1f2feb327ceb071475d3e",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1EBq6ONxAoDQXikuLoFxkPS9DYIMtOpQRliTkqC9MZeK",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1xJvn2PAtVuxBhnQOrAlS3HARM46weGtfleOm7m815ig",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1kyhYp2HM52E8k5N7jvSLQJCePWCVjxQ1Gn0JLYOnmNg",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f2d533fa5e8aebc4192b143e282582f2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1wIpMpUTHNGl4eh3UHc8cryimznzJXt9nKpWJcLwGIeA",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "45b4f11dd5d9636ac9e48dfd46c11529",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1OfOETyzK3MQ9YnAaKQUb2hDV6WYyVXJ8VY8bflVovqS",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1C9x1iPCFgwz94bTfvwIe4IQLwOiZPomY9t66NhOe34C",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
