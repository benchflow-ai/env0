"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "PagerDuty"
VENDOR_EMAIL = "billing@pagerduty.com"
TARGET_LABEL = "PagerDuty Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Mar 2026",
    "Dec 2025",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $12.00\n'
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
        'subject': 'Your PagerDuty receipt for Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://app.pagerduty.com/billing\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for Dec 2025',
        'body_plain': 'Hi Alex,\n'
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
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: May 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://app.pagerduty.com/billing\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Action needed: confirm your PagerDuty email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using PagerDuty.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'A new sign-in to your PagerDuty account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your PagerDuty account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— PagerDuty Security',
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
        'is_read': True,
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
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
