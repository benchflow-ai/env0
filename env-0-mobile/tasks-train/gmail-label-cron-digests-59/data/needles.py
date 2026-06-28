"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Cron"
VENDOR_EMAIL = "weekly@cron.com"
TARGET_LABEL = "Cron Digests"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Apr 2026",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': 'Your Cron weekly digest — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Here is your weekly schedule digest.\n'
                      '\n'
                      'Week of Feb 2026\n'
                      'Meetings: 24\n'
                      'Focus blocks: 4\n'
                      '\n'
                      'Open Cron: https://cron.com/app\n'
                      '\n'
                      '— Cron',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': 'Your Cron weekly digest — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Here is your weekly schedule digest.\n'
                      '\n'
                      'Week of Apr 2026\n'
                      'Meetings: 45\n'
                      'Focus blocks: 4\n'
                      '\n'
                      'Open Cron: https://cron.com/app\n'
                      '\n'
                      '— Cron',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': 'Your Cron weekly digest — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Here is your weekly schedule digest.\n'
                      '\n'
                      'Week of Jan 2026\n'
                      'Meetings: 18\n'
                      'Focus blocks: 4\n'
                      '\n'
                      'Open Cron: https://cron.com/app\n'
                      '\n'
                      '— Cron',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': 'A new sign-in to your Cron account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Cron account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Cron Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': 'Action needed: confirm your Cron email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Cron.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Cron',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 13,
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
        'days_ago': 31,
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
