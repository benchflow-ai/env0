"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1QvHKybBR54G2SuCKWIXu0Blp8sA77vwUdkj6bokJRNT",
    "1Pi7QmUikntiJL3DMaDPqEhvIx6uaGVYSPTmih9UdyOE",
    "1KaxZaKd0ifl0ivNsn7aETCKmXKyT0NTOD6FEQEWLMY8",
    "1lOg0lFdPhYLJXbfY4LU9DAf8xODgkCDELI5Qld5n3VS",
    "1ogfSLtBkx3YP4VFbg4AcHgm1zh2riIk1jbQqYq6FDsd"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "0de5012bc046704c81205df3af5a7d1c",
    "b20e9a6d31d7ce58c8df04ea9a858b39",
    "d0052e0b8e9d29203accb510f9cea168",
    "744ee5cfdcf531a6b25516d10c57b1a1",
    "a04f456c487d5d014327c1bb03f23eec"
]

LEGIT_PERM_IDS = [
    "039c48d7fc662fd9e8beef61d6dfb84c",
    "4f55fc994a8b48b22d540d773adef9de",
    "5d8f7705f8990dff71c8db41e36b0e6d"
]

NEEDLES = [
    {
        "id": "1QvHKybBR54G2SuCKWIXu0Blp8sA77vwUdkj6bokJRNT",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0de5012bc046704c81205df3af5a7d1c",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1Pi7QmUikntiJL3DMaDPqEhvIx6uaGVYSPTmih9UdyOE",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "b20e9a6d31d7ce58c8df04ea9a858b39",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1KaxZaKd0ifl0ivNsn7aETCKmXKyT0NTOD6FEQEWLMY8",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "d0052e0b8e9d29203accb510f9cea168",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1lOg0lFdPhYLJXbfY4LU9DAf8xODgkCDELI5Qld5n3VS",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "744ee5cfdcf531a6b25516d10c57b1a1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ogfSLtBkx3YP4VFbg4AcHgm1zh2riIk1jbQqYq6FDsd",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "a04f456c487d5d014327c1bb03f23eec",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1alPOivzkin5GWfyzu7IeWl4eG0xmGLCEPxKrU9M7en3",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "039c48d7fc662fd9e8beef61d6dfb84c",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1miyM5kxdI8WudguXZGIfbFSmbA5lh8NakGB5gwRtslF",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "4f55fc994a8b48b22d540d773adef9de",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1VaQu6WKLciBMIhsu6Kt2uA428B1H2CPuIRlRK6KXvVA",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1KBHtJbrjvMAsvXUBkF8UgAznrFE4aGB99TwdMGIUcyw",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "5d8f7705f8990dff71c8db41e36b0e6d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1c6QiDlPfaqq1swaErLDwIzHrDk6yIzb4UC4w0mYaxkF",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
