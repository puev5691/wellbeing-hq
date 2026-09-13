# Transport contract

## Exact provider route

Only:
- method: `POST`;
- URL: `https://api.anthropic.com/v1/messages`;
- model: `claude-sonnet-5`;
- `anthropic-version: 2023-06-01`;
- `content-type: application/json`.

No redirects or alternate provider routes are constructed by this package. The request blueprint must exactly match the accepted adapter hash and structure before auth injection.

## Credential boundary

Secret interface: environment variable reference `ANTHROPIC_API_KEY`.

The key value is read only inside the separately enabled live path, after D0 blueprint validation and live-switch validation. The value is used only to construct the in-memory `x-api-key` request header. It is not returned in request plans, provenance, results, logs or errors.

Tests use `InjectedSecretReader` with a non-secret placeholder. They do not read OPERATOR secrets or environment credentials.

## Default deny

Without `--live`, launcher validates and exits with `LIVE_DISABLED_DEFAULT_DENY`.

Live requires exact environment switch:
`ANTHROPIC_LIVE_D0=EXPLICIT_D0_LIVE`.

Missing or wrong switch fails before the live secret reader or provider executor is used.

## Timeout/errors

Allowed timeout: 1..60 seconds, default 30.

One request attempt only. No automatic retry and no fallback.

Sanitized outcomes:
- 401/403 → `AUTH_ERROR`;
- 429 → `RATE_LIMITED`, `retriable=true`, but no automatic retry;
- 5xx → `PROVIDER_HTTP_ERROR`, `retriable=true`, but no automatic retry;
- timeout → `NETWORK_TIMEOUT`, `retriable=true`;
- other network failure → `NETWORK_ERROR`;
- malformed provider JSON/usage/content/model → fail closed.

Provider error bodies and exception details are not echoed.

## Accepted policy remains authoritative

The inherited `PolicyGuard` must first PASS D0 synthetic config. Therefore data class must remain `D0_SYNTHETIC`; tools, search, files, caching, MCP, Managed Agents, code execution, fallback, alternate provider, network flag inside the accepted content policy, project mutation and production must all remain false.

The outer live switch authorizes only the single network transport attempt for the already validated blueprint. It does not mutate or broaden the accepted policy config.
