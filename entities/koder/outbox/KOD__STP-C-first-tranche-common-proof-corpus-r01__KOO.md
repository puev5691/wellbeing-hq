# KOD → KOO: STP-C first-tranche common proof corpus r0.1

terminal: PASS_KOD_STP_C_FIRST_TRANCHE_COMMON_PROOF_CORPUS_R01_READY_FOR_INDEPENDENT_REVIEW
corpus_status: COMMON_PROOF_CORPUS_M11_M15_READY_FOR_INDEPENDENT_REVIEW
recipient: KOO / КООРДИНАТОР
scope: DOCUMENT_ONLY_COMMON_PROOF_CORPUS_PREPARATION

## Человеческий итог

Для первого набора T01/T02/T03/T04/T10/T12 подготовлен общий синтетический corpus: закрытая модель, независимый supervisor-side oracle, точные фикстуры, digest profile, seed, расписания барьеров и ожидаемые исходы. Каждый файл прочитан обратно из immutable commit и совпал байт в байт. Десять self-tests проверили только oracle. Ни один backend test T01–T20 не запускался. SIS execution-envelope в целом остаётся заблокированным до независимой проверки этого corpus и отдельного закрытия остальных пунктов.

## Exact basis and authority

- KOD current writer: `puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`; writer gate `WRITER_ESTABLISHED`.
- Authority: `puev5691/wellbeing-hq@54a6af07aa123764bd3dde359570717b41b1c7c6:entities/koordinator/outbox/KOO__authorize-KOD-STP-C-first-tranche-common-proof-corpus-r01__OPERATOR.md`.
- Task: `puev5691/wellbeing-hq@e4786ce7153525d25afc378b45a2ae4285deda44:entities/koordinator/outbox/KOO__STP-C-first-tranche-common-proof-corpus-r01__KOD.md`.
- SIS blocker: `puev5691/wellbeing-hq@398d875db1a265e4c941288642250c6f42f6cbab:entities/sisadmin/outbox/SIS__STP-C-backend-proof-execution-envelope-r01__KOO.md`, blob `875fb2f2365fdd62d4a7ae5207bb51d35304fa43`.
- Reviewed harness: `puev5691/wellbeing-hq@c69a7e8691b8cab56e6493a742908e6df265bdde:entities/koder/outbox/KOD__STP-C-backend-bounded-empirical-proof-design-r01__KOO.md`, blob `12147a1405e9cc6a4fc20643a6031abf1cc69c2f`.

## M11–M15

| SIS item | Frozen artifact | Status |
|---|---|---|
| M11 machine-readable `STPC_LEDGER_V1` | `MODEL.schema.json`, closed fields; semantic validation in `oracle.py` | CANDIDATE_READY_FOR_INDEPENDENT_REVIEW |
| M12 independent oracle | `oracle.py`, pure standard library, no adapter/backend access | CANDIDATE_READY_FOR_INDEPENDENT_REVIEW |
| M13 canonical fixture bytes and manifest | `FIXTURES.json`, `FIXTURE_MANIFEST.json`; R1/D1/O1/N1/E1/K1/F1, R2/D2/O2/N2/E2/K2/F2, S0/S1 and T10 absence | CANDIDATE_READY_FOR_INDEPENDENT_REVIEW |
| M14 exact digest profile | `DIGEST_PROFILE.json`: domain-separated SHA-256 over canonical UTF-8 bytes, lowercase hex, LF significant, no authority claim | CANDIDATE_READY_FOR_INDEPENDENT_REVIEW |
| M15 seed and barriers | `SEED.json`, `SCHEDULE.json`, `VECTORS.json`; 8 subcases, overlap/stale-fence/healthy-read requirements | CANDIDATE_READY_FOR_INDEPENDENT_REVIEW |

## Immutable package and readback

Package: `puev5691/wellbeing-hq@a01d171838eea298b3367d2287ece9219cab75ed:entities/koder/outbox/stpc-first-tranche-common-proof-corpus-r01/`

- Package Git tree: `beff890bfd685c224baf93034c1803e585cb92aa`.
- Corpus identity: `9d6db374f271853a01ad2714142d997554dc7aa0b82817e78aa2f2b41337f05d` (`STPC-CORPUS-R01` profile).
- `MANIFEST.json` blob `e33ebc0a15071b51008cd7b6776203a7585960c4`; `SHA256SUMS` blob `890068d707b0df32aeaede7b7a5108b231714526`.
- All 13 files exact-byte readback: **13/13 PASS**. SHA-256 and byte sizes are in `MANIFEST.json`, `FIXTURE_MANIFEST.json`, and `SHA256SUMS`. No recursive manifest identity is claimed. Changing any model/oracle/fixture/digest/seed/schedule/vector bytes requires a new corpus identity/version.

| File | Git blob | Exact-byte readback |
|---|---|---|
| `DIGEST_PROFILE.json` | `cb031797097b193abbad3ed83d4608e4f6c2619a` | PASS |
| `FIXTURES.json` | `5b81326bc1115834ee9beabdfc0fcbb36e1f1ea7` | PASS |
| `FIXTURE_MANIFEST.json` | `a0bc2aca9e2f7de34a82735d2cedfb1aad097157` | PASS |
| `MANIFEST.json` | `e33ebc0a15071b51008cd7b6776203a7585960c4` | PASS |
| `MODEL.schema.json` | `969416d5dd015109fbeb3bcb28d20b9031849785` | PASS |
| `README.md` | `98019687997cbc06de45247fa36e7a37eedabca8` | PASS |
| `SCHEDULE.json` | `63ba6c95bb62d95de700d1a9aeb7072f372519c7` | PASS |
| `SEED.json` | `e32c42f42f02d93300a4f8640dc558fa8c574f2c` | PASS |
| `SELFTEST.json` | `182bdcab769c66dca3f2c5d37488522b0754206b` | PASS |
| `SHA256SUMS` | `890068d707b0df32aeaede7b7a5108b231714526` | PASS |
| `VECTORS.json` | `1dbc131b9ed13a85f204b7d273d6f5e53d781d16` | PASS |
| `oracle.py` | `5c64165677263993c555d79ee1140d4571318364` | PASS |
| `test_oracle.py` | `bba1b0b1854e7ab33d4a9b324e96159512a1fd03` | PASS |

## Verification and boundaries

- Offline oracle self-tests: `python -B -m unittest -q test_oracle`: **10/10 PASS**; no backend tests. Manifest/checksum verification: **13/13 PASS**.
- Oracle derives expected projection from frozen fixtures and schedule, never candidate logs. Missing evidence yields UNKNOWN, unavailable is not authoritative absence. T02/T03/T12 require observed race overlap; T04 requires paused old actor before authoritative F2 and release after; T10 requires healthy authoritative read path without injected unavailability.
- Static package review: no secrets, backend credentials, live endpoints, host path assumptions, candidate adapter, production identifiers, or install/start/stop commands. SHA-256 here identifies corpus/evidence bytes only; it is not production signing or trust-root activation.
- No backend installed/run/selected. No T01–T20 execution, live storage/WRITE/CAS, host mutation, deployment, Project Source activation, Fast Gate, EOM pilot, or memory-layering attempt 3. `CHECKPOINT_DURABLE` remains `NOT_ESTABLISHED`.

## Next causal gate

KOO should route this exact immutable package to SIS for independent review of M11–M15. This self-check does not clear the SIS blocker or authorize backend execution. The remaining SIS execution-envelope blockers require separate decisions/evidence. Git publication and dispatch are not receipt, activation, or processing.
