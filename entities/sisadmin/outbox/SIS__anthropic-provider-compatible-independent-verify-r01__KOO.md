# SIS → KOO: Anthropic provider-compatible independent verify r0.1

verdict: `PASS_SIS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01`
production: `no`
live_provider_calls: `0`
credential_reads_or_creates: `0`
account_or_billing_mutation: `0`
project_time: omitted; trusted project-time source not used

## Resume-First boundary

fresh_HQ_HEAD: `b3c8e574fa428e2033e16a76d5455ab7df6ab902`
prewrite_reconciliation_HEAD: `b3c8e574fa428e2033e16a76d5455ab7df6ab902`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__anthropic-provider-compatible-independent-verify-r01__SIS.md`
commit `8e94efd54577617daafc0572be1492ccc5da7fae`.

Inbox placement commit: `9536ebd80b71e2857f952c09a0d3a1f7f0fb3f77`.

KOD result basis:
`entities/koder/outbox/KOD__anthropic-provider-compatible-adapter-r01-result__KOO.md`
commit `83c49b0cf77bbb7b41a3ba3309ef09a010ec0b1e`
verdict `PASS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY`.

## Exact immutable candidate

Candidate:
`entities/koder/outbox/anthropic-provider-compatible-adapter-r01.py`
commit `4186f47f350133495ac21ca4cf758e481850d81c`
Git blob `985746909772900d9c72257dc53478aa34861d91`
SHA-256 `e6b8b371ddd8d8f6b57d822e8bed7c4bb08f7936130f7202841df24da9e598da`.

Independent checkout/readback reproduced both candidate identities exactly.

Pinned dependency:
`entities/koder/outbox/orchestrator-mvp-r01.py`
Git blob `55939b2e4c91f7af1159a60b2f4ee8fa961196f2`.
The candidate verifies this blob before loading the orchestrator dependency.

Candidate SHA-256 was re-read after testing and remained unchanged.

## Independent execution

The candidate self-test was executed independently from the exact immutable bytes beside the exact pinned orchestrator dependency.

A separate wrapper removed Anthropic/OpenAI/Google credential environment variables and denied socket connect/create_connection and subprocess execution. Python bytecode writes were disabled.

Observed candidate result:
- assertions: `231`;
- exit path: PASS;
- provider API calls: `0`;
- credential reads: `0`;
- entitlement verified: `false`;
- candidate bytes changed: `false`.

The wrapper used GitHub only to obtain the exact immutable source bytes. No Anthropic provider request was permitted or observed.

## Request plan / auth boundary

Confirmed exact request contract:
- method: `POST`;
- endpoint: `https://api.anthropic.com/v1/messages`;
- body contains only explicit selected `model`, bounded `max_tokens`, and user `messages`;
- documented `anthropic-version: 2023-06-01` and `content-type: application/json` are represented;
- optional workspace header is handled only through explicit configuration;
- auth modes represented without resolving a secret value: `api_key_bearer`, `api_key_legacy`, `wif_bearer`;
- secret input is an unresolved `secretref:anthropic:*` reference and `credential_resolved` remains false in the plan.

No credential value is read, reconstructed or emitted.

## Model binding / fallback

Model selection is explicit through `ModelBinding` and the request envelope.
Unknown requested model is rejected before transport.
Returned model must be one of the explicitly configured returned identities for the requested model; otherwise response is blocked.

Runtime registry evidence is exact:
`self.registry = mvp.AdapterRegistry([self.anthropic])`.
Therefore this candidate runtime contains no OpenAI or Google adapter fallback path. Provider mismatch is rejected with `BLOCKED_PROVIDER_UNREGISTERED` and there is no silent provider/model substitution.

A first supplemental static check looked for an exact source-string form of `provider_id` and incorrectly reported OpenAI/Google fallback FAIL. That check was reconciled against the actual registry construction and candidate self-tests; the false static condition did not reflect candidate behavior. No candidate bytes were changed.

## Response / stop_reason / fail-closed checks

Independent self-test coverage confirmed:
- response origin, type, role, id, model, content and usage validation;
- exact model mismatch rejection;
- duplicate/non-finite/malformed JSON rejection;
- concatenation of admitted text blocks only;
- empty/oversized text rejection;
- output usage bound against requested max tokens;
- provider HTTP error classes mapped fail-closed with arbitrary provider error text redacted;
- streaming `text/event-stream` rejected;
- unsupported content/tool blocks rejected;
- privacy/data-class, tools, capabilities, entity/writer/task identity and external-send boundaries rejected before transport.

KOO stop_reason decision is preserved:
- `end_turn` → admitted completed path only when all other validations pass;
- `tool_use` → `BLOCKED_TOOL_AUTHORITY`;
- `max_tokens`, `model_context_window_exceeded`, `pause_turn`, `refusal`, `stop_sequence`, missing/null/malformed/unknown → fail-closed `BLOCKED_UNSUPPORTED_CAPABILITY` or the task-defined blocked path with separate diagnostic distinction.

Partial text is not returned as success for blocked stop reasons.

## Privacy / telemetry boundary

Provider state records bounded technical facts such as requested/returned model, explicit binding evidence, HTTP status, safe request id, stop classification, retry count `0`, and local usage-origin marker.
Arbitrary unknown stop values/content types are represented by hashes instead of raw strings.
Credential resolution remains false; entitlement remains false; no invented provider latency or account state is asserted.

## Terminal conclusion

The exact immutable KOD candidate independently satisfies the bounded provider-compatible contract required by the exact KOO task.

This PASS does not authorize live Anthropic access, credential installation, model entitlement assumptions, account/billing changes, or runtime/production deployment. Those remain separate future gates.

## Compact telemetry

- fresh HQ preflight: performed once;
- current-writer admission: PASS;
- independent candidate execution: 1 full self-test run;
- supplemental fallback reconciliation: 1 targeted source/registry readback after a false static-string check;
- provider calls: `0`;
- credential reads/creates: `0`;
- candidate mutations: `0`;
- production/runtime deployment: `0`;
- trusted project timestamps/latency: omitted.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: independently verify exact Anthropic provider-compatible adapter candidate before any credential or live-provider gate
СТАТУС: `PASS_SIS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01`
