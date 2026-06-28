"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Linear"
VENDOR_EMAIL = "weekly@linear.app"
TARGET_LABEL = "Linear Reports"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "Jan 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'Your Linear weekly report — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      "Here's what your team shipped this week.\n"
                      '\n'
                      'Week of Apr 2026\n'
                      'Issues completed: 12\n'
                      'Cycles on track: 3 of 4\n'
                      '\n'
                      'Open dashboard: https://linear.app/team/insights\n'
                      '\n'
                      '— Linear',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'Your Linear weekly report — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      "Here's what your team shipped this week.\n"
                      '\n'
                      'Week of Jan 2026\n'
                      'Issues completed: 18\n'
                      'Cycles on track: 3 of 4\n'
                      '\n'
                      'Open dashboard: https://linear.app/team/insights\n'
                      '\n'
                      '— Linear',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'Your Linear weekly report — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      "Here's what your team shipped this week.\n"
                      '\n'
                      'Week of Nov 2025\n'
                      'Issues completed: 96\n'
                      'Cycles on track: 3 of 4\n'
                      '\n'
                      'Open dashboard: https://linear.app/team/insights\n'
                      '\n'
                      '— Linear',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'Action needed: confirm your Linear email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Linear.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Linear',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
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
        'is_read': False,
        'days_ago': 13,
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
