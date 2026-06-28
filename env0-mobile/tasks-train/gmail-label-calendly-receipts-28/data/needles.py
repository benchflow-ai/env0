"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Calendly"
VENDOR_EMAIL = "receipts@calendly.com"
TARGET_LABEL = "Calendly Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Jan 2026",
    "May 2026",
    "Feb 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Your Calendly receipt — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for subscribing to Calendly.\n'
                      '\n'
                      'Plan: Calendly Teams\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing settings: https://calendly.com/app/admin/billing\n'
                      '\n'
                      '— Calendly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Your Calendly receipt — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for subscribing to Calendly.\n'
                      '\n'
                      'Plan: Calendly Teams\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing settings: https://calendly.com/app/admin/billing\n'
                      '\n'
                      '— Calendly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Your Calendly receipt — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for subscribing to Calendly.\n'
                      '\n'
                      'Plan: Calendly Teams\n'
                      'Billing period: May 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing settings: https://calendly.com/app/admin/billing\n'
                      '\n'
                      '— Calendly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Your Calendly receipt — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for subscribing to Calendly.\n'
                      '\n'
                      'Plan: Calendly Teams\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing settings: https://calendly.com/app/admin/billing\n'
                      '\n'
                      '— Calendly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Your Calendly receipt — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for subscribing to Calendly.\n'
                      '\n'
                      'Plan: Calendly Teams\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing settings: https://calendly.com/app/admin/billing\n'
                      '\n'
                      '— Calendly',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'A new sign-in to your Calendly account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Calendly account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Calendly Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Action needed: confirm your Calendly email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Calendly.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Calendly',
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
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 13,
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
