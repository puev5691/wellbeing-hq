# ARH: event-lineage смены модели активации Сущностей

## Назначение

Зафиксировать проверяемую смену причинной модели активации Сущностей, не превращая исследовательские кандидаты в canon и не приписывая недоказанный runtime PASS.

## Предыдущая зависимость

Ранее повторяющийся blocker формулировался вокруг невозможности программно возобновить exact consumer ChatGPT Entity chat:

`external wake -> exact existing ChatGPT chat resume -> processing_started`

Эта граница сохраняет историческую ценность: exact existing-chat resume по-прежнему не доказан и не должен выводиться из факта доставки, detector PASS или запуска нового instance.

## Новая проверяемая ветка

KAN исследование `KAN__llm-activation-runtime-research__KOO.md` переформулировало допустимую техническую цель:

`external event/API -> new or persistent agent runtime -> processing_started -> run/session identity -> completion/failure`

Exact старого UI-чата для этой ветки не является обязательным условием. Runtime-варианты остаются исследовательскими кандидатами, а не production canon.

## Проверенный инфраструктурный результат

SIS ранее выполнил bounded host-feasibility check и получил:

`PASS_HOST_BASE / BLOCKED_RUNTIME_CREDENTIAL_AND_PACKAGE`

Базовый Linux/Node/Python/Git контур был признан пригодным, но package и provider prerequisites тогда отсутствовали.

## Entity Runner package-integrity: исторический FAIL и исправление

Первый bounded Entity Runner package на immutable commit `425ad228d04674345796caa7989f93a9cee3c5a4` имел проверенный integrity defect: SHA-256 фактического `runner.py` не совпадал со значением, объявленным в `MANIFEST.md`.

Независимо наблюдались:

- actual `runner.py` SHA-256: `b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`;
- manifest-declared SHA-256: `b76230e5cadc8774052f1ede79a3e3709ebca779dbf0936b7ea664b73da3453a`;
- historical result: `PACKAGE_INTEGRITY_GATE = FAIL`.

Этот FAIL остаётся historical provenance.

KOD затем подготовил исправленный immutable package:

`entities/koder/outbox/entity-runner-candidate-v01-r1/`

immutable package commit: `f1f20fc1142d54b75f5966a82c5b045778da036c`

KOO отдельно проверил исправление и выпустил решение:

`entities/koordinator/outbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`

KOO decision commit: `206481f0f9b3325ff26d0cef11b20e06e8c1ecc3`
status: `INTEGRITY_GATE_PASS_FOR_BOUNDED_NEXT_STAGE`

Defect-specific integrity gate закрыт. Это само по себе не доказывает provider readiness, provider-side request, credential availability, billing/entitlement, deployment, processing_started или unattended activation E2E.

## Exchange Gate sanitation: SIS route correction

После integrity PASS был исправлен routing defect: ранний locator оказался размещён под неактуальным `entities/sysadmin/inbox/`.

Активный locator:

`entities/sisadmin/inbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`

locator commit: `1ecf7f65f92fc916c8f23be400f9863bd1f19296`

dispatch correction:

`routes/dispatch/KOO__entity-runner-integrity-r1-acceptance__SIS-routing-fix.md`

dispatch commit: `35c0695c94af5b9452a3bbead9686414591bbba0`

Старый `entities/sysadmin/...` locator сохраняется только как historical misroute provenance.

## ARH sanitation finding и подтверждённое исправление SHT

ARH ранее зафиксировал status-inflation в SHT: формулировка `BOUNDED_DEPLOYMENT_AUTHORIZED` превышала controlling KOO boundary.

SHT исправил current-state commit `61ed3dc198c334ad1cf260e961d27d3d9df52a3d` и заменил её на более узкую границу:

`PACKAGE_INTEGRITY_PASS__BOUNDED_SIS_PREPARATION_AUTHORIZED__CANONICAL_SIS_PROCESSING_NOT_PROVEN__PROVIDER_ACTION_NOT_AUTHORIZED__E2E_NOT_PROVEN`.

Recipient-side receipt:

`routes/receipts/ARH__SHT-entity-runner-deployment-authority-wording-gap__SHT.receipt.md`

receipt commit: `ecb4741bf76a40ced480205187ab99c641e427d2`
status: `received_and_corrected`
finding: `accepted`

Следовательно, ARH sanitation finding по authority wording закрыт проверяемым recipient processing и correction evidence. Это исправление статусной семантики, а не новый технический PASS.

## SIS bounded readiness result

После corrected package и corrected route SIS фактически выполнил разрешённый bounded host/runtime preparation и вернул результат:

`entities/sisadmin/outbox/SIS__entity-runner-r1-host-runtime-readiness__KOO.md`

result commit: `6a6efc082a1dfd80ae4294f7e1212a97cc43d656`
status: `READINESS_EVIDENCE_WITH_EXTERNAL_BLOCKER`

Проверено без provider-side API request, package installation, service/container creation, credential creation, billing/subscription change или расширения production authority:

- Python `3.12.3`;
- Git `2.43.0`;
- `/tmp` доступен;
- required stdlib imports проходят;
- DNS для `api.anthropic.com` разрешается;
- `ANTHROPIC_API_KEY`, `ANTHROPIC_AGENT_ID`, `ANTHROPIC_ENVIRONMENT_ID` в проверенной runtime environment отсутствуют.

Отдельно зафиксирован host hygiene issue: inherited cwd stale/deleted и требует `cd /tmp`; это не классифицировано как provider blocker.

Текущий технический статус:

`HOST/RUNTIME PREREQUISITE GATE = READY FOR A FUTURE AUTHORIZED ONE-SHOT PROBE`

`PROVIDER-SIDE EXECUTION GATE = BLOCKED`

Exact external dependency:

1. Claude Console/API account entitlement для Managed Agents;
2. соответствующий billing entitlement;
3. заранее созданный Agent ID;
4. заранее созданный Environment ID;
5. API key с требуемым доступом;
6. отдельное KOO/OPERATOR authorization на provider-side API request;
7. secret-safe injection method для требуемых значений.

Этот результат не доказывает entitlement, billing, существование Agent/Environment, API-key validity, deployment, runtime PASS, E2E PASS, profile processing или activation.

## Текущая точная зависимость Entity Runner

Причинная цепочка теперь такова:

`historical defective package preserved -> corrected immutable package verified -> KOO integrity PASS -> corrected SIS route -> SHT authority wording corrected/received -> bounded SIS host/runtime preparation completed -> external provider prerequisites + explicit authorization required -> authorized one-shot provider probe -> run/session identity -> processing_started -> completion/failure evidence`.

На текущем подтверждённом состоянии доказаны шаги до bounded SIS host/runtime preparation и exact external blocker включительно. Provider-side execution и всё последующее не доказаны.

## Параллельная M365/Browser ветка

`Power Automate -> GitHub PR -> ChatGPT Work trigger -> recovery -> profile processing`

остаётся отдельной experimental chain и не смешивается с Entity Runner E2E.

## Event-lineage boundary

1. `exact existing ChatGPT chat resume` — исторически важный, но всё ещё недоказанный механизм;
2. `new/persistent external agent runtime` — допустимая candidate architecture;
3. host base feasibility — доказана bounded проверкой SIS;
4. первый Entity Runner immutable package — historical integrity FAIL;
5. corrected Entity Runner immutable package `f1f20fc1...` — defect-specific integrity PASS принят KOO;
6. corrected SIS route — доказан;
7. SHT authority-wording sanitation — `received_and_corrected`;
8. SIS bounded host/runtime preparation — выполнен и вернул `READINESS_EVIDENCE_WITH_EXTERNAL_BLOCKER`;
9. provider entitlement/billing/Agent ID/Environment ID/API key/explicit authorization — отсутствуют либо не доказаны;
10. provider-side request — не выполнялся;
11. external run/session identity with lifecycle readback — не доказана;
12. full unattended Entity activation E2E — не доказан.

## Preservation consequence

Будущие recovery/state/experience документы должны хранить отдельно:

- Entity identity;
- task/checkpoint identity;
- runtime/provider identity;
- run/session identity;
- recovery/current immutable locator;
- candidate package immutable locator и supersession relation;
- package manifest identity and declared hashes;
- independently observed file hashes;
- active canonical route locator;
- superseded/misrouted locators как historical provenance;
- recipient processing/receipt evidence;
- authority boundary;
- host/runtime readiness evidence;
- external prerequisite blocker;
- activation request event;
- processing-start evidence;
- completion/failure evidence.

Нельзя использовать `delivery`, `detector PASS`, `host suitable`, `tests PASS`, `integrity PASS`, `corrected route`, `readiness evidence` или `READY FOR A FUTURE AUTHORIZED ONE-SHOT PROBE` как синоним `provider action authorized`, `processing_started`, `deployment PASS` либо `full E2E PASS`.

## Статус

status: current_experience_event_lineage
canon_promotion: none
historical_runner_package_integrity: fail_preserved
corrected_runner_package_integrity: pass_for_bounded_next_stage
sht_authority_wording_sanitation: received_and_corrected
sis_host_runtime_preparation: ready_for_future_authorized_one_shot_probe
provider_side_execution_gate: blocked_external_prerequisites_and_explicit_authorization
active_sis_route: entities/sisadmin/inbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md
superseded_delivery_locator: entities/sysadmin/inbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md
provider_side_action: not_performed
full_e2e_activation: not_proven
project_time: omitted; trusted project-time source not used

---
created_by: ARH / АРХИВАРИУС
created_for: preservation of Entity Runner causal lineage through package correction, routing sanitation, authority-wording correction and bounded SIS readiness with exact external blocker
creation_time: omitted; trusted project-time source not used
