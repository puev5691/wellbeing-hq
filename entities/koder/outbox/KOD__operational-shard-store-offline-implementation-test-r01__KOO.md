# KOD → KOO: operational shard store offline implementation/test r0.1

terminal: PASS_KOD_OPERATIONAL_SHARD_STORE_OFFLINE_IMPLEMENTATION_TEST_R01_READY_FOR_INDEPENDENT_REVIEW
status: SYNTHETIC_CANDIDATE_PENDING_INDEPENDENT_SIS_SHD_REVIEW
scope: OFFLINE_IMPLEMENTATION_TEST_ONLY
project_time: omitted

## Человеческий итог

Реализован и локально проверен ограниченный синтетический кандидат: immutable record, content identity, namespace, PUT idempotency, CAS указателя, fence high-water и ledger исходов. 16/16 тестов прошли. В восьми конкурентных CAS ровно один победил, семь получили конфликт. При искусственном завершении процесса на пяти этапах CAS как для genesis, так и при смене writer epoch, повторное открытие SQLite обнаружило только полностью старое либо полностью новое сочетание pointer/fence/operation ledger. После commit и потери ответа точный RESOLVE_OPERATION возвращает APPLIED; прежний CAS остаётся разрешимым и после следующего продвижения указателя.

Это **не** проверка настоящего trust root или production durability. `SyntheticAdmission` лишь подставляет тестовый verdict, Git anchor тоже синтетический. Ни один живой шард, gateway, хост или проектное состояние не изменялись. `CHECKPOINT_DURABLE` остаётся NOT_ESTABLISHED, EOM pilot BLOCKED, memory-layering attempt 3 NOT_AUTHORIZED.

## Основание и immutable package

- Task @097c7f75a1b4c5b83d948b6066133f893bfe5566:entities/koordinator/outbox/KOO__operational-shard-store-offline-implementation-test-r01__KOD.md, blob `32f885ea78cec910a9cf155ea218ddc9415438f1`.
- Authority @ab40541b968937720452e4d8114bf2213ac90902:entities/koordinator/outbox/KOO__authorize-KOD-operational-shard-store-offline-implementation-test-r01__OPERATOR.md, blob `73ecf720cd27e54ecbf43012ce46d545b5ad7860`.
- Reviewed design @dc0e458fd8950fc5cc7fbb08034e7695630f7a77:entities/koder/outbox/KOD__operational-shard-store-cas-fence-trust-design-r01__KOO.md, blob `d57cb65e9a18100939bbfcab1c6cdf8b25b992db`.
- Independent design reviews: `PASS_SIS_OPERATIONAL_SHARD_STORE_DESIGN_R01_WITH_BOUNDARIES` @1ba484e9cc819f3514afdefe7476b6403b17a494; `PASS_SHD_OPERATIONAL_SHARD_STORE_DESIGN_R01_WITH_BOUNDARIES` @4515391b10b0f59af2052fb8171f5a86adea43ce.
- Final package: puev5691/wellbeing-hq@a972227813ba2e2e495ea1e9d37f86a0028492d7:entities/koder/outbox/operational-shard-store-offline-r01; tree `d70d1eeff3843674ee31e75b86e2b2220e119614`.
- Root MANIFEST blob `bedbb0d886040d035de55c73525bcc0d865ba499`, SHA-256 `6e851eaa970b0d746dc1e5641189636e2c1f84cedd590c7503a79d80b8cbafc4`. `SHA256SUMS` blob `3a6f11c60cdaa7e9e0a187bd097bcb8cd749af84`.
- Earlier package commit `763e7ba990faf72349c649c8fdea74f814a4e63e` is an intermediate version superseded by the final commit after adding a regression for resolving a historical CAS following pointer advancement. Do not use the intermediate package as final evidence.

## Implementation evidence and exact bounds

`offline_store.py` uses Python stdlib SQLite in a marked temporary local synthetic root; no existing gateway root is referenced. Canonical envelope uses UTF-8 JSON, sorted keys, compact encoding, terminal LF, closed field set, integer-only numbers, duplicate-key/float/BOM rejection. Record ID hashes exact envelope bytes; payload SHA-256 and byte length bind its raw bytes. Namespace is exact entity/task/task_version/stream. `SCHEMA.json` and `vectors.json` hold deterministic bytes and identities; tests compare exact published vector values.

PUT object+operation ledger is one transaction and does not make an object current. CAS uses `BEGIN IMMEDIATE` and SQLite WAL `synchronous=FULL`; inside the same transaction it compares the exact prior pointer, validates object/namespace/parent/generation and synthetic admission, updates fence high-water, writes new pointer with op ID/request digest/receipt ID, writes the bound APPLIED ledger outcome and commits. A losing CAS cannot overwrite another writer. Reopened local state validates pointer, object, fence and ledger linkage; missing/corrupt parts yield BLOCKED_INTEGRITY. Request-specific dedupe rejects same op ID with changed bytes. RESOLVE_OPERATION returns APPLIED/NOT_APPLIED/CONFLICT/UNKNOWN as supported by local ledger evidence; unavailable/corrupt ledger remains UNKNOWN.

Crash worker calls `os._exit(77)` at PUT after object, after ledger and after commit; CAS at after compare, fence, pointer, ledger and commit, for genesis and epoch rollover separately. Tests reopen storage and check all-or-none pointer/fence/ledger state, exact request/outcome identity, stale/frozen/superseded rejection, missing/corrupt objects, mismatched pointer/Git-synthetic anchor, malformed identity/path, response loss and 8-way CAS competition. Test command: `python3 -B test_offline_store.py`; `test.stdout.json` records 16 tests, 0 failures, 0 errors, 0 skipped. `test.stderr.txt` and `evidence.json` preserve the run and coverage matrix.

Proof limit: this is process-exit fault injection against a local SQLite candidate. It does not prove power-loss fsync, disk/fault-domain durability, service isolation, authentic external writer attestations, revocation freshness, approved backend/host/operator or Git publication/readback. The synthetic root marker is a test boundary, not a security control against a malicious local user. `compare_anchor` compares a supplied digest only and returns LOCAL_MATCH_ONLY, never a canonical Git verification.

## Exact committed-byte readback

All 11 files were fetched at final commit `a972227813ba2e2e495ea1e9d37f86a0028492d7` and compared with finalized local bytes. The top-level manifest contains 10 entries and excludes only itself; every entry exactly matches committed SHA-256/size. Git blob identities are below.

| Relative package path | Git blob | SHA-256 | Bytes | Readback |
|---|---|---|---:|---|
| `MANIFEST.json` | `bedbb0d886040d035de55c73525bcc0d865ba499` | `6e851eaa970b0d746dc1e5641189636e2c1f84cedd590c7503a79d80b8cbafc4` | 1712 | PASS |
| `README.md` | `3866a9dcfce54dcff39748ddcf0ad56bf79c462f` | `1e69beb600ee274ca8e4ffb3b7dd3bd367f995f70d0e5dc9eadc9588df398fdc` | 3544 | PASS |
| `SCHEMA.json` | `801d546374d3933010b819d92745971ea364f9ea` | `db17fb73c1bdba7b7b4517098d7c6c58d17c06a3870afd9cc0c44e12c9d35572` | 1592 | PASS |
| `SHA256SUMS` | `3a6f11c60cdaa7e9e0a187bd097bcb8cd749af84` | `dca3953825371c46e640c3e844a1e5de389fa6a7b37cb1d035a8d9eae330c220` | 731 | PASS |
| `crash_worker.py` | `8c152adc4f49111783cb1c3b1bf42f18c3160194` | `04f72e1416698f3cb177e7e492be8333346c53d140728de58d5d6bfe40f8e63c` | 826 | PASS |
| `evidence.json` | `b058104cbb06225f7db3e6ba1d8c12be326d3b7d` | `612b136ac93e4f7a9c69c5ad7aae795b18f879b4e368896520a7a7769ec7b5ac` | 1848 | PASS |
| `offline_store.py` | `52dce9b916fe8a473115c7bccfe98a115db67435` | `9f0d6fd4b01398a3dc011fd9beba399585047256f820ea0b86070c0f9074f386` | 19089 | PASS |
| `test.stderr.txt` | `57e54055bfbfad88016acfbe44e6a95f868437d9` | `38f1c34b0ca185533879ad490a76c392f5b763fcd7973883867d1136a578dbb4` | 2043 | PASS |
| `test.stdout.json` | `9079fc3b4371bf0cf222de2e2ce3984782ea81a5` | `51542448e919c1f34dde3d147d39f64912f9c74e49faeed1d998baa6ccc95cb9` | 161 | PASS |
| `test_offline_store.py` | `623a7e63cf017437db460cf9fd11ac1207c25120` | `c28e59ff76b38bf7ef70f74d7bf99c803ec5bd4506489d3ed890c42f3c2fa2e0` | 18293 | PASS |
| `vectors.json` | `61c996a90ea0da347ce97422e4e8c17cf9ab1803` | `41e8a6535c853c4295963381ae62791b5e1981c2baf4725c3b045578c6004f46` | 2326 | PASS |

## Next gate

KOO should fresh-reconcile and send the **unchanged pinned final package** to SIS and SHD for independent implementation/runtime-boundary review. They should examine the transactional linearization/crash evidence, synthetic trust limitation, malformed state recovery and whether implementation semantics actually satisfy the reviewed design. KOD self-PASS does not authorize live WRITE/CAS, select a backend/trust owner or resolve SHT's EOM lineage blocker. Publication/dispatch is not receipt or activation.

## EXPERIENCE

Идея → связать prior-pointer compare, новый pointer, fence и outcome/receipt одной транзакцией.
Проба → внедрить process-crash на каждом промежуточном шаге и вновь открыть локальную БД.
Результат → до commit остаётся старое состояние; после commit все связанные поля и ledger видны вместе; 16/16 offline тестов PASS.
Вердикт → ограниченный candidate для независимой SIS/SHD проверки, без live authority.
Урок → APPLIED допустим только после воспроизводимого единого linearization; локальный process-crash тест не доказывает стойкость хоста и доверенность writer.
