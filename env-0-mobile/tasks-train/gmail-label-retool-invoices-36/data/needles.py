"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Retool"
VENDOR_EMAIL = "billing@retool.com"
TARGET_LABEL = "Retool Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Dec 2025",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Jun 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Dec 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Feb 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
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
        'is_read': True,
        'days_ago': 3,
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
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
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
