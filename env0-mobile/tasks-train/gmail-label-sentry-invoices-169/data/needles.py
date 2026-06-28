"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Sentry"
VENDOR_EMAIL = "billing@sentry.io"
TARGET_LABEL = "Sentry Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jan 2026",
    "Feb 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
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
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $45.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'A new sign-in to your Sentry account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Sentry account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Sentry Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Spotify',
        'sender_email': 'receipts@spotify.com',
        'subject': 'Your Spotify Premium receipt',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Spotify Premium subscription renewed. Amount: $11.99.\n'
                      '\n'
                      '— Spotify',
        'labels': ['INBOX'],
        'is_read': True,
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
