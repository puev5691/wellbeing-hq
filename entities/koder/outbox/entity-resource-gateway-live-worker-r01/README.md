# Entity Resource Gateway live worker r0.1

Isolated candidate for the LiveExecutorPort/live-worker boundary. It is not deployed and performed no real provider request in this cycle.

## Immutable inputs

- accepted gateway PASS: `fd49601948827cc43e46331ae98ab1f680101c0a`;
- executor-preparation independent PASS: `888e9fe64dccc2c12571b246cdf8d754e0df1214`;
- OpenAI final technical gate: `787ec5df1878c7ddb0a5f2928c61e265b40959b0`;
- Anthropic adapter independent PASS: `d92b3a9ba5abc0c4d1f03169425fb2dcb6e6cd6a`.

Accepted provider/gateway/preparation bytes are dependencies only and are not modified by this package.

## Boundary

`bind_prepared(prepared, admission, now_tick=...)` accepts the already prepared execution object only when:
- preparation remains `live_enabled=false`;
- admission mode is exactly `LIVE`;
- request, plan and requester hashes match the preparation;
- admission has not expired.

It returns a `WorkerPlan` bound to provider/model/native request plan, credential reference and one-call policy.

`LiveWorker.invoke_once(plan, now_tick=...)` then:
1. validates provider/model/endpoint/native plan before any credential resolution;
2. atomically consumes the authority/request/plan key in a durable SQLite ledger;
3. resolves only a typed `secretref:<provider>:<slot>`;
4. performs exactly one HTTP-client call under a hard POSIX deadline;
5. rejects redirects, oversized responses and response-model mismatch;
6. returns a redacted `WorkerReply` with `project_acceptance=NOT_GRANTED`, unchanged caller writer and no project-state application.

The candidate also supplies `enforce_resource_result_boundary()` for the accepted gateway `ResourceResult`: NOT_GRANTED, unchanged caller writer, no gateway/provider writer authority, no project-state application, no external dispatch, routing not started.

## Durable one-shot ledger

`DurableOneShotLedger` uses SQLite with:
- primary-key uniqueness on the attempt key;
- `BEGIN IMMEDIATE` around reservation;
- `journal_mode=WAL`;
- `synchronous=FULL`;
- reservation committed before credential resolution or transport.

A successful attempt, provider error, resolver error, timeout or other ambiguous outcome does not restore the consumed key. Reopening the same SQLite file after process restart preserves the consumed key. The tests also race two threads against the same key and allow only one claim.

Durability here is the SQLite/local-filesystem contract. Correct file ownership, disk/fs durability, backup and deployment location remain operational responsibilities for a future runtime task.

## Timeout and response bound

`HardDeadline` uses POSIX `signal.setitimer` and therefore fails closed outside the main thread or where that primitive is unavailable. The worker additionally passes the same timeout to its HTTP client.

`BoundedUrllibClient` reads at most `max_response_bytes + 1`, rejects an oversized body, and installs a redirect handler that never follows redirects. Any 3xx result is rejected.

No retry loop exists. `WorkerPolicy` requires max_calls=1 and automatic_retries=0.

## Credential boundary

The candidate defines only a `CredentialResolver` interface. The worker receives a `SecretRef`, never a raw secret in the plan. The resolved value is passed directly into the request header and is excluded from `WorkerReply.redacted()`, repr fields and project files.

No real resolver implementation, key file, environment lookup, terminal prompt or credential was used in this cycle.

## Provider binding

OpenAI:
- endpoint exactly `https://api.openai.com/v1/responses`;
- POST;
- content-type JSON;
- model in the native plan must equal WorkerPlan.model;
- authorization is absent from the persisted plan and attached only after resolution.

Anthropic:
- endpoint exactly `https://api.anthropic.com/v1/messages`;
- POST;
- `anthropic-version: 2023-06-01`;
- model must match;
- authorization is attached only after resolution.

The package does not alter the accepted OpenAI/Anthropic adapters and does not add fallback or model substitution.

## Tests

Command used on UID 1000:

`python3 -I -B test_live_worker.py`

Result: 27 methods, failures 0, errors 0, skipped 0.

Covered:
- OpenAI/Anthropic synthetic success paths;
- SQLite restart-safe duplicate prevention;
- competing atomic claims;
- hard timeout;
- response-byte bound;
- redirect rejection;
- model mismatch;
- stale authority;
- endpoint/model binding;
- secret-reference boundary and redaction;
- zero automatic retries;
- exact prepared/admission attachment;
- ResourceResult authority guard;
- zero-network synthetic execution.

The first run exposed only a missing `asdict` import in two test methods. Candidate code was not modified; only the test import was corrected and the entire suite was rerun successfully.

## Not authorized / not performed

- no real provider call;
- no real credential read/create;
- no billing/account mutation;
- no production deployment;
- no Telegram/TERA2/WBN;
- no accepted gateway/executor-prep/provider byte modification;
- no project acceptance or state application.

Independent verification is required before any live attachment or deployment.
