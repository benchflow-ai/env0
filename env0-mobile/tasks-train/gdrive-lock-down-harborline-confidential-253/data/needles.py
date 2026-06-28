"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1XHuSwHqlAkGxZ97qHRElqVFQZkp0zcd3gJ0jEZO5y3W",
    "1CdLZMMXtJqtD7HkHBDiS6fw1YhO80l4OM3bkRNaPbHp",
    "1e8GQq148msoGorXUBKjqgDRYBKLnBLAww8IQ71nDxj2",
    "1TVckb2CmETSjv7f9E5BJ7TzX125nwXYkwv3MDoSoiyq"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "e15b7bc3dc47e43427da40ff8e4453c4",
    "cb8125079e5528d4080f60c110961426",
    "89031a8e6ff7a9d561ee399b85460392",
    "26fa4f65bf3204ed9cf034e1ec16e03e"
]

LEGIT_PERM_IDS = [
    "e509d8faece3351c0a21dc5fbf132229",
    "865e4af5febcd025eb65b594ccdc4ad7"
]

NEEDLES = [
    {
        "id": "1XHuSwHqlAkGxZ97qHRElqVFQZkp0zcd3gJ0jEZO5y3W",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "e15b7bc3dc47e43427da40ff8e4453c4",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1CdLZMMXtJqtD7HkHBDiS6fw1YhO80l4OM3bkRNaPbHp",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "cb8125079e5528d4080f60c110961426",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1e8GQq148msoGorXUBKjqgDRYBKLnBLAww8IQ71nDxj2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "89031a8e6ff7a9d561ee399b85460392",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1TVckb2CmETSjv7f9E5BJ7TzX125nwXYkwv3MDoSoiyq",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "26fa4f65bf3204ed9cf034e1ec16e03e",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1XFcc3zLJaMyrnnRomHSP03Ge5YhgAOjHm8MTTakey8A",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1YCBdZWm5TUqktnK60tchsw7kUBxS3XVAWIqYZ1LNiik",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e509d8faece3351c0a21dc5fbf132229",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1px0JR7y4vwGBSy5u7RVGuyxSyZATsrBF4xF4tAbV0Nf",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "865e4af5febcd025eb65b594ccdc4ad7",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1f0AK2yIE88ajTO9O3miVj0RlNe9T8avS5XBRN4ZQUKJ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
