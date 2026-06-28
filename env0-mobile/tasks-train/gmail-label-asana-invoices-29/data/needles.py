"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Asana"
VENDOR_EMAIL = "billing@asana.com"
TARGET_LABEL = "Asana Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Feb 2026",
    "May 2026",
    "Dec 2025",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Nov 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Feb 2026\n'
                      'Amount: $24.00\n'
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
        'subject': 'Your Asana invoice — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: May 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Dec 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Mar 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Action needed: confirm your Asana email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Asana.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
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
        'days_ago': 13,
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
