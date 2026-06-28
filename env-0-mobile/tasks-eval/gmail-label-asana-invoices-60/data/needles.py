"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Asana"
VENDOR_EMAIL = "billing@asana.com"
TARGET_LABEL = "Asana Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Feb 2026",
    "Apr 2026",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Jun 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Feb 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Apr 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Jan 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Action needed: confirm your Asana email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Asana.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
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
        'is_read': True,
        'days_ago': 31,
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
        'days_ago': 31,
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
