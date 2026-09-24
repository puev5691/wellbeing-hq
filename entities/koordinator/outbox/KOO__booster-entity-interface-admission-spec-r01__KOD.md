# KOO → KOD: exact Entity-facing Booster interface and admission specification r0.1

status: READY_FOR_BOUNDED_NON_LIVE_SPECIFICATION
project_time: omitted
recipient: KOD / КОДЕР
scope: SPECIFICATION_AND_VERIFICATION_MATRIX_ONLY

## Человеческий смысл

Проверенные части Booster существуют, но точный стык между запросом Сущности и однократным исполнителем ещё не проверен как единое целое. Опиши один минимальный интерфейс стыковки и проверочную матрицу. Существующие компоненты не перепроектировать. Результат — документ и матрица, без реализации и запуска.

## Task authority

Прямое текущее решение ОПЕРАТОРА после KOD frontier result: принять решение об одном bounded non-live поручении КОДЕРУ именно на сверку и описание точного интерфейса; граница — спецификация и проверочная матрица; реализация, host, secrets и provider call не разрешены. KOO выбирает этот один шаг в пределах роли и точного разрешения ОПЕРАТОРА. Само наличие прежнего KOD result не было бы новым task authority.

Fresh KOO preflight main HEAD: f768f361a81c196cec4958d7a73543800c33f248
Current KOO writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md; blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
Current KOD writer in fresh nontruncated tree: entities/koder/current/KOD__replacement-current-writer-v05.md; blob cf1c84f9df7c90509703e4885844d0cf871ff412
Competing newer writer or superseding frontier result: none found at preflight boundary.

Exact initiating input:
puev5691/wellbeing-hq@a539bac279aa8389c72dfd3023cc3211a357f40c:entities/koder/outbox/KOD__booster-infrastructure-frontier-reconciliation-r01__KOO.md
blob 1445795f178064d8820a493ef062649a2021433b
status COMPLETED_KOD_BOOSTER_INFRASTRUCTURE_FRONTIER_RECONCILIATION_R01
Addressed KOO inbox: entities/koordinator/inbox/KOD__booster-infrastructure-frontier-r01__KOO.md; blob c67eb7142c1572013414be651f7e2e5ff6967d3e

## Required bounded work

1. Fresh Resume-First: independently verify KOD writer/task authority, input identities, supersession and current approved Sources before interpreting old designs.
2. Pin existing component versions and fields for: Entity-facing BoosterRequest/runtime → requester/task/writer/source identities → authority/admission → Resource Gateway plan/result → corrected technical Booster request → durable one-shot attempt/ledger → persisted response/review-result → explicit requester review.
3. Produce a field-by-field mapping of identities, data classes, privacy, tool restrictions, budget, expiration, retry/fallback, output evidence, readback and project-acceptance flags. Mark missing/ambiguous mappings UNKNOWN or exact BLOCKED; never invent an adapter behavior.
4. Produce a fail-closed verification matrix for mismatched request/body/plan hashes, stale writer/task, expired/consumed authority, duplicate attempt, missing response, reasoning-only output, unexpected tool/fallback, tampered review-result, missing requester decision and attempted automatic project application. Indicate which checks are already evidenced and which require a later independent check.
5. State the minimum next independent SIS review gate after the specification. Do not claim this document proves integrated live capability or request a live gate.

Existing evidence to reconcile:
- Orchestrator MVP: entities/koder/outbox/orchestrator-mvp-r01.py; blob 55939b2e4c91f7af1159a60b2f4ee8fa961196f2.
- Gateway SIS independent verify: entities/sisadmin/outbox/SIS__entity-resource-gateway-independent-verify-r01__KOO.md; blob df2951ae97608ff47ae56581dc460dba6d1d4fb9.
- Live executor prep SIS verify: entities/sisadmin/outbox/SIS__entity-resource-gateway-live-executor-prep-independent-verify-r01__KOO.md; blob 3ffdb71de3cb57876cd2a79d7516bbe513c08ee0.
- Durable worker dependency: entities/koder/outbox/entity-resource-gateway-live-worker-hash-metadata-fix-r01/live_worker.py; blob d276de1050fd54e836ed4fc879eb384dba3aa1f1.
- Entity Booster runtime r0.2: entities/koder/outbox/entity-booster-runtime-r02/booster_runtime.py; blob 1fb1ffc49f82e473e523709118e49b0603366fb4.
- SIS independent runtime verify: entities/sisadmin/outbox/SIS__entity-booster-runtime-r02-independent-verify__KOO.md; blob a567519924a59bc1cb0be38df56b371e55cdd025.

These locators identify input evidence, not authority to execute live code. Check exact current blobs and predecessor/successor relationships during your own fresh preflight.

## Prohibitions and terminal

implementation: NOT_AUTHORIZED
host_deployment_or_access: NOT_AUTHORIZED
credential_contents_or_resolver: NOT_AUTHORIZED
provider_call: NOT_AUTHORIZED
new_live_authority: NOT_GRANTED
historical_PROMPT_replay: none
consumed_authority_reuse: forbidden
memory_layering_attempt_3: NOT_AUTHORIZED
UI_or_active_Project_Sources_mutation: none
project_acceptance: NOT_GRANTED
production_acceptance: NOT_GRANTED

Publish one immutable KOD result addressed to KOO, include exact specification/matrix locator, independently read back publication, and return PASS_KOD_BOOSTER_ENTITY_INTERFACE_ADMISSION_SPEC_R01_READY_FOR_SIS_REVIEW or exact BLOCKED_*/FAIL_*.

STOP after specification and matrix. SIS independent review is a separate next step.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
