"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1nYdVSvDJnzuJNuy0XI50tCuBlAGopTRsqo8yZDrhNIf",
    "1tsRERw3DGOP1MHpv71j0ONwsgeTFyN1ueWWkLx0KIe7",
    "1e8GZ0uwHzPwssQ8D9QEzRvGklpP208H79oLh3z0qgkJ",
    "1iQHjMKcq2Z18yajAeE0xVuLWIRYd8pwJaIuLBnfYMeh"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "6cde85eb2ef012d22539b19d4c53cab3",
    "b7212d6612ba70ed069cc587245fb88b",
    "8b99998aedf2ff171122965f9c5ade60",
    "49015ef3d1d9710ec60cc5d059f7d832"
]

LEGIT_PERM_IDS = [
    "f2e0c4acfda43940188fe8b9e7568495",
    "34e5d136e4b01749a14a6f3f03c65d26"
]

NEEDLES = [
    {
        "id": "1nYdVSvDJnzuJNuy0XI50tCuBlAGopTRsqo8yZDrhNIf",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "6cde85eb2ef012d22539b19d4c53cab3",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1tsRERw3DGOP1MHpv71j0ONwsgeTFyN1ueWWkLx0KIe7",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "b7212d6612ba70ed069cc587245fb88b",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1e8GZ0uwHzPwssQ8D9QEzRvGklpP208H79oLh3z0qgkJ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "8b99998aedf2ff171122965f9c5ade60",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1iQHjMKcq2Z18yajAeE0xVuLWIRYd8pwJaIuLBnfYMeh",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "49015ef3d1d9710ec60cc5d059f7d832",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YwDJOMm6I1W98bhQAUu930D1WPTSRoMybHmk6Z2hUxD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f2e0c4acfda43940188fe8b9e7568495",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1phaBKxmcmFhFyWddKHRe3mzhOaGBk02zRYUnUo87hBw",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1lnvDd7hFthxdL0Ybols2oryLHOru7GHxJbAwGxVXACb",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "34e5d136e4b01749a14a6f3f03c65d26",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Hi8gqdzQ3kZJbYNwmWAeSWQ3afht7oJCrtoaoHGrCz8",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1nxbmmQGC8vciaTHcBOp39FpUdpaw2zT7eYxzNZq1SKg",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
