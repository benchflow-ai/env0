"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "11HwGecmcKcZsuk9opw5BhQrwebpSPLu4V7eT2DJ571Y",
    "1JEqCIJE1QoGyCx5fw1oXRiKaWBfWRB3LY7MnxbmQIdM",
    "1n7WQiPK7QDcf63Omts5z8efo8qu0V9DwyKlEI0bDnqp",
    "1jK994ih5a9FFZ8U4zLC2HB3JqsgDP4eCYKh3kTZoQLa"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "ec2d8bd4e83fbe41a3c8f3f9250112ee",
    "40c8c9c1bd759a8eb0480e5627d51d0e",
    "4c6004626668b1d3a411cce0c68aea90",
    "4fb58061f0a1aff8da29387f03462358"
]

LEGIT_PERM_IDS = [
    "30d60a9f7ebbf4ecdb32c29792eeacd3",
    "5a55b7b1cc87ebc3b4067eee8fd41d47"
]

NEEDLES = [
    {
        "id": "11HwGecmcKcZsuk9opw5BhQrwebpSPLu4V7eT2DJ571Y",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ec2d8bd4e83fbe41a3c8f3f9250112ee",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JEqCIJE1QoGyCx5fw1oXRiKaWBfWRB3LY7MnxbmQIdM",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "40c8c9c1bd759a8eb0480e5627d51d0e",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1n7WQiPK7QDcf63Omts5z8efo8qu0V9DwyKlEI0bDnqp",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "4c6004626668b1d3a411cce0c68aea90",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1jK994ih5a9FFZ8U4zLC2HB3JqsgDP4eCYKh3kTZoQLa",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "4fb58061f0a1aff8da29387f03462358",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1aXHheC5aQdz1RmOtenZ4kfokAEjr1IVD1yeN2zRdivf",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "30d60a9f7ebbf4ecdb32c29792eeacd3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1z67WZPdcUxXiOQ5QvM08TXTSqM7niWns1gV4z5f9YOL",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1EhYqLs6V9FRizEWSDkkHRKITBkjUb613EiHcrxEtUeH",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1NKt75expogG7wrPpYjSwwlV74SjFjgnPHtu0MNm7yy3",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "5a55b7b1cc87ebc3b4067eee8fd41d47",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
