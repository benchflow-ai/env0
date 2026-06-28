"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1MtAj2samwObT76n3jGs2CzDUGbqO7Xk6wZlcanwkbUZ",
    "1HCuQUS3qutiI8n7cNqewA5RlFvWyiz8ZjtkIF6Y7bTO",
    "11EdDL0ZAITvfoOqX9a1krsKJzvhkAVBfknznPcmTNxx",
    "116l8Qsvn16PrgqpL8EPycODAyPDolqE6LRanyonG7TH"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "6398f2ac374f8e481eeb2c8a2c8474f7",
    "9ace11916cfad2ccd639415bae86a80a",
    "380da27732853c7d33ef7bb2fde1a8cd",
    "edade9138543df5cd28f87744ec57aac"
]

LEGIT_PERM_IDS = [
    "27e99050ddde21c577be39bada97c22a",
    "2d6ec40a267d413c864b27db46d7df3e"
]

NEEDLES = [
    {
        "id": "1MtAj2samwObT76n3jGs2CzDUGbqO7Xk6wZlcanwkbUZ",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "6398f2ac374f8e481eeb2c8a2c8474f7",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1HCuQUS3qutiI8n7cNqewA5RlFvWyiz8ZjtkIF6Y7bTO",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "9ace11916cfad2ccd639415bae86a80a",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "11EdDL0ZAITvfoOqX9a1krsKJzvhkAVBfknznPcmTNxx",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "380da27732853c7d33ef7bb2fde1a8cd",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "116l8Qsvn16PrgqpL8EPycODAyPDolqE6LRanyonG7TH",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "edade9138543df5cd28f87744ec57aac",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1oG9OiR9lCGQg5tx27NTB8qZqLREignpBXd9mn4lqqi9",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1wLtLnDGgfSLExuwuNg4TaPOn7XvBhzs5xbh9THS5PqL",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "27e99050ddde21c577be39bada97c22a",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1rMN2RAw02j1uRwOIjE1wjkzSFLg0UH86aQ9Y3qZ5y6B",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "2d6ec40a267d413c864b27db46d7df3e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1KEn1JzXmEQ2um7LxIWYlJ8PeuKf4RbBviGPXZLg4GDS",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
