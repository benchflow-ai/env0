"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Canva"
VENDOR_EMAIL = "receipts@canva.com"
TARGET_LABEL = "Canva Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Mar 2026",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $96.00\n'
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
        'subject': 'Your Canva receipt for Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'A new sign-in to your Canva account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Canva account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Canva Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 22,
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
