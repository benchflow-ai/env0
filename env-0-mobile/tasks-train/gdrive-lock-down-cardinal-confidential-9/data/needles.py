"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1qxcZI7ifo8DWgScDxNZUs9qzEFjuh77gPF8dTB5Kjt1",
    "1UmNM1e2pznUak7ptSy4cNBb3rpTX2ZmHIQGsVRoSgKD",
    "1n0ZHEFcmcmx62KGBUmPiahzb0x4gWCzxXWYh4lRoupd"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "f16eb5cf80c7e746cb1a39bc07090849",
    "e20e60a6cef718c55cbceefd477b5da7",
    "61412b1ba9fe2c708a63caaf95f52e99"
]

LEGIT_PERM_IDS = [
    "a135ad0c2c889f3337a2dd6e1a6da214",
    "85cb50e558b509536ea803fdd5107719"
]

NEEDLES = [
    {
        "id": "1qxcZI7ifo8DWgScDxNZUs9qzEFjuh77gPF8dTB5Kjt1",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "f16eb5cf80c7e746cb1a39bc07090849",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1UmNM1e2pznUak7ptSy4cNBb3rpTX2ZmHIQGsVRoSgKD",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "e20e60a6cef718c55cbceefd477b5da7",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1n0ZHEFcmcmx62KGBUmPiahzb0x4gWCzxXWYh4lRoupd",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "61412b1ba9fe2c708a63caaf95f52e99",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1BW1pCfAoQwidb7eFSgL2Tahwlu9w3lLQEuMSq29wXgq",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1zEnl2mRqFVDSOn18OsdfukfFK8T7LxD0yLqHUCLeKNK",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1aMZhj2N2Ei0tFAUWPoB0lcLwKgKHRWd1jgEik4S3Pro",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a135ad0c2c889f3337a2dd6e1a6da214",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LWGhA5IisczJrJ4cQx71pZOLPMR3GTSgSCDeSvbTG1Z",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1jyWux7ngqjLmX9IF99pso1gW3YU5kA8jsBmOh5WCApn",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "85cb50e558b509536ea803fdd5107719",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
