"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Slack"
VENDOR_EMAIL = "billing@slack.com"
TARGET_LABEL = "Slack Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Nov 2025",
    "Jun 2026",
    "Jan 2026",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
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
        'subject': 'Your Slack invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
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
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Your Slack invoice — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Slack workspace has been billed.\n'
                      '\n'
                      'Plan: Slack Pro\n'
                      'Billing period: May 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'View invoice: https://slack.com/account/billing\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'Action needed: confirm your Slack email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Slack.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Slack',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Slack',
        'sender_email': 'billing@slack.com',
        'subject': 'A new sign-in to your Slack account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Slack account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Slack Security',
        'labels': ['INBOX'],
        'is_read': False,
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
        'days_ago': 22,
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
