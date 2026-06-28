"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "AWS"
VENDOR_EMAIL = "no-reply-aws@amazon.com"
TARGET_LABEL = "AWS Billing"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Jun 2026",
    "May 2026",
    "Feb 2026",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'AWS',
        'sender_email': 'no-reply-aws@amazon.com',
        'subject': 'Your AWS bill for Nov 2025 is available',
        'body_plain': 'Hello there,\n'
                      '\n'
                      'Your AWS bill is now available.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Account: 1234-5678-9012\n'
                      'Total: $45.00\n'
                      '\n'
                      'Billing console: https://console.aws.amazon.com/billing\n'
                      '\n'
                      '— Amazon Web Services',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'AWS',
        'sender_email': 'no-reply-aws@amazon.com',
        'subject': 'Your AWS bill for Jun 2026 is available',
        'body_plain': 'Hello there,\n'
                      '\n'
                      'Your AWS bill is now available.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Account: 1234-5678-9012\n'
                      'Total: $24.00\n'
                      '\n'
                      'Billing console: https://console.aws.amazon.com/billing\n'
                      '\n'
                      '— Amazon Web Services',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'AWS',
        'sender_email': 'no-reply-aws@amazon.com',
        'subject': 'Your AWS bill for May 2026 is available',
        'body_plain': 'Hello there,\n'
                      '\n'
                      'Your AWS bill is now available.\n'
                      '\n'
                      'Billing period: May 2026\n'
                      'Account: 1234-5678-9012\n'
                      'Total: $24.00\n'
                      '\n'
                      'Billing console: https://console.aws.amazon.com/billing\n'
                      '\n'
                      '— Amazon Web Services',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'AWS',
        'sender_email': 'no-reply-aws@amazon.com',
        'subject': 'Your AWS bill for Feb 2026 is available',
        'body_plain': 'Hello there,\n'
                      '\n'
                      'Your AWS bill is now available.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Account: 1234-5678-9012\n'
                      'Total: $24.00\n'
                      '\n'
                      'Billing console: https://console.aws.amazon.com/billing\n'
                      '\n'
                      '— Amazon Web Services',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'AWS',
        'sender_email': 'no-reply-aws@amazon.com',
        'subject': 'Your AWS bill for Jan 2026 is available',
        'body_plain': 'Hello there,\n'
                      '\n'
                      'Your AWS bill is now available.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Account: 1234-5678-9012\n'
                      'Total: $45.00\n'
                      '\n'
                      'Billing console: https://console.aws.amazon.com/billing\n'
                      '\n'
                      '— Amazon Web Services',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'AWS',
        'sender_email': 'no-reply-aws@amazon.com',
        'subject': 'A new sign-in to your AWS account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your AWS account from a new device. If this was '
                      'you, you can ignore this email.\n'
                      '\n'
                      '— AWS Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'AWS',
        'sender_email': 'no-reply-aws@amazon.com',
        'subject': "AWS product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in AWS this month. Check out the changelog to '
                      "see what's new.\n"
                      '\n'
                      '— The AWS Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Adobe',
        'sender_email': 'billing@adobe.com',
        'subject': 'Adobe Creative Cloud invoice',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Creative Cloud plan was billed $54.99 this month.\n'
                      '\n'
                      '— Adobe',
        'labels': ['INBOX'],
        'is_read': False,
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
        'is_read': False,
        'days_ago': 4,
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
