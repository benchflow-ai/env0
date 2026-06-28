"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1fsgbj7lhsc4cJYtebgnPHKWG0CMTlo24IKJRCt0pewG",
    "1WQkxlKzPscnyfpXcRqOhfudDS67e0lqQyvzHHru2H0P",
    "1wLhlVKY6eQCyr2dgXDW3dG6kXMy5RiJJnFCNcxAe94V",
    "1go780gb7mG0l523S4mJWfjjkY2Yd5ST7ElWjziRdotE"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "829bc9bcd35069fa1940a0967e1faf89",
    "f1b7772a7acdb48656bb408f1ba2b18f",
    "87c625eb67589dbde9264e7965b65b47",
    "a46e3927b7ace6903a7330ad4ff2007c"
]

LEGIT_PERM_IDS = [
    "ff1787a600b199614d56bcb768f34d7c",
    "241c69be3fc0fff864f5c5eb0949af8a"
]

NEEDLES = [
    {
        "id": "1fsgbj7lhsc4cJYtebgnPHKWG0CMTlo24IKJRCt0pewG",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "829bc9bcd35069fa1940a0967e1faf89",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1WQkxlKzPscnyfpXcRqOhfudDS67e0lqQyvzHHru2H0P",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f1b7772a7acdb48656bb408f1ba2b18f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1wLhlVKY6eQCyr2dgXDW3dG6kXMy5RiJJnFCNcxAe94V",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "87c625eb67589dbde9264e7965b65b47",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1go780gb7mG0l523S4mJWfjjkY2Yd5ST7ElWjziRdotE",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "a46e3927b7ace6903a7330ad4ff2007c",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "174DHYyuUu2qDLdQBCBQoDxNG1WNEeulaeU8lUk2Lcm1",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "ff1787a600b199614d56bcb768f34d7c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LAr3iVCmOkTuIHmOxW8cGYCVDXqhlzHg2JswRlH391x",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1aq6ysnuol2AI45xxIj36eJQzgNONFDZX0MSQjjqt9FT",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1gg4RLcWzbdh6tqtiCFeJPaoYasAtDuJ6oXjV9e1KM9D",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1CqQcfckfeTvGc39Wlp8RprvxS4FJwF00fsKUet0Y5Qd",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "241c69be3fc0fff864f5c5eb0949af8a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
