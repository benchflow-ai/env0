"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Zoom"
VENDOR_EMAIL = "billing@zoom.us"
TARGET_LABEL = "Zoom Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Apr 2026",
    "Mar 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Zoom',
        'sender_email': 'billing@zoom.us',
        'subject': 'Your Zoom payment receipt — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment.\n'
                      '\n'
                      'Plan: Zoom Pro\n'
                      'Billing period: Dec 2025\n'
                      'Amount charged: $18.00\n'
                      '\n'
                      'Billing portal: https://zoom.us/billing\n'
                      '\n'
                      '— Zoom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Zoom',
        'sender_email': 'billing@zoom.us',
        'subject': 'Your Zoom payment receipt — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment.\n'
                      '\n'
                      'Plan: Zoom Pro\n'
                      'Billing period: Apr 2026\n'
                      'Amount charged: $96.00\n'
                      '\n'
                      'Billing portal: https://zoom.us/billing\n'
                      '\n'
                      '— Zoom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Zoom',
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
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Zoom',
        'sender_email': 'billing@zoom.us',
        'subject': 'Your Zoom payment receipt — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment.\n'
                      '\n'
                      'Plan: Zoom Pro\n'
                      'Billing period: Feb 2026\n'
                      'Amount charged: $15.00\n'
                      '\n'
                      'Billing portal: https://zoom.us/billing\n'
                      '\n'
                      '— Zoom',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
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
        'days_ago': 4,
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
