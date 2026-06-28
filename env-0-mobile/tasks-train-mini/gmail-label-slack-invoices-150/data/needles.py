"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Slack"
VENDOR_EMAIL = "billing@slack.com"
TARGET_LABEL = "Slack Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Jan 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $45.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'A new sign-in to your Slack account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Slack account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Slack Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': "Slack product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Slack this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Slack Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
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
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 22,
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
