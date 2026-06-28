"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1GWcfG2BAdnk5N4gg1gp2UUc5dUggyckhHrDpMiI6M5b",
    "1czjnaWU6p7dffeyeKPcoZcaeTGJJCqI4R0GeQyk9UxE",
    "11MOPEbEfaSiiBrQ3dKxvG3MZnOEuursMYhEw1GirtiW"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "9c62adb3de3e096c3df50c86f214956a",
    "5a80cdab40998ab8e06daef54a3ea3af",
    "49a5b6587503a6fe784523e93c01e4bb"
]

LEGIT_PERM_IDS = [
    "535702a8306031f048bde59a4061da12",
    "b4af90b6e190ac4e33775a956c50ef10"
]

NEEDLES = [
    {
        "id": "1GWcfG2BAdnk5N4gg1gp2UUc5dUggyckhHrDpMiI6M5b",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "9c62adb3de3e096c3df50c86f214956a",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1czjnaWU6p7dffeyeKPcoZcaeTGJJCqI4R0GeQyk9UxE",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "5a80cdab40998ab8e06daef54a3ea3af",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "11MOPEbEfaSiiBrQ3dKxvG3MZnOEuursMYhEw1GirtiW",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "49a5b6587503a6fe784523e93c01e4bb",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1BYMnsuWRepwQBwVnsXXtEbi8uwy0GJDzkZgTZlHk8Hg",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1ESobqU3bH2iAy2TPT7gyctldGB0oRjhu45cYoVqhPnF",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "535702a8306031f048bde59a4061da12",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1eWBluLMDCk8yTG26afWTcovdYAPzKBSFYrc9mGIKWB1",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b4af90b6e190ac4e33775a956c50ef10",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1CKsHca7vXFX07Mjysy6PAEWJ6MHtO87awVbYuCHHRRw",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
