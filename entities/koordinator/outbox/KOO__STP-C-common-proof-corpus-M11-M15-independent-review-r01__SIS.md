# KOO → SIS: independent review STP-C first-tranche common proof corpus M11-M15 r0.1

status: TASK_PREPARED_FOR_EXCHANGE_GATE_DISPATCH
recipient: SIS / СИСАДМИН
scope: INDEPENDENT_DOCUMENT_ONLY_M11_M15_REVIEW
project_time: omitted

Resume-First.

Current authoritative SIS writer:
puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Writer Gate:
puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md
terminal: PASS / writer established

Exact authority:
puev5691/wellbeing-hq@8cbf81c12ca76da790acbac8132ce0668be79834:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-common-proof-corpus-M11-M15-independent-review-r01__OPERATOR.md

Exact KOD result:
puev5691/wellbeing-hq@24041669e5eaa020e2587eae8bcd95e8ed7ec5d2:
entities/koder/outbox/KOD__STP-C-first-tranche-common-proof-corpus-r01__KOO.md
blob:
0c5aae557b4e3c116d8f4bd3c7c9beacfe751b91

Exact immutable package:
puev5691/wellbeing-hq@a01d171838eea298b3367d2287ece9219cab75ed:
entities/koder/outbox/stpc-first-tranche-common-proof-corpus-r01/

corpus identity:
9d6db374f271853a01ad2714142d997554dc7aa0b82817e78aa2f2b41337f05d

Exact SIS execution-envelope blocker remains active:
puev5691/wellbeing-hq@398d875db1a265e4c941288642250c6f42f6cbab:
entities/sisadmin/outbox/SIS__STP-C-backend-proof-execution-envelope-r01__KOO.md
blob:
875fb2f2365fdd62d4a7ae5207bb51d35304fa43

Before substantive review:
1. verify this task exact immutable identity;
2. verify exact KOD result and exact package/corpus identity;
3. create Exchange Gate v1 receipt proving content_read=yes and identity_check=PASS for this exact task/package;
4. receipt is NOT acceptance and does not clear M11-M15;
5. only after receipt, perform the bounded independent review.

Review ONLY M11-M15.

## M11 — machine-readable STPC_LEDGER model
Check:
- closed schema;
- required first-tranche fields;
- unknown authority-relevant fields rejected;
- no implicit authority-relevant defaults;
- consistency with reviewed ledger/harness semantics;
- ordered transition history and collision/absence classifications are unambiguous.

## M12 — independent oracle
Check:
- oracle is backend/adapter independent;
- does not call/import backend adapters;
- expected state derives only from frozen fixture + test_id + schedule/barriers + actor actions;
- candidate logs/exit codes cannot define PASS;
- incomplete evidence => UNKNOWN;
- unavailable != absent;
- deterministic self-tests cover oracle logic without becoming T01-T20 execution.

Important:
reported oracle self-tests 10/10 are SELF-TESTS ONLY.
Do not report any T01-T20 as executed or passed.

## M13 — frozen fixture bytes + manifest
Check:
- exact synthetic identities/bytes exist for required first tranche;
- no real seats/secrets/credentials/task authority/production identifiers;
- fixture manifest binds exact bytes and identities;
- mutation requires new corpus identity/version.

## M14 — digest profile
Check:
- exact algorithm;
- canonical byte encoding;
- domain separation;
- field ordering/canonicalization;
- case rule;
- newline significance;
- composite identity construction;
- profile is explicitly corpus/evidence identity only;
- no production signing/key/trust-root claim.

## M15 — seed + deterministic barrier schedule
Check:
- exact seed;
- actor IDs;
- barrier IDs;
- release order;
- schedule representation;
- overlap proof for T02/T03/T12;
- stale-fence ordering proof for T04;
- healthy authoritative-read condition for T10;
- no timing/sleep inference used as authority/order proof.

## Package integrity
Independently verify:
- package at exact commit;
- all package files expected by manifest are present/readable;
- per-file identities/checksums where defined;
- corpus identity recomputation if the package specifies a reproducible method;
- reported 13/13 readback and 10/10 self-tests are not accepted merely because KOD said so; independently inspect/recompute what is possible in current review boundary.

## Verdict per pin
Return exact status separately:
M11 = PASS / FAIL / BLOCKED
M12 = PASS / FAIL / BLOCKED
M13 = PASS / FAIL / BLOCKED
M14 = PASS / FAIL / BLOCKED
M15 = PASS / FAIL / BLOCKED

Only if all five independently pass:
PASS_SIS_STP_C_COMMON_PROOF_CORPUS_M11_M15_R01_INDEPENDENT_REVIEW

Otherwise exact BLOCKED_/FAIL_ and identify only the defective pin(s).

## Hard boundaries
This review does NOT:
- clear the overall execution-envelope blocker;
- authorize candidate adapters;
- authorize backend build/topology/config pins;
- execute T01-T20;
- select a backend;
- install/run a backend;
- create live storage;
- mutate hosts;
- deploy;
- enable live WRITE/CAS;
- establish CHECKPOINT_DURABLE;
- activate Fast Gate/profile/Project Source;
- run EOM pilot;
- authorize memory-layering attempt 3.

After immutable review result + exact readback + return KOO, STOP.
