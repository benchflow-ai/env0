"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Airtable"
VENDOR_EMAIL = "billing@airtable.com"
TARGET_LABEL = "Airtable Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "Feb 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'A new sign-in to your Airtable account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Airtable account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Airtable Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
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
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 22,
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
        'days_ago': 22,
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
