"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1H4Vb48QL6dpsQUmnqfi1QKtWndH7kqmcI8hPad2mhAF",
    "17QkVkPv8d2vkLbSdgCkkNMF4xU171BdhyqaDnKtdx33",
    "1CPqoNVvhlhNi74YS3qY9v8tU3dK5PQCfXFj3MBA4eKz"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "b25face1c5dc1e3f5e81e0902496f28d",
    "521e7c3c9563e5f11af720906696ca20",
    "909bfe57a95971774d02222e4b8661d1"
]

LEGIT_PERM_IDS = [
    "0853e5810a708703105563f27bff3af9"
]

NEEDLES = [
    {
        "id": "1H4Vb48QL6dpsQUmnqfi1QKtWndH7kqmcI8hPad2mhAF",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b25face1c5dc1e3f5e81e0902496f28d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "17QkVkPv8d2vkLbSdgCkkNMF4xU171BdhyqaDnKtdx33",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "521e7c3c9563e5f11af720906696ca20",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1CPqoNVvhlhNi74YS3qY9v8tU3dK5PQCfXFj3MBA4eKz",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "909bfe57a95971774d02222e4b8661d1",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1PiaVvYB619HWuf0XfEMLhL8W7rwv01SIJ7zdU65iB5p",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "18JJKRQHdZ61UJDYawJVlTHwbhnDDf1eiu6NZCnkbrN6",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0853e5810a708703105563f27bff3af9",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "19sm1VbpvaqOdAPcyZIwnGWDrEsSj3RMD3PwvunRzovp",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1XiJFBDZ5TCqn6jqcU22RirKOgiyvaObLbh9FbIVrcTD",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1TsgqjGpnBuW7W4YAoxFYtGnL1gIcdTzhi3WWBUM223V",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
