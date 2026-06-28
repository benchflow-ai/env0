"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1r0utzsfBQ9kI5eggPG3UjtvrV2Nf44rVcJq6i8geggK",
    "1Eg9Gy80rFkNfD6nOGGv1yX5Ap895hZ1vPfqE5h2FXw2",
    "1xulHkhBuH4h9879GrZ46PYIq1G3HxLESLt4wYu8AxbF"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "8614ab964ce545187993046f5968bb14",
    "f70354ae148d8f7f99ad0b1cc5c192d1",
    "1e9c06e10b513549acb8189607dcb7c6"
]

LEGIT_PERM_IDS = [
    "b3d0d0b3e228c9448e4ea707e37cb90e"
]

NEEDLES = [
    {
        "id": "1r0utzsfBQ9kI5eggPG3UjtvrV2Nf44rVcJq6i8geggK",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "8614ab964ce545187993046f5968bb14",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Eg9Gy80rFkNfD6nOGGv1yX5Ap895hZ1vPfqE5h2FXw2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f70354ae148d8f7f99ad0b1cc5c192d1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xulHkhBuH4h9879GrZ46PYIq1G3HxLESLt4wYu8AxbF",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "1e9c06e10b513549acb8189607dcb7c6",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "176l3ecOyd4NfO04xWEF4H7nkH4EM7LDZiR27cpVUZDU",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1i3YvFscn1EW1APICCqCTvoN2wseYcyvaeDvPucSIYWQ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1vRfmXLkwhQOsfVuGFuT9Cd8pUhSwDIa22GDRxUs4Cl6",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1XMLZ78l1XEtpjVYg6LvP5lSJe5TrkzkUIu1zlSrhjRe",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b3d0d0b3e228c9448e4ea707e37cb90e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
