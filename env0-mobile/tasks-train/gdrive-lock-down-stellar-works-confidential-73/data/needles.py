"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1Z3cqVKWyKAKvitvEXuQtoG9QFIoW5MHs3oD6KNVJSZS",
    "1CsJDQSf8MGirhALC3sek2P4eU2o8Uay163Bx1kl5taU",
    "1i9S6woq4Snrty3ewcBQ1XR0nPDof3RDULgEvWWEPivS",
    "14aOjRnrGQiAYnk4NW1kt7GHdyFWjpvCN7dN40WSoxCy"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "b328f1679184312f1a2f7cd78987ecfa",
    "4089b9d915bd9c2099ece1abaa77e447",
    "296c3252ff0ee05b924106c871287ca5",
    "2b4d727555c48b48183e6a046d47ab00"
]

LEGIT_PERM_IDS = [
    "81ee9c368340d04312126f30d4933ac6",
    "26ecc51fd4cc4b548fa70e20ff4a701f"
]

NEEDLES = [
    {
        "id": "1Z3cqVKWyKAKvitvEXuQtoG9QFIoW5MHs3oD6KNVJSZS",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "b328f1679184312f1a2f7cd78987ecfa",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1CsJDQSf8MGirhALC3sek2P4eU2o8Uay163Bx1kl5taU",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "4089b9d915bd9c2099ece1abaa77e447",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1i9S6woq4Snrty3ewcBQ1XR0nPDof3RDULgEvWWEPivS",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "296c3252ff0ee05b924106c871287ca5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "14aOjRnrGQiAYnk4NW1kt7GHdyFWjpvCN7dN40WSoxCy",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "2b4d727555c48b48183e6a046d47ab00",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ZSMHWCLi3lfcjfrR7qGiJrCzZetpVQreL493Ez5OkXJ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1ZIk2FAnoEK60JPctJ6QyAgANpgJuTDkw9xUCPFBx1UR",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "81ee9c368340d04312126f30d4933ac6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Xk6weCkEMV5JtEGb46gOaeHhFDQNqunlHrQO9FzChlh",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "26ecc51fd4cc4b548fa70e20ff4a701f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1s5ZVSSMl5RRTuOa5C8sfXtA31OBTq5UD1TQHvuuSxEy",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1khbJ3oJ2Dnu6Z1fsB12fEWOguryZ1j5VnIatIpApFZf",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1UszyuKlqI2nPSTlNHNgxvgwgrldOy1YohkX61iGuC8P",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
