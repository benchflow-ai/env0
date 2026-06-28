"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Heroku"
VENDOR_EMAIL = "invoices@heroku.com"
TARGET_LABEL = "Heroku Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Jan 2026",
    "Jun 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Nov 2025',
        'body_plain': 'Hi Alex,\n'
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
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Heroku usage has been invoiced.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
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
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Heroku usage has been invoiced.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Dynos: included\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://dashboard.heroku.com/account/billing\n'
                      '\n'
                      '— Heroku',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': 'Heroku invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
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
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Heroku',
        'sender_email': 'invoices@heroku.com',
        'subject': "Heroku product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Heroku this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Heroku Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 13,
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
        'days_ago': 31,
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
        'days_ago': 4,
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
