"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1lZuln68gmrfn68WUjemDcolS9sYW1Slnt1xtfKIhie6",
    "1ofQ9cy3lJZ7SOyFs6b55SrvzxiUYDespA9WtoQagMIO",
    "1j35OaEHIAWck1vSH8Heu8MXhvZsV53HsKDn0r9jDLCX"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "d0457272f0fa9d36e106bdf49b90eda3",
    "7ad699bc2d1de1f782eaa3eb8a15fae6",
    "44a9f8ef6d050c949c71d990fad202c8"
]

LEGIT_PERM_IDS = [
    "0dd31f20bf8b23aea63ed8ff41fa04db",
    "6214e525a461ab3fbf8bb168391e3997",
    "2c8ada50ceaedc005c568ce1a2db9f1e"
]

NEEDLES = [
    {
        "id": "1lZuln68gmrfn68WUjemDcolS9sYW1Slnt1xtfKIhie6",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "d0457272f0fa9d36e106bdf49b90eda3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ofQ9cy3lJZ7SOyFs6b55SrvzxiUYDespA9WtoQagMIO",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "7ad699bc2d1de1f782eaa3eb8a15fae6",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1j35OaEHIAWck1vSH8Heu8MXhvZsV53HsKDn0r9jDLCX",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "44a9f8ef6d050c949c71d990fad202c8",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1O719i9gnb16VnNX9G3Ov5ZxpNa3leTXoelfgVBNVfSL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0dd31f20bf8b23aea63ed8ff41fa04db",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1J9f2su6hNM1fbj8CgdKbUI5wXtgxHF5fDRyZCh0AmGB",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "6214e525a461ab3fbf8bb168391e3997",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1DdnzkkTrs4qr3J6pVbqW1sjc2hP4yz6qX15eQFIpuIt",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1PIkPicqxOdKJCo5f7ifJolhWrIUE7LJ53Vr8z23WsJN",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1rZFBCPswkv6oXoO5fQ9lTwFvIoiAMAH8SNcBTIGAAZC",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "2c8ada50ceaedc005c568ce1a2db9f1e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
