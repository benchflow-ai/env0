"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1UPPLJNRCTa41EDXfeHnSrItaGpKOZvLiHNnyGfBPtI3",
    "1wvx5N34yzC7frbrzGxUJNnQ365JwxdXmUdi1mvGQZEz",
    "1PtVzA4q3fIbBh9Mbrp2e1AW6QnNbZygemYzfflc1NIl"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "75ab61dfbd069f2b5fc654b56a31050a",
    "d92c932614f0cfe08de17da6e181209a",
    "83b74d9a57e886bbb3aadc6c91248096"
]

LEGIT_PERM_IDS = [
    "ba0ffddda4061d0560d823f75e7c05d8",
    "668d57251d2920ee2a12873da5db32ec"
]

NEEDLES = [
    {
        "id": "1UPPLJNRCTa41EDXfeHnSrItaGpKOZvLiHNnyGfBPtI3",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "75ab61dfbd069f2b5fc654b56a31050a",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1wvx5N34yzC7frbrzGxUJNnQ365JwxdXmUdi1mvGQZEz",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "d92c932614f0cfe08de17da6e181209a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1PtVzA4q3fIbBh9Mbrp2e1AW6QnNbZygemYzfflc1NIl",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "83b74d9a57e886bbb3aadc6c91248096",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "10jgNzYnesxcMHI7qM6QhGsZkDR4hSSGefkxvIrQ6BsD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ba0ffddda4061d0560d823f75e7c05d8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1cG46ANbeBdHxLZEA6WiFRLNrvaKX8zxYanjjtpSWSFj",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1pbtZbcnPrCkikrOyoj1kdHoyTpDTSPKkVPfvq0zHUvP",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "668d57251d2920ee2a12873da5db32ec",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1C5vgPk0a8Pv93VtIRdEFAMLbqrI0pxSllOhZfwrfci2",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1YKdtOomSygddlPGm72cpye9dbPbbdvJNNSH1ccS2S2E",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1YJ0vUW9S5j8TA5Jbdqn1vRZwRUgtPxKCbHc9AtNhX9W",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
