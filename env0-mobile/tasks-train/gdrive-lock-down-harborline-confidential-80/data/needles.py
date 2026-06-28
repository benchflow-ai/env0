"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "17kHlstQuwmxvCITtgscl0gMYCRQwKAutSIgODAXsKZF",
    "1SxczTcwMJw7QIetR5hFbjtKj5w3U5F0YxgwljUh1SwC",
    "1OK8YBXCIYfar207j7JVLIgHwpKC8OVgPH8HSnDMZybu"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "441ea474c116c19608495bfb0dad7db7",
    "c101efb183afe686359180cb92379f9c",
    "97ee12a7b3b5ba409b9f1d9281d6292f"
]

LEGIT_PERM_IDS = [
    "def4be7d4b7609e5ea7a6cd57d202448"
]

NEEDLES = [
    {
        "id": "17kHlstQuwmxvCITtgscl0gMYCRQwKAutSIgODAXsKZF",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "441ea474c116c19608495bfb0dad7db7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1SxczTcwMJw7QIetR5hFbjtKj5w3U5F0YxgwljUh1SwC",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "c101efb183afe686359180cb92379f9c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1OK8YBXCIYfar207j7JVLIgHwpKC8OVgPH8HSnDMZybu",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "97ee12a7b3b5ba409b9f1d9281d6292f",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1zeTS49Z1mKhOexxeAETYoxQ3nsafMXWqyb1XzE7XDBZ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1o6aKZHj6ngUnuUSNkZCzyAAv5HVRC9Uvpiyy42zECuw",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1bOQ8Wd1c7sC2p51nwvQ9oKkLcHoX9jRd7J0L6Os4Ofn",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1s2grjdzKIadMBNiJDU6AUfQHJMyNFeD3CnBtK546m3b",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "def4be7d4b7609e5ea7a6cd57d202448",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "11pYEJYoFjKS5FYLpf9M7HcRJr9aJQb5yQpBm8n4nA3C",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
