"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1b7wXNUcEUumvQWwPpTqLZWK2w0nAh4dWONqnfBOFbpB",
    "13FeRt7MOyXmKMPTCsOUG9e6ffWp6g531fy6m71VpvAr",
    "1bz6nbrCQ4mPIXWFI2r7Tb9oFwdEPixzSZZ8Eb1Vr12l"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "7b3d00d86415d2086a08ba26f739267e",
    "a27c74bf77b89db1c7255281ae7b4bc3",
    "c03816af37525f357012e23fe9affd02"
]

LEGIT_PERM_IDS = [
    "742b96ff19ec833fb36fa41d70039aee",
    "8c09579b765451b6865d5502a9751ba0"
]

NEEDLES = [
    {
        "id": "1b7wXNUcEUumvQWwPpTqLZWK2w0nAh4dWONqnfBOFbpB",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "7b3d00d86415d2086a08ba26f739267e",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "13FeRt7MOyXmKMPTCsOUG9e6ffWp6g531fy6m71VpvAr",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a27c74bf77b89db1c7255281ae7b4bc3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bz6nbrCQ4mPIXWFI2r7Tb9oFwdEPixzSZZ8Eb1Vr12l",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c03816af37525f357012e23fe9affd02",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "19Agz2dvcoK438QVL0fqCMCMs7WGH9D4Q2ZqIeAiam3U",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "742b96ff19ec833fb36fa41d70039aee",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1O4FaguZJuKxfbrX2iU6brOsW8A2x8EQA7zJrUXHxzP1",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1NELu0QDi0Hm6YXE2JrfqKHXXkkef2NmtNLMpgWWJWxq",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1Wg0JT36Sf382fOyacIibOyRY0yfFspTDyU5aKY94Jgx",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "8c09579b765451b6865d5502a9751ba0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
