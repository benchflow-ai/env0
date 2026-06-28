"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1IpuqNIiP28V5mwni5kMzz6e5zjVXyIzsDNlpMGz631M",
    "11SsjtnkWzGVAJbpjLs1mkFnou6GPStXSdSYQamVb8bE",
    "1fKz7eB9xeolIlw3JawDUWUBiDa9a6yAfxn3W9y8bnjL"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "28f33d7f8368b4a6aba34706207d201a",
    "75a9fa569fc53d59247228ca9780a3b1",
    "6be58820d365e7a5b104c5943c9a12f9"
]

LEGIT_PERM_IDS = [
    "cb96987225085b2d2555a61b1a67fef8",
    "49430b98ea0669c75f480208a0e4842b"
]

NEEDLES = [
    {
        "id": "1IpuqNIiP28V5mwni5kMzz6e5zjVXyIzsDNlpMGz631M",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "28f33d7f8368b4a6aba34706207d201a",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "11SsjtnkWzGVAJbpjLs1mkFnou6GPStXSdSYQamVb8bE",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "75a9fa569fc53d59247228ca9780a3b1",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1fKz7eB9xeolIlw3JawDUWUBiDa9a6yAfxn3W9y8bnjL",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "6be58820d365e7a5b104c5943c9a12f9",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1mJ2WM4gqdsIuCq2oFSNnMEGgC5Vhtu6TBuY9ouxUmSm",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1IUYQ0y9XHPJsNacRzeLwxVolGjhgqOPUTpb0sw5QjPx",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "cb96987225085b2d2555a61b1a67fef8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1HyFrgtff1RNOgLUHmWaPb4K9Cj0EqhqMkNGSAWCc9ve",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1pT8fwExGlpQjuJrH0hIpcdw1nLL9l2Zz5kQhDJ3bK5T",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "49430b98ea0669c75f480208a0e4842b",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1GhccqHQ4lBrXRcvqIYr4TivfCr5ghMPoRdkUbAEZICy",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1N7fJ1B93w0yYJul8WviSMInZzpP2bBu6XDomPWePOt2",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
