"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Mailchimp"
VENDOR_EMAIL = "receipts@mailchimp.com"
TARGET_LABEL = "Mailchimp Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Jan 2026",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Mailchimp',
        'sender_email': 'receipts@mailchimp.com',
        'subject': 'Your Mailchimp receipt — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Mailchimp payment.\n'
                      '\n'
                      'Plan: Standard\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://admin.mailchimp.com/account/billing\n'
                      '\n'
                      '— Mailchimp',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Mailchimp',
        'sender_email': 'receipts@mailchimp.com',
        'subject': 'Your Mailchimp receipt — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Mailchimp payment.\n'
                      '\n'
                      'Plan: Standard\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://admin.mailchimp.com/account/billing\n'
                      '\n'
                      '— Mailchimp',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Mailchimp',
        'sender_email': 'receipts@mailchimp.com',
        'subject': 'Your Mailchimp receipt — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Mailchimp payment.\n'
                      '\n'
                      'Plan: Standard\n'
                      'Billing period: May 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://admin.mailchimp.com/account/billing\n'
                      '\n'
                      '— Mailchimp',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Mailchimp',
        'sender_email': 'receipts@mailchimp.com',
        'subject': 'A new sign-in to your Mailchimp account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Mailchimp account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Mailchimp Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Mailchimp',
        'sender_email': 'receipts@mailchimp.com',
        'subject': 'Action needed: confirm your Mailchimp email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Mailchimp.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Mailchimp',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 13,
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
        'is_read': False,
        'days_ago': 4,
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
