"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1KX6DSOvSrlInUQgNzY3Wig2YtThybZ0LxpbdpxThqjr",
    "1X603VKcZDSyOPl6t3ZU9UsOCprEaVF3jiOeSqNpKfQL",
    "17yvjqh9WDqrMgQRDpBZGZXMLs9MR3MQORYNEqeNkFTi"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "2e1842db410c42c42b6a84d23c0e6207",
    "63aef7d4448f1703f25bad75c18090a0",
    "332d58389d26969cb306fdfd2adfaa2f"
]

LEGIT_PERM_IDS = [
    "47cd5f52acbf90043d24f21595ffad23",
    "1bae9e311b1e49a4c2260650253845ae"
]

NEEDLES = [
    {
        "id": "1KX6DSOvSrlInUQgNzY3Wig2YtThybZ0LxpbdpxThqjr",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "2e1842db410c42c42b6a84d23c0e6207",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1X603VKcZDSyOPl6t3ZU9UsOCprEaVF3jiOeSqNpKfQL",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "63aef7d4448f1703f25bad75c18090a0",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "17yvjqh9WDqrMgQRDpBZGZXMLs9MR3MQORYNEqeNkFTi",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "332d58389d26969cb306fdfd2adfaa2f",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1gXAnLFCqlIboJR7InraKO34dOPWNTL7DbuCHZKe6Yj0",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1vViCOZwaLY3A2Tj6UasynLoBKIefEcpnJNigcLJWUMZ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "47cd5f52acbf90043d24f21595ffad23",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1G2PbEFH0jqAKmbHyyzjS1sw37yZQbcQ7XaQC7MMaFkr",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1jwBYhYNoBJvVwhasGKwpu6YrxTNEAxjuIs2obzpnoYE",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "1bae9e311b1e49a4c2260650253845ae",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1aHyYNXtI83W6GEu2LkhiivmeL3Aw0DXxAutU71wEyRs",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
