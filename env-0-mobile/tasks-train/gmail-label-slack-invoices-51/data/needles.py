"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Slack"
VENDOR_EMAIL = "billing@slack.com"
TARGET_LABEL = "Slack Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "May 2026",
    "Dec 2025",
    "Nov 2025",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: May 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
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
        'is_read': False,
        'days_ago': 28,
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
