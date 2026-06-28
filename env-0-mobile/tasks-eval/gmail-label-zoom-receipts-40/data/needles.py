"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Zoom"
VENDOR_EMAIL = "billing@zoom.us"
TARGET_LABEL = "Zoom Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "May 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Zoom',
        'sender_email': 'billing@zoom.us',
        'subject': 'Your Zoom payment receipt — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment.\n'
                      '\n'
                      'Plan: Zoom Pro\n'
                      'Billing period: Mar 2026\n'
                      'Amount charged: $18.00\n'
                      '\n'
                      'Billing portal: https://zoom.us/billing\n'
                      '\n'
                      '— Zoom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Zoom',
        'sender_email': 'billing@zoom.us',
        'subject': 'Your Zoom payment receipt — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment.\n'
                      '\n'
                      'Plan: Zoom Pro\n'
                      'Billing period: May 2026\n'
                      'Amount charged: $12.00\n'
                      '\n'
                      'Billing portal: https://zoom.us/billing\n'
                      '\n'
                      '— Zoom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Zoom',
        'sender_email': 'billing@zoom.us',
        'subject': 'Your Zoom payment receipt — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment.\n'
                      '\n'
                      'Plan: Zoom Pro\n'
                      'Billing period: Nov 2025\n'
                      'Amount charged: $45.00\n'
                      '\n'
                      'Billing portal: https://zoom.us/billing\n'
                      '\n'
                      '— Zoom',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Zoom',
        'sender_email': 'billing@zoom.us',
        'subject': 'A new sign-in to your Zoom account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Zoom account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Zoom Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Zoom',
        'sender_email': 'billing@zoom.us',
        'subject': "Zoom product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Zoom this month. Check out the changelog to '
                      "see what's new.\n"
                      '\n'
                      '— The Zoom Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 11,
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
        'is_read': False,
        'days_ago': 22,
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
