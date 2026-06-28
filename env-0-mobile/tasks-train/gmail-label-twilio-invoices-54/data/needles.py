"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Twilio"
VENDOR_EMAIL = "invoices@twilio.com"
TARGET_LABEL = "Twilio Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Feb 2026",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': 'Your Twilio invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Twilio usage invoice is ready.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Messages sent: included\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Console: https://console.twilio.com/billing\n'
                      '\n'
                      '— Twilio',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': 'Your Twilio invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Twilio usage invoice is ready.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Messages sent: included\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Console: https://console.twilio.com/billing\n'
                      '\n'
                      '— Twilio',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': 'Your Twilio invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Twilio usage invoice is ready.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Messages sent: included\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Console: https://console.twilio.com/billing\n'
                      '\n'
                      '— Twilio',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': "Twilio product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Twilio this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Twilio Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Twilio',
        'sender_email': 'invoices@twilio.com',
        'subject': 'A new sign-in to your Twilio account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Twilio account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Twilio Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 11,
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
