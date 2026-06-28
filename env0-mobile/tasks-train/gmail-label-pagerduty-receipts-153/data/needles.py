"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "PagerDuty"
VENDOR_EMAIL = "billing@pagerduty.com"
TARGET_LABEL = "PagerDuty Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Dec 2025",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://app.pagerduty.com/billing\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://app.pagerduty.com/billing\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.pagerduty.com/billing\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'A new sign-in to your PagerDuty account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your PagerDuty account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— PagerDuty Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 11,
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
        'is_read': False,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
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
