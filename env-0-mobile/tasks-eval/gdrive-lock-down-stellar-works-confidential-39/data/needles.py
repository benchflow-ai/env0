"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1Mu1bgLIq2r5Dwp4RiwkN8n6G31VA4jcKfqaTzsMQgoj",
    "1UkbGcvGGofePXGvKpSOCDt8sxKrTprmmbw1FHn5aVo1",
    "1IIyvIWwld3rvGaDTQYdrFRerXQZ2UzjYFIpx1pRUk2l"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "0a495b1914a0e08333f7efac1567a04f",
    "b61eaaabba10ac7a77ca62e16d9461fc",
    "86a9cbfbb36d7d24651da32a000ca27b"
]

LEGIT_PERM_IDS = [
    "1d4b57630f8b15cd7115ecb758a368b6",
    "0d3602b887ac6ba24cb4e565819f7bbf",
    "f16ad7dc78aed918e19bc5ea41449a73"
]

NEEDLES = [
    {
        "id": "1Mu1bgLIq2r5Dwp4RiwkN8n6G31VA4jcKfqaTzsMQgoj",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0a495b1914a0e08333f7efac1567a04f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1UkbGcvGGofePXGvKpSOCDt8sxKrTprmmbw1FHn5aVo1",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "b61eaaabba10ac7a77ca62e16d9461fc",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1IIyvIWwld3rvGaDTQYdrFRerXQZ2UzjYFIpx1pRUk2l",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "86a9cbfbb36d7d24651da32a000ca27b",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1q6qQYk7FL6UJKpcHcwvKangZCqTQTE2MJDPlVBrRYom",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "1d4b57630f8b15cd7115ecb758a368b6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1kPiEIaxOTsHUV3ATQZV8xbP5eiNLfM6xMenuZWlGCke",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0d3602b887ac6ba24cb4e565819f7bbf",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1dRHDSadCf4DuDYhLLB1UiDJNN1se9aG5GeFw5vG4A25",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f16ad7dc78aed918e19bc5ea41449a73",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1wB4qHmZwrmtUvCXLV4wUkHXVvBTgmDrqINXSgPktKbs",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
