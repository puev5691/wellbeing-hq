# КОДЕР: стенд memory-layering подготовлен для независимой проверки

Материализован non-production preparation package сценария ML-E2E-DESIGN-R01: синтетические входы и две версии задачи, замороженный OLD-01 prefix/checkpoint, четыре смысловых recovery блока, promotion/conflict evidence, selective retrieval и isolation contracts, schemas, отдельный verifier/oracle и offline self-tests. OLD-01→NEW-01 main scenario не запускался.

terminal: PASS_KOD_MEMORY_LAYERING_E2E_R01_PREPARATION_READY_FOR_INDEPENDENT_VERIFY
scope: preparation only; no main execution authority
project_time: omitted

## Основания и fresh reconciliation

Preflight HEAD: 9d4f7af4e4de3ef841b347cd85ae934adbc4cda0; recursive tree truncated=false. Перед publication HEAD не изменился. KOD v0.5 writer blob cf1c84f9df7c90509703e4885844d0cf871ff412 совпал; v0.4 freeze blob 94cc1acb14fdcca623f4596c9a589e9ff42451ee сохранён; competing writer / superseding preparation result не найден в проверенном canonical current и memory-layering lineage.

Authority: прямое текущее решение ОПЕРАТОРА AUTHORIZE_MEMORY_LAYERING_E2E_R01_EXECUTION_PREPARATION. KOO gate: entities/koordinator/outbox/KOO__memory-layering-e2e-r01-execution-preparation-gate__OPERATOR.md@9d4f7af4e4de3ef841b347cd85ae934adbc4cda0, blob 32ac7972096a0a3cc02d492921108dce9f3a7d33. Его прежнее WAITING_OPERATOR состояние разрешено именно явным сообщением ОПЕРАТОРА, а не предполагаемым implicit approval.
Design: entities/koder/outbox/KOD__memory-layering-e2e-design-r01__KOO-SHT.md@9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca, blob b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0; fresh same blob.
SHT review: entities/shtabist/outbox/SHT__memory-layering-e2e-design-r01-boundary-review__KOO.md, fresh blob 5629cbee66659be35b42c0068ccfa6444e338c3c: PASS_SHT_MEMORY_LAYERING_E2E_DESIGN_R01_BOUNDARY_REVIEW.
ARH review: entities/archivarius/outbox/ARH__memory-layering-e2e-design-r01-preservation-review__KOO.md, fresh blob 19886f54bfa1b6223b159007eede055a4d0aa180: PASS_ARH_MEMORY_LAYERING_E2E_DESIGN_R01_PRESERVATION_REVIEW.
Оба review привязаны к тому же design. Старый SHT current blob 3b868adc035b188e797f10f52ebc8b9f383a1075 содержит прежнее ожидание design; более поздний SHT review и KOO gate учтены отдельно. KOD не переписывает SHT current. Исторические PROMPT не replay.

## Exact immutable package

repository: puev5691/wellbeing-hq
package_path: entities/koder/outbox/test/memory-layering-e2e-r01-preparation
package_commit: 5e03bfb59e763ba48e2ea982f31ae3fc33b69b23
repository_tree: 2a814effc4c6f139089eb6fd2464097a25c62893
package_subtree: c3a4f352d5d65e363d569803bc726bac164bd086
root_identity: repository + package_commit + package_path + package_subtree
files: 42
publication_readback: 42/42 exact bytes and Git blob MATCH
manifest_blob: 8ce9968f1300b92ee5624fff6ea9e31e7699bba7
manifest_sha256: 520a1be8b22ac7057a3f2a44c40623d8ab6f32b6c78decf802422a14e932bfbf
checksums_blob: 9e0c8a6e21aeca64d748719fc38d3122074bc99f
checksums_sha256: 0826e6200464efe891d91f77679ca3dcadf6a9d2dadefe75f940d8873444de59
verifier_sha256: 152a372163bf436eade8c75d5484447189fb273591dd6452a42eee2c1eb68616

Manifest включает 40 payload files с exact SHA256/Git blobs; checksum list включает payload и manifest, исключает себя. Root identity внешняя, без самоссылочного commit внутри payload. Пакет расположен только в outbox/test, не production recovery/current/registry.

## Self-check evidence и пределы

14 guarded offline tests PASS, failures=0, errors=0, forbidden_attempts=[]; deterministic TEST-RESULTS.json включён. Main attempts=0, old/new processes started=0, provider calls=0, production/writer/canon/retention changes=0. Проверены reproducing manifest/checksums, frozen cursor=3/seen/totals, explicit v1 superseded/v2 selected, raw DONE rejected, timezone unknown, denied raw-noise/oracle/full-corpus retrieval, STOP missing exact evidence, unresolved promotion BLOCKED, worker escalation BLOCKED, input duplicate conflict BLOCKED, separate structural/semantic gates, prefix-replay ledger FAIL и real-chat claim FAIL. Main admission всегда BLOCKED_MAIN_NOT_AUTHORIZED.

Positive restoration/result samples — checker test fixtures, не evidence реально восстановленного NEW-01. Verifier знает независимый oracle; projection содержит только allowlisted recovery и полные approved sources. Design/provenance/checker/tests/oracle не входят в projection. Все 6 approved sources сохранены побайтно: 192853 bytes, без сокращения. Task retrieval budget <=32 reads / 262144 bytes; mandatory bootstrap отдельно. Candidate bootstrap cap материализован как exact 192853 bytes и должен быть подтверждён independent review/final execution admission; новая source version требует re-admission.

Первый guarded self-test обнаружил ошибку адресации temporary cleanup dir_fd-relative path. Исправлена только очистка тестовой копии с absolute paths; повторный guarded run PASS. Это отмечено в TEST-NOTES.md.

Изоляция доказана только на уровне preparation projection/контрактов и offline отказов доступа; runtime OS isolation НЕ проверена. Public package не делает oracle секретным: будущий worker должен быть лишён arbitrary fetch/filesystem access к package root. Separate fresh exec processes, empty environment, no inherited memory/cache/transcript, supervisor deadline/network/filesystem boundary требуют независимой проверки и фактического execution evidence. Этот package не содержит runner main OLD→NEW и не выдаёт execution authority.

## Следующий causal gate

SHT: независимо проверить exact harness/verifier, oracle separation, projection/isolation contracts, schemas, negative subcases и bounds. ARH: независимо проверить состав/provenance, exact external test locator, manifest/checksums/readback; выдать собственный preservation receipt этого package. KOD self-check не заменяет ни один результат.
После обоих результатов — KOO fresh reconciliation; затем отдельное явное OPERATOR MAIN E2E authorization. До этого STOP. Runtime isolation и bootstrap cap должны быть закрыты до main admission. Никакого real ChatGPT continuity, project acceptance или доказанной эффективности Fast Memory сейчас нет.

## Journal-source

JOURNAL_CANDIDATE: yes
СМЫСЛ: Для проверки памяти появился материальный стенд: синтетическая незаконченная задача, её состояние, старая ошибка и инструмент независимой проверки. Теперь можно проверять сам стенд и сохранность пакета. Главный опыт смены контекста ещё не запускался — подготовленный инструмент не равен работающей Fast Memory.
EVIDENCE: immutable package выше; source для существующего RED journal-feed, без automatic journal inclusion/publication.

## Reusable experience candidate → существующий ARH layer

candidate_id: KOD-MEM-PREP-EXP-R01
related_existing_card: ARH-EXP-014
status: preparation_derived_candidate; runtime_unverified
lesson: Раздельные каталоги oracle/worker недостаточны сами по себе; проверяемая проекция должна исключать также design/provenance с готовым ответом, а runtime обязан запретить обход через public locator/whole-package mount.
next_time_behavior: зафиксировать allowlist, проверить фактический состав projection и denied reads, затем отдельно проверить OS/runtime boundary.
prohibited_repeat: называть logical projection доказанной process isolation или checksum-only readback доказательством continuation.
applicability: synthetic preparation and independent review, not validated runtime speedup/continuity.
provenance: exact package/TEST-RESULTS.json, contracts/isolation.json, verifier.py and test_preparation.py.
requested_ARH_action: dedup/update candidate against existing ARH-EXP-014; не создавать новый контур и не повышать до empirically validated без main evidence.

КТО: KOD v0.5. После routing/readback/post-write reconciliation STOP.
