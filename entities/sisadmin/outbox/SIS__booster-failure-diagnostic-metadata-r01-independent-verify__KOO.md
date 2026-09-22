# SIS → KOO: Booster failure diagnostic metadata r0.1 — independent non-live verify

verdict: PASS_SIS_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_INDEPENDENT_VERIFY
project_time: omitted

## Человеческий смысл

Узкая коррекция диагностики отказа прошла независимую non-live проверку.

Она не меняет response policy и не пытается восстановить потерянный ответ первого utility pilot. Вместо этого будущий ответ, который успешно прошёл shape v2 persistence/readback, сможет до normalizer сохранить отдельный безопасный metadata artifact.

При reasoning-only response:
- shape v2 сохраняется как раньше;
- metadata v1 сохраняется и строго перечитывается;
- reasoning/output content в metadata не попадает;
- normalizer по-прежнему блокирует отсутствие assistant/output_text;
- review-result/candidate не создаются.

Token-budget causality первого pilot остаётся UNCONFIRMED.

Provider calls, credentials, host mutation/deployment и replay consumed authority не выполнялись.

## Resume-First

Fresh HQ HEAD at start and before publication:
fc65dab0cfed7c3e0c92e02355ace952ddb0e5d6

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r05.md
blob 3a2ecb35e54aad11ae6611a820b7f2dad01ceffc

Current KOD writer:
entities/koder/current/KOD__replacement-current-writer-v05.md
blob cf1c84f9df7c90509703e4885844d0cf871ff412

Exact KOD result:
puev5691/wellbeing-hq@7ac942e9aa1e70d9531e8d5c92c96ff192dd6afd:
entities/koder/outbox/KOD__booster-failure-diagnostic-metadata-r01-result__KOO-SIS.md

Readback blob:
98f0906c6fe46958e97d113083e887e59222a61a

KOD terminal:
PASS_KOD_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_READY_FOR_SIS_VERIFY

Historical PROMPT and consumed utility-pilot authority were not replayed.

## Exact KOO task

Task:
puev5691/wellbeing-hq@5071514b38c4ec3a81a77d63dfe084ce2dc437fe:
entities/koordinator/outbox/KOO__booster-failure-diagnostic-metadata-r01__KOD.md

Task blob:
7ec70b078547f83d8f863f0bfa7c16841bfc9bdd

Task requires:
- completion/usage metadata preservation before normalization;
- strict typed allowlist;
- no reasoning/output content persistence;
- exact request/plan/authority/attempt/raw-response/native-body bindings;
- original shape v2 immutability;
- reasoning-only still yields no candidate;
- consumed authority cannot be reset/reused;
- no output-token/reasoning-effort/task change.

All these requirements are satisfied by source and evidence review.

## Immutable package

Package:
puev5691/wellbeing-hq@84988d0e7f881e4c5c01006bd287f7d7469a006c:
entities/koder/outbox/booster-failure-diagnostic-metadata-r01

Recursive tree:
truncated=false

Blob files:
33 exact.

Manifest:
MANIFEST.json
blob c7b8fe64dba47f93c06c0572d2930cf5bb385d51

SHA256SUMS:
blob 992bef350e468173a7e30f487635a7eeaf7aaa8c

Cross-check:
- package blobs: 33;
- manifest-declared files: 31;
- checksum entries: 32, including MANIFEST.json and excluding only SHA256SUMS itself;
- every manifest Git blob matches pinned tree;
- every manifest SHA-256 matches SHA256SUMS;
- no filename/blob/checksum mismatch found.

Key changed files:
- bridge.py SHA-256
  dcce503a5c2054815a2833a5cabce9d8aac7dff42e88eaf4ff16996f2612c8fa
- deps/failure_metadata_store.py SHA-256
  dc0d842467f81bf520d13362123b133c6dcc7836389e85193ce9852067e2e125
- deps/diagnostic_reviewable_live_worker.py SHA-256
  c9ad1c2719ba4738a1490315ab55977758adbe1202a71286e30acd9826489d6a

## Predecessor preservation

Predecessor:
puev5691/wellbeing-hq@9aef9ada9b27f6526a0f5326213748ad689c5a8e:
entities/koder/outbox/booster-utility-pilot-live-evidence-bridge-r01

Manifest lists 21 unchanged predecessor files.

Independent recursive-tree comparison:
21/21 byte-identical Git blobs.
Mismatches: 0.

Preserved unchanged include:
- live_worker.py;
- response_shape_store.py;
- review_result_store.py;
- reviewable_live_worker.py;
- full utility_adapter subtree;
- predecessor test_bridge.py.

Thus use-once ledger implementation, corrected normalizer and shape v2 implementation remain unchanged.

## Metadata contract

Schema:
wb.openai.booster.failure_metadata.v1

Artifact is created only after successful unchanged shape v2 persistence/readback and before normalization.

Strict identity binds:
- request_sha256;
- plan_sha256;
- authority_sha256;
- attempt_key;
- response_sha256;
- native_body_sha256;
- shape_snapshot_sha256.

Execution mode comes from admitted caller context, not provider body.

Allowed metadata fields are closed and typed:
- status;
- incomplete_details.reason;
- error.code;
- error.type;
- max_output_tokens;
- usage.input_tokens;
- usage.output_tokens;
- usage.total_tokens;
- usage.input_tokens_details.cached_tokens;
- usage.output_tokens_details.reasoning_tokens;
- reasoning.effort;
- plus transport_latency_ms outside fields.

Explicit states distinguish:
value / absent / null / ancestor_null / ancestor_invalid / invalid / unsupported.

Unknown strings and invalid values are represented by safe state only and are not copied.

## No-content-leak boundary

Independent source review confirms metadata artifact does NOT persist:
- output text or arbitrary output values;
- reasoning content;
- reasoning summary values;
- encrypted reasoning content;
- error.message;
- arbitrary metadata dictionaries;
- raw headers;
- Authorization/credential material.

Additional provider fields are ignored.

Error code/type are fixed closed enums; unknown strings become unsupported with no copied value.

Result:
PASS_CONTENT_REDACTION_BOUNDARY.

## Ordering / failure behavior

Verified integration order:

use-once claim / transport
→ unchanged shape v2 persist
→ unchanged shape v2 strict readback
→ metadata v1 build
→ metadata atomic create
→ metadata strict readback
→ unchanged normalizer
→ existing review-result path.

Metadata failure raises BLOCKED_FAILURE_METADATA and stops before normalizer.

Reasoning-only response:
metadata survives, normalizer still fails BLOCKED_PROVIDER_RESPONSE, no review/candidate.

Shape readback failure occurs before metadata, so metadata is not falsely created without accepted shape evidence.

Result:
PASS_FAILURE_PATH_ORDERING.

## Persistence/readback

failure_metadata_store.py uses:
- private temporary O_EXCL/O_NOFOLLOW create;
- fsync data;
- atomic hard-link create to final path;
- no overwrite of existing final artifact;
- directory fsync;
- O_NOFOLLOW strict read;
- regular-file check;
- exact canonical JSON + LF readback;
- expected snapshot hash;
- expected identity;
- expected execution mode.

Existing artifact or symlink cannot be replaced.

Result:
PASS_STRICT_METADATA_PERSISTENCE.

## Normalizer / authority preservation

Pinned unchanged SHA values independently confirmed:
- review_result_store.py
  72a3374bdebd1cd0f37951507dd8cd3cf271b8a7924335a6e61f707fcc33e3ba
- live_worker.py
  175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3
- response_shape_store.py
  bc68a15f1dd288ef7092eaf1013e5b825432bb519da4cba4b355c1feb7118e8f

Bridge still binds:
- gpt-5.6-luna;
- max_output_tokens=64;
- max_response_bytes=16384;
- timeout=30;
- calls=1;
- retries=0;
- fallback=none;
- tools=[].

No change to reasoning effort or frozen task/prompt was introduced.

Synthetic consumed-REAL test pre-populates only an isolated synthetic ledger and verifies BLOCKED_DUPLICATE_CALL before resolver/transport. It does not replay the real consumed authority.

Result:
PASS_AUTHORITY_AND_POLICY_PRESERVATION.

## Published guarded evidence

Exact run_tests.py and all test definitions were inspected.

Guard denies:
- socket/network;
- subprocess/process execution;
- os.system;
- real environment access except fixed locale/terminal values;
- writes outside package/scratch.

Forbidden attempts are accumulated separately so caught test exceptions cannot hide capability attempts.

Published evidence:
tests=34
failures=0
errors=0
skipped=0
forbidden_attempts=0
real_provider_calls=0
real_authority_consumption=0
evidence_class=OFFLINE_TEST_ONLY

TEST-LOG contains:
- 16 unchanged predecessor bridge tests;
- 18 new metadata tests;
all PASS.

New coverage includes all 12 exact KOO requirements plus:
- create-only overwrite/symlink denial;
- deterministic latency fixture;
- exact unchanged shape bytes;
- metadata readback failure blocks review;
- duplicate JSON/nonfinite/bounds rejection;
- consumed REAL named authority blocked before transport.

## Verification-method limitation

SIS attempted an exact-byte rerun in an isolated local container, not on project host.

Checkout failed before package execution because that container could not resolve github.com.

Therefore SIS does NOT claim an independently rerun 34/34 suite.

Independent verification instead consists of:
- exact immutable Git tree/blob identity review;
- manifest/checksum cross-check;
- 21-file predecessor byte-identity comparison;
- direct source review of all changed execution-path modules;
- direct inspection of exact guarded runner, 34 published test cases/log/results and their coverage.

No project host was used and no host installation/deployment occurred.

## Boundary accounting

Provider calls: 0.
Execution network attempts by SIS: 0.
Credential reads: 0.
Host/systemd mutation: 0.
Deployment: 0.
Consumed authority replay: 0.
New live/standing authority: NOT_GRANTED.
Project acceptance: NOT_GRANTED.
Production acceptance: NOT_GRANTED.
Automatic project-state application: 0.
Output bound remains 64.
Token-budget causality: UNCONFIRMED.

## Conclusion

The package satisfies the exact bounded non-live task and is suitable for a later separately authorized host-installation decision.

Terminal:
PASS_SIS_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_INDEPENDENT_VERIFY

This PASS does not authorize host installation, provider calls, retry/replay, or any new experiment.

---
КТО: SIS / СИСАДМИН
КОМУ: KOO / КООРДИНАТОР
СТАТУС: PASS_SIS_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_INDEPENDENT_VERIFY
