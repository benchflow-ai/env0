"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1LgguEoHBahZGqN0oSQuqRRIgrSX7vjXGF6c0F8kCcKf",
    "1sJKwyGp3v3epiOy4MadRroYSD9WTf0cfvgSh9vpD1l3",
    "1XKttQob2ulTT8zUnwnaA95TbjCwKRdWb8MyLzUcuBDR",
    "14y9jPznO9oC2sPGjTXZkmNE8nA74w22N9xHhgoa4nQo",
    "1QLWJXkaxVGcS7FOXfIblDQn0wu6RESqy1UICcR4zOls"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "982e5f9b7e9012f66b3c8e35413012e5",
    "5fe69651170e63001e4f476d9aa656a7",
    "f92a7cfb364d8bb3d3a110c957742802",
    "5857bc776984f4281a860c9d1a0220df",
    "02ac026c9dcddd88c091f05af7a653f9"
]

LEGIT_PERM_IDS = [
    "a3c3f2e7f569423ec6625bf1c567dfc7",
    "674f0c99b2cc33debb3d075266a91ead",
    "53c8c44fede8d826ace7db8caccd3869"
]

NEEDLES = [
    {
        "id": "1LgguEoHBahZGqN0oSQuqRRIgrSX7vjXGF6c0F8kCcKf",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "982e5f9b7e9012f66b3c8e35413012e5",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1sJKwyGp3v3epiOy4MadRroYSD9WTf0cfvgSh9vpD1l3",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "5fe69651170e63001e4f476d9aa656a7",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1XKttQob2ulTT8zUnwnaA95TbjCwKRdWb8MyLzUcuBDR",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "f92a7cfb364d8bb3d3a110c957742802",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "14y9jPznO9oC2sPGjTXZkmNE8nA74w22N9xHhgoa4nQo",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "5857bc776984f4281a860c9d1a0220df",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QLWJXkaxVGcS7FOXfIblDQn0wu6RESqy1UICcR4zOls",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "02ac026c9dcddd88c091f05af7a653f9",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Wmu4oSumhrnXxaYTJmUDJbeqNeMM45v5jwCnfwkFYPv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a3c3f2e7f569423ec6625bf1c567dfc7",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1MIOsn9gv7ziCCPWMn27qIaDKeLLrYc4gudW0qwoV0cp",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "674f0c99b2cc33debb3d075266a91ead",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1D76J35jmyBXUnfY2r4HMxpczony5AA5ik4X2fKwUYo1",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1jgu8Uqv3rupUln0a2Tm0Y1pizw8oZcmAVCqoHWMfq7x",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "53c8c44fede8d826ace7db8caccd3869",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
