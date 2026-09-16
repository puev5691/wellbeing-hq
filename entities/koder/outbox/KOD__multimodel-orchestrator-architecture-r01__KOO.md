# KOD → KOO: multi-model orchestrator architecture r0.1

status: `PASS_MULTIMODEL_ORCHESTRATOR_ARCH_R01_READY_FOR_REVIEW`
production: `no`
live_provider_calls: `no`
credentials: `no`
private_project_data_external_send: `no`
silent_fallback: `no`
tera2_wbn: `PARKED_BACKGROUND`
project_time: omitted; trusted project-time source not used

## Exact task / admission

Exact task:
`entities/koordinator/outbox/KOO__multimodel-orchestrator-architecture-r01__KOD.md`
commit `0e8af1f56e1355d7a04fe7412ed99582b1053bd6`
blob `7374ef08830b944b18b8aa5b8f102f1a92dcfe72`.

Fresh HQ preflight:
`b104b1caa70ff876b508462530dffb956b4fa3b7`.

Current KOD writer boundary verified:
`entities/koder/current/KOD__replacement-current-writer-v02.md`
blob `23f20f04504c65497c154c099d8090cde11fba83`.
Admission: `PASS_CURRENT_KOD_WRITER`.

Accepted OpenAI basis:
`entities/koder/outbox/KOD__openai-responses-d0-adapter-r01-result__KOO.md`
commit `e053746c55f7c8317069ac0bc60f7dcbc5fe66ac`
blob `05f34f809db22d8a7f5b5f7b12b8281cac6f99b0`
verdict `PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE`.

Design input, not canon:
`entities/koordinator/outbox/KOO__execution-observability-notes-r01__OPERATOR.md`
blob `213bebf034c0a23c08aad10df5f4531631e89513`.

## 1. Architecture boundary

The candidate is a provider-neutral orchestration layer above provider adapters. It does not replace canonical project state in files/GitHub and it does not allow a provider response to become project authority by itself.

Layering:

1. `TaskAdmission` — verifies Entity/current-writer/task identity before profile execution.
2. `RequestNormalizer` — converts a project task into the common request envelope.
3. `RoutingPolicy` — evaluates allowed providers/models against task class, declared capabilities, cost evidence, observed latency and privacy boundary.
4. `ProviderAdapter` — maps the neutral envelope to one provider contract.
5. `ToolBoundary` — mediates tools; provider output can request a tool but never execute one directly.
6. `RunState` — owns orchestration lifecycle, terminal detection, retries and telemetry.
7. `RoutingState` — separately owns artifact/dispatch/receipt completion.
8. `OperatorResult` — emits compact terminal status + immutable locator + next gate/blocker.

Provider state is transient adapter state. Project state remains external/canonical and is not silently copied into provider state.

## 2. Common request envelope

Machine contract candidate:

```json
{
  "schema": "wellbeing.orchestrator.request.v1",
  "run_id": "opaque-run-id",
  "entity": "KOD",
  "task_identity": {
    "path": "entities/...",
    "commit": "git-sha",
    "blob": "git-blob-or-null"
  },
  "task_class": "architecture|coding|research|review|routing|other",
  "input": {
    "content": "bounded task payload",
    "data_class": "synthetic|public|project_internal|sensitive",
    "external_send_allowed": false
  },
  "reasoning": {
    "recommended": "MEDIUM|HIGH|XHIGH|UNSPECIFIED",
    "provider_native": null
  },
  "capabilities_required": ["text"],
  "tools": {
    "allowed": [],
    "mode": "none"
  },
  "routing": {
    "provider_allowlist": ["openai"],
    "model_allowlist": [],
    "cost_ceiling": null,
    "latency_class": "interactive|batch|unspecified",
    "fallback": "explicit_only"
  },
  "secret_refs": [],
  "terminal_contract": {
    "success": ["PASS_*"],
    "blocked": ["BLOCKED_*"],
    "failure": ["FAIL_*"]
  }
}
```

Rules:
- provider/model are never changed silently;
- `project_internal` or `sensitive` input is rejected for external providers unless an explicit task authority marks `external_send_allowed=true` for that exact bounded payload;
- `tools.mode=none` means adapters must send no tool definitions and must reject provider tool calls;
- secret values never enter the envelope, repository, logs or telemetry; only opaque `secret_refs` may exist.

## 3. Common response envelope

```json
{
  "schema": "wellbeing.orchestrator.response.v1",
  "run_id": "opaque-run-id",
  "provider": "openai|anthropic|google",
  "model": "provider-model-id",
  "provider_request_id": null,
  "status": "completed|blocked|failed|tool_request",
  "output": [{"type":"text","text":"..."}],
  "usage": {
    "input_tokens": null,
    "output_tokens": null,
    "total_tokens": null,
    "provider_details": {}
  },
  "reasoning": {
    "requested": "HIGH",
    "provider_native": null,
    "applied": "supported|omitted_unsupported|rejected"
  },
  "tool_calls": [],
  "retryable": false,
  "provider_state": {},
  "evidence_strength": "provider_output_candidate_only"
}
```

Missing usage/provider detail remains `null`/absent. Normalization must not invent token counts, latency or reasoning metadata.

## 4. ProviderAdapter interface

```text
ProviderAdapter
  provider_id() -> str
  capability_snapshot() -> ProviderCapabilities
  validate(request) -> PASS | BLOCKED_*
  map_request(request, provider_config) -> provider_request
  invoke(provider_request, secret_handle) -> provider_raw_response
  normalize(provider_raw_response) -> common_response
  classify_error(error) -> retryable/nonretryable + exact class
```

`invoke` exists as an interface only in this architecture task. Live provider calls are disabled.

Provider capabilities are explicit data, not assumptions. A route is eligible only if all required capabilities are declared supported for the selected adapter/model snapshot.

## 5. OpenAI adapter integration

Status: `implemented_basis_accepted / orchestrator_wrapper_candidate`.

Use the accepted immutable Responses D0 package without modifying its live gate:
- transport: `POST https://api.openai.com/v1/responses`;
- accepted D0 model boundary: `gpt-5.6-luna`;
- credential reference: runtime `OPENAI_API_KEY` only;
- accepted request boundary: text input, bounded output, `store=false`, `tools=[]`, `tool_choice=none`, `parallel_tool_calls=false`;
- accepted response/usage normalization remains authoritative for this adapter basis.

The orchestrator adds run/task/entity/routing telemetry around the adapter. It does not weaken the accepted D0 policy and does not enable live execution.

Reasoning mapping: common `reasoning.recommended` is retained in orchestration metadata. It is passed to OpenAI only after a future provider/model contract explicitly confirms a supported native mapping. Otherwise `provider_native=null` and `applied=omitted_unsupported`; no guessed parameter is sent.

## 6. Anthropic adapter contract candidate

Status: `interface_candidate_from_current_official_docs / no_live_call`.

Current official evidence locators used:
- `https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview`
- `https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables`
- `https://docs.anthropic.com/en/docs/about-claude/pricing`

Verified architecture facts:
- Messages transport uses `POST https://api.anthropic.com/v1/messages`;
- normal API examples use `x-api-key`, `anthropic-version` and JSON content;
- client tool declarations are supplied in `tools`; model tool requests are structured `tool_use` blocks and results return as `tool_result` blocks;
- response usage exposes at least input/output token accounting, with additional cache/server-tool fields where applicable;
- current Claude guidance supports provider-native thinking/effort controls on supported current models, but exact support depends on model/version.

Candidate mapping:
- provider model ID is runtime configuration, not hardcoded here;
- common text input maps to Messages `messages` content;
- `tools.mode=none` maps to no tools and explicit no-tool policy; provider tool output when tools are disabled is fail-closed;
- common reasoning metadata maps only when the selected current model contract supports the documented thinking/effort mechanism;
- price is not hardcoded. Estimated cost requires a separately versioned price catalog/evidence snapshot.

No API key value, current model default, price or unsupported capability is guessed.

## 7. Google adapter contract candidate

Status: `interface_candidate_from_current_official_docs / no_live_call`.

Current official evidence locators used:
- `https://ai.google.dev/api/generate-content`
- `https://ai.google.dev/gemini-api/docs/generate-content/function-calling`
- `https://ai.google.dev/gemini-api/docs/thinking`
- `https://ai.google.dev/gemini-api/docs/openai`

Verified architecture facts:
- `models.generateContent` uses `POST https://generativelanguage.googleapis.com/v1beta/{model=models/*}:generateContent`;
- request carries `contents`; optional `tools`/`toolConfig` expose function calling and code execution capabilities;
- function calls expose structured name/args and may expose an id used to match function responses;
- response exposes `usageMetadata`, `modelVersion` and `responseId` where supplied;
- Gemini thinking controls vary by model family; current docs expose thinking levels/budgets and an official mapping from OpenAI-style reasoning effort for supported models.

Candidate mapping:
- provider model ID is runtime configuration, not hardcoded here;
- neutral text input maps to `contents`;
- tools are omitted unless explicit project authority allows specific tool schemas;
- thought/signature/provider-state artifacts remain provider state and are not project authority;
- common reasoning recommendation maps through an adapter capability table populated from a pinned current model snapshot; unsupported mapping is omitted, never guessed;
- price is not hardcoded. Estimated cost requires a separately versioned price catalog/evidence snapshot.

## 8. Routing policy

Eligibility is fail-closed. Routing evaluates in this order:

1. instance/task admission;
2. privacy boundary;
3. explicit provider/model allowlist;
4. required capability coverage;
5. tool boundary compatibility;
6. reasoning-effort compatibility if mandatory;
7. cost ceiling using only pinned/current cost evidence;
8. latency preference using observed comparable telemetry, never guessed provider speed;
9. deterministic tie-break by configured provider priority.

Routing input factors:
- `task_class`;
- required capability set;
- price evidence snapshot and cost ceiling;
- measured latency aggregates by comparable task class/model;
- data classification/privacy authority;
- explicit provider/model availability and health.

If selected provider/model fails, the orchestrator returns `BLOCKED_PROVIDER_OR_MODEL_UNAVAILABLE` or another exact class. It does not silently move to another provider/model. Any retry on a different provider/model requires an explicit new routing decision recorded in run state.

## 9. Reasoning-effort policy

Common advisory levels:
- `MEDIUM`: normal profile work;
- `HIGH`: architecture/debugging/reconciliation;
- `XHIGH`: rare critical recovery/audit;
- `UNSPECIFIED`: no policy request.

The common level is project metadata, not a promise that a provider accepts the same enum.

Adapter mapping returns one of:
- `supported(native_value)`;
- `omitted_unsupported`;
- `rejected_required_but_unsupported`.

If task metadata marks reasoning level mandatory and the provider/model cannot express the required policy, the route is ineligible rather than silently degrading effort.

## 10. Tool-use capability boundary

Tool use is a separate authority gate from provider selection.

- Provider model may propose a tool call only if the exact tool schema is in `tools.allowed`.
- Provider never executes project tools directly.
- Orchestrator validates tool name, arguments, entity authority, privacy and mutation class before invocation.
- Tool result returns to the provider only if the task permits external transmission of that result.
- `computer`, `shell`, web/search, files, GitHub writes, connected apps and production mutations are distinct capability flags.
- A provider's built-in/server-side tool is disabled unless the task explicitly allows that exact external capability.
- Tool denial is terminal or returns a structured `BLOCKED_TOOL_AUTHORITY`, never an automatic fallback.

## 11. Secret injection contract

Repository/config stores only:

```json
{"provider":"anthropic","secret_ref":"runtime://anthropic/default"}
```

Runtime secret resolver:
1. resolves `secret_ref` only at invoke boundary;
2. returns an opaque handle/value directly to adapter transport;
3. never serializes secret into request envelope, provider state, orchestration state, telemetry, logs, artifacts or exceptions;
4. redacts known auth headers on failures;
5. destroys/forgets runtime reference after invocation scope.

The accepted OpenAI adapter retains its existing `OPENAI_API_KEY` boundary. Anthropic official examples support `ANTHROPIC_API_KEY`; other provider secret names are runtime configuration and are not guessed here.

## 12. Orchestration state vs provider state

Orchestration state, externally persistable:

```json
{
  "run_id":"...",
  "entity":"KOD",
  "task_identity":{},
  "selected_route":{"provider":"openai","model":"..."},
  "cycle_state":"ADMITTED|RUNNING|TERMINAL|ROUTING",
  "terminal_status":null,
  "result_locator":null,
  "routing_status":"not_started|dispatched|receipt_pending|routing_complete"
}
```

Provider state, ephemeral/provider-specific:
- provider request/response ids;
- provider conversation/thread/session handles;
- thought signatures or provider-specific continuation metadata;
- raw provider error details after redaction.

Provider state must never overwrite task identity, current-writer state, canonical project status, acceptance or routing receipt.

## 13. Execution-cycle / terminal detection

State machine:

`QUEUED → ADMISSION → RUNNING → TERMINAL_RESULT → ROUTING → ROUTING_COMPLETE`

Terminal execution statuses:
- `PASS_*`
- `BLOCKED_*`
- `FAIL_*`

A task leaves execution WIP when a terminal result exists. Routing may remain open afterward.

`TERMINAL_RESULT` is not equal to `ROUTING_COMPLETE`.

Routing complete requires the current project Exchange Gate conditions, including addressable artifact, dispatch/locator/registry evidence and required receipt semantics. Receipt itself is not substantive acceptance.

With `WIP_LIMIT_2`, only execution cycles in pre-terminal states consume execution slots; background/retired-instance research is not promoted into a profile WIP slot unless explicitly tasked.

## 14. Telemetry contract

Per run, record only actually available values:

```json
{
  "run_id":"...",
  "entity":"KOD",
  "task_identity":{},
  "surface":"chat|api|worker",
  "provider":"openai",
  "model":"...",
  "reasoning_effort":"HIGH",
  "lifecycle":{
    "dispatch_at":null,
    "activation_at":null,
    "first_work_at":null,
    "terminal_result_at":null,
    "routing_complete_at":null
  },
  "latency":{
    "queue":null,
    "startup":null,
    "execution":null,
    "routing":null,
    "wall":null
  },
  "usage":{"input_tokens":null,"output_tokens":null,"total_tokens":null},
  "estimated_cost":null,
  "tool_calls":0,
  "github_reads":0,
  "github_writes":0,
  "retries":0,
  "reconciliations":0,
  "operator_rewakes":0,
  "terminal_status":null,
  "routing_status":null
}
```

Latency is derived only when both corresponding event timestamps are real evidence. Estimated cost is emitted only when usage plus a pinned applicable price snapshot are available; otherwise it is `null`.

## 15. Compact operator result

```text
STATUS: PASS_* | BLOCKED_* | FAIL_*
TASK: <short task identity>
ROUTE: <provider/model or none>
RESULT: <one-line result>
ARTIFACT: <immutable locator>
ROUTING: complete | receipt_pending | blocked
NEXT: <single gate/action or stop>
```

No evidence dump is required in chat when the artifact contains full detail.

## 16. Static contract verification

Required task surfaces checked against this artifact:

1. neutral request envelope — PASS
2. neutral response envelope — PASS
3. adapter interface — PASS
4. accepted OpenAI adapter integration — PASS
5. Anthropic current-official-doc contract — PASS
6. Google current-official-doc contract — PASS
7. task/capability/cost/latency/privacy routing — PASS
8. reasoning metadata mapping — PASS
9. no silent provider/model fallback — PASS
10. tool-use authority boundary — PASS
11. secret injection contract — PASS
12. telemetry fields — PASS
13. orchestration/provider state separation — PASS
14. terminal-cycle detection — PASS
15. terminal vs routing-complete distinction — PASS
16. compact operator result — PASS
17. no live calls/credentials/billing/deploy/external private send — PASS
18. TERA2/WBN parked — PASS

Static architecture matrix: `18/18 PASS`.

## 17. Verified provider facts vs project choices

Verified provider facts are limited to the current official source locators stated in sections 5–7 and the accepted immutable OpenAI D0 result. Everything else in this document that defines neutral envelopes, routing order, WIP behavior, fallback semantics, secret references and telemetry normalization is a Project WELLBEING candidate architecture choice, not a provider claim.

No provider API call was made. No provider key was requested/read. No billing or production state changed. No project/private payload was sent to a provider.

## 18. FAST_PATH telemetry

Confirmed values only:
- execution mode: `FAST_PATH`;
- initial preflight: `1`;
- prewrite reconciliation: `1`;
- provider-doc search batches: `2`;
- retries: `0`;
- reconciliations: `1` (prewrite HEAD unchanged);
- operator re-wakes after activation: `0`;
- latency events: not asserted; no trusted execution timestamp instrumentation was used;
- exact aggregate tool-call count: not asserted because tool discovery/search surfaces do not expose one canonical counter in this run.

FAST_PATH target was exceeded in tool calls because the task explicitly required current official evidence for two external providers plus immutable project-state reads and Exchange Gate publication. No adjacent defects were investigated or repaired.

## Verdict

`PASS_MULTIMODEL_ORCHESTRATOR_ARCH_R01_READY_FOR_REVIEW`

This PASS means architecture candidate readiness for KOO review only. It grants no live-provider, credential, billing, tool, deployment or external-data-send authority.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: materialize provider-neutral OpenAI-first orchestrator architecture with current Anthropic/Google compatibility contracts
СТАТУС: `PASS_MULTIMODEL_ORCHESTRATOR_ARCH_R01_READY_FOR_REVIEW`
