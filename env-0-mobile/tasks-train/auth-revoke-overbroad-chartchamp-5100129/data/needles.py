"""Auto-generated env-0 tasks-lite needle data (auth revoke over-permissioned app). Dependency-free.

Consumed by the auth seeder (AUTH_USERS / AUTH_CLIENTS / AUTH_CONSENTS)
and tests/evaluate.py (REVOKE_TARGET / LEGIT_APPS / OWNER_USER_ID).
"""

OWNER_USER_ID = "user1"

REVOKE_TARGET = {
    "client_id": "chartchamp-5100129",
    "client_name": "ChartChamp",
    "scopes": [
        "docs.full",
        "drive.full"
    ],
    "last_used_days_ago": 210
}

LEGIT_APPS = [
    {
        "client_id": "drive-backup",
        "client_name": "Drive Backup",
        "scopes": [
            "drive.readonly"
        ],
        "last_used_days_ago": 2
    },
    {
        "client_id": "inbox-digest",
        "client_name": "Inbox Digest",
        "scopes": [
            "gmail.readonly"
        ],
        "last_used_days_ago": 4
    }
]

_THIRD_PARTY_APPS = [REVOKE_TARGET] + LEGIT_APPS

# user1 / user2 already exist in auth's base seed.
AUTH_USERS = []

AUTH_CLIENTS = [
    {
        "client_id": app["client_id"],
        "client_name": app["client_name"],
        "client_type": "confidential",
        "redirect_uris": [f"http://localhost:7000/{app['client_id']}/callback"],
        "allowed_scopes": app["scopes"],
        "grant_types": ["authorization_code", "refresh_token"],
    }
    for app in _THIRD_PARTY_APPS
]

AUTH_CONSENTS = [
    {
        "user_id": OWNER_USER_ID,
        "client_id": app["client_id"],
        "scopes": app["scopes"],
        "last_used_days_ago": app["last_used_days_ago"],
    }
    for app in _THIRD_PARTY_APPS
]
