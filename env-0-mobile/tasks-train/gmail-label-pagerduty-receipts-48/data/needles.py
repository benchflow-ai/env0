"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "PagerDuty"
VENDOR_EMAIL = "billing@pagerduty.com"
TARGET_LABEL = "PagerDuty Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "Jan 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://app.pagerduty.com/billing\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://app.pagerduty.com/billing\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': 'Your PagerDuty receipt for Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your PagerDuty subscription renewed.\n'
                      '\n'
                      'Plan: Professional\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://app.pagerduty.com/billing\n'
                      '\n'
                      '— PagerDuty',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
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
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'PagerDuty',
        'sender_email': 'billing@pagerduty.com',
        'subject': "PagerDuty product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in PagerDuty this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The PagerDuty Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 11,
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
    {   'sender_name': 'Spotify',
        'sender_email': 'receipts@spotify.com',
        'subject': 'Your Spotify Premium receipt',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Spotify Premium subscription renewed. Amount: $11.99.\n'
                      '\n'
                      '— Spotify',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}}]

GMAIL_FILL_CONFIG = {
    "target_count": 800,
    "include_ambiguous": True,
    "distribution": {
        "notifications": 0.35,
        "newsletters": 0.25,
        "work": 0.20,
        "personal": 0.15,
        "spam": 0.05,
    },
}
