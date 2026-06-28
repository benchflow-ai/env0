"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Webflow"
VENDOR_EMAIL = "receipts@webflow.com"
TARGET_LABEL = "Webflow Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "May 2026",
    "Apr 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Webflow',
        'sender_email': 'receipts@webflow.com',
        'subject': 'Your Webflow receipt — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Webflow payment.\n'
                      '\n'
                      'Plan: Site plan\n'
                      'Billing period: May 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing dashboard: https://webflow.com/dashboard/billing\n'
                      '\n'
                      '— Webflow',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Webflow',
        'sender_email': 'receipts@webflow.com',
        'subject': 'Your Webflow receipt — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Webflow payment.\n'
                      '\n'
                      'Plan: Site plan\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing dashboard: https://webflow.com/dashboard/billing\n'
                      '\n'
                      '— Webflow',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Webflow',
        'sender_email': 'receipts@webflow.com',
        'subject': 'Your Webflow receipt — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Webflow payment.\n'
                      '\n'
                      'Plan: Site plan\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing dashboard: https://webflow.com/dashboard/billing\n'
                      '\n'
                      '— Webflow',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Webflow',
        'sender_email': 'receipts@webflow.com',
        'subject': 'Action needed: confirm your Webflow email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Webflow.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Webflow',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Webflow',
        'sender_email': 'receipts@webflow.com',
        'subject': "Webflow product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Webflow this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Webflow Team',
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
        'days_ago': 22,
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
