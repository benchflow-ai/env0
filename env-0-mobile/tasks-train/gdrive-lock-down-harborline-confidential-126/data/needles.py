"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1gmc6jAvpz2l2Yx6w9VBS6xVbRocVgSWm8ablojwXHq3",
    "1U0rSLmRRwhXCpjTjVMKTzmHyzNZkD5s15tqZTFnMkCd",
    "1pCasElOJW0d7WPMZdxFHHgYWtqNPVO7kQHiqMvhL6p1",
    "12jgBomLBd68IgKoDoyhBJOQ5z5hpsLWIvTTDVxCX6WR",
    "1YResfvwQfDSAexmwCvfCtXzCEbREmisYyAP8lWWwsLV"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "378e8a416da5d1a1fd71452775f2cb84",
    "1bfb8725495c411456e7415af6ef40c3",
    "61036ec97f4e9bbbbda8144bae7e2458",
    "de31ee59b98c08e0f411029ef70750a2",
    "5820d741915b91de67dd4cafcc1ca4fc"
]

LEGIT_PERM_IDS = [
    "782e051f35e1ca0b9e0d274bdc061756"
]

NEEDLES = [
    {
        "id": "1gmc6jAvpz2l2Yx6w9VBS6xVbRocVgSWm8ablojwXHq3",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "378e8a416da5d1a1fd71452775f2cb84",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1U0rSLmRRwhXCpjTjVMKTzmHyzNZkD5s15tqZTFnMkCd",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1bfb8725495c411456e7415af6ef40c3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1pCasElOJW0d7WPMZdxFHHgYWtqNPVO7kQHiqMvhL6p1",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "61036ec97f4e9bbbbda8144bae7e2458",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12jgBomLBd68IgKoDoyhBJOQ5z5hpsLWIvTTDVxCX6WR",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "de31ee59b98c08e0f411029ef70750a2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1YResfvwQfDSAexmwCvfCtXzCEbREmisYyAP8lWWwsLV",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "5820d741915b91de67dd4cafcc1ca4fc",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1NiZewru60gQjRtJHgWH1Gony711VwT4m5NMpRnG18oE",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1z2rLDCMyu3oLb6lK4Bxw4KbBljy3tgGuAEMVHgWyvJD",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1OBMcidlpL9elBFHnk69qZYFrKJs928YNwJPNMwTEEot",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "782e051f35e1ca0b9e0d274bdc061756",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1JgzhKqckpxbKd5P8Q2AWQ5A4t1sbUatp9x1fLBPNa1D",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1ERLkCqsrp0GLINzMx9rzwgilcjtsc0Cenvowq48JYBQ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
