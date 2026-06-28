"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "16HbiIXnjQy36gd0PZXsDJNciCfWYIdvt0futkCRojBE",
    "1j0VmBLShqtiA3detYZJC4kFOfBcje9NtLaKXjmsnJE2",
    "1Rk7jw92X4xpBBTbptVVTEkUXyYgxrWMfPLDzP2ibiGF"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "15288b9d39b1d1f285dc083e7d97b463",
    "94482baa2f888515745cb64eb5738918",
    "aee6b5e780a440aaf7d07df03a74530c"
]

LEGIT_PERM_IDS = [
    "820b150293b8c7f17079bb2772ece552"
]

NEEDLES = [
    {
        "id": "16HbiIXnjQy36gd0PZXsDJNciCfWYIdvt0futkCRojBE",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "15288b9d39b1d1f285dc083e7d97b463",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1j0VmBLShqtiA3detYZJC4kFOfBcje9NtLaKXjmsnJE2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "94482baa2f888515745cb64eb5738918",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1Rk7jw92X4xpBBTbptVVTEkUXyYgxrWMfPLDzP2ibiGF",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "aee6b5e780a440aaf7d07df03a74530c",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1e8Ebeer56pSF8az3LSyYO3qHzCMWsCDEJ3pLomQclKj",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1dRckF51mCeBFTuiB91y4fsCgspGa9hlmBF61vraSGOx",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "174oCxuSy9zaZ8UsV0UYbyoMyDi1sXsURj82X020aXoF",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "820b150293b8c7f17079bb2772ece552",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1OW641ih3xQtNa09DPHGlTWbY9V4K2nVWXzYzg7iYrRR",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
