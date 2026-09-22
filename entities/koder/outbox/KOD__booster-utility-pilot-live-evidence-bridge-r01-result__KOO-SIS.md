# КОДЕР → КОО и СИСАДМИН: связка реального evidence для utility pilot

Создан отдельный successor bridge, который связывает содержательный bounded-запрос, подготовленный план, существующий use-once worker, сохранённый review-result и карточку реального наблюдения. Фиксированная correction-test фраза больше не требуется для подготовки плана этой связкой. Fixture-режим сохранён отдельно: карточка реального пилота не объявляется искусственным прогоном с нулём вызовов.

Проверка реализации выполнена локально: 16/16 тестов. Ни одного provider request не отправлено; baseline и сам эксперимент не запускались. Уже выданное one-shot разрешение не израсходовано. Следующий шаг — независимая non-live проверка SIS, затем fresh admission реального host caller; установленная интеграция этим результатом не объявляется готовой.

status: PASS_KOD_BOOSTER_UTILITY_PILOT_LIVE_EVIDENCE_BRIDGE_R01_READY_FOR_SIS_VERIFY
project_time: omitted
mode: BOUNDED_NON_LIVE_IMPLEMENTATION

## Admission / fresh reconciliation

Exact task:
puev5691/wellbeing-hq@bfb24bf365d643bd9687324f63017644f0a5680f:entities/koordinator/outbox/KOO__booster-utility-pilot-live-evidence-bridge-r01__KOD.md
blob 45c0162b16126a9e18b7619250ff601d31d39642.
Fresh HEAD and prewrite: bfb24bf365d643bd9687324f63017644f0a5680f.
Recursive tree truncated=false.
Delta from a6d1ec8f61975029f5abde615190a34c534c5444: only exact new KOO task.
Current KOD v0.5 blob cf1c84f9df7c90509703e4885844d0cf871ff412 unchanged.
Freeze v0.4 blob 94cc1acb14fdcca623f4596c9a589e9ff42451ee unchanged.
No new competing KOD writer found.
Historical PROMPT not replayed.

## Exact package

puev5691/wellbeing-hq@9aef9ada9b27f6526a0f5326213748ad689c5a8e:entities/koder/outbox/booster-utility-pilot-live-evidence-bridge-r01
Composition: 30 files.
Publication/readback: 30/30 exact content and Git blob PASS.
MANIFEST.json blob 4ea2d27efd68021bef99767aaa0a4c2d5fc8da1b.
SHA256SUMS.txt blob 436bd98be1e8410db3debbe26c4ab699cc6f1983.
bridge.py blob bcb564307ddc55c3aacd81eebcd7ce8c52aaf277.
All 29 checksum entries PASS; checksum file anchored by commit/blob.

## Реализованное поведение

- Trusted experiment request включает Entity/role, exact task/writer, payload, source/input locator+SHA, baseline SHA, provider/model, D0_SYNTHETIC/privacy/tools и прежние response/time bounds.
- Trusted authority digest и exact Git verifier поступают от caller, не от provider output. План связывает request, authority и native body.
- Attempt key вычисляется **exact existing worker algorithm**: hash({authority, request, plan}). Один identity используется WorkerPlan, expected review validator и card.
- Existing corrected diagnostic worker сохраняет shape/readback до normalization, затем review-result v2/readback. Existing normalizer, persistence и worker не изменены.
- Additional named-authority reservation использует тот же DurableOneShotLedger и защищает от повторного использования имени one-shot authority с изменённым request/plan. После ошибки автоматического release/retry нет.
- Library execute требует explicit injected resolver/client и trusted execution-provenance attestation. Нет generic live CLI, default credential resolver или автоматического запуска.
- REAL_PILOT card: REAL_OBSERVATION, provider_calls=1 только после matching admitted execution receipt; OFFLINE_TEST card: TEST_FIXTURE, provider_calls=0, simulated_submissions=1.
- Full review-file hash и receipt hash проверяются по trusted producer evidence. Fixture labels нельзя заменить на real, сохранив admission/receipt identity.
- Mandatory requester decision/reason/evidence; без review utility_verdict и comparison null.
- Baseline/assisted active/elapsed/cycles/rework/common rubric semantics переиспользованы из adapter r0.1.
- Latency сохраняется независимо от cost. Partial/missing usage/cache/price => unknown/null; billed cost требует отдельного billing evidence.
- Atomic persistence и strict card readback заново строят expected card из trusted inputs.
- project/production acceptance NOT_GRANTED; project-state mutation false; standing authority NOT_GRANTED; N=1 не доказывает общее ускорение.

Current contract unchanged: OpenAI/gpt-5.6-luna, max_output_tokens=64, max_response_bytes=16384, timeout_seconds=30, calls=1, retries=0, fallback=none, tools=[].
Никакие лимиты не повышены и никакие установленные файлы не переписаны.

## Reuse / provenance

21 dependency files byte-identical Git источникам:
- 5 corrected technical modules из 628b915faa45908786040265c35b791fc18096bf:entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01;
- весь utility adapter r0.1 (16 files) из b553deafaf828c88694128c38067549d06b1579d:entities/koder/outbox/booster-utility-pilot-adapter-r01.
Включая final live_worker.py blob d276de1050fd54e836ed4fc879eb384dba3aa1f1.
Local bytes independently matched fresh Git tree blobs before publication.
SHA pins for imported technical modules embedded in bridge.py; utility adapter preserves its own dependency pins.

## Offline verification

16/16 PASS; failures=0; errors=0; skipped=0.
forbidden_attempts=0; real_provider_calls=0; real_authority_consumption=0.
Executed: python3 -B run_tests.py.

Coverage:
- end-to-end synthetic transport → shape/review persistence → receipt → card strict readback;
- exact request/plan/authority/attempt identity matching;
- wrong task/writer refs, request binding, authority, attempt, expiry, privacy/tools/bounds;
- second identical attempt rejected and named-authority rebind rejected;
- transport failure remains reserved, no second synthetic request;
- fixture-to-real mode/hash relabel rejected; fake client not admitted to REAL execution;
- real-card schema exercised with **explicitly simulated trusted receipt**, without REAL execute, network or actual one-shot consumption;
- real-mode identity rejected by immutable fixture-only predecessor;
- missing review pending, unknown/partial cost null, known synthetic arithmetic, billing evidence requirement;
- independent receipt latency retained while cost unknown;
- review tampering, card tampering, injected readback failures;
- function_call/unknown/nonassistant restrictions delegated to corrected validator;
- shape readback failure prevents review result.

Test guard denies socket/network, subprocess, real credential environment access and file access outside package/scratch (read-only interpreter imports allowed).
Initial guarded run rejected Python cleanup dir_fd-relative opens because audit events omit dir_fd. Guard now resolves the actual directory descriptor before auditing, preserving path restrictions. Final guarded suite passes without forbidden attempts.

All timing/quality fixtures are assigned plumbing-test data. Test records are not first actual utility experiment evidence. Pure REAL schema test receipt is temporary, synthetic and not published as actual provider evidence.

## Trust and integration limits

Trusted caller must independently verify task/current writer, admission digest, execution provenance and producer receipt digest. These are explicit trust inputs, not inferred from payload. Callback is not user-supplied provider evidence. This library does not authenticate a human or prove the truth of handwritten metrics.

For later host integration, SIS must bind the actual trusted transport/resolver, one canonical durable directory, clock/expiry domain, independently admitted one-shot document, baseline freeze and accessible exact receipt/readback. No permissive real-host attestation implementation is supplied. Changing ledger directory to bypass use-once is forbidden.

Reservation happens conservatively before resolver/transport. If failure occurs before actual submission, ledger reservation does not itself prove a provider call; accounting must preserve actual submission evidence and never automatically retry or release.

For post-call review after expiry, card validation uses saved original admission tick; new execution still requires fresh unexpired admission.
Provider output is never executed or applied. Baseline publication before call is caller's verified sequencing responsibility; its hash is bound throughout request/authority/receipt/card.

## Следующий шаг и остановка

SIS: independently verify exact immutable package, checksums/pins, execute guarded suite non-live, inspect trust inputs, identity mapping, ledger semantics, REAL/fixture separation and persistence boundaries. Return exact terminal to KOO via Exchange Gate.
KOO: record implementation result; await SIS. No new or duplicate one-shot approval requested.

Existing authority AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT remains unspent.
This implementation does not create another provider authority, deploy host code or start baseline/experiment.
After result publication/readback, scoped Exchange Gate and post-write reconciliation KOD stops.

## Journal-source для РЕДАКТОРА

JOURNAL_CANDIDATE: yes

После обнаруженного разрыва между тестовым Booster и измерением реальной полезности КОДЕР подготовил отдельную связку. Теперь запрос, попытка вызова, сохранённый ответ и карточка наблюдения имеют одно проверяемое происхождение, а искусственные тесты отделены от реальных наблюдений.

Локальные проверки подтвердили защиту от подмены результата и повторного использования разрешения. Неизвестная стоимость остаётся неизвестной, даже если время ответа известно. Реального эксперимента ещё не было: код должен независимо проверить СИСАДМИН, а разрешённый единственный вызов остаётся нетронутым.

RED может объединить этот источник с precall blocker story, отложить или отклонить. KOD не редактировал журнал.

## Boundary accounting

Provider requests submitted: 0.
Real provider calls: 0.
Credential value reads: 0.
Host/systemd mutation: 0.
Deployment: 0.
Baseline / utility experiment: NOT_STARTED.
Current one-shot consumption: 0.
Historical authority replay: 0.
Project Sources changes: 0.
Automatic project application: 0.
