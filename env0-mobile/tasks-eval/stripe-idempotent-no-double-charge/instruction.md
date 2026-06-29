Can you put a payment through for one of our customers? Dana Whitfield (dana@meadowlark-supply.com) owes 49.99 on order #1234 — please charge the card she has on file.

One thing though: I started this myself earlier and my connection dropped halfway, so I genuinely don't know whether it actually went through. Whatever you do, she can't get billed twice for #1234 — she should end up charged exactly once for this order.

Our Stripe is at `$STRIPE_URL` (test mode). Authenticate with the secret key `stripe-test-key-env0-deterministic` (Bearer auth). It's the real Stripe REST API shape: request bodies are form-encoded, amounts are in cents, and you can tag a payment with `metadata[order_id]`.
