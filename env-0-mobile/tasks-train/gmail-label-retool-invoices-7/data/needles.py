"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Retool"
VENDOR_EMAIL = "billing@retool.com"
TARGET_LABEL = "Retool Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "May 2026",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Nov 2025\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: May 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Jan 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Action needed: confirm your Retool email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Retool.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
    {   'sender_name': '1Password',
        'sender_email': 'receipts@1password.com',
        'subject': 'Your 1Password receipt',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Families plan renewed for $4.99/mo.\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 13,
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
