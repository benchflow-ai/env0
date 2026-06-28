"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Calendly"
VENDOR_EMAIL = "receipts@calendly.com"
TARGET_LABEL = "Calendly Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Apr 2026",
    "Jun 2026"
]

NEEDLES = [   {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Your Calendly receipt — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for subscribing to Calendly.\n'
                      '\n'
                      'Plan: Calendly Teams\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing settings: https://calendly.com/app/admin/billing\n'
                      '\n'
                      '— Calendly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Your Calendly receipt — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for subscribing to Calendly.\n'
                      '\n'
                      'Plan: Calendly Teams\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing settings: https://calendly.com/app/admin/billing\n'
                      '\n'
                      '— Calendly',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': 'Your Calendly receipt — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for subscribing to Calendly.\n'
                      '\n'
                      'Plan: Calendly Teams\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing settings: https://calendly.com/app/admin/billing\n'
                      '\n'
                      '— Calendly',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Calendly',
        'sender_email': 'receipts@calendly.com',
        'subject': "Calendly product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Calendly this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The Calendly Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
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
