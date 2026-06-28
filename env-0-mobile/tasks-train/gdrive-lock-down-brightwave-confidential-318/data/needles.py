"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1YtaT8OLsGqDYFMxeMODOcXvtRQpGhZDhinGAlqFdO0i",
    "1TEezNA9tzyyHweICQs1gSebg560fRcnanv4wTwhVHz1",
    "1vJl1dvsAzrw7Q2cDTVu0sYSeGtpjp0T9uf0GXBUsUF4"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "513d364560e44a56508438e8236d1515",
    "a537839f1280a4c9bf957d731ff952d2",
    "13813869ea25a60bd43cb94bbd7db920"
]

LEGIT_PERM_IDS = [
    "9a686c45cc438a3e93cc6660a81a2df6",
    "6b6c0d0cc6bb6b8636fbb77234910bdd",
    "f2d4737411ad01e97a86ff02cb9fc2dd"
]

NEEDLES = [
    {
        "id": "1YtaT8OLsGqDYFMxeMODOcXvtRQpGhZDhinGAlqFdO0i",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "513d364560e44a56508438e8236d1515",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1TEezNA9tzyyHweICQs1gSebg560fRcnanv4wTwhVHz1",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "a537839f1280a4c9bf957d731ff952d2",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1vJl1dvsAzrw7Q2cDTVu0sYSeGtpjp0T9uf0GXBUsUF4",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "13813869ea25a60bd43cb94bbd7db920",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "13AzyEi2smRhVHJ4jRh8zRECfm527pTGXXI7K6iFbmzh",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1L2CyMPom1NNbTCwPjVDAlnpJozFKC6rndMXrhscUjde",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "9a686c45cc438a3e93cc6660a81a2df6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "178G61y3HfCIjd6XZ3rKXsVo2U0ZbnQ2BILFfuUnsqHT",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1k4JdtIi3zmc02mltVqAvGmvExUZg00yPXAXY0rzKJjl",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "6b6c0d0cc6bb6b8636fbb77234910bdd",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1xksQGrcIbXx0sIRFmJzpkZ4slU9ZZK208gEUVRrxr8z",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f2d4737411ad01e97a86ff02cb9fc2dd",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1cnHxAmlA9YK1zeiK39YrIZ4yqKGkbnbxxhv7Q3Qbwi1",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
