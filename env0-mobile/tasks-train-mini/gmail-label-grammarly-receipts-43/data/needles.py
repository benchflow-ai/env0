"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Grammarly"
VENDOR_EMAIL = "receipts@grammarly.com"
TARGET_LABEL = "Grammarly Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Mar 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'Your Grammarly receipt — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Grammarly Premium payment.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Account: https://account.grammarly.com/subscription\n'
                      '\n'
                      '— Grammarly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'Your Grammarly receipt — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Grammarly Premium payment.\n'
                      '\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Account: https://account.grammarly.com/subscription\n'
                      '\n'
                      '— Grammarly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'Your Grammarly receipt — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your Grammarly Premium payment.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Account: https://account.grammarly.com/subscription\n'
                      '\n'
                      '— Grammarly',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'Action needed: confirm your Grammarly email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Grammarly.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Grammarly',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Grammarly',
        'sender_email': 'receipts@grammarly.com',
        'subject': 'A new sign-in to your Grammarly account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Grammarly account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Grammarly Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
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
        'days_ago': 31,
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
