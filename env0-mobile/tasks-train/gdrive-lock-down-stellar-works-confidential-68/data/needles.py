"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1fScjNpOMewt3xabJnV762sSuBPbpQx6utX7F19vHoeG",
    "1IQNMkH7WDDa0fLfMJoLRp34UDdk4BkYBzDYAoShd0X2",
    "1tb7vDOhyk8BNyK6W4qBSw4FnGKuuMhD1TJJAWscqjjB",
    "1Vv3I1jSG4GCG6p1j4mj6p7zuMILv2WAZDLNlP8kUIrp",
    "1DVWK2c5WvbXQPFYeuBdiDBgHxKLpXGbxpGDRTqzprzO"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "fbebda4cd84a1d70cf03852c0bd7d76b",
    "526b9e0f9f32f0019a5c4358b673f100",
    "c729121aaf18f2c9052d184d1639319b",
    "701e4a8da1e5d21358678dff475ed218",
    "e0a98d4cc990f9e9effd173bdd2ff8e4"
]

LEGIT_PERM_IDS = [
    "85d3184aa788a2e9c0f7a317d7c21d7d",
    "ddc5d5539534d024b78b40b55db91443",
    "e09c9ed68c3ca0529c3c5cdcaed8eb3f"
]

NEEDLES = [
    {
        "id": "1fScjNpOMewt3xabJnV762sSuBPbpQx6utX7F19vHoeG",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "fbebda4cd84a1d70cf03852c0bd7d76b",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1IQNMkH7WDDa0fLfMJoLRp34UDdk4BkYBzDYAoShd0X2",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "526b9e0f9f32f0019a5c4358b673f100",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1tb7vDOhyk8BNyK6W4qBSw4FnGKuuMhD1TJJAWscqjjB",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "c729121aaf18f2c9052d184d1639319b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Vv3I1jSG4GCG6p1j4mj6p7zuMILv2WAZDLNlP8kUIrp",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "701e4a8da1e5d21358678dff475ed218",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1DVWK2c5WvbXQPFYeuBdiDBgHxKLpXGbxpGDRTqzprzO",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "e0a98d4cc990f9e9effd173bdd2ff8e4",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1yGPXFgRjpGCplVOUNpf9paSoxyj4GelZPknjZc8fv1V",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "85d3184aa788a2e9c0f7a317d7c21d7d",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1QnhCJXtDHbPShsbyunihxw4l6mr6V0gFGRJUDhcbRMD",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ddc5d5539534d024b78b40b55db91443",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1GViMUkh6V8bOpn9JvAYA9OIthRKdTf3dXUTEsp7cs5I",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1pTTyezVd6sI7UhtRDu1qRuZpXnVgdeEZorn9q3uhzMm",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1uo1IpzXV6AwwIP01zddRH1EkXgmehEreiXYhdQ0q6sv",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e09c9ed68c3ca0529c3c5cdcaed8eb3f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1SP6BPiqzL3XtgJUC081SE7xYFPIJurdpn3boDAknemW",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
