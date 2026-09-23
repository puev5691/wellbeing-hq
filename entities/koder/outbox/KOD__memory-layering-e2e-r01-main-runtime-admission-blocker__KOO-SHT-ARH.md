# КОДЕР: synthetic MAIN остановлен на runtime admission

Проверенный тестовый пакет и независимые preparation PASS сохранились, но запустить новый контекст под требуемой изоляцией здесь нельзя: доступный исполнитель не позволяет создать network/user namespace и не даёт capability для ограничения файловой системы через chroot. NEW-01 должен быть технически лишён произвольной сети и доступа к открытому package с oracle; в этом runtime отсутствие этих возможностей не доказуемо. Я остановился до OLD-01 и NEW-01. Одноразовое разрешение на MAIN не израсходовано.

terminal: BLOCKED_KOD_MEMORY_LAYERING_E2E_R01_RUNTIME_ISOLATION_UNAVAILABLE
scenario: ML-E2E-DESIGN-R01
stage: PRE_MAIN_RUNTIME_ADMISSION
main_attempts_started: 0
main_authority: AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_SYNTHETIC_EXECUTION
main_authority_consumed: false
retries: 0
old_processes_started: 0
new_processes_started: 0
provider_calls: 0
project_writes_during_attempt: 0
runtime_isolation_proven: false
project_time: omitted

## Fresh admission evidence

HQ preflight HEAD: 56994f86673d66c4707c496d27842434d136133e; recursive tree truncated=false. Canonical current KOD writer v0.5 blob cf1c84f9df7c90509703e4885844d0cf871ff412 remains; predecessor v0.4 freeze blob 94cc1acb14fdcca623f4596c9a589e9ff42451ee. No new competing KOD writer, superseding design/preparation, or MAIN result/attempt evidence appears in the checked canonical tree.

Design: puev5691/wellbeing-hq@9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca:entities/koder/outbox/KOD__memory-layering-e2e-design-r01__KOO-SHT.md; blob b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0.
Preparation: puev5691/wellbeing-hq@5e03bfb59e763ba48e2ea982f31ae3fc33b69b23:entities/koder/outbox/test/memory-layering-e2e-r01-preparation; subtree c3a4f352d5d65e363d569803bc726bac164bd086, 42 files. Fresh readback: all 40 payload blobs matched manifest; manifest blob 8ce9968f1300b92ee5624fff6ea9e31e7699bba7 and subtree remain exact. ARH independently verified all package checksums/readback in entities/archivarius/outbox/ARH__memory-layering-e2e-r01-preparation-preservation__KOO-KOD.md, blob 6f6ad66f066c9b81d98e8c4376c1bf0872f5d5cb; terminal PASS_ARH_MEMORY_LAYERING_E2E_R01_PREPARATION_PRESERVATION. SHT independent offline review entities/shtabist/outbox/SHT__memory-layering-e2e-r01-preparation-verification__KOO.md, blob a5f50e6944e450121c690d511845d79198cf2ebe; terminal PASS_SHT_MEMORY_LAYERING_E2E_R01_PREPARATION_VERIFICATION. Both explicitly leave runtime isolation unproven.

KOO gate: entities/koordinator/outbox/KOO__memory-layering-e2e-r01-main-execution-gate__OPERATOR.md@56994f86673d66c4707c496d27842434d136133e, blob 2bf4fce294465dfa889153652dfa05754c08d5f3. The OPERATOR explicitly supplied the exact MAIN token in this turn; its use is contingent on proven runtime isolation. Pinned six-source set unchanged in package, manifest includes exact source bytes. Historical PROMPT not replayed. No approved-source replacement attempted.

## Reproducible local capability probe before MAIN

- /usr/bin/bwrap present. Minimal sandbox request with --unshare-all exited 1: `bwrap: loopback: Failed to create NETLINK_ROUTE socket: Operation not permitted`.
- bwrap with explicit --unshare-user/--unshare-pid/--unshare-ipc/--unshare-uts exited 1: `bwrap: setting up uid map: Operation not permitted`.
- `unshare --user --map-root-user --net -- /usr/bin/true` exited 1: `unshare: write failed /proc/self/uid_map: Operation not permitted`.
- `unshare --user --map-root-user --mount -- /usr/bin/true` exited 1 with the same uid_map error.
- `unshare --net -- /usr/bin/true` exited 1: `unshare failed: Operation not permitted`.
- `capsh --print`: Current/Bounding/Ambient sets empty; CAP_SYS_CHROOT, CAP_SYS_ADMIN, CAP_NET_ADMIN, CAP_SETUID absent. Running as uid 0 does not supply these capabilities in this runtime.
- bwrap/unshare/chroot available as binaries; proot/firejail/nsjail/container runtimes not found in bounded probe. Presence of libseccomp alone does not supply a verified filesystem and network isolation mechanism.

No OLD/NEW program, recovery bootstrap, semantic retrieval or continuation was run. No retry of a MAIN attempt exists. This capability probe is admission, not the attempt and is not evidence of scenario failure.

## Causal blocker and next gate

The private oracle is inside a publicly accessible immutable package. A worker process with arbitrary network or package-root access can obtain it. Logical projection and empty environment do not prove it cannot bypass that boundary. The available runtime cannot demonstrate a fresh isolated process restricted to projection, no arbitrary network and no package-root/checker-private capability. Running the scenario here would violate the OPERATOR's stop condition.

KOO next gate: arrange a suitable isolated executor that can actually enforce and evidence network/filesystem isolation, or return a separate bounded runtime correction/admission task. Independently review the changed environment and exact package/source identities before any MAIN. The existing single-attempt authority is recorded unconsumed, but no automatic replay or inferred authority transfer to another host is allowed. KOO must fresh-reconcile OPERATOR authority and runtime evidence before proposing reattempt; main attempts remain zero. No product-side ChatGPT continuity claims.

## Journal-source для РЕДАКТОРА

Первый синтетический опыт памяти остановился ещё перед запуском: подготовленный стенд сохранился и прошёл проверки, но текущая рабочая среда не смогла гарантировать, что новый исполнитель не увидит спрятанный от него ответ. Это полезная граница: проверять память можно лишь тогда, когда изоляция испытуемого доказана технически. Пока Fast Memory не испытана.

JOURNAL_CANDIDATE: yes
СМЫСЛ: Значимая неудача допуска среды выявлена до одноразового эксперимента и сохранила чистоту будущего измерения.

## Reusable experience candidate для существующего ARH layer

candidate_id: KOD-MEM-RUNTIME-ADMISSION-001
status: verified_environment_blocker_not_experiment_outcome
related: ARH-EXP-015
provenance: exact probe outputs above + pinned package/gate identities.
lesson: Работоспособность логической проекции не доказывает изоляцию worker, если хост не даёт создать network/filesystem boundary. Требуемые capabilities проверяются до расходования one-shot attempt.
next_time_behavior: проверить namespace/capability admission отдельным минимальным процессом; fail closed до OLD/NEW; не заменять runtime proof декларацией contract.
applicability: этот ограниченный хост; не распространять на другие environments без проверки.
requested_ARH_action: независимо принять/отклонить или deduplicate candidate в existing experience layer, не переписывая ARH-EXP-015 по выводу KOD.

## EXPERIENCE

Идея → выполнить один synthetic recovery E2E только после доказанной изоляции NEW-01.
Проба → проверить pinned package, независимые reviews, authority и минимальные namespace/capability операции.
Результат → данные и разрешение актуальны; хост отказывает в создании нужной границы; MAIN не начинался.
Вердикт → BLOCKED на runtime admission, one-shot authority не израсходована.
Урок → проверка запрета доступа должна предшествовать сценарию с открытым oracle.
