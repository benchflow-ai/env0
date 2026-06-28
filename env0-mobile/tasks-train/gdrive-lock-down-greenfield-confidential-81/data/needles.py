"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1L3OM213goGxjyYv1GauXhDJGeId5Ik5CwFDW1vBP1BA",
    "18YS6uNBiPMLWO40fFA8hzI4wO48PlDPk8TEq7w60zaM",
    "1aBBwKuTKDHiwlhX3GVZAT0P54MlCD8f4pISUYpO0w7s"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "c719a070763a3ed6a20bdf06464f6826",
    "fc04f0525f439ffb3f1465fb24220de2",
    "0b18c6f6ca3d95b93b4c8e3daa573adc"
]

LEGIT_PERM_IDS = [
    "fc94275a4c09648ba517c41cb35ab01d",
    "3169208d2f6ba89ed102ae2167e77ea0"
]

NEEDLES = [
    {
        "id": "1L3OM213goGxjyYv1GauXhDJGeId5Ik5CwFDW1vBP1BA",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c719a070763a3ed6a20bdf06464f6826",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "18YS6uNBiPMLWO40fFA8hzI4wO48PlDPk8TEq7w60zaM",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "fc04f0525f439ffb3f1465fb24220de2",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1aBBwKuTKDHiwlhX3GVZAT0P54MlCD8f4pISUYpO0w7s",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "0b18c6f6ca3d95b93b4c8e3daa573adc",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1loIX3YyuaxuIjLSdQ6G1PfLmcgp9z1lzATq0T49Kevy",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1je9uBG1iF9ivQcIQJRV9pd0TF2DosLjBd5QIhTPtSSN",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1qEmmbTSsTWUt0tHhu8U7PTdkEBOKT6WkqCLWPUZdHzI",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fc94275a4c09648ba517c41cb35ab01d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1YsdHpaKaDwvKEPlgGzXPKVxfCRg90gwAzrwqtoDwE9A",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "11KEde3D40lMUU24tyW1Kdtsev5O01O9E6zmYlLGcV9H",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "3169208d2f6ba89ed102ae2167e77ea0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
