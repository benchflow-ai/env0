"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1iG2ysxaN5cIwSK6iE741Vz28l8COu6JKRWpSC0nsIxX",
    "1ri76srnncMaqCb9YeW11w8gYpDm2qe4dc5Uhkj1PXRv",
    "1xhYV1eRcnKfYESxqyVzUsfmHrAvT6HIUFHFsNUMRJzd"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "6d4bac9bb2132602855b0c395f188a53",
    "956ea8ce01f285408c6c0b498ad62a88",
    "55e315e3edd390e226a610b5fb2c219a"
]

LEGIT_PERM_IDS = [
    "9561e0caa06e8b0a7aae0ad63e01d73c",
    "417e04abaa25bceba3da3474dfe24764"
]

NEEDLES = [
    {
        "id": "1iG2ysxaN5cIwSK6iE741Vz28l8COu6JKRWpSC0nsIxX",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "6d4bac9bb2132602855b0c395f188a53",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ri76srnncMaqCb9YeW11w8gYpDm2qe4dc5Uhkj1PXRv",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "956ea8ce01f285408c6c0b498ad62a88",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1xhYV1eRcnKfYESxqyVzUsfmHrAvT6HIUFHFsNUMRJzd",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "55e315e3edd390e226a610b5fb2c219a",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1q5gPtbe6JUo6fOXpXbP6G8jTaJ20k2d29h89JtI88gW",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "9561e0caa06e8b0a7aae0ad63e01d73c",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1auTrKEiXwdRmHsuXyR9KQSQjrl0lUQDr0IpwFa3qc00",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1kc3PrUbcE7Wituxi24WecrR9CrOCW7MtVEreF5TwUgH",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "417e04abaa25bceba3da3474dfe24764",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1iqbPgjNlj0DjYw5NAERcUNrl1YF2F8kxiNqFySyfLjl",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
