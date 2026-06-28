"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "12kMlBSNxIx7nbzztJIAkVBe937WsZ6n95FMmt7DZFzF",
    "1T6mWW4EXgDIGkJAVydn4JOgDHoYU6rsMc1ywGTWvhhA",
    "1wtZapoIlpF6KhZ8CKUxSqiyfZC1YCEJjWIPD1nb3HXN"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "c7e95254879cb041495a65e252675b3f",
    "56af478d37449ad9e6d8be9d9c80194c",
    "c7e640fa9badacc012db9a94c39928b9"
]

LEGIT_PERM_IDS = [
    "d5f2102f5851a6508a47cb4a77fcfc2a"
]

NEEDLES = [
    {
        "id": "12kMlBSNxIx7nbzztJIAkVBe937WsZ6n95FMmt7DZFzF",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "c7e95254879cb041495a65e252675b3f",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1T6mWW4EXgDIGkJAVydn4JOgDHoYU6rsMc1ywGTWvhhA",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "56af478d37449ad9e6d8be9d9c80194c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1wtZapoIlpF6KhZ8CKUxSqiyfZC1YCEJjWIPD1nb3HXN",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c7e640fa9badacc012db9a94c39928b9",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1fRaLg6A0NsQZ3cOjVeYGyNKCDTZzM7Ww1cPZdZf8Nid",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "d5f2102f5851a6508a47cb4a77fcfc2a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ysqfC431XEhFYEmeiMLwdzA6qKMnYvA2Cl3a0WO3X0B",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1rV8f0AiTvNP98zQyoV6SoyaLMYucknUdTjcshb5Qdyl",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1WTv1TNMJQylZECgLvc1RuUA0mgIDdiLbLTk8gfpxtCi",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1Pv1BY8ZUZzBSLbtdYREodLMMduWAhkCxjbj74jVRT3A",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
