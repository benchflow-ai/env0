"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "17066b5jSzDOtASRM4N909YcLOpb96SZ4vdoLaZYWJkX",
    "1oECl8jAnzdT5O07N1KE2fNFtBPzq3F5zOFt8Orp0doH",
    "1QTtDzsfWc2zxm6vhYKwKeGdAKoWojdi7wA2sHVwPobz",
    "174fphwPu3xwCmOXKkVokXT7XZz6BCg4YBcuPdUi0GNc"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "d8f78b81df6ba5af51606a120e622df6",
    "50c07afdd1564486ca189e0fc50a274a",
    "5809d381c94447b23f30ac4d8cd2f743",
    "6cacc6b96716ff4ddfe4cc0a477eb8e1"
]

LEGIT_PERM_IDS = [
    "d415e0e19edfde515a8d68b97dcd5854",
    "af168296b157f2a461a1197c21e253a1"
]

NEEDLES = [
    {
        "id": "17066b5jSzDOtASRM4N909YcLOpb96SZ4vdoLaZYWJkX",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "d8f78b81df6ba5af51606a120e622df6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1oECl8jAnzdT5O07N1KE2fNFtBPzq3F5zOFt8Orp0doH",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "50c07afdd1564486ca189e0fc50a274a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QTtDzsfWc2zxm6vhYKwKeGdAKoWojdi7wA2sHVwPobz",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "5809d381c94447b23f30ac4d8cd2f743",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "174fphwPu3xwCmOXKkVokXT7XZz6BCg4YBcuPdUi0GNc",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "6cacc6b96716ff4ddfe4cc0a477eb8e1",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1JpTxxe7EkDgLJaFgFLbI4LgmyOXsVz4WDqy661gu1PK",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "d415e0e19edfde515a8d68b97dcd5854",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "116vTQUJwg2zVH84suCv11OPof54phcqWrRF5kIQngs2",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "af168296b157f2a461a1197c21e253a1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1szkdbrLdU4FTjNUSRfALXkxubpv5eQWVTWNXOseKMZr",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1Mb7DTu2b2vXKhy8XP3ZVePakVER25yRj8oAtgmwvh0y",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
