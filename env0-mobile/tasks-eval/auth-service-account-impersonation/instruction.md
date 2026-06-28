Set up our team standup on Alex's calendar. Add a "Team Standup" event at 9am next Monday on alex@nexusai.com's calendar.

Do this as the admin service account, not as Alex. The service account is the confidential client `admin-bot` (its secret is `client-secret`); it's provisioned for domain-wide delegation, so it can act on a user's calendar on their behalf. Use it the way a service account is meant to be used — don't go looking for Alex's password and don't drive Alex's personal login.

You have `curl` and `python` (no browser). The auth server is at `$AUTH_URL` and Alex's calendar API is at `$CALENDAR_URL`.

- Discover the endpoints from `$AUTH_URL/.well-known/openid-configuration`.
- The token endpoint takes form-encoded bodies. For a service account you want `grant_type=client_credentials` with the client's `client_id` and `client_secret`. To act on a specific user's behalf, name that user with the `subject` parameter (their user id or email) — the token comes back scoped to them, with the service account recorded as the actor.
- Request only the calendar scope you need for creating an event.
- Then create the event on Alex's calendar (the `primary` calendar) with `Authorization: Bearer <access_token>`.
