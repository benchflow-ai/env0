"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Intercom"
VENDOR_EMAIL = "billing@intercom.com"
TARGET_LABEL = "Intercom Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "Nov 2025",
    "Dec 2025",
    "Feb 2026",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Action needed: confirm your Intercom email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Intercom.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'A new sign-in to your Intercom account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Intercom account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Intercom Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
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
