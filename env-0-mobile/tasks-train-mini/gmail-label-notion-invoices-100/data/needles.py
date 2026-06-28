"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Notion"
VENDOR_EMAIL = "billing@notion.so"
TARGET_LABEL = "Notion Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Nov 2025",
    "May 2026",
    "Apr 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Jun 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Jun 2026\n'
                      'Total: $45.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Nov 2025',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Nov 2025\n'
                      'Total: $12.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for May 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: May 2026\n'
                      'Total: $15.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Apr 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Apr 2026\n'
                      'Total: $96.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Feb 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Feb 2026\n'
                      'Total: $15.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': "Notion product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Notion this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'A new sign-in to your Notion account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Notion account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Notion Security',
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
        'is_read': True,
        'days_ago': 13,
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
