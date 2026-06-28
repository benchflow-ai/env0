"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Audible"
VENDOR_EMAIL = "receipts@audible.com"
TARGET_LABEL = "Audible Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "Jan 2026",
    "Dec 2025",
    "May 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Apr 2026\n'
                      '1 credit used\n'
                      'Membership charge: $12.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Jan 2026\n'
                      '1 credit used\n'
                      'Membership charge: $18.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Dec 2025\n'
                      '1 credit used\n'
                      'Membership charge: $45.00\n'
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
        'subject': 'Your Audible purchase receipt — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: May 2026\n'
                      '1 credit used\n'
                      'Membership charge: $45.00\n'
                      '\n'
                      'Your library: https://audible.com/library\n'
                      '\n'
                      '— Audible',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Audible',
        'sender_email': 'receipts@audible.com',
        'subject': 'Your Audible purchase receipt — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Audible order.\n'
                      '\n'
                      'Order date: Nov 2025\n'
                      '1 credit used\n'
                      'Membership charge: $45.00\n'
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
        'subject': 'A new sign-in to your Audible account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Audible account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Audible Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 13,
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
        'is_read': False,
        'days_ago': 13,
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
        'is_read': False,
        'days_ago': 4,
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
