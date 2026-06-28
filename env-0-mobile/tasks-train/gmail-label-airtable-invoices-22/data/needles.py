"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Airtable"
VENDOR_EMAIL = "billing@airtable.com"
TARGET_LABEL = "Airtable Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "May 2026",
    "Apr 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: May 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': "Airtable product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Airtable this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The Airtable Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
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
