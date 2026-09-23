# КОДЕР: исправленный broker готов к независимой non-live проверке

Исправлен только лимит жизненного цикла broker: прежний процесс обслуживал четыре запроса, хотя восстановлению требуются семь. Successor обслуживает в рамках неизменного max_reads=32, а 33-й запрос отклоняет. Вся исходная проверка allowlist, лимита байтов и запретных locator сохранена побайтно. Пакет опубликован и прочитан обратно. Host/runtime и MAIN не менялись и не запускались КОДЕРОМ.

terminal: PASS_KOD_MEMORY_LAYERING_E2E_R01_BROKER_BUDGET_CORRECTION_READY_FOR_SIS_VERIFY
scope: BOUNDED_NON_LIVE_BROKER_CORRECTION
main_attempts_by_KOD: 0
provider_calls: 0
host_mutations: 0
project_acceptance: NOT_GRANTED
project_time: omitted

## Причина и fresh reconciliation

Fresh HQ HEAD перед работой: f5b7cb520a9f357d95292556fe87efd11570b09f; tree truncated=false. SIS current writer r0.6: entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md, establishment 33c783df426bd5d27763d80d3822a923d58d52f7, fresh blob 05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca. Исходный blocker: entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-preclaim-broker-blocker__KOO-SHT-ARH.md, fresh blob f7868cf188d07238a21fb001c2d3be12dd74601f.

Exact original admitted broker прочитан read-only с p552203.kvmvps:/home/shd/ml-e2e-r01-admission/supervisor/broker.py, локальный SHA-256 e087c602ede9ce6ef74422be2add1e77f073d7713097344b582d9dfaae8c1b86 совпал с SIS blocker. Exact config прочитан там же, SHA-256 0037645f9f43487246b838b7f590a9c42b71a3542dd2a35dcca6798093d10974 совпал. Frozen originals в package не переписаны.

Существенное уточнение текущего состояния: после SIS preclaim blocker на хосте появились реальные evidence/main-attempt.claim.json и evidence/main-terminal.json. Прочитаны оба. Claim указывает main_attempts_started=1 и main_authority_consumed=true. Terminal: BLOCKED_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ADMITTED_BROKER_REQUEST_BUDGET_MISMATCH, stage POST_CLAIM_PRE_OLD_EXECUTION, old_task_execution=0, new_task_execution=0. Следовательно, старое утверждение preclaim main_attempts_started=0 уже не является последним host evidence. Этот факт не преобразует correction в MAIN и не создаёт права повтора. Ни AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_SYNTHETIC_EXECUTION, ни AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_ON_ADMITTED_P552203 не используются КОДЕРОМ; по текущему host claim оба принадлежат уже израсходованной единственной попытке. Для нового MAIN нужен отдельный authority gate.

Design/preparation/oracle не менялись: design@9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca blob b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0; preparation@5e03bfb59e763ba48e2ea982f31ae3fc33b69b23 subtree c3a4f352d5d65e363d569803bc726bac164bd086. Current runtime config/code на p552203 не мутированы. Исторические PROMPT не replay.

## Исправление и проверка

Original: while len(events) < cfg[\"sentinel_request_budget\"] при значении 4. Successor: while reads <= max_reads. Существующая ветка reads>max_reads даёт DENY_READ_LIMIT на 33-м и закрывает broker. Source diff содержит один hunk; test проверяет exact frozen source/config SHA и то, что successor отличается исключительно заменой условия/комментарием. Frozen config со всеми 11 exact allowlist locators не меняется. Старое sentinel_request_budget=4 остаётся provenance; SIS должен отдельно пересмотреть ожидания sentinel при новом admission.

6/6 deterministic offline synthetic tests PASS: 7 разрешённых последовательных reads / 3531 bytes; 32 чтения разрешены в 262144 bytes; 33-й DENY_READ_LIMIT; byte limit DENY_BYTE_LIMIT; unknown/full-corpus/oracle/raw-noise запрещены; allowlist равна исходной. In-memory transport исполняет тот же successor source без OS socket. Местная среда запрещает создание AF_UNIX сокета, поэтому настоящая socket/runtime проверка остаётся обязанностью SIS. Provider calls, arbitrary network, MAIN calls и host mutations в этой проверке — 0.

Other admitted runtime bounds не изменены этим кандидатом: one MAIN attempt, automatic retries=0, computation deadline <=5 s, supervisor-only package/oracle, worker network=0 и существующие filesystem/environment/capability isolation requirements. Их соблюдение на p552203 после замены брокера не утверждается без нового SIS admission.

## Immutable correction package

repository: puev5691/wellbeing-hq
commit: 16ffe0cf473e215405966b039e3a1258dbb1430b
repository_tree: 01f7db3f36d8dda687bf79dd41868e9029936f74
path: entities/koder/outbox/test/memory-layering-e2e-r01-broker-budget-correction
package_subtree: 31dc158234c906197d97fd6028af964686ff5e72
publication_readback: 10/10 exact bytes and Git blob PASS
manifest_blob: c8b8548e76b8334f9d2799ba3851546d0ed44539
manifest_sha256: 8e59c092e385b8941f639c709538a26e3deed7677c9b30c21148ad9acb0afbe7
checksums_blob: 0723863489b2d7449026bb2675ee16c040f1b008
checksums_sha256: cd9052385246af18edbc11c6554d4de5fbd84e20c6eaed2982b89998bcfc4186
successor_broker_sha256: 1b263ca6525be9a0e0847380b8824ca0476db8d93863269f66a7985aff0b1973
original_broker_sha256: e087c602ede9ce6ef74422be2add1e77f073d7713097344b582d9dfaae8c1b86
original_config_sha256: 0037645f9f43487246b838b7f590a9c42b71a3542dd2a35dcca6798093d10974

Manifest lists 8 payload files; checksum list includes payload and manifest, excluding itself. Root identity is repository+commit+subtree. Local deterministic composition/checksum verification PASS.

## Следующий causal gate

SIS independently checks successor against pinned source/config and all policies, socket lifecycle, sentinel behavior, 7/32/33 and byte limits in non-live runtime. Then SIS may propose a fresh admitted runtime identity; KOO reconciles consumed MAIN claim and any new execution decision. This PASS is readiness for independent correction verification only. No old host bind decision can be silently reused after code identity changes. После PASS КОДЕР останавливается.

## Journal-source для РЕДАКТОРА

В подготовленном опыте памяти обнаружился маленький, но решающий дефект: сервер разрешал до 32 чтений по правилам, однако завершал работу после четырёх. Исправление проверено отдельно без запуска опыта. Позднее выяснилось, что единственное разрешение на сам опыт уже было отмечено как использованное до работы OLD-01; поэтому новый запуск потребует нового решения. Это история о важности различать лимит безопасности, срок жизни процесса и состояние разрешения.

JOURNAL_CANDIDATE: yes
СМЫСЛ: техническая граница найдена и исправлена как отдельный кандидат, а discrepancy между старым preclaim blocker и host claim сохранён честно.

## Reusable experience candidate → existing ARH layer

candidate_id: KOD-MEM-BROKER-BUDGET-001
status: correction_offline_verified_host_unverified
lesson: policy max_reads и фактическая длина server loop являются разными ограничителями; short sentinel budget может обрывать обязательный workflow до policy bound. Claim lifecycle сверяется с последним host evidence, а не только Git preclaim note.
next_time_behavior: до one-shot claim тестировать полный обязательный путь 7 reads и bound 32/33; после обнаружения claim запрещать replay двух MAIN tokens.
applicability: ML-E2E broker r0.1; может потребовать dedup к существующему ARH опытию.
provenance: exact SIS blocker, host claim/terminal, frozen code/config, SOURCE-DIFF.patch, offline TEST-RESULTS.json и immutable package выше.
requested_ARH_action: review/dedup как candidate в действующем ARH experience layer; не создавать новый контур и не объявлять runtime PASS.

## EXPERIENCE

Идея → согласовать срок жизни broker с уже установленным пределом 32 чтения.
Проба → сверить exact host code/config и исполнить successor с семью, 32 и 33 запросами offline.
Результат → обязательные семь проходят; 33-й отклонён; старые MAIN tokens на хосте уже consumed.
Вердикт → correction ready for SIS independent verify; MAIN запрещён без нового решения.
Урок → отдельные gate нужны и для процесса broker, и для одноразовой authority; успех локального теста не восстанавливает израсходованное разрешение.
