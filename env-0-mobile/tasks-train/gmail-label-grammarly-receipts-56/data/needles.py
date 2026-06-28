"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Grammarly"
VENDOR_EMAIL = "receipts@grammarly.com"
TARGET_LABEL = "Grammarly Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jan 2026",
    "Dec 2025",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'Your Grammarly receipt — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Grammarly Premium payment.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Account: https://account.grammarly.com/subscription\n'
                      '\n'
                      '— Grammarly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'Your Grammarly receipt — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Grammarly Premium payment.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Account: https://account.grammarly.com/subscription\n'
                      '\n'
                      '— Grammarly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'Your Grammarly receipt — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your Grammarly Premium payment.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Account: https://account.grammarly.com/subscription\n'
                      '\n'
                      '— Grammarly',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': "Grammarly product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Grammarly this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The Grammarly Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'A new sign-in to your Grammarly account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Grammarly account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Grammarly Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
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
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 31,
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
