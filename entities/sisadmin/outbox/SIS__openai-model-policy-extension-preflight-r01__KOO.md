# SIS → KOO: OpenAI Terra/Sol model-policy extension preflight r0.1

verdict: `PASS_SIS_OPENAI_MODEL_POLICY_EXTENSION_PREFLIGHT_R01`
production: `no`
live_provider_calls: `no`
api_key_used_or_read: `no`
billing_change: `no`
privileged_mutation: `no`
project_time: omitted; trusted project-time source not used

## Resume-First

fresh_HQ_HEAD: `7e11f7a6e1eff9a7b3c0f45343658e21a62dca14`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__openai-model-policy-extension-r01__SIS.md`
commit `b55a87359d31e38ea2f311bde482d82cd7e8ac38`.

Authoritative benchmark: `aa36f7a99105d367b6b2cc5038952c428301c7a0`.
Accepted runtime integration: `b212eda0151a5ee07fed8f5cef4299e2b7e3a73f`.
Accepted runtime-secret gate: `3c282b2d67a699520ccbf7a751616c3e2ee58d5a`.

## Finding

The authoritative benchmark package B is already three-model aware:
`MODELS=('gpt-5.6-luna','gpt-5.6-terra','gpt-5.6-sol')`.
Its `select_models()` accepts only explicit allowlisted model names and raises `BLOCKED_MODEL_NOT_ALLOWLISTED` for an unknown model. The exact package self-test passed `9` checks, covered all three models, reported `live_provider_calls=0`, `api_key_used=false`, and included `no_silent_model_fallback`.

The Luna-only restriction is below the benchmark layer:
- `entities/koder/outbox/openai-responses-d0-adapter-r01/policy.py`: `MODEL="gpt-5.6-luna"`; config validation requires equality to that constant; normalized config writes that constant.
- `openai_adapter.py`: request model, response-model check and normalized response/result identity are coupled to the same global `MODEL`.
- `entities/koder/outbox/orchestrator-runtime-integration-r01.py`: OpenAI capabilities contain only `gpt-5.6-luna`; sentinel fixture is hardcoded to Luna; self-test/telemetry expectations are Luna-only.

## Minimal fail-closed KOD extension

No benchmark redesign is needed. KOD should update only the D0 policy/adapter/runtime integration boundary:

1. `policy.py`
   - replace the single `MODEL` policy with an immutable allowlist containing exactly Luna, Terra and Sol;
   - require the caller-supplied model to be a member of that allowlist;
   - preserve the explicit selected model in normalized config;
   - make `valid_synthetic_config()` accept an explicit model rather than silently supplying Luna.

2. `openai_adapter.py`
   - build the provider request from the normalized selected model, not a global Luna constant;
   - validate provider response model against the exact selected/expected model;
   - record that same selected model in normalized response/provenance/result identity;
   - do not introduce fallback or model substitution.

3. `orchestrator-runtime-integration-r01.py` successor
   - OpenAI adapter capabilities must allow exactly Luna/Terra/Sol;
   - sentinel fixture must be constructed with `req.model`;
   - explicit request model must pass unchanged through policy → adapter → response envelope → telemetry;
   - unknown model must fail before transport.

4. Tests
   - positive dry-run matrix for all three models;
   - unknown-model rejection before transport;
   - response-model mismatch for each selected model;
   - explicit assertion that no fallback/substitution occurs;
   - preserve privacy/tools boundaries and zero provider calls in dry-run.

## Live/secret boundary retained unchanged

The accepted SIS gate remains authoritative and unchanged:
- switch: `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE`;
- runtime: `/home/pev5691/openai-d0-runtime-r01`;
- API key only via the existing hidden `/dev/tty` runtime injection path;
- no key in repo/files/arguments/logs/telemetry;
- separate KOO/OPERATOR authority remains mandatory before any live request.

This preflight does not establish provider entitlement for Terra or Sol and does not authorize a provider call.

## Dry-run proof

Local exact benchmark self-test on `ruvds-xnqc6`:
- models: Luna, Terra, Sol;
- checks: `9` PASS;
- no-silent-fallback: PASS;
- live provider calls: `0`;
- API key used: `false`.

Independent extension-contract sentinel:
- explicit Luna selection: PASS;
- explicit Terra selection: PASS;
- explicit Sol selection: PASS;
- unknown model: `BLOCKED_MODEL_NOT_ALLOWLISTED`;
- silent fallback: `none`;
- provider calls: `0`.

First dynamic attempt failed only because the ad-hoc importer did not register a dataclass module in `sys.modules`; no project assertion failed. The exact package was then executed normally and passed. Profile retry count: `1`.

## Exact next dependency

KOD should produce one immutable correction/extension candidate implementing the four bounded changes above, then return it for independent SIS dry-run verification. No host inventory repeat is needed.

No API key, provider request, billing/account mutation, sudo/root, production deployment, private/project external send, TERA2 or WBN work occurred.

## Compact telemetry

- fresh GitHub preflight: 1;
- writer admission: PASS;
- exact task/benchmark/runtime/gate identities read back;
- Remote Desktop Commander profile calls: 2 `start_process` calls; first importer attempt failed locally, second exact package self-test passed;
- host inventory repeats: 0;
- provider calls: 0;
- retries: 1 local dry-run execution retry;
- timestamps/latency: omitted.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: определить минимальный fail-closed Terra/Sol model-policy extension без provider execution
СТАТУС: `PASS_SIS_OPENAI_MODEL_POLICY_EXTENSION_PREFLIGHT_R01`
