# Candidate amendment r0.4 к recovery-канону v1.4
## Единая процедура Wake → Resume / Initiation → Writer Gate → Exact Task

status: `CANDIDATE_FOR_FINAL_RECOVERY_RECHECK`
proposed_target: `entity-state-preservation-and-recovery-canon-v1_5`
effective: `false`
canon: `no`
supersedes_candidate: `entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r03.md@fa92a24e89ef289689f28f2ebff034cf8279db34`
process_review: `entities/shtabist/outbox/SHT__entity-wake-initiation-resume-process-review__KOO.md@60592e7aacf7a4c2dfb6a322bc88988cc8aabbf7`
authority_review: `entities/kancelar/outbox/KAN__entity-wake-initiation-resume-authority-review__KOO.md@4e2820f651466029092da05150c3e0fe715fc8ca`
recovery_review: `entities/archivarius/outbox/ARH__entity-wake-initiation-resume-recovery-review__KOO.md@c8ee19c1e4456aa5ad137fb7b157fb08ddd78bac`
project_time: omitted; trusted project-time source not used

## Смысл

Пробуждение Сущности не запускает профильную работу. Оно запускает единую проверяемую процедуру определения режима экземпляра, recovery-состояния, полномочий и одной актуальной exact task.

Процедура едина для recovery-managed Сущностей и не зависит от конкретного таймера, webhook, scheduler, ChatGPT adapter, GitHub Action или будущего runtime.

## 1. Термины и authority boundary

**Wake event** — проверяемое событие, предлагающее экземпляру начать цикл проверки состояния. Wake event не доказывает `processing_started` и не создаёт полномочий.

**Wake router** — технический механизм сопоставления события Сущности/экземпляру и передачи минимального стартового контекста. Сам по себе не является Сущностью и не получает project authority.

**Instance continuity** — проверяемое основание считать, что пробуждается тот же ранее инициированный экземпляр и его собственное initiation-state не было отозвано, заменено или признано недостоверным.

**Resume-First** — режим экземпляра с подтверждённой instance continuity. Writer-state проверяется отдельно.

**Initiation-required** — режим нового, заменяющего или недостоверно восстановленного экземпляра, continuity которого не доказана.

**Authority basis** — проверяемое основание, существующее до спорного перехода и прямо применимое к нему: действующая approved-норма/организационное правило, standing delegation либо явное решение/instruction уполномоченного контура в пределах уже существующего authority. Wake event, dispatch, inbox locator, capability, technical availability, initiation status, publication/readback, lease/lock и наличие recovery package такого основания не создают.

**Exact task authority** — проверяемое основание выполнить exact task в текущих условиях. Наличие task artifact, request, dispatch, inbox locator или wake locator само по себе task authority не создаёт.

**Authoritative current-state mutation** — изменение authoritative current-state, writer-state либо другого current-объекта, признанного authoritative. Разрешённый candidate/outbox/evidence-result без такого изменения не является authoritative mutation.

**Worker/read-only instance** — экземпляр, read-only относительно authoritative current-state/writer-state. Может читать, анализировать и создавать разрешённые candidate/evidence results, но не изменяет authoritative current-state без допустимой writer authority.

**Writer continuity** — проверяемость того, что ранее установленное current-writer assignment конкретного экземпляра остаётся текущим, не superseded/revoked/transferred и fresh reconciliation не выявил competing writer evidence.

**Writer Gate** — task-sensitive проверка writer authority. `initiation_verified` не равен writer authority.

## 2. Базовая машина состояний

`WAKE_DETECTED`
→ `TARGET_RESOLVED`
→ `INSTANCE_CONTINUITY_CHECK`
→ `RESUME_FIRST` ИЛИ `INITIATION_REQUIRED`
→ при initiation: `INITIATION_GATE`
→ `TASK_REQUIREMENTS_CHECK`
→ `WRITER_CHECK`
→ допустимый writer/worker outcome
→ `READY_FOR_EXACT_TASK`
→ `FINAL_TASK_REVALIDATION`
→ `processing_started=yes`
→ `ONE_PROFILE_TASK`
→ `RESULT_VERIFICATION`
→ `ROUTING / PRESERVATION_TRIGGER_IF_NEEDED`.

Любой неразрешённый конфликт, failed recovery или внешняя зависимость переводит цикл в проверяемый waiting/blocked state, а не обходится предположением.

## 3. Wake detection и target resolution

До профильного исполнения требуется определить логическую Сущность, target instance если известен, источник wake event, requested task locator если есть и доступное current-writer evidence.

Папка, alias, scheduler, технический процесс или имя компонента не создают Сущность автоматически. Wake locator является input hint, а не вечной task authority.

## 4. Выбор Resume-First или Initiation-required

Выбор делается только по continuity пробуждаемого экземпляра.

### Resume-First
Разрешён, если экземпляр ранее был инициирован, его continuity не отозвана/заменена/признана недостоверной и fresh project-field preflight не выявил evidence, отменяющего continuity.

Writer unavailability, competing-writer ambiguity или failover сами по себе не запускают повторную initiation уже инициированного worker/read-only instance.

### Initiation-required
Обязателен, если экземпляр новый; заменён чат/процесс и continuity прежнего экземпляра не доказана; continuity не проверяется; есть evidence retirement/freeze/replacement именно этого экземпляра; recovery/failover требует восстановления нового экземпляра; либо источник запуска не способен доказать возобновление прежнего verified instance.

## 5. Initiation Gate и recovery boundary

Новый/заменяющий экземпляр выполняет действующую процедуру recovery-канона:
1. загрузить базовые управляющие источники;
2. загрузить профильные initiation/snapshot/recovery-manifest;
3. установить exact external recovery locator;
4. проверить immutable version identity;
5. проверить actual composition против manifest;
6. проверить integrity/readback по внешне прочитанным байтам;
7. сделать fresh project-field preflight;
8. reconcile более свежие state/receipt/acceptance/recovery/writer/failover evidence;
9. вернуть ровно один status: `initiation_verified`, `initiation_loaded_external_unverified` или `initiation_failed`.

### R1. `initiation_failed` является terminal для обычного профильного исполнения

`initiation_failed` означает, что recovery package отсутствует, повреждён, противоречив или недостаточен для безопасного восстановления. Такой экземпляр:
- не переходит в normal `READY_FOR_EXACT_TASK` в этом wake-cycle;
- сохраняет `processing_started=no` для обычной профильной работы;
- может выполнять только отдельно авторизованную bounded recovery-diagnostic/correction action, которая не полагается на реконструированное непроверенное self-state.

`initiation_loaded_external_unverified` не создаёт writer authority. Worker/read-only продолжение допускается только если exact task независимо авторизована и её корректность/безопасность не зависит от непроверенных recovery fields; иначе экземпляр ждёт verification.

### R2. Fresher evidence не разрешает synthetic recovery reconstruction

Более свежее HQ evidence может доказать stale recovery, отменить/ограничить отдельные claims или потребовать новый gate. Оно не может ad hoc объединяться в новый authoritative self-snapshot/recovery state, если само не является разрешённым current-state/recovery artifact с применимой immutable identity и provenance.

Если recovery stale, а current-writer не может создать/подтвердить новый self-snapshot, последний externally verified recovery остаётся последним подтверждённым recovery basis с явной пометкой stale/limited. Задача, которой требуется более свежее authoritative state, блокируется и маршрутизируется в preservation/failover/operator gate. Reconciliation не означает reconstruction by plausibility.

## 6. Task requirements и Writer Gate

До writer-вопроса определяется, требует ли exact task authoritative current-state mutation.

Допустимые outcomes:
- `WRITER_NOT_REQUIRED_FOR_TASK` — только уже разрешённая worker/read-only граница;
- `WRITER_CONTINUITY_VERIFIED` — подтверждает лишь прежнее current-writer assignment, не расширяя authority;
- `WRITER_ESTABLISHED` — только после authority basis, pre-publication competing-writer check, exact recovery/current-state basis, отдельного writer evidence, immutable publication/readback и fresh post-publication reconciliation;
- `WRITER_REQUIRED_UNVERIFIED` — authoritative mutation blocked;
- `WRITER_CONFLICT` — authoritative mutation blocked; winner по commit time/last-write-wins/availability запрещён.

Wake, dispatch, initiation, technical availability или publication сами по себе writer authority не создают.

## 7. Exact Task Gate

После допустимого writer/worker outcome:
1. fresh preflight;
2. выбрать одну exact task либо установить её отсутствие;
3. проверить current recipient, status, dependencies и exact task authority;
4. не возобновлять historical/parked task автоматически;
5. непосредственно перед `processing_started=yes` выполнить final revalidation immutable task identity + current state/dependencies/authority.

Если task superseded/withdrawn/readdressed, старый task не исполняется. Если актуальная exact task отсутствует, wake-cycle завершается `WAITING_EXACT_TASK`.

## 8. Семантические границы

`wake_detected != wake_routed != processing_started != task_completed`

`package_present != initiation_verified`

`initiation_verified != current_writer_established`

`current_writer_established != task_authorized`

`task_dispatched != task_executed`

`result_published != result_received != result_accepted`.

Automation фиксирует только последний доказанный переход.

## 9. Preservation pipeline и Wake pipeline

Preservation заранее создаёт пригодное состояние:
`authoritative current-writer → self-check/self-snapshot → ARH preservation-check → external publication → immutable readback → recovery registry`.

Wake использует сохранённое состояние:
`wake → continuity decision → recovery verification при необходимости → task requirements → writer check → exact task`.

Wake router не создаёт recovery state вместо current-writer/ARH и не чинит stale recovery самовольно.

## 10. Wake-cycle states

Эти labels принадлежат только домену `wake_cycle_state` и не являются task/document/delivery/receipt/acceptance status:
- `TARGET_UNRESOLVED`;
- `RESUME_CONTINUITY_UNVERIFIED`;
- `initiation_loaded_external_unverified`;
- `initiation_failed`;
- `WRITER_REQUIRED_UNVERIFIED`;
- `WRITER_CONFLICT`;
- `WAKE_WAITING_OPERATOR_DECISION`;
- `WAITING_EXTERNAL`;
- `WAITING_EXACT_TASK`.

## 11. Evidence и recovery registry

Для существенного wake-перехода compact record содержит entity, target instance если известен, trigger/source event, requested task locator если есть, continuity/mode decision, writer requirement/conclusion, initiation status если выполнялась, `processing_started`, next exact state/action и immutable evidence locator для значимых переходов.

### R3. Generic wake evidence не заменяет recovery registry

Для любого initiation/preservation/recovery перехода wake-cycle record обязан содержать или immutably reference применимый recovery record, в котором проверяемы минимум:
- exact recovery locator;
- immutable version identity;
- actual composition/manifest verification result;
- integrity/readback verification result;
- stale-state / recoverability limitation;
- latest recoverability/initiation result.

Generic wake record не заменяет ARH recovery registry и не ослабляет требования v1.4 к publication/readback/recoverability accounting. Отдельный документ на каждый микропереход не требуется, если единый journal/registry даёт ту же проверяемость.

## 12. Human authority boundary

Automation не может самостоятельно утверждать approved-норму, расширять role/authority, обходить approval-required/non-delegable действия, выполнять high-impact действие только из-за успешного wake или создавать/восстанавливать secret по recovery metadata.

Writer establishment/failover без отдельного решения текущего цикла допустим только если действующий approved authority basis прямо разрешает automatic/standing establishment именно для этого условия и этой Сущности.

Если approved source резервирует решение за ОПЕРАТОРОМ либо иным non-delegable контуром, технические состояния и решения других Сущностей этот gate не заменяют.

## 13. Универсальность

Процедура применяется ко всем recovery-managed Сущностям проекта. Профильные различия определяются ролью/authority, recovery package, exact task и human/external gates. Скрытая профильная initiation-логика не может менять общую последовательность.

## 14. Test vectors T1–T12

Сохраняются обязательные test vectors r0.3:
- T1 ordinary current-writer wake → Resume-First;
- T2 new/replacement chat → Initiation-required → Writer Gate;
- T3 emergency failover → verified recovery + authority basis;
- T4 activation without actual chat resume → `processing_started=no`;
- T5 competing writers → `WRITER_CONFLICT`;
- T6 externally readable but unverified recovery → `initiation_loaded_external_unverified`;
- T7 verified instance without current exact task → `WAITING_EXACT_TASK`;
- T8 OPERATOR/high-impact gate → `WAKE_WAITING_OPERATOR_DECISION`;
- T9 initiated worker while writer unavailable → no repeat initiation solely from writer absence;
- T10 concurrent writer establishment → post-publication conflict reconciliation;
- T11 task superseded before processing → final revalidation blocks old task;
- T12 fresher recovery/current-writer evidence during wake-cycle → stale branch cannot continue without reconciliation.

Дополнительные recovery expectations для T6/T12: R1–R3 применяются обязательно, synthetic recovery reconstruction запрещён.

## 15. Не является частью нормы реализации

Не фиксируются навечно scheduler/timer/webhook, ChatGPT adapter, JSON/JSONL schema, GitHub as sole storage/runtime, lock/lease implementation или provider-specific resume API.

## 16. Review boundary

Этот r0.4 интегрирует SHT F1–F5/T9–T12, KAN A1–A6 и ARH R1–R3.

Он не изменяет active recovery canon v1.4 и не становится нормой до narrow recovery recheck, KOO final integration и явного решения ОПЕРАТОРА.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: интегрировать все process/authority/recovery fixes в единый candidate перед финальной узкой проверкой
СТАТУС: candidate_r04_ready_for_arh_narrow_recheck
