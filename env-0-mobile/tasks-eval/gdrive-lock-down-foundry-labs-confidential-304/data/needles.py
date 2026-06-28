"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "11BMogWns688J7LW7kU7pcnN604oGPQ8kuBAlMbZEqy9",
    "1URgBa3JIybCdduL07rOpQBe5jST1hQlePTlTXaQYRkW",
    "1bNs47FotOSHztlFEqPLijX41V2FQw0tZ1J1RaCakIAs",
    "1c2dfaDBBTisX9yzGoWeQzfZ4uPFWGvBl0dnEpNVum41"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "afbcbb787eb059482ee5144bf38728a4",
    "067a67d4ae3df735031a2abf815cdba0",
    "24b631ea5827f8c944ec452d14455aa8",
    "02938a834fa0c23d5a1aefff1211b28a"
]

LEGIT_PERM_IDS = [
    "02c94c6a21c57e44ec2658e483eca548",
    "b5c713aabf4803dca519aa3086bfbce1"
]

NEEDLES = [
    {
        "id": "11BMogWns688J7LW7kU7pcnN604oGPQ8kuBAlMbZEqy9",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "afbcbb787eb059482ee5144bf38728a4",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1URgBa3JIybCdduL07rOpQBe5jST1hQlePTlTXaQYRkW",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "067a67d4ae3df735031a2abf815cdba0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bNs47FotOSHztlFEqPLijX41V2FQw0tZ1J1RaCakIAs",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "24b631ea5827f8c944ec452d14455aa8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1c2dfaDBBTisX9yzGoWeQzfZ4uPFWGvBl0dnEpNVum41",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "02938a834fa0c23d5a1aefff1211b28a",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MGeZ0lOfCyMPPWSJZo57xwp0aCUCYz2AzUd8dCr8pJz",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1STYX89wRRmBajTvv4cCv6xGS0kX2OVBdLFsl6U3HWwK",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1TAKxJzfZcG57y7lX0r2PRI2uaP1Tw7PVVDA7ORgcRzS",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1PhxamHIF8ECyMVrV0wLmcbQRoDkfEiILwngfeC22uqH",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "02c94c6a21c57e44ec2658e483eca548",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1qXVxwv0fryX4ROltse8HWNm3CjlGn4udNt0icOhmGVj",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "14Zysqae0e5o0XObvIOZHB8wUgQIbBnzS1PTsTiMIbwS",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "b5c713aabf4803dca519aa3086bfbce1",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
