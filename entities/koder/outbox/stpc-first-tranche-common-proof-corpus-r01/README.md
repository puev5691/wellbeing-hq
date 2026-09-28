# STP-C first-tranche common proof corpus r0.1 — candidate

**Scope:** synthetic, non-production common corpus for T01/T02/T03/T04/T10/T12 only. This package closes document/code artifact pins M11–M15 for independent review. It contains no backend adapter, installation command, live endpoint, credential, host path assumption or production authority. Oracle self-tests do not execute any T01–T20 backend test. SIS's other execution-envelope blockers remain open.

## Immutable basis

- Reviewed harness: `puev5691/wellbeing-hq@c69a7e8691b8cab56e6493a742908e6df265bdde:entities/koder/outbox/KOD__STP-C-backend-bounded-empirical-proof-design-r01__KOO.md`, blob `12147a1405e9cc6a4fc20643a6031abf1cc69c2f`.
- SIS blocker: `puev5691/wellbeing-hq@398d875db1a265e4c941288642250c6f42f6cbab:entities/sisadmin/outbox/SIS__STP-C-backend-proof-execution-envelope-r01__KOO.md`, blob `875fb2f2365fdd62d4a7ae5207bb51d35304fa43`.
- Authority: `puev5691/wellbeing-hq@54a6af07aa123764bd3dde359570717b41b1c7c6:entities/koordinator/outbox/KOO__authorize-KOD-STP-C-first-tranche-common-proof-corpus-r01__OPERATOR.md`, blob `0b3ea3d9e0b9ac758b26a3a5ab1d76f041157cec`.

## Files and exact role

| File | Purpose |
|---|---|
| `MODEL.schema.json` | Closed machine-readable STPC_LEDGER_V1 projection schema. Semantic constraints additionally checked by oracle. |
| `oracle.py` | Independent supervisor-only pure Python oracle; no candidate/backend import, I/O only for explicitly supplied corpus files. |
| `FIXTURES.json` | Frozen canonical UTF-8 JSON bytes: R1/D1/O1/N1/E1/K1/F1, R2/D2/O2/N2/E2/K2/F2, S0/S1, transition projections, T10 authoritative-absence declaration. |
| `FIXTURE_MANIFEST.json` | Exact fixture file SHA-256, byte count and per-value domain-separated identities. |
| `DIGEST_PROFILE.json` | SHA-256 domain/encoding/canonicalization profile solely for corpus/evidence; **not** STP-C production signing, keys or trust-root activation. |
| `SEED.json` | Frozen 32-byte hex seed, synthetic actor names. |
| `SCHEDULE.json` | Eight fixed subcases across six tests, barriers and release order; T02/T03/T12 overlap requirement, T04 stale ordering, T10 healthy read. |
| `VECTORS.json` | Machine-readable initial projections, actor operations, allowed state identities/classifications, forbidden outcomes and evidence/PASS/UNKNOWN conditions. |
| `test_oracle.py`, `SELFTEST.json` | Deterministic oracle-only self-tests and recorded result. Not candidate test evidence. |
| `SHA256SUMS`, `MANIFEST.json` | Exact file inventory and corpus identity; manifest itself excluded from recursion. |

## Identity and consistency

Every JSON file has sorted keys, compact separators, UTF-8, no BOM, exactly one terminal LF; newline is significant. Unknown fields and floats are rejected for closed model/evidence. `D1`/`D2` are computed from exact canonical synthetic request core under `STPC-REQUEST-R01`; the other labels are intentionally synthetic strings, not production identities. A future adapter maps these exact semantic values and may not change oracle or vectors. Expected projection is generated from frozen fixtures/schedule, not candidate logs. Candidate readback must be authoritative and independently evidenced in a later execution gate; a boolean asserted by a candidate is insufficient.

The supervisor's barrier events are ordered and identity-bound. For T02/T03/T12, both actors must be at `B-*-RACE` before supervisor release and neither may finish beforehand; without observed overlap classification is UNKNOWN. T04 requires `P1 PAUSE < authoritative F2 < P1 RELEASE`; T10 requires supervisor-attested healthy authoritative read and no injected fault. Future execution must prove those events independently of the candidate adapter. No wall-clock timestamp substitutes for order/currentness.

The corpus identity is domain-separated SHA-256 of canonical sorted `{path,bytes,sha256}` entries for all payload files excluding only recursive `MANIFEST.json` and `SHA256SUMS`. The manifest records that identity plus each payload file digest/size; SHA256SUMS lists payload files and manifest. Any change to model, oracle, fixtures, profile, seed, schedule or vectors creates a new identity/version. The Git package tree and every committed blob must be read back after publication. No outcome of a candidate backend is asserted here.

## Self-test and limits

The only executed command in preparation is `python -B -m unittest -q test_oracle` in this package directory. It uses invented observations in memory, validates positive oracle branches and fail-closed UNKNOWN/FAIL cases. It does not import or contact PostgreSQL, FoundationDB, etcd, CockroachDB, a host, shard or effecting system. `SELFTEST.json` preserves count/result. Future T01–T20 execution, candidate-specific topology/config/build, adapters, runtime/environment, fake downstream and evidence root require separate authority. `CHECKPOINT_DURABLE` remains NOT_ESTABLISHED; EOM pilot and memory-layering attempt 3 are not authorized.
