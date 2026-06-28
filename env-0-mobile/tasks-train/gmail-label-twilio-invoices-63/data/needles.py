"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Twilio"
VENDOR_EMAIL = "invoices@twilio.com"
TARGET_LABEL = "Twilio Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "Jun 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': 'Your Twilio invoice — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Twilio usage invoice is ready.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Messages sent: included\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Console: https://console.twilio.com/billing\n'
                      '\n'
                      '— Twilio',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': 'Your Twilio invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Twilio usage invoice is ready.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Messages sent: included\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Console: https://console.twilio.com/billing\n'
                      '\n'
                      '— Twilio',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': 'Your Twilio invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Twilio usage invoice is ready.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Messages sent: included\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Console: https://console.twilio.com/billing\n'
                      '\n'
                      '— Twilio',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': "Twilio product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Twilio this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Twilio Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': 'Action needed: confirm your Twilio email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Twilio.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Twilio',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 13,
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
        'is_read': True,
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
