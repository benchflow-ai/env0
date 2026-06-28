"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Sentry"
VENDOR_EMAIL = "billing@sentry.io"
TARGET_LABEL = "Sentry Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "Feb 2026",
    "Jun 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $24.00\n'
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
        'subject': 'Your Sentry invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
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
        'is_read': False,
        'days_ago': 28,
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
        'is_read': True,
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
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
        'is_read': True,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}}]

GMAIL_FILL_CONFIG = {
    "target_count": 600,
    "include_ambiguous": True,
    "distribution": {
        "notifications": 0.35,
        "newsletters": 0.25,
        "work": 0.20,
        "personal": 0.15,
        "spam": 0.05,
    },
}
