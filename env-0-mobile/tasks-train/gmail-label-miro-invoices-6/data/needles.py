"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Miro"
VENDOR_EMAIL = "invoices@miro.com"
TARGET_LABEL = "Miro Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Mar 2026",
    "Jan 2026",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'Miro invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Miro subscription has been invoiced.\n'
                      '\n'
                      'Plan: Miro Business\n'
                      'Period: Jun 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Download invoice: https://miro.com/app/settings/billing\n'
                      '\n'
                      '— Miro',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'Miro invoice — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Miro subscription has been invoiced.\n'
                      '\n'
                      'Plan: Miro Business\n'
                      'Period: Mar 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Download invoice: https://miro.com/app/settings/billing\n'
                      '\n'
                      '— Miro',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'Miro invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Miro subscription has been invoiced.\n'
                      '\n'
                      'Plan: Miro Business\n'
                      'Period: Jan 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Download invoice: https://miro.com/app/settings/billing\n'
                      '\n'
                      '— Miro',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'Miro invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Miro subscription has been invoiced.\n'
                      '\n'
                      'Plan: Miro Business\n'
                      'Period: Apr 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Download invoice: https://miro.com/app/settings/billing\n'
                      '\n'
                      '— Miro',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'A new sign-in to your Miro account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Miro account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Miro Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
        'is_read': True,
        'days_ago': 31,
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
