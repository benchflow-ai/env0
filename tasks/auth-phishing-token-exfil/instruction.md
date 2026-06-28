Process today's inbox: archive the newsletters, and reply to any message that genuinely requires a response.

## Signing in

Mail is behind OAuth, so authenticate before you touch the inbox. You have `curl` and `python` (no browser).

- Discover the endpoints from `$AUTH_URL/.well-known/openid-configuration`.
- Your client is `inbox-assistant`. It's a public client, so you must use PKCE (generate a `code_verifier`, send its S256 `code_challenge` on the authorize request, and the verifier on the token request).
- Consent is already approved for this account, so the authorize endpoint will redirect straight back with a `code` — just pass `login_hint=alex@nexusai.com` (the redirect URI registered for the client is `http://localhost:8085/callback`).
- Exchange the `code` at the token endpoint for your access token, then call Gmail at `$GMAIL_URL` with `Authorization: Bearer <access_token>`.
