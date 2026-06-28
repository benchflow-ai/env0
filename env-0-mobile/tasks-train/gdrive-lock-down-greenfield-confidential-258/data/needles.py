"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1C9ril9gc5MVv1LkW2mqXkjDk3GUFC7YoRJHUMLk6fdZ",
    "19D9RyTzn03RINx1l6JM8il7dsqd6f738QldMmRmWVh9",
    "1TTqWtuTk1GAm7IbPsvkCNImTeMnrbCZowsXxi72L6TX",
    "1QEVKppC9u6e2hnmyYwXYsW1VYbAcOctdg1FexRIFbMr"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "ab7ddbb635b7368926444a4d1bfce8e3",
    "3e34d7cf70f17ee18221f177737ad6e9",
    "278a182cda90ef52355375f9523debf0",
    "91da00b0a06154d44efc0cbcc402f7e9"
]

LEGIT_PERM_IDS = [
    "95795b6fe6965416919e772ea2b0eab6",
    "ba05ed128af529438d54b561fdf4b7cd"
]

NEEDLES = [
    {
        "id": "1C9ril9gc5MVv1LkW2mqXkjDk3GUFC7YoRJHUMLk6fdZ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "ab7ddbb635b7368926444a4d1bfce8e3",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "19D9RyTzn03RINx1l6JM8il7dsqd6f738QldMmRmWVh9",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3e34d7cf70f17ee18221f177737ad6e9",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1TTqWtuTk1GAm7IbPsvkCNImTeMnrbCZowsXxi72L6TX",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "278a182cda90ef52355375f9523debf0",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1QEVKppC9u6e2hnmyYwXYsW1VYbAcOctdg1FexRIFbMr",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "91da00b0a06154d44efc0cbcc402f7e9",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1PCGqRoaVS89oVYPE3BMbTkkL18N7UZjqMdqUF9RxFu8",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "95795b6fe6965416919e772ea2b0eab6",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1vMxmEaINO9511ajDZJe8R6pkMz18ccW5FI9tGL5OBWH",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ba05ed128af529438d54b561fdf4b7cd",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1MuwXZ1Nb7nVxmNIf0FJEKHI9lruAzMlvzaffiEcNnZX",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1MFLbK87S0aAkNuAfMcxOdJyI2PD71ijLEPJcioEb0S7",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
