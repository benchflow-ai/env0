"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Heroku"
VENDOR_EMAIL = "invoices@heroku.com"
TARGET_LABEL = "Heroku Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "Jun 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Heroku usage has been invoiced.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Dynos: included\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://dashboard.heroku.com/account/billing\n'
                      '\n'
                      '— Heroku',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Heroku usage has been invoiced.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Dynos: included\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://dashboard.heroku.com/account/billing\n'
                      '\n'
                      '— Heroku',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Heroku usage has been invoiced.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Dynos: included\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://dashboard.heroku.com/account/billing\n'
                      '\n'
                      '— Heroku',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Action needed: confirm your Heroku email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Heroku.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Heroku',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
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
        'is_read': False,
        'days_ago': 31,
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
        'is_read': False,
        'days_ago': 4,
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
