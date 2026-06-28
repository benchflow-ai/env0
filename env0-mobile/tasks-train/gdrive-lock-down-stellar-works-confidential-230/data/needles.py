"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1TlRqXxqs2QF1p2qcpBtYFhRA3esBPqrO0cEGbdhBVyz",
    "1UV2yCCDsPuYCVkCZNKEzUYhXPtKw49XCJ1QmDPk1ixP",
    "1CGmABBXPaEZRn7W24cQ1HpIFBMPsZN7uqVPBI4Gaj7p",
    "1AkzQMlkaMHsMfLmlwSYJEmRwP6VcPLiswAW0bKDlHRq"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "fefc83d7bdc74175893c689f43eaf8f5",
    "314dcd8070a8aab172529092caedcad7",
    "26c1c5b4f4c29bb69ffceee471f6549f",
    "b79bcbbedcdd8dab5d4fcc06f391a354"
]

LEGIT_PERM_IDS = [
    "b85b03deca7398dab0827d71cefe2751",
    "4472354d17fda8fe6583b4a2e1efe5d9",
    "7b15574dff6980e6f66457f187fb4570"
]

NEEDLES = [
    {
        "id": "1TlRqXxqs2QF1p2qcpBtYFhRA3esBPqrO0cEGbdhBVyz",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "fefc83d7bdc74175893c689f43eaf8f5",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1UV2yCCDsPuYCVkCZNKEzUYhXPtKw49XCJ1QmDPk1ixP",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "314dcd8070a8aab172529092caedcad7",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1CGmABBXPaEZRn7W24cQ1HpIFBMPsZN7uqVPBI4Gaj7p",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "26c1c5b4f4c29bb69ffceee471f6549f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1AkzQMlkaMHsMfLmlwSYJEmRwP6VcPLiswAW0bKDlHRq",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "b79bcbbedcdd8dab5d4fcc06f391a354",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1KuoNQ8S7nTr8JyORvXQhajOrUqhvEpfue0RKALICtzo",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1g5RbllOU8vt7rEhqkNoNSlACeIyBFo1M48ZK5stgd1C",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b85b03deca7398dab0827d71cefe2751",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1gYFuRpt0UDbArBV4so0e24CJglBPQbDl1xgkKVp1Ek5",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1TI0XlDFUiLbKPwQkVCVsWzJq959CyFDAfnKADuzo9FT",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4472354d17fda8fe6583b4a2e1efe5d9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1N1Uy6UbSbw8YgCUvI9uPFwcja3lBAN3OIFdzcV6MCL8",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7b15574dff6980e6f66457f187fb4570",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
