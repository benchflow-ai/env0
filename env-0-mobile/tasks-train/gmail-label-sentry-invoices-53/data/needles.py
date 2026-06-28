"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Sentry"
VENDOR_EMAIL = "billing@sentry.io"
TARGET_LABEL = "Sentry Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Jan 2026",
    "May 2026",
    "Feb 2026",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $12.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: May 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Action needed: confirm your Sentry email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Sentry.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Adobe',
        'sender_email': 'billing@adobe.com',
        'subject': 'Adobe Creative Cloud invoice',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Creative Cloud plan was billed $54.99 this month.\n'
                      '\n'
                      '— Adobe',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 4,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Spotify',
        'sender_email': 'receipts@spotify.com',
        'subject': 'Your Spotify Premium receipt',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Spotify Premium subscription renewed. Amount: $11.99.\n'
                      '\n'
                      '— Spotify',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}}]

GMAIL_FILL_CONFIG = {
    "target_count": 400,
    "include_ambiguous": True,
    "distribution": {
        "notifications": 0.35,
        "newsletters": 0.25,
        "work": 0.20,
        "personal": 0.15,
        "spam": 0.05,
    },
}
