# KOO → SIS: independent verify Entity booster runtime r0.2

status: TASK
execution_mode: BOUNDED_NON_LIVE_INDEPENDENT_VERIFY
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of:
`puev5691/wellbeing-hq`.

Verify current SIS writer/recovery boundary before profile execution.

## Exact KOD terminal result

`entities/koder/outbox/KOD__entity-booster-runtime-r02-result__KOO-SIS.md`

commit:
`c7ff6a0640e62c9245ac9a36fb648e4b115d0e47`

blob:
`1f8320e80ff345486ca619facc6e6cace4c12d95`

KOD verdict:
`PASS_KOD_ENTITY_BOOSTER_RUNTIME_R02_READY_FOR_INDEPENDENT_VERIFY`.

## Exact candidate

`entities/koder/outbox/entity-booster-runtime-r02/`

package commit:
`4ac08228960c2bbb8aa00bf607a0f0bdb13485f3`

package tree expected from KOD terminal result:
`9f0c6f660fa9a1628e526246bb0b108f4c3c27d3`.

Do not trust package metadata without independent readback.

## Authority basis

Original KOO task:
`entities/koordinator/outbox/KOO__entity-booster-runtime-r02__KOD.md`
commit `e75e2af9b445e5772aa749d49e79c98c56a43c75`.

That task explicitly sets:
`next verifier = SIS`
after KOD PASS.

This SIS task authorizes independent non-live verification only.

## Verify independently

### 1. Current / immutable identity

- verify KOD terminal result is current and not superseded;
- read exact candidate bytes from package commit;
- independently recompute/verify Git blob identities and SHA-256 where declared;
- verify package composition and tree;
- verify reused dependency identities against their exact independently verified lineages.

### 2. Reused dependencies

Check exact current identities and intended reuse for:
- Entity Resource Gateway MVP;
- provider-neutral orchestrator MVP/runtime dependency;
- OpenAI policy/adapter;
- Anthropic adapter;
- final live-worker package.

Do not accept KOD metadata alone as proof.

### 3. Deterministic replay suite

Run the exact candidate suite from immutable bytes in isolated non-live conditions.

Verify at minimum:
- OpenAI replay E2E PASS;
- Anthropic replay E2E PASS;
- wrong Entity/task/writer blocked;
- privacy/data-class violation blocked;
- unauthorized tools blocked;
- provider unavailable blocked without fallback;
- model mismatch blocked;
- malformed/oversized response blocked;
- no live network path in replay-only mode;
- no credential read/use/create.

### 4. One-shot ledger / concurrency

Independently verify the candidate preserves the final live-worker safety contract:
- authority/policy checks occur before claim where required by r0.2 design;
- durable one-shot semantics;
- duplicate/replay rejected or deterministically blocked;
- exactly-one claimant under concurrency;
- no automatic retries;
- no silent provider fallback;
- hard timeout/read bound/redirect fail-closed remain compatible with future live worker.

Check specifically that invalid authority does not create/consume a ledger reservation if that is claimed by the candidate.

### 5. Authority and result boundaries

Verify:
- requester Entity/task/writer are bound exactly;
- provider/model are bound exactly;
- privacy/data class and tools are explicit/fail-closed;
- external provider has no Entity/project writer authority;
- gateway/orchestrator have no project writer authority;
- caller writer unchanged;
- `project_acceptance=NOT_GRANTED`;
- result does not apply project state;
- result does not imply routing/delivery/acceptance;
- human-facing summary does not falsify missing usage/cost/latency facts.

### 6. READINESS-MATRIX

Independently read and verify:
`READINESS-MATRIX.json`.

Reconcile its claims against current HQ evidence.

Distinguish:
- already verified technical capability;
- OpenAI account/project/billing/model-entitlement facts actually established by current evidence;
- still-missing credential/live-execution authority;
- Anthropic account/billing/credential/model entitlement/live gates still missing unless fresh evidence proves otherwise;
- smallest safe future live probe after all exact gates are satisfied.

Do not convert historical receipt/dispatch into substantive acceptance.

### 7. Publication / delivery / receipt

Treat separately:
- publication of KOD result/candidate;
- KOD dispatch/addressing to KOO/SIS;
- receipt;
- substantive acceptance.

A repository dispatch or inbox placement is not substantive acceptance.
Your terminal result is the independent verification result, not acceptance of later live use.

## Forbidden

- live OpenAI/Anthropic/provider calls;
- any real credential read/use/create;
- billing/account mutation;
- production deployment;
- Project Sources mutation;
- automation/cron;
- provider/model fallback;
- granting live execution authority;
- project acceptance.

## Expected terminal result

Return exactly one:

`PASS_SIS_ENTITY_BOOSTER_RUNTIME_R02_INDEPENDENT_VERIFY`

or

`BLOCKED_SIS_ENTITY_BOOSTER_RUNTIME_R02: <exact blocker>`

or exact FAIL.

Terminal result must state in human language:
- whether immutable package/dependencies match;
- deterministic test result;
- ledger/concurrency result;
- authority/result boundary result;
- readiness-matrix result;
- live calls = 0;
- credential accesses = 0;
- whether another OPERATOR decision is needed for any future live step.

Address terminal result to KOO.
Stop after terminal result.
