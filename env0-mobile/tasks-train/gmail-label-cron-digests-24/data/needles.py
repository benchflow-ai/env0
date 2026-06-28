"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Cron"
VENDOR_EMAIL = "weekly@cron.com"
TARGET_LABEL = "Cron Digests"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "May 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': 'Your Cron weekly digest — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Here is your weekly schedule digest.\n'
                      '\n'
                      'Week of Dec 2025\n'
                      'Meetings: 12\n'
                      'Focus blocks: 4\n'
                      '\n'
                      'Open Cron: https://cron.com/app\n'
                      '\n'
                      '— Cron',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': 'Your Cron weekly digest — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Here is your weekly schedule digest.\n'
                      '\n'
                      'Week of May 2026\n'
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
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': 'Your Cron weekly digest — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Here is your weekly schedule digest.\n'
                      '\n'
                      'Week of Mar 2026\n'
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
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Cron',
        'sender_email': 'weekly@cron.com',
        'subject': "Cron product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Cron this month. Check out the changelog to '
                      "see what's new.\n"
                      '\n'
                      '— The Cron Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
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
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
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
