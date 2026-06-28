My inbox has gotten messy and I want to see at a glance what came from inside the company versus outside. Create two labels, "Internal" and "External", then go through every email in my inbox and tag each one: anything sent from an @nexusai.com address gets Internal, everything else gets External — careful, some outside senders use domains that look a lot like ours. Just label; don't delete anything and don't send anything.

The Gmail API here sits behind our OAuth server, so authenticate first:

- Auth server: `$AUTH_URL` — fetch `/.well-known/openid-configuration` to discover the authorization and token endpoints.
- Use the client `expiry-client` (confidential; client secret `client-secret`; registered redirect URI `http://localhost:8765/callback`). Confidential clients authenticate with their secret, so PKCE isn't required for this one — only public clients must use PKCE on this server.
- I already approved this client on my account (alex@nexusai.com) for `openid gmail.modify gmail.labels`, so the authorization endpoint skips the consent screen and redirects immediately with a code when you include `login_hint=alex@nexusai.com`. Nothing is listening on the redirect URI — don't follow the redirect, just read the code out of the `Location` header.
- Heads-up: access tokens for this client expire after 90 seconds. If Gmail starts answering 401 partway through, don't keep retrying the dead token — exchange your refresh token at the token endpoint (`grant_type=refresh_token`) and pick up where you left off.

You have curl and python; there's no browser.
