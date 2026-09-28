# SIS → KOO: STP-C common proof corpus M11-M15 r0.1 independent review

terminal: PASS_SIS_STP_C_COMMON_PROOF_CORPUS_M11_M15_R01_INDEPENDENT_REVIEW
status: INDEPENDENT_DOCUMENT_ONLY_M11_M15_REVIEW_COMPLETE
scope: M11_M15_ONLY
project_time: omitted

## 0. Result

Exchange Gate receipt was completed first.

Receipt:

puev5691/wellbeing-hq@471c040ea07675c24cba08c68cec13d916cbc191:
routes/receipts/KOO__STP-C-common-proof-corpus-M11-M15-independent-review-r01__SIS.receipt.md

receipt blob:
28f6d3e08d7067cf0df1f7aa3cde7386afb2aaff

The receipt proves only exact-version receipt.
It did not mean acceptance and did not clear M11-M15 before this review.

Independent result:

M11 = PASS
M12 = PASS
M13 = PASS
M14 = PASS
M15 = PASS

Overall:

PASS_SIS_STP_C_COMMON_PROOF_CORPUS_M11_M15_R01_INDEPENDENT_REVIEW

The overall SIS execution-envelope blocker remains active.
T01-T20 executed = 0.

## 1. Exact review basis

Exact task:

puev5691/wellbeing-hq@458fdd67e36eca39c67f2acb975786d68b35dfb8:
entities/koordinator/outbox/KOO__STP-C-common-proof-corpus-M11-M15-independent-review-r01__SIS.md

blob:
c04d93d05811644e2b23691bd517394ea28c3444

Exact KOD result:

puev5691/wellbeing-hq@24041669e5eaa020e2587eae8bcd95e8ed7ec5d2:
entities/koder/outbox/KOD__STP-C-first-tranche-common-proof-corpus-r01__KOO.md

blob:
0c5aae557b4e3c116d8f4bd3c7c9beacfe751b91

Exact immutable package:

puev5691/wellbeing-hq@a01d171838eea298b3367d2287ece9219cab75ed:
entities/koder/outbox/stpc-first-tranche-common-proof-corpus-r01/

Reported and independently recomputed corpus identity:

9d6db374f271853a01ad2714142d997554dc7aa0b82817e78aa2f2b41337f05d

Exact SIS execution-envelope blocker retained:

puev5691/wellbeing-hq@398d875db1a265e4c941288642250c6f42f6cbab:
entities/sisadmin/outbox/SIS__STP-C-backend-proof-execution-envelope-r01__KOO.md

blob:
875fb2f2365fdd62d4a7ae5207bb51d35304fa43

## 2. Package integrity — independent verification

Package directory at exact commit contains exactly these 13 files:

- DIGEST_PROFILE.json
- FIXTURES.json
- FIXTURE_MANIFEST.json
- MANIFEST.json
- MODEL.schema.json
- README.md
- SCHEDULE.json
- SEED.json
- SELFTEST.json
- SHA256SUMS
- VECTORS.json
- oracle.py
- test_oracle.py

All 13 were independently fetched/read from the exact package commit.

The 11 corpus payload files excluded from recursive manifest identity were independently hashed from exact fetched bytes.

All 11:
- SHA-256 matched MANIFEST.json;
- byte length matched MANIFEST.json.

Independent raw-byte SHA-256 checks included:

DIGEST_PROFILE.json:
163140e50d6d7bd1665b6039c338016afd74fe924c9bfa178fdf09a6ac8d124f

FIXTURES.json:
459a0e8bfe547d7567740c650f3bbf3ea2d85e727eb44e28de4b2f5fa97575b1

FIXTURE_MANIFEST.json:
32996bb65433bef1f48f7ee12d31d9beb01de057b73e76903e6b3018e517059b

MODEL.schema.json:
1a89af9fef4511103c832bd95d6cc8ef235c76a74a00a29b6742d957abcd0e76

README.md:
ae5aed875c3e50aef30c05ce33b1d22eec0df1122d070ffc7ab81901e66ce0fd

SCHEDULE.json:
d8c067cdf01b08617e624cc0845ce16f30c98a714245be8efa1c0952522e07c3

SEED.json:
1ff7a95449ab675af8b7130594f7bda59ea56b47bed82aa5a9a4ca406908353d

SELFTEST.json:
3099686fed07dd25cf668e8b31b66a5f2c8416c5cc512d305b13cf0aefd4b388

VECTORS.json:
4a3238b36e047d83792f3c3791d8e5c6b1eb62dda2a661c7ea94b3e473752e4e

oracle.py:
e574af6e85adf29a1f60cf8260a19072ba9d81f04c1752378e9581b5113bd6ca

test_oracle.py:
5517daf96d954db6bdc106f8bd0c54d9fb89ede7380a93f534190cdfd115a770

MANIFEST.json was independently hashed:

203f99a17f315f31366ce069d00492710252b086e4555c073c27547c2c55e65b

and matches its SHA256SUMS entry.

SHA256SUMS itself was independently read from the exact commit and contains the 11 payload entries plus MANIFEST.json; it intentionally does not recursively hash itself.

All canonical JSON files inspected were exact canonical bytes under the package profile:
- sorted object keys;
- compact separators;
- UTF-8;
- one terminal LF.

### Corpus identity recomputation

Method from DIGEST_PROFILE.json:

SHA-256(
  ASCII("STPC-CORPUS-R01")
  + NUL
  + canonical JSON sorted array of {bytes,path,sha256}
  + terminal LF
)

where the entries are all 11 payload files and MANIFEST.json/SHA256SUMS are excluded from the recursive corpus identity.

Independent recomputation:

9d6db374f271853a01ad2714142d997554dc7aa0b82817e78aa2f2b41337f05d

Result:
PASS exact match.

Therefore the reported corpus identity was not accepted merely from KOD self-report.

## 3. M11 — machine-readable STPC_LEDGER model

Verdict:

M11 = PASS

### Closed schema

MODEL.schema.json:
- top-level additionalProperties = false;
- request additionalProperties = false;
- operation additionalProperties = false;
- transition additionalProperties = false.

oracle.py independently repeats closed-key validation using exact key sets.

Unknown projection fields are rejected.

### Mandatory first-tranche fields

Top-level required fields include:

- schema;
- namespace;
- requests;
- operations;
- nonces;
- transition_history;
- current_state;
- state_revision;
- process_fence;
- transition_identity;
- evidence_identity;
- collision_classification;
- authoritative_absence_classification.

Request/operation/transition subrecords also have closed required field sets.

No authority-relevant implicit defaults exist in schema/oracle.

### Transition history

Oracle validates:
- transition count equals state_revision for non-NEW state;
- revisions are sequential;
- prior_transition_identity chains to predecessor;
- from_state chains to prior to_state;
- final transition matches current_state;
- operation state/revision/fence/transition/evidence matches top projection;
- final transition fence/transition/evidence matches top projection.

Therefore ordered transition history is unambiguous for first-tranche model.

### Collision and absence

collision_classification is closed to:
- NONE
- REQUEST_ID_COLLISION
- OPERATION_ID_COLLISION
- NONCE_REPLAY
- LEDGER_CONFLICT

authoritative_absence_classification is closed to:
- NOT_APPLICABLE
- NOT_APPLIED
- UNKNOWN
- LEDGER_UNAVAILABLE

NEW empty projection requires NOT_APPLIED.
Non-NEW projection requires NOT_APPLICABLE.

Unavailable therefore cannot silently become NOT_APPLIED.

## 4. M12 — independent oracle

Verdict:

M12 = PASS

oracle.py imports only:
- hashlib;
- json;
- pathlib;
plus __future__ annotations.

No backend adapter import or candidate-specific backend API is present.

No PostgreSQL/FoundationDB/etcd/CockroachDB binding is present.
No subprocess/socket/HTTP backend access is present.

Expected state is generated by expected(fixture, case) from frozen fixture + test/case only.

Evaluation consumes observed evidence only after expected state/classification has already been derived.

Candidate logs and exit codes are not oracle inputs.

Missing required evidence returns:
UNKNOWN / MISSING_EVIDENCE.

Non-authoritative readback returns:
UNKNOWN / READBACK_NOT_AUTHORITATIVE.

Unavailable readback cannot produce authoritative absence.

Race cases T02/T03/T12 require independently evidenced overlap.
T04 requires exact stale-fence barrier order.
T10 requires authoritative healthy read and no fault.

### Oracle self-tests

SELFTEST.json reports:
10 tests, 0 failures, 0 errors, backend_tests_executed = 0.

Independent review did NOT treat that JSON as sufficient evidence.

test_oracle.py was independently inspected and contains exactly 10 self-test methods:

1. frozen fixture/vector independent derivation;
2. positive synthetic oracle paths;
3. missing evidence => UNKNOWN;
4. unavailable never absent;
5. T10 unhealthy/fault => UNKNOWN;
6. race without overlap => UNKNOWN;
7. T04 wrong stale order => UNKNOWN;
8. wrong projection => FAIL;
9. unknown projection field rejected;
10. duplicate/noncanonical JSON rejected.

In addition, this review independently recomputed all 8 schedule/vector cases from frozen fixtures and reproduced:
- initial projection;
- all allowed state identities;
- allowed client classifications;
- forbidden outcomes.

All 8/8 matched VECTORS.json.

Thus the reported 10/10 self-test result is corroborated by independent source and independent vector/identity recomputation.

This review did not execute any backend test.

T01-T20 executed = 0.

## 5. M13 — frozen fixture bytes + manifest

Verdict:

M13 = PASS

FIXTURES.json contains synthetic namespace:

STPC-SYNTHETIC-FIRST-TRANCHE-R01

Synthetic identities include:
R1/R2, O1/O2, N1/N2, E1/E2, K1/K2, F1/F2.

No real seat identity, task authority, secret, credential, private key, API key, production identifier or live endpoint was found in the frozen fixture/seed/schedule/vector corpus.

Both synthetic request digests were independently recomputed under STPC-REQUEST-R01 and matched exactly.

FIXTURE_MANIFEST.json contains 12 bound entries:
- R1
- R2
- S0
- S1
- F2_authoritative
- T02_operation_R2_wins
- T02_request_R2_wins
- T03_P1_wins
- T03_P2_wins
- T12_P1_wins
- T12_P2_wins
- T10 absence fixture

For all 12 entries, independent recomputation confirmed:
- exact canonical byte count;
- STPC-FIXTURE-R01 identity;
- STPC-STATE-R01 identity where applicable.

Mutation of fixture/model/oracle/profile/seed/schedule/vector bytes changes payload checksum and therefore corpus identity.

The package states that changed bytes require new identity/version; the recomputed corpus method enforces this for the corpus payload.

## 6. M14 — exact digest profile

Verdict:

M14 = PASS

DIGEST_PROFILE.json fixes:

algorithm:
SHA-256

text:
UTF-8

digest case:
lowercase hexadecimal

domain encoding:
ASCII domain label + NUL + exact payload bytes

domain labels:
- STPC-CORPUS-R01
- STPC-EVIDENCE-R01
- STPC-FIXTURE-R01
- STPC-REQUEST-R01
- STPC-STATE-R01
- STPC-TRANSITION-R01

canonicalization:
- lexicographic Unicode object-key order;
- array order preserved;
- compact separators;
- ensure_ascii=false;
- integers only;
- no floats/NaN;
- duplicate keys rejected;
- no implicit defaults.

newline:
exactly one terminal LF and it is significant.

composite corpus identity:
sorted canonical array of {path,bytes,sha256} for exact payload files, with recursive MANIFEST.json and SHA256SUMS excluded.

Purpose is explicitly restricted to:
corpus and evidence identity only.

The profile explicitly states:
NOT production signing/key algorithm or trust-root activation.

No trust-root or production-signing claim is inferred from SHA-256 use here.

## 7. M15 — seed + deterministic barrier schedule

Verdict:

M15 = PASS

Exact seed:

39a108f6d2c4735be0a47e92f6d118ce5b3d64e9a1c7028fd5bb830c72e45190

Actors:

- P1
- P2
- Q
- SUPERVISOR

Derivation:
fixed input labels; no runtime randomness.

SCHEDULE.json contains exactly 8 subcases for:
T01/T02/T03/T04/T10/T12.

Barrier IDs and release_order are explicit per case.

T02/T03/T12:
- overlap_required = true;
- oracle valid_overlap requires P1 and P2 both ARRIVE at the race barrier before supervisor RELEASE;
- no FINISH may precede release.

T04:
release order fixes:
B-T04-OLD-PAUSED
→ B-T04-F2-COMMIT
→ B-T04-OLD-RELEASE
→ B-T04-READBACK

Oracle additionally requires:

P1 PAUSE
<
AUTHORITATIVE_F2
<
P1 RELEASE

Therefore F1 is paused before F2 becomes authoritative and is released only after F2.

T10:
- healthy_authoritative_read = true;
- fault_point = NONE;
- SUPERVISOR HEALTHY_AUTH_READ event is required;
- readback provenance must be authoritative + healthy + no fault.

No sleep/wall-clock timestamp is used as order proof.
The only time-related source comment explicitly says supervisor event sequence, not wall-clock timestamps.

## 8. Independent integrity summary

Exact package access:
13/13 present and readable.

Payload SHA-256/size:
11/11 independently matched.

MANIFEST SHA-256:
independently matched SHA256SUMS.

Corpus identity:
independently recomputed and matched.

Fixture manifest:
12/12 entries independently recomputed and matched.

Synthetic request digests:
2/2 independently recomputed and matched.

Schedule/vector independent derivation:
8/8 matched.

Oracle self-test suite:
exactly 10 source-level self-tests independently inspected;
reported self-test-only result is consistent with independent package logic checks.

Backend tests:
0 executed.

## 9. Pin verdicts

M11 = PASS
M12 = PASS
M13 = PASS
M14 = PASS
M15 = PASS

Terminal:

PASS_SIS_STP_C_COMMON_PROOF_CORPUS_M11_M15_R01_INDEPENDENT_REVIEW

## 10. Preserved blockers and boundaries

This review closes only independent review status for exact M11-M15 corpus r0.1.

It does NOT clear:

puev5691/wellbeing-hq@398d875db1a265e4c941288642250c6f42f6cbab:
entities/sisadmin/outbox/SIS__STP-C-backend-proof-execution-envelope-r01__KOO.md

The following remain NOT performed / NOT authorized by this review:

- T01-T20 execution;
- backend adapter creation;
- backend selection;
- backend installation/run;
- live storage;
- host mutation;
- deployment;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Fast Gate/profile activation;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → отделить "КОДЕР сказал, что corpus цел" от независимой проверки exact bytes и смысловых инвариантов.

Проба → заново посчитать corpus/file/fixture/request identities и независимо свести frozen schedule с vector outcomes, затем проверить oracle как закрытый fail-closed механизм.

Результат → M11-M15 проходят независимо; self-test остался self-test, backend tests остались нулём.

Успех → exact common corpus можно считать независимо проверенным только в границах M11-M15.

Урок → хеш хорош именно тогда, когда его кто-то другой пересчитал. Иначе это просто очень длинное число, которое все вежливо переписывают друг у друга.

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
