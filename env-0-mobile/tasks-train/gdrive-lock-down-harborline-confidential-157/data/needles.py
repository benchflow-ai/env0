"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "17SPtv8NWmvaznIpinNKVa3kJf48FuxdhqafyZ6yryh6",
    "1FfAshrc49l1te16S07nPxLg36yoYqGH39jAEmafp7IV",
    "1Crv2pxYWYRzUo7UO5y3BXpXcL1mNteQXDK3FBoddcK1",
    "12kyFQBq2YPS0cg2Sqq2JtTLaG3Unv9TpB03PCyT9abg",
    "1XbGh1S4QvOnDRw1YRSiUTkc1IpE27rRe92qE9Ufhdx8"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "3ede87c224dc4b76c42d0ea126ab9b61",
    "988e30b23c64bc65bb8252c14a87fcb8",
    "c09711edf9ab52f055755c947da9b384",
    "45a8377c2c4a217a83c3f366a9a21549",
    "ca17765f1a216fbe8d1d94ae58e680af"
]

LEGIT_PERM_IDS = [
    "7ff86df649ebac05d4767905850d9e3b",
    "2357f71e1abef6006022b27a96dc0169"
]

NEEDLES = [
    {
        "id": "17SPtv8NWmvaznIpinNKVa3kJf48FuxdhqafyZ6yryh6",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3ede87c224dc4b76c42d0ea126ab9b61",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FfAshrc49l1te16S07nPxLg36yoYqGH39jAEmafp7IV",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "988e30b23c64bc65bb8252c14a87fcb8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Crv2pxYWYRzUo7UO5y3BXpXcL1mNteQXDK3FBoddcK1",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "c09711edf9ab52f055755c947da9b384",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "12kyFQBq2YPS0cg2Sqq2JtTLaG3Unv9TpB03PCyT9abg",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "45a8377c2c4a217a83c3f366a9a21549",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1XbGh1S4QvOnDRw1YRSiUTkc1IpE27rRe92qE9Ufhdx8",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "ca17765f1a216fbe8d1d94ae58e680af",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1pQtlFtLZ9W0b4lk9y16VK3SlpsMmFr15hpCXuzF2vnv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7ff86df649ebac05d4767905850d9e3b",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "19oBF27ATmgrsg7oSBcRPD56qIAAwH1RKRTubDWfrtc1",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1g4OxpQexqus0etX0C9oQROrg2Eg1rqrTgXySj0Lx5KX",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "2357f71e1abef6006022b27a96dc0169",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1p2dZvJQ9SXjPNfFX56rwf6z5nGWQ9uggbc34vspbD6A",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1sJ8hR8d00vQQ8qCLhfsaKSY6Fo2wuR16gUKoBSVtpma",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
