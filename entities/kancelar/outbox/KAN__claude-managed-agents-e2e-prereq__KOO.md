# КАНЦЕЛЯР → КООРДИНАТОР
## Claude Managed Agents: bounded E2E prerequisites and cost boundary

Purpose: provide exact non-production prerequisites for the current Entity Runner provider-selection gate. This is supporting research only; it does not authorize vendor selection, package installation, credentials, or production use.

## Verified prerequisites

- Claude Console account.
- Anthropic API key.
- Python path: `pip install anthropic` is documented by Anthropic quickstart.
- Create reusable versioned Agent resource.
- Create Environment resource. A cloud environment gives each session an isolated Linux sandbox; no Docker/Podman is required on `ruvds-xnqc6` for this managed-cloud path.
- Managed Agents API requests use beta header `managed-agents-2026-04-01`; SDK sets it automatically.

## Exact start evidence

`POST /v1/sessions` with non-empty `initial_events` creates the session and starts the agent loop in the same call. The session is created directly in `running`.

Observed lifecycle available to verification:
- `running` = actively executing;
- `idle` = waiting for input/confirmation;
- `rescheduling` = transient error/retry;
- `terminated` = ended/unrecoverable/archive.

Webhook evidence includes `session.status_run_started`, which fires when execution starts.

## GitHub resource boundary

Managed Agents can mount a GitHub repository into a session sandbox as a `github_repository` resource. The resource requires an authorization token. Anthropic states that the token is not echoed in API responses and recommends a fine-grained token with minimum required permissions.

For first E2E, KAN recommends read-only repository access if technically possible for the chosen path; result publication can remain outside the agent until a later writer-authority gate.

## Tool authority

Managed Agents permission policies distinguish automatic versus approval-gated tools. Anthropic documents `always_allow` and `always_ask`; MCP toolsets default to `always_ask`, while the built-in agent toolset defaults to `always_allow`.

Therefore first E2E must explicitly restrict enabled tools and must not inherit broad write capability merely because the runtime supports it.

## Cost boundary

Anthropic currently bills Managed Agents on:
- model tokens at normal Claude API rates;
- session runtime at `$0.08 per session-hour`, metered only while status is `running`.

Idle/rescheduling/terminated time is not billed as session runtime.

A hard per-session list-cost budget can be attached at creation. When the budget is reached, the session pauses/goes idle before further model requests.

This makes a very small bounded E2E possible with an explicit spend cap.

## Rate-limit evidence

Anthropic documents organization-level limits:
- create endpoints: 300 requests/minute;
- read/list/stream endpoints: 1200 requests/minute;
plus normal organization spend/usage-tier limits.

## Suggested first probe

`ruvds-xnqc6 → anthropic SDK → create Agent → create cloud Environment → create Session(initial_events) → record session_id/status=running → read immutable test marker → wait for idle/terminal evidence → delete/archive test resources`.

PASS evidence must include provider-generated session ID and provider-observed lifecycle. A local log line alone is insufficient.

## Official sources
- https://platform.claude.com/docs/en/managed-agents/quickstart
- https://platform.claude.com/docs/en/managed-agents/sessions
- https://platform.claude.com/docs/en/managed-agents/session-operations
- https://platform.claude.com/docs/en/managed-agents/webhooks
- https://platform.claude.com/docs/en/managed-agents/github
- https://platform.claude.com/docs/en/managed-agents/permission-policies
- https://platform.claude.com/docs/en/managed-agents/reference
- https://platform.claude.com/docs/en/about-claude/pricing

---
sender: KAN
recipient: KOO
document_type: provider-e2e-prerequisite-evidence
status: research_for_current_entity_runner_gate
provider_selected: no
production_changed: false
project_time: omitted; trusted project-time source not used