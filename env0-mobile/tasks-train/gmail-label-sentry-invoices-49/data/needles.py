"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Sentry"
VENDOR_EMAIL = "billing@sentry.io"
TARGET_LABEL = "Sentry Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Apr 2026",
    "Jun 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Sentry',
        'sender_email': 'billing@sentry.io',
        'subject': 'Your Sentry invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $45.00\n'
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
        'subject': 'Your Sentry invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Sentry usage has been billed.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'View invoice: https://sentry.io/settings/billing\n'
                      '\n'
                      '— Sentry',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
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
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Adobe',
        'sender_email': 'billing@adobe.com',
        'subject': 'Adobe Creative Cloud invoice',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Creative Cloud plan was billed $54.99 this month.\n'
                      '\n'
                      '— Adobe',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': '1Password',
        'sender_email': 'receipts@1password.com',
        'subject': 'Your 1Password receipt',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Families plan renewed for $4.99/mo.\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 4,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
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
