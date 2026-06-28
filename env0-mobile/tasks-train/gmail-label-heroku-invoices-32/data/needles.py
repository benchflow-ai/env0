"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Heroku"
VENDOR_EMAIL = "invoices@heroku.com"
TARGET_LABEL = "Heroku Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jan 2026",
    "Nov 2025",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Heroku usage has been invoiced.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Dynos: included\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://dashboard.heroku.com/account/billing\n'
                      '\n'
                      '— Heroku',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Heroku usage has been invoiced.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Dynos: included\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://dashboard.heroku.com/account/billing\n'
                      '\n'
                      '— Heroku',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Heroku usage has been invoiced.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
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
        'params': {'marker': 'Apr 2026'}},
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
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 4,
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
        'days_ago': 22,
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
