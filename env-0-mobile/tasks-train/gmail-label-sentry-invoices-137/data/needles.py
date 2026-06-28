"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Sentry"
VENDOR_EMAIL = "billing@sentry.io"
TARGET_LABEL = "Sentry Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "May 2026",
    "Feb 2026"
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
        'subject': 'Your Sentry invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: May 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
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
                      'Amount: $18.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': "Sentry product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Sentry this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Sentry Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
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
        'is_read': False,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': '1Password',
        'sender_email': 'receipts@1password.com',
        'subject': 'Your 1Password receipt',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your 1Password Families plan renewed for $4.99/mo.\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 4,
        'role': 'decoy',
        'params': {}}]

GMAIL_FILL_CONFIG = {
    "target_count": 800,
    "include_ambiguous": True,
    "distribution": {
        "notifications": 0.35,
        "newsletters": 0.25,
        "work": 0.20,
        "personal": 0.15,
        "spam": 0.05,
    },
}
