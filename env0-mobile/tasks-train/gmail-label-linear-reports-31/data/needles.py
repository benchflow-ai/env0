"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Linear"
VENDOR_EMAIL = "weekly@linear.app"
TARGET_LABEL = "Linear Reports"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Apr 2026",
    "Dec 2025",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'Your Linear weekly report — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      "Here's what your team shipped this week.\n"
                      '\n'
                      'Week of Nov 2025\n'
                      'Issues completed: 15\n'
                      'Cycles on track: 3 of 4\n'
                      '\n'
                      'Open dashboard: https://linear.app/team/insights\n'
                      '\n'
                      '— Linear',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'Your Linear weekly report — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      "Here's what your team shipped this week.\n"
                      '\n'
                      'Week of Apr 2026\n'
                      'Issues completed: 24\n'
                      'Cycles on track: 3 of 4\n'
                      '\n'
                      'Open dashboard: https://linear.app/team/insights\n'
                      '\n'
                      '— Linear',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'Your Linear weekly report — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      "Here's what your team shipped this week.\n"
                      '\n'
                      'Week of Dec 2025\n'
                      'Issues completed: 12\n'
                      'Cycles on track: 3 of 4\n'
                      '\n'
                      'Open dashboard: https://linear.app/team/insights\n'
                      '\n'
                      '— Linear',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'Your Linear weekly report — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      "Here's what your team shipped this week.\n"
                      '\n'
                      'Week of Feb 2026\n'
                      'Issues completed: 24\n'
                      'Cycles on track: 3 of 4\n'
                      '\n'
                      'Open dashboard: https://linear.app/team/insights\n'
                      '\n'
                      '— Linear',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Linear',
        'sender_email': 'weekly@linear.app',
        'subject': 'A new sign-in to your Linear account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Linear account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Linear Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
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
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
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
