"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Audible"
VENDOR_EMAIL = "receipts@audible.com"
TARGET_LABEL = "Audible Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "Feb 2026",
    "Dec 2025",
    "Jun 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Mar 2026\n'
                      '1 credit used\n'
                      'Membership charge: $18.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Feb 2026\n'
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
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Dec 2025\n'
                      '1 credit used\n'
                      'Membership charge: $18.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Jun 2026\n'
                      '1 credit used\n'
                      'Membership charge: $15.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Nov 2025\n'
                      '1 credit used\n'
                      'Membership charge: $18.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Action needed: confirm your Audible email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Audible.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 11,
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
        'days_ago': 31,
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
