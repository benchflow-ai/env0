"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Intercom"
VENDOR_EMAIL = "billing@intercom.com"
TARGET_LABEL = "Intercom Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "Mar 2026",
    "Jan 2026",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: May 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'A new sign-in to your Intercom account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Intercom account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Intercom Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
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
        'days_ago': 31,
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
        'is_read': True,
        'days_ago': 13,
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
