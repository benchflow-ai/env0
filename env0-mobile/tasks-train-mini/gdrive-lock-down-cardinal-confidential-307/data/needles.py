"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1kE5uQB6orZ4zWLW9OlG4kWAe4QhIeu7HBz2pmOvXFZ8",
    "1OTVyi4ZPXXMAw7ZLsC9xxpmEQylLOIoZ9wQ9GYIV1d8",
    "1T88454vGqZ4wEp8tv5hmh3cIOpkUiK24QWSsWckIxHp",
    "1mYEJjZ2moXR0HfZvNxYsiS336JZNVgPy0HSVSeya9Co",
    "1LtO4rHNyYb0LvzNRtOw1USqfEoSezvkalLgHQqB67Xv"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "c32000783b9dda7c2d31f27d803f4cee",
    "de71c48dcc857aa8bca94d0c536493cd",
    "662053b41ff8747f948eb9972e31f437",
    "e4445f6a3694c737cba9849030b02fd8",
    "fe0e4e01fe209ffe7ecaa5693a5d1453"
]

LEGIT_PERM_IDS = [
    "c4612cf3514e4a038e68cafa4b27bb78",
    "7b5ad6e698087fff2aa0cb6451592956",
    "073447672f1d841cca00cae56cf80c78"
]

NEEDLES = [
    {
        "id": "1kE5uQB6orZ4zWLW9OlG4kWAe4QhIeu7HBz2pmOvXFZ8",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "c32000783b9dda7c2d31f27d803f4cee",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1OTVyi4ZPXXMAw7ZLsC9xxpmEQylLOIoZ9wQ9GYIV1d8",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "de71c48dcc857aa8bca94d0c536493cd",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1T88454vGqZ4wEp8tv5hmh3cIOpkUiK24QWSsWckIxHp",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "662053b41ff8747f948eb9972e31f437",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1mYEJjZ2moXR0HfZvNxYsiS336JZNVgPy0HSVSeya9Co",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "e4445f6a3694c737cba9849030b02fd8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LtO4rHNyYb0LvzNRtOw1USqfEoSezvkalLgHQqB67Xv",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "fe0e4e01fe209ffe7ecaa5693a5d1453",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1OWcnwWTWUNAOR8rOKsne6eb09e9sGnb5DdTRuGJKgV0",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1uYsnTP7EUifqtpUrNtTui2R1YBXB0VhrBoJLJThORnb",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c4612cf3514e4a038e68cafa4b27bb78",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "16TCpCqPDbIdkfjso8bwT7NNHoDwMuP1K9HRzxCIsR6I",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7b5ad6e698087fff2aa0cb6451592956",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "17PE4eLPJ97od8hg6ZyXvT8ziN6GzBMAuXaBcUP268EC",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "073447672f1d841cca00cae56cf80c78",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1gy5Ey6FUboEOf7rg6FFUJb69olPiCWLrgMWnRFpZ9QF",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "12YfGd6r6DERGNhlQIvlsn62FEK845FBEoMWJZRdRqtD",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
