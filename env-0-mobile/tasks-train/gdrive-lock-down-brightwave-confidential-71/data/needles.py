"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1qRRznVRJV2gihBcPP7iVo1BpkavFiTusERbpxFvtdTP",
    "1nnCYc6u8x1edrLOggQipg9iqbJbbhoOJh63NaMQV4vn",
    "1gg1uBBmFJ9Hg8VFMAxUHrJ7qx5G7uSMRm6pCDaRhpMb",
    "1KAaia4pbofivQFJng42IqxxwoZCqWnkf2efwkLfKJJh",
    "1Fpn2tY73E3KHI6CZOwzvIXW40xZ8gQizZKYyTbsjw85"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "8baf3b8e00e1cc8d6464c91722636448",
    "8ad5ca47b9aa4e0826dd256a95c82c03",
    "62625942c65f29ea2e2a8416d9863d5b",
    "8219759ce42e4b8ba1794e08bf86e01d",
    "832c15d2c9780e3c095e060b6aae763c"
]

LEGIT_PERM_IDS = [
    "d857ff4eb2307e54a32f93702051b958",
    "d7c8a52e3508a967ce6e87d3e9e59cad",
    "88c5bf528e68d91e7ab2ff0821c400a9"
]

NEEDLES = [
    {
        "id": "1qRRznVRJV2gihBcPP7iVo1BpkavFiTusERbpxFvtdTP",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "8baf3b8e00e1cc8d6464c91722636448",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1nnCYc6u8x1edrLOggQipg9iqbJbbhoOJh63NaMQV4vn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "8ad5ca47b9aa4e0826dd256a95c82c03",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gg1uBBmFJ9Hg8VFMAxUHrJ7qx5G7uSMRm6pCDaRhpMb",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "62625942c65f29ea2e2a8416d9863d5b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1KAaia4pbofivQFJng42IqxxwoZCqWnkf2efwkLfKJJh",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "8219759ce42e4b8ba1794e08bf86e01d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Fpn2tY73E3KHI6CZOwzvIXW40xZ8gQizZKYyTbsjw85",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "832c15d2c9780e3c095e060b6aae763c",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1RXnyJ0WfdhdQL1Z2OMp0vrgHivYgbYMpKgSvq7gIF38",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1UTUJaQ7coftqILWWXcp4OI8mi5D0TFrmrHVQQ0hvjqR",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1pMV4yOeIfc6wr8FqaqkN4NVO6OKS7dKUwYE8Gw64v4M",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d857ff4eb2307e54a32f93702051b958",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1feX8Y81WrdI1p9QOTcbx2ZqBCv0tf8FEivByPu44vEY",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d7c8a52e3508a967ce6e87d3e9e59cad",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1zlsBAdskqPxlUcuP1kPNhhw80jmm2I8DqVmT9pqYKOx",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "88c5bf528e68d91e7ab2ff0821c400a9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1zawFD40ql7DpaibrNjLimkW4gyyM4yPgSLOwhPcSVM9",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
