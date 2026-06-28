"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "19AySObe0vgmQCW5698y1p4U3ZElYbPZNiq2kN7qdhso",
    "1xxg0VLVgZ3KC1WBw53Z3hHbRGYvQooLgUGVaYJxAYpg",
    "1zlg7lpBgZQjpzugs81lkU22ILfJ1qabJtKvzxZVSlH8",
    "1WFFVFK78InL5WJbIlbq84nHKaW6aEexbPyD0Kasnt0e",
    "14mWVjsBxsrLpUOxA9tiJlRuvKzsy4oLAZ4hNkNvA0Nq"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "bb114c6907f25374de8aa763208f63fc",
    "19ce03d50e514cfd09d9d4239266c6e2",
    "993b6b5db56949df55665af64043a57a",
    "9012c187fea802bc7cb30a057570083b",
    "e356fcd112b80e9687376b2103c3f1b4"
]

LEGIT_PERM_IDS = [
    "7a60cced628507950a5f00bbe709aa3f",
    "522d3e00f81782190041086a8e8b0dfb"
]

NEEDLES = [
    {
        "id": "19AySObe0vgmQCW5698y1p4U3ZElYbPZNiq2kN7qdhso",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "bb114c6907f25374de8aa763208f63fc",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1xxg0VLVgZ3KC1WBw53Z3hHbRGYvQooLgUGVaYJxAYpg",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "19ce03d50e514cfd09d9d4239266c6e2",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1zlg7lpBgZQjpzugs81lkU22ILfJ1qabJtKvzxZVSlH8",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "993b6b5db56949df55665af64043a57a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1WFFVFK78InL5WJbIlbq84nHKaW6aEexbPyD0Kasnt0e",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "9012c187fea802bc7cb30a057570083b",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "14mWVjsBxsrLpUOxA9tiJlRuvKzsy4oLAZ4hNkNvA0Nq",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "e356fcd112b80e9687376b2103c3f1b4",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1wIRtxe0t8ZLDhXG2lHf13teB5pdzHLz4TtRh3mEXE6E",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1OVB5N5AOIT2XlNZVHnuHzvwtpiZ5LVLA2AXUmtNPPnE",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1BwUJOLs3SymqDWmKRm1CwWtPBRz9gDpWYzWClAPNCIt",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7a60cced628507950a5f00bbe709aa3f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ODpepOnX5vphhDOPRDc12nrdNCCx61X7qbdsPkyaBzX",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1xtU7kCocijzIYYjLYKpbxRMbPnP1HwkLfMnyi23gyKu",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1TxqxfK2pab7NHQBa9ZM3Fb8Mi6l47mvQbNJDuFYOa9s",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "522d3e00f81782190041086a8e8b0dfb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
