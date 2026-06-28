"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Audible"
VENDOR_EMAIL = "receipts@audible.com"
TARGET_LABEL = "Audible Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jan 2026",
    "Mar 2026",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Jan 2026\n'
                      '1 credit used\n'
                      'Membership charge: $24.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Mar 2026\n'
                      '1 credit used\n'
                      'Membership charge: $12.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: May 2026\n'
                      '1 credit used\n'
                      'Membership charge: $18.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Action needed: confirm your Audible email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Audible.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Audible',
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
        'is_read': False,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 4,
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
        'is_read': True,
        'days_ago': 4,
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
