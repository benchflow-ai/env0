"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1mdpxMeWViWXQZ1YEGHHfii2UJqVPljdZGZGxz7Qkdek",
    "11B5lxXKcof34LDZiSFoCZlwt3XlgAa4JthXWTqZd3H3",
    "1iDGfFiAZSnPsvVVyYv7BepwI0sAb9RiaXaj4UvZQwdG",
    "1AuHTn8JvzF12oJ2OdrnEyp4j3vP9pTrQku13ZM02LsX"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "a6f9104fa31b422114f2d7a5acb6fa3d",
    "d39e11c623fccd0ab9f9278625e54886",
    "d69e34e6f7561d4ffb1ab55524f55392",
    "73f5034e8a55c3311163fe502c7f5d57"
]

LEGIT_PERM_IDS = [
    "df95b8734e799e8ebc9f922200305064",
    "4e2b48a3f4299e8c7e77d8b3a73ccf23"
]

NEEDLES = [
    {
        "id": "1mdpxMeWViWXQZ1YEGHHfii2UJqVPljdZGZGxz7Qkdek",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a6f9104fa31b422114f2d7a5acb6fa3d",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "11B5lxXKcof34LDZiSFoCZlwt3XlgAa4JthXWTqZd3H3",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "d39e11c623fccd0ab9f9278625e54886",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1iDGfFiAZSnPsvVVyYv7BepwI0sAb9RiaXaj4UvZQwdG",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "d69e34e6f7561d4ffb1ab55524f55392",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1AuHTn8JvzF12oJ2OdrnEyp4j3vP9pTrQku13ZM02LsX",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "73f5034e8a55c3311163fe502c7f5d57",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1o9YWBrqOiVrHhS7AAXgAecp6yKx26e8mm7Wv6MqTmsX",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1603bDI0p0q5QOVmD6dgJOwF3L7DQ0kXjM0tFp9P0gdI",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1TXD7HK9LFL303wIJIUresTYznEJk3JUX1Yrj5IVir2p",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "df95b8734e799e8ebc9f922200305064",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "16oq8eQYzkQDHrm74wTgWydMS7NrPQevwzMLyHum9Cc3",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4e2b48a3f4299e8c7e77d8b3a73ccf23",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
