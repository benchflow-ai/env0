"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "10gyl58lca9WfLz3C0OYwSOcyiltEGMvWKL5JDcDtioo",
    "1kWUshmtiwKv1iutmXEtvOl7KnfEbnA2a31RdMAYmbgG",
    "1jFEbQnAAwrwHUgzs5GNghH5ctC3wUYJuRRJdjsThfLB",
    "16LaPXclIQkJiBt9kujt70XlJFd8INTjkBzuTQf3WUbM"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "769d71edfb73b0d946ebd3b2c4e4b0db",
    "55417568e6d1195153a0354048271837",
    "5d73cf6322509f12c8905f270bc6d733",
    "29b996e9662efb29dd2b5ec14ad096b7"
]

LEGIT_PERM_IDS = [
    "ee74fc03ee90a0b9d430586668356c77"
]

NEEDLES = [
    {
        "id": "10gyl58lca9WfLz3C0OYwSOcyiltEGMvWKL5JDcDtioo",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "769d71edfb73b0d946ebd3b2c4e4b0db",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1kWUshmtiwKv1iutmXEtvOl7KnfEbnA2a31RdMAYmbgG",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "55417568e6d1195153a0354048271837",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1jFEbQnAAwrwHUgzs5GNghH5ctC3wUYJuRRJdjsThfLB",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5d73cf6322509f12c8905f270bc6d733",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "16LaPXclIQkJiBt9kujt70XlJFd8INTjkBzuTQf3WUbM",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "29b996e9662efb29dd2b5ec14ad096b7",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "16kztCRBXpJu9PeEAE55uuVswCv6YBKV3qv3kKyqQoTH",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "15gEhFWz27TaCPi8Wxeb3GiNWxptk0q02BI2HBFFTUL1",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ee74fc03ee90a0b9d430586668356c77",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Lu9740r1AVVEmGnS5M8hUY0bLwR5NifdPtB2vaS0eYx",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "17z1RTYhzKpHmC9liClbxUNZIB2JU1zEgX9pzi7FgJ8M",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
