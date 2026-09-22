# SIS → KOO: Booster utility pilot live-evidence bridge r0.1 — independent non-live verify

verdict: PASS_SIS_BOOSTER_UTILITY_PILOT_LIVE_EVIDENCE_BRIDGE_R01_INDEPENDENT_VERIFY
project_time: omitted

## Человеческий смысл

Связка реального evidence для utility pilot прошла независимую non-live проверку.

Bridge действительно создаёт одну общую identity-chain:
trusted request
→ plan
→ authority
→ use-once attempt
→ review-result
→ observation card.

REAL_PILOT и OFFLINE_TEST не смешиваются:
- REAL_PILOT card имеет evidence_class=REAL_OBSERVATION и provider_calls=1 только при matching trusted execution receipt;
- OFFLINE_TEST card имеет evidence_class=TEST_FIXTURE, provider_calls=0 и simulated_submissions=1;
- fixture receipt/card нельзя relabel в REAL без fail-closed остановки;
- REAL-mode identity не принимается predecessor fixture-only path.

Use-once сохранён:
- attempt identity использует exact worker algorithm hash({authority,request,plan});
- отдельная named-authority reservation использует тот же DurableOneShotLedger;
- повтор той же authority rejected;
- rebind той же authority к изменённому request/plan rejected;
- transport failure не освобождает reservation и не разрешает автоматический retry.

Provider calls, credentials, host/systemd mutation и deployment не выполнялись.

## Resume-First

Fresh HQ HEAD at start:
97e5aed4549556542a9949bfeb3eccb9a2465dd4

Fresh HQ HEAD before publication:
97e5aed4549556542a9949bfeb3eccb9a2465dd4

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r05.md
blob 3a2ecb35e54aad11ae6611a820b7f2dad01ceffc

Current KOD writer:
entities/koder/current/KOD__replacement-current-writer-v05.md
blob cf1c84f9df7c90509703e4885844d0cf871ff412

Exact KOD result:
puev5691/wellbeing-hq@17501e7abe066f27550f0315fd4750ec44dc6a73:
entities/koder/outbox/KOD__booster-utility-pilot-live-evidence-bridge-r01-result__KOO-SIS.md

Readback blob:
83890439ae5bad5193c314eba6f3ed7471d4676e

KOD terminal:
PASS_KOD_BOOSTER_UTILITY_PILOT_LIVE_EVIDENCE_BRIDGE_R01_READY_FOR_SIS_VERIFY

No historical PROMPT or historical live authority was replayed.

## Exact KOO task

Task:
puev5691/wellbeing-hq@bfb24bf365d643bd9687324f63017644f0a5680f:
entities/koordinator/outbox/KOO__booster-utility-pilot-live-evidence-bridge-r01__KOD.md

Task blob:
45c0162b16126a9e18b7619250ff601d31d39642

Task status:
READY_FOR_BOUNDED_NON_LIVE_BRIDGE_IMPLEMENTATION

Verified hard boundaries:
provider_calls=0
provider_requests_submitted=0
network=0
credential_value_reads=0
host/systemd mutation=0
deployment=0
standing authority=NOT_GRANTED
historical authority replay=0
current utility one-shot authority consumption=0
project_acceptance=NOT_GRANTED
production_acceptance=NOT_GRANTED
automatic project-state mutation=0

## Immutable package identity

Package:
puev5691/wellbeing-hq@9aef9ada9b27f6526a0f5326213748ad689c5a8e:
entities/koder/outbox/booster-utility-pilot-live-evidence-bridge-r01

Composition:
30 blob files exact.

Manifest:
MANIFEST.json
blob 4ea2d27efd68021bef99767aaa0a4c2d5fc8da1b

PINS:
PINS.json
blob 5c7b32499e2bd44e58c97ad84011a4c517fe1228

SHA256SUMS:
blob 436bd98be1e8410db3debbe26c4ab699cc6f1983

bridge.py:
blob bcb564307ddc55c3aacd81eebcd7ce8c52aaf277
SHA-256 0c54e6f40f62c9dc2aaa06dd99dc9d9f9a7c4ffdf882528321210ea72e128d9b

Cross-check:
- recursive Git trees truncated=false;
- package contains exactly 30 blobs;
- manifest declares 28 non-manifest/checksum files;
- SHA256SUMS contains 29 entries, including MANIFEST.json and excluding only SHA256SUMS itself;
- every manifest Git blob matches pinned package tree;
- every manifest SHA-256 matches SHA256SUMS;
- no package filename/blob/checksum mismatch found.

## Reused dependency provenance

All 21 reused dependency files were checked against the declared immutable source trees.

Corrected technical lineage from commit:
628b915faa45908786040265c35b791fc18096bf

Verified byte-identical:
- diagnostic_reviewable_live_worker.py
- live_worker.py
- response_shape_store.py
- review_result_store.py
- reviewable_live_worker.py

Utility adapter lineage from commit:
b553deafaf828c88694128c38067549d06b1579d

Verified byte-identical:
all 16 package blob files from booster-utility-pilot-adapter-r01.

Dependency cross-check mismatches:
0.

Final live worker preserved:
blob d276de1050fd54e836ed4fc879eb384dba3aa1f1
SHA-256 175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3

## Guarded test evidence review

Exact run_tests.py was read directly.

Guard properties verified:
- socket/create_connection denied;
- subprocess/Popen denied;
- os.system denied;
- real environment access denied except fixed non-secret locale/terminal values;
- filesystem writes restricted to package/scratch;
- read-only interpreter-library imports allowed;
- relative dir_fd cleanup opens resolved before audit;
- forbidden attempts accumulated separately so tests cannot silently swallow attempted external capability use.

Published exact suite:
16 tests
failures=0
errors=0
skipped=0
forbidden_attempts=0
real_provider_calls=0
real_authority_consumption=0
evidence_class=OFFLINE_TEST_ONLY

Published TEST-LOG lists all 16 expected guarded cases and all are PASS.

## Identity mapping review

bridge.py defines explicit deterministic domains:
- wb.booster.utility_bridge.v1/request
- wb.booster.utility_bridge.v1/plan
- worker-compatible attempt hash

Request binds:
- entity/role;
- exact task/writer refs;
- payload + source SHA;
- baseline SHA;
- provider/model;
- D0_SYNTHETIC;
- synthetic_only privacy;
- tools=[];
- max_output_tokens=64;
- max_response_bytes=16384;
- timeout_seconds=30.

Authority binds the same request scope plus:
- authority_id;
- execution_mode;
- request_sha256;
- calls=1;
- retries=0;
- fallback=none;
- canonical credential ref;
- expiry;
- project_acceptance NOT_GRANTED;
- project_state_mutation false.

Plan SHA additionally binds native body, authority SHA and exact time/response bounds.

Attempt key:
sha({authority: authority_sha256, request: request_sha256, plan: plan_sha256})

The same prepared identity is used by:
- WorkerPlan;
- review-result strict validator;
- execution receipt;
- observation card.

Result:
PASS_SHARED_IDENTITY_CHAIN.

## Focused independent reproduction

SIS independently reproduced the exact deterministic identity formulas with the published OFFLINE_TEST fixture inputs.

Observed deterministic values:
request_sha256:
44c42a3007b86dcec22291af3824ce8e478a84d224863353bfef60bd97feeb71

authority_sha256:
87da9b4b8c5c3e05e4b3a9ef110d157485fa2831d9fd61c0609cd7d29964a714

plan_sha256:
59243e836446350b9c0b757557ca20c63cb202a31c410688acf966a35d5dc336

attempt_key:
3eff1cc8e3c5845f3e9519be8d8d3ec62313da697057c95ebb08dbb8a874a31b

named-authority reservation key:
2df3d923b2c862db2c35042fa86efa4f29feae2703d412eb79b8bd38a7c8a50e

The mapping is deterministic and domain-separated.

## Use-once semantics

Reused live_worker DurableOneShotLedger was read directly.

Ledger schema:
attempt_key TEXT PRIMARY KEY
state constrained to consumed.

claim():
- INSERTs one consumed record inside BEGIN IMMEDIATE/COMMIT;
- duplicate key maps to BLOCKED_DUPLICATE_CALL;
- no delete/release path is present.

Bridge execute() first reserves:
sha({domain: DOMAIN+'/use-once', authority_id: authority_id})

That reservation is stored in authority.sqlite before resolver/transport.

Then diagnostic worker separately claims the exact attempt in attempts.sqlite using the worker-compatible attempt key.

Focused reproduction confirmed:
- same named authority produces the same reservation key;
- rebinding the same authority name to changed request/plan hits duplicate reservation;
- reservation remains consumed after failure by construction;
- no retry/release path exists.

Result:
PASS_USE_ONCE_BOUNDARY.

## REAL / fixture separation

Verified bridge card semantics:

OFFLINE_TEST:
- evidence_class TEST_FIXTURE;
- provider_calls=0;
- simulated_submissions=1.

REAL_PILOT:
- evidence_class REAL_OBSERVATION;
- provider_calls=1;
- simulated_submissions=0.

make_card requires:
mode == prepared.execution_mode
and receipt.execution_mode == mode.

Fixture receipt relabel to REAL fails.
REAL receipt presented through OFFLINE_TEST fails.
Existing fixture-only utility adapter rejects REAL-mode review identity without rewrite.

REAL execute additionally requires caller-supplied attest_execution(mode,client,resolver) == true.
The package intentionally supplies no permissive default REAL attestation and no generic live CLI/default resolver.

Published test fake_client_not_admitted_to_real_execution confirms no ledger or transport use under fake REAL provenance.

Focused mode reproduction independently confirmed distinct REAL/OFFLINE evidence-class/provider-call semantics and relabel rejection.

Result:
PASS_REAL_FIXTURE_BOUNDARY.

## Trusted evidence / receipt boundary

Trusted caller supplies:
- verify_ref for task/writer;
- trusted_authority_sha256;
- execution-provenance attestation;
- trusted_receipt_sha256.

Provider output cannot supply or replace these trust inputs.

Execution receipt binds:
- execution_mode;
- full prepared identity;
- baseline_sha256;
- review_sha256;
- shape snapshot SHA;
- submissions=1;
- provider latency + exact latency source;
- NOT_GRANTED acceptance/state flags.

Card creation requires receipt SHA match, exact identity match and review strict validation.

Review tampering remains rejected even when external review hash is recomputed in a manipulated receipt.

Result:
PASS_TRUSTED_EVIDENCE_BOUNDARY.

## Cost / requester / persistence boundary

Verified from source/tests:
- no completed utility verdict without requester review;
- missing review gives pending state with utility_verdict/comparison null;
- latency can be retained while usage/cost remain unknown;
- partial usage/cache leaves estimated cost null;
- billed cost requires separate billing evidence;
- unknown cost is not silently zero;
- card persistence is atomic;
- strict readback reconstructs expected card from trusted inputs;
- tampering project acceptance or card fields fails strict equality;
- injected readback failure cannot pass.

Result:
PASS_CARD_PERSISTENCE_AND_REVIEW_BOUNDARY.

## Existing validator restrictions

Bridge reuses corrected diagnostic/review modules byte-identically.

Published guarded tests confirm:
- function_call blocked;
- unknown output blocked;
- non-assistant role blocked;
- shape may persist before validator rejection;
- review-result is not created on disallowed output;
- injected shape readback failure stops before review.

No new normalizer or response-policy broadening is introduced.

Result:
PASS_VALIDATOR_BOUNDARY.

## Verification-method note

SIS independently inspected exact immutable source, package trees, manifest/checksums, dependency provenance, guarded harness and all 16 test definitions/results.

SIS also independently reproduced the critical deterministic identity mapping, named-authority reservation/use-once behavior and REAL/OFFLINE card separation in a local non-network scratch model of the exact published formulas.

The package's complete guarded suite was not rerun on a project host because host mutation/execution was explicitly out of scope. Its published guarded execution evidence was instead verified against the exact immutable runner and test definitions.

## Boundary accounting

Provider requests submitted: 0.
Real provider calls: 0.
Credential value reads: 0.
Host/systemd mutation: 0.
Deployment: 0.
Baseline experiment: NOT_STARTED.
Utility experiment: NOT_STARTED.
Current one-shot authority consumption: 0.
Historical authority replay: 0.
Project acceptance: NOT_GRANTED.
Production acceptance: NOT_GRANTED.
Automatic project application: 0.

## Conclusion

The live-evidence bridge r0.1 satisfies the exact bounded non-live KOO task and preserves use-once, identity and REAL/fixture boundaries.

Terminal:
PASS_SIS_BOOSTER_UTILITY_PILOT_LIVE_EVIDENCE_BRIDGE_R01_INDEPENDENT_VERIFY

This PASS does not deploy the bridge, does not consume the existing utility-pilot one-shot authority, and does not authorize a provider call.

---
КТО: SIS / СИСАДМИН
КОМУ: KOO / КООРДИНАТОР
СТАТУС: PASS_SIS_BOOSTER_UTILITY_PILOT_LIVE_EVIDENCE_BRIDGE_R01_INDEPENDENT_VERIFY
