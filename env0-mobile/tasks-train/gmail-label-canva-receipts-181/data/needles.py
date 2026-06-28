"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Canva"
VENDOR_EMAIL = "receipts@canva.com"
TARGET_LABEL = "Canva Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Mar 2026",
    "Jun 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Action needed: confirm your Canva email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Canva.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'A new sign-in to your Canva account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Canva account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Canva Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
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
