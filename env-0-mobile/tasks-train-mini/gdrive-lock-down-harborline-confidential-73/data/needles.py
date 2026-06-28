"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1s4mk6JysrcSUtzWKz0fqRqbezCbwJU8GZbOKDk79gvf",
    "1tRQRmDuSZDOKorva4RMhOgVO9OwoQCYatQbmgRCFHVX",
    "1NVafCUDQbuPtoTrGhCGGcdLPwQeR104nK9Kguv6LfO0",
    "1cHPW3JtZMtyQk5IU5MVKAQODbAMTYVjCi9O8ZEaLrR3",
    "1BdKRjNZsLTp1vbyDbFEPKB08KsUG4GLX7eiA5uUMbhl"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "d2cd85ba56f571e3c7d24b64c0a7ae78",
    "937d7f33536856216e4c875f51e859bc",
    "92d5e8b7e207b8c1494a001f60cf7720",
    "fd66e8f8d51876361ce7f06487deb0ec",
    "fb5606190ad36ca4487e85293d673de0"
]

LEGIT_PERM_IDS = [
    "54e535735c8014559f78e87411ac2b17",
    "0031956ba921cad468e35e8c51556841"
]

NEEDLES = [
    {
        "id": "1s4mk6JysrcSUtzWKz0fqRqbezCbwJU8GZbOKDk79gvf",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "d2cd85ba56f571e3c7d24b64c0a7ae78",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tRQRmDuSZDOKorva4RMhOgVO9OwoQCYatQbmgRCFHVX",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "937d7f33536856216e4c875f51e859bc",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1NVafCUDQbuPtoTrGhCGGcdLPwQeR104nK9Kguv6LfO0",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "92d5e8b7e207b8c1494a001f60cf7720",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1cHPW3JtZMtyQk5IU5MVKAQODbAMTYVjCi9O8ZEaLrR3",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "fd66e8f8d51876361ce7f06487deb0ec",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1BdKRjNZsLTp1vbyDbFEPKB08KsUG4GLX7eiA5uUMbhl",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "fb5606190ad36ca4487e85293d673de0",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YLQzfFcrlJafru16VRCd3QFT5cyTzdi6awRS0MSyMWP",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "12KCqwB0I1oY0SIvVgb1nelRtv0ptWoT2HP7mO7VvqHM",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "54e535735c8014559f78e87411ac2b17",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1bMkPCOzfqXt1yApCntX4JqCPacDFFngsrXqFb7g1dUj",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "0031956ba921cad468e35e8c51556841",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "16pYetEaodrixlSgtLGpI03xmFogRkaDIjTgo38IdqGP",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1WyDdV86CZOtwNt9YAaz334dnrPTfQtSeg2cf3XIxu2x",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
