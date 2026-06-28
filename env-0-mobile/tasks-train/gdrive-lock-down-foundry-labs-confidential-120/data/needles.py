"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1I2eIj9o75urh0tsHUJ2QCn2pgzXQUEQKlBF0NdqUg6M",
    "1KzacIRtpklJvj39LSNtwxdSDfL5FjDEC4WHprPNjdDh",
    "1dWasLEm7VaAQO6olMDQo2qkXCjRWC0WnBdc5J5mpYQH"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "b96841229e0b4265c385a38dd5dcf190",
    "b6c14b5b81c3bd46f876662dde04edf8",
    "9f8d10acbe060d40e5caeb0b05438bca"
]

LEGIT_PERM_IDS = [
    "da21ff749e058b9049231fa7d9b9904d",
    "000fb5c03a38077bf76e67174a7360b0"
]

NEEDLES = [
    {
        "id": "1I2eIj9o75urh0tsHUJ2QCn2pgzXQUEQKlBF0NdqUg6M",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b96841229e0b4265c385a38dd5dcf190",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1KzacIRtpklJvj39LSNtwxdSDfL5FjDEC4WHprPNjdDh",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b6c14b5b81c3bd46f876662dde04edf8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1dWasLEm7VaAQO6olMDQo2qkXCjRWC0WnBdc5J5mpYQH",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "9f8d10acbe060d40e5caeb0b05438bca",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1oxSmfyPnDszH9zFIXIlDwcoD87PZpmruzUPT6R8z2QH",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1bcTVziiugr0GU75NQLBOcmlpLnOQmfTN1iL5KxB0Pdi",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "da21ff749e058b9049231fa7d9b9904d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1po4uSsjx0vXkZYhsBBwQc37vca0j8a7Q4TcRIhxqQmX",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "153BnDSyWqct8eiluhqm8eld9hBkOgipEdHFUs7BOgw1",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "000fb5c03a38077bf76e67174a7360b0",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
