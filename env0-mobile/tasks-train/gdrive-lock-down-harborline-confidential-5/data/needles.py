"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "17eQ8K9k3DRZZlOEvOpB0Sh02UjK60vjPPp9S3iuI6CJ",
    "1VYtIIFUTY2nYCssTLWqE6xEecnPt94UJIHQrECTmmFf",
    "1lCJxs3tA7ENyQU4HhDFrbageKeYdoDWwYzk5najB3lv",
    "1f3KVRQPBpiHeqVWARmxbP2prM92z0RyiEheuzYosxw2"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "2983622b8232a59391c4166888bd836e",
    "dcb3632d70e8594d40ed08c7c64dbc8f",
    "3de42ddd25cc4a25d9d23e7cf65161d7",
    "25122b4328c2179103e60c970ffdd7a7"
]

LEGIT_PERM_IDS = [
    "ad294fca87be14da8e079fa6e64f9c45"
]

NEEDLES = [
    {
        "id": "17eQ8K9k3DRZZlOEvOpB0Sh02UjK60vjPPp9S3iuI6CJ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "2983622b8232a59391c4166888bd836e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1VYtIIFUTY2nYCssTLWqE6xEecnPt94UJIHQrECTmmFf",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "dcb3632d70e8594d40ed08c7c64dbc8f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1lCJxs3tA7ENyQU4HhDFrbageKeYdoDWwYzk5najB3lv",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "3de42ddd25cc4a25d9d23e7cf65161d7",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1f3KVRQPBpiHeqVWARmxbP2prM92z0RyiEheuzYosxw2",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "25122b4328c2179103e60c970ffdd7a7",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1AVnNmC63QFX2KKUQf6BdeAn6RpvAfFkP15ylqLexQ6q",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ad294fca87be14da8e079fa6e64f9c45",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1t5NXyeLX4xTTqJymI2WHvnfAOdcf4IcEdCPytgSfUXM",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "10JcKsFHK3wisluceYLQhTRXIxipLZ5PDuvlWTPiLF9L",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1kCgc0gVshq6wdDY4U3mXjSmUgbfFYkvAvgkJ9IgwTSy",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
