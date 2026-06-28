"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1suIexJMGPA61SJQgK3KinkS1ig6fliGm4lpfEJFBG0w",
    "1Gq3r23FMQzsl9WYU5qWPOOe2NDUKxdQs70uCTuFQvlZ",
    "1Wxivc3zTU7mxuOcKjxL5QimwWcBZZSKP62jtImOoD8p"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "3252b3b1bf85aa28455381376c123fb0",
    "6f39b2c07cc660b3c0db6636bdaf4f13",
    "4c08a501d9a93bced1915016f460f567"
]

LEGIT_PERM_IDS = [
    "40dbd22ade389503aa631ab2e8b44a4c",
    "c866cefe40b2bfab9545f242d50a50bc"
]

NEEDLES = [
    {
        "id": "1suIexJMGPA61SJQgK3KinkS1ig6fliGm4lpfEJFBG0w",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3252b3b1bf85aa28455381376c123fb0",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Gq3r23FMQzsl9WYU5qWPOOe2NDUKxdQs70uCTuFQvlZ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "6f39b2c07cc660b3c0db6636bdaf4f13",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Wxivc3zTU7mxuOcKjxL5QimwWcBZZSKP62jtImOoD8p",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "4c08a501d9a93bced1915016f460f567",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1oekPpOyyYX15sn4y13Gs8TwHDv4MlwxQUF33Lr0EnNf",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1MF0Ji69mxBGsyZzsDZGLVwsllnDbhphJaPuY9sUs8kB",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1C5szJipLF13Mhcc7z3SBBw9uYrBDFfbhym3cQl5QYOY",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1HTudMkf5Lu6OwPEjPHILXIRwuAuiAz3WvmGX1YdLMDd",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "40dbd22ade389503aa631ab2e8b44a4c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1bScyIb0MnJOCnowNcQmi84yQdQCd4xKc2osVw5jlgHM",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c866cefe40b2bfab9545f242d50a50bc",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
