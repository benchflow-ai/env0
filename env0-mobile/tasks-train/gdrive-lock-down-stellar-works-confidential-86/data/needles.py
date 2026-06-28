"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1uX2w7ExrOUkNyumHc38bV3aU4kZfdNnPvxGLe1ye7ZT",
    "18NnrpUmMUiC7QENnxnXBKh6g9tWGu0wewwoMQ0bLC2k",
    "1UD0X40mrt1k6pBU22ex6Prdt18laCdrZVqAcLKcLDOd",
    "1AmWKA2jab9ZWbGyGOyKXSkFbDQySIigCJc683qJJC2s",
    "1AbePcrkYNBxy0Ku92WIMfr6nDuzHy0IMPEA51K139aD"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "4254a11ee97e281e6c1e32f75d540f4c",
    "b44949d15882e5f9a9ceb224dae79df7",
    "ad9219bc442d068cc6fa5522f1c504a1",
    "cecc0a0d5ec588498e3efc298e4f58a9",
    "9c16155c6c538e7f25a9613f87a2b26d"
]

LEGIT_PERM_IDS = [
    "a4da51ae76cc36f69da86dbea7ed6170",
    "76159274806b21d90f59a93fd62a1921",
    "0ad92df5e0f45827af991bf084f37cc9"
]

NEEDLES = [
    {
        "id": "1uX2w7ExrOUkNyumHc38bV3aU4kZfdNnPvxGLe1ye7ZT",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "4254a11ee97e281e6c1e32f75d540f4c",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "18NnrpUmMUiC7QENnxnXBKh6g9tWGu0wewwoMQ0bLC2k",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "b44949d15882e5f9a9ceb224dae79df7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1UD0X40mrt1k6pBU22ex6Prdt18laCdrZVqAcLKcLDOd",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "ad9219bc442d068cc6fa5522f1c504a1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1AmWKA2jab9ZWbGyGOyKXSkFbDQySIigCJc683qJJC2s",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "cecc0a0d5ec588498e3efc298e4f58a9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1AbePcrkYNBxy0Ku92WIMfr6nDuzHy0IMPEA51K139aD",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "9c16155c6c538e7f25a9613f87a2b26d",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1xyGA2SauIeVFHrnkW2GgLf2XIgpYEwFEnQwsfN0nJgN",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a4da51ae76cc36f69da86dbea7ed6170",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1hG8iC8IcsGLilC3gb7sM0DtOKjPPm8jBKCO8bsnosCS",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "76159274806b21d90f59a93fd62a1921",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "19Pg9uF7Qcg8IP6oLOmypktq7D4RdfjfUeW6rllQrQGF",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1rkTn4tOGJXoYpcdOOM3hHBiRz7b8o8FXCJdZVBNmyXF",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0ad92df5e0f45827af991bf084f37cc9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1MZD562d4s6lYMDAhrhIq811rBESzAfvN5BkdglrEFSL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1lW3NeawqxFrf6EIPSdu5JMPveFa2uJhrYBLk7n6mI6N",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
