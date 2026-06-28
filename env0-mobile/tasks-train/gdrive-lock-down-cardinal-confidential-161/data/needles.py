"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "18Ef60WjQSX4dezqwd9UAGUyAigOHuLUiriSSeYQz6FH",
    "1DLZq9IjALHnokdaynZl1MkyTGmlFhmeZCnvkCP8ivdb",
    "1ealOTRNCO52eP0cJxMdQ9zsjiGC0B5RIndF59UzXs4M",
    "1O998xCqY8fcvd9oMAkMEujmPp8Ap5z2l1yIaUBBSuBP"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "1823b4ae6e40087ad23c7275b0ddcbb8",
    "c82647ad6479f81f06a54d2dcc74c1a7",
    "b00b1d0169de848d24924b2413ddaa80",
    "4d7e45e284d9d10eac8bff80a6d8975a"
]

LEGIT_PERM_IDS = [
    "dc96e170043305dc6b8ae41783ce32bb",
    "49b828083ed37e660bbbcff432e4c6ba"
]

NEEDLES = [
    {
        "id": "18Ef60WjQSX4dezqwd9UAGUyAigOHuLUiriSSeYQz6FH",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "1823b4ae6e40087ad23c7275b0ddcbb8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1DLZq9IjALHnokdaynZl1MkyTGmlFhmeZCnvkCP8ivdb",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "c82647ad6479f81f06a54d2dcc74c1a7",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1ealOTRNCO52eP0cJxMdQ9zsjiGC0B5RIndF59UzXs4M",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "b00b1d0169de848d24924b2413ddaa80",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1O998xCqY8fcvd9oMAkMEujmPp8Ap5z2l1yIaUBBSuBP",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "4d7e45e284d9d10eac8bff80a6d8975a",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1yMLMxVByMjfp3AE1FUQbugyKynE6Ttexq1bh1AUxWBY",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "dc96e170043305dc6b8ae41783ce32bb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1KvpjqWH6ioJASW2nFpFhxGcxW8Cb610aAh6sXQh8oNN",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1vZbeLHqPcbKWJNkgpfizfoSUfhqxzUcIIEsLEZAv0Wm",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1b96dViPLJvi8S4ySTIxcz8o2nMRrCsj4e8oCXCBi0Bb",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "49b828083ed37e660bbbcff432e4c6ba",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
