"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "GitHub"
VENDOR_EMAIL = "receipt@github.com"
TARGET_LABEL = "GitHub Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Nov 2025",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': '[GitHub] Payment receipt for Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your GitHub payment was successful.\n'
                      '\n'
                      'Period: Dec 2025\n'
                      'Plan: GitHub Pro\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing settings: https://github.com/settings/billing\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': '[GitHub] Payment receipt for Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your GitHub payment was successful.\n'
                      '\n'
                      'Period: Nov 2025\n'
                      'Plan: GitHub Pro\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing settings: https://github.com/settings/billing\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': '[GitHub] Payment receipt for Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your GitHub payment was successful.\n'
                      '\n'
                      'Period: Apr 2026\n'
                      'Plan: GitHub Pro\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing settings: https://github.com/settings/billing\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': 'A new sign-in to your GitHub account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your GitHub account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— GitHub Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': "GitHub product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in GitHub this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The GitHub Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 19,
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
        'is_read': True,
        'days_ago': 22,
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
