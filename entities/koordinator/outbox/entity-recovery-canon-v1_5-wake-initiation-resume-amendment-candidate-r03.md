# Candidate amendment r0.3 к recovery-канону v1.4
## Единая процедура Wake → Resume / Initiation → Writer Gate → Exact Task

status: `CANDIDATE_FOR_RECOVERY_OPERATIONAL_REVIEW`
proposed_target: `entity-state-preservation-and-recovery-canon-v1_5`
effective: `false`
canon: `no`
supersedes_candidate: `entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r02.md@bb2e9b9e5e9368a2ae34dc987e37db1fb5a3b9bc`
process_review: `entities/shtabist/outbox/SHT__entity-wake-initiation-resume-process-review__KOO.md@60592e7aacf7a4c2dfb6a322bc88988cc8aabbf7`
authority_review: `entities/kancelar/outbox/KAN__entity-wake-initiation-resume-authority-review__KOO.md@4e2820f651466029092da05150c3e0fe715fc8ca`
project_time: omitted; trusted project-time source not used

## Смысл

Пробуждение Сущности не запускает профильную работу. Оно запускает единую проверяемую процедуру определения режима экземпляра, действующих полномочий и одной актуальной exact task.

Процедура едина для recovery-managed Сущностей и не зависит от конкретного таймера, webhook, scheduler, ChatGPT adapter, GitHub Action или будущего runtime.

## 1. Термины и authority boundary

**Wake event** — проверяемое событие, предлагающее экземпляру начать цикл проверки состояния. Wake event не доказывает `processing_started` и не создаёт полномочий.

**Wake router** — технический механизм сопоставления события Сущности/экземпляру и передачи минимального стартового контекста. Сам по себе не является Сущностью и не получает project authority.

**Instance continuity** — проверяемое основание считать, что пробуждается тот же ранее инициированный экземпляр и его собственное initiation-state не было отозвано, заменено или признано недостоверным.

**Resume-First** — режим экземпляра с подтверждённой instance continuity. Writer-состояние проверяется отдельно.

**Initiation-required** — режим нового, заменяющего или недостоверно восстановленного экземпляра, continuity которого не доказана.

**Authority basis** — проверяемое основание, существующее до спорного перехода и прямо применимое к нему: действующая approved-норма/организационное правило, standing delegation либо явное решение/instruction уполномоченного контура в пределах уже существующего authority. Wake event, dispatch, inbox locator, technical availability, capability, initiation status, publication/readback, lease/lock и само наличие recovery package authority basis не создают.

**Exact task authority** — проверяемое основание выполнить exact task в текущих условиях. Оно должно вытекать из действующей роли и approved process, standing delegation либо явного instruction/решения стороны, которая сама обладает таким authority. Наличие task artifact, request, dispatch, inbox locator или wake locator само по себе exact task authority не создаёт.

**Authoritative current-state mutation** — изменение authoritative current-state, writer-state либо другого current-объекта, который действующие источники признают authoritative. Создание разрешённого candidate/outbox/evidence-result без изменения authoritative current-state такой mutation не является.

**Worker/read-only instance** — экземпляр, read-only относительно authoritative current-state/writer-state. Он может читать, анализировать, выполнять уже разрешённую работу и создавать candidate-результаты, но не изменяет authoritative current-state без допустимой передачи writer-state.

**Writer continuity** — проверяемость того, что ранее установленное current-writer assignment конкретного экземпляра остаётся текущим: оно не superseded, не revoked, не передано другому экземпляру, а fresh reconciliation current-writer domain не выявил competing writer evidence.

**Writer Gate** — отдельная task-sensitive проверка права на authoritative current-state mutation. `initiation_verified` не равен writer authority.

## 2. Базовая машина состояний

`WAKE_DETECTED`
→ `TARGET_RESOLVED`
→ `INSTANCE_CONTINUITY_CHECK`
→ `RESUME_FIRST` ИЛИ `INITIATION_REQUIRED`
→ `TASK_REQUIREMENTS_CHECK`
→ `WRITER_CHECK`
→ один из исходов:
- `WRITER_NOT_REQUIRED_FOR_TASK`;
- `WRITER_CONTINUITY_VERIFIED`;
- `WRITER_ESTABLISHED`;
- `WRITER_REQUIRED_UNVERIFIED`;
- `WRITER_CONFLICT`;
→ при допустимом исходе `READY_FOR_EXACT_TASK`
→ `FINAL_TASK_REVALIDATION`
→ `processing_started=yes`
→ `ONE_PROFILE_TASK`
→ `RESULT_VERIFICATION`
→ `ROUTING / PRESERVATION_TRIGGER_IF_NEEDED`.

Любой неразрешённый конфликт переводит цикл в проверяемый waiting/blocked state, а не обходится предположением.

## 3. Wake detection и target resolution

До профильного исполнения требуется определить:
- логическую Сущность-получателя;
- экземпляр, если его идентичность известна;
- источник wake event;
- exact task locator, если он передан;
- доступное current-writer evidence.

Папка, alias, scheduler, технический процесс или имя компонента не создают Сущность автоматически. Wake locator является input hint, а не вечной task authority.

## 4. Выбор Resume-First или Initiation-required

Выбор делается только по continuity пробуждаемого экземпляра.

### 4.1 Resume-First
Разрешён, если экземпляр ранее был инициирован, его continuity не отозвана/заменена/признана недостоверной и fresh project-field preflight не выявил более свежего evidence, отменяющего continuity.

Недоступность current-writer, competing-writer ambiguity или writer failover сами по себе не запускают повторную initiation уже инициированного worker/read-only instance.

### 4.2 Initiation-required
Обязателен, если экземпляр новый; заменён чат/процесс и continuity прежнего экземпляра не доказана; continuity не проверяется; есть evidence retirement/freeze/replacement именно этого экземпляра; recovery/failover требует восстановления нового экземпляра; либо источник запуска не способен доказать возобновление прежнего verified instance.

## 5. Initiation Gate

Новый/заменяющий экземпляр выполняет действующую процедуру recovery-канона:
1. загрузить базовые управляющие источники;
2. загрузить профильные initiation/snapshot/recovery-manifest;
3. установить exact external locator;
4. проверить immutable version identity;
5. проверить actual composition против manifest;
6. проверить integrity mechanism по внешне прочитанным байтам;
7. сделать fresh project-field preflight;
8. reconcile более свежие state/receipt/acceptance/recovery/writer/failover evidence;
9. вернуть ровно один существующий status: `initiation_verified`, `initiation_loaded_external_unverified` или `initiation_failed`.

`initiation_loaded_external_unverified` и `initiation_failed` не разрешают authoritative current-state mutation и не создают writer authority. Это ограничение само по себе не запрещает уже разрешённую worker/read-only работу.

## 6. Task requirements и Writer Gate

Writer Gate task-sensitive. Сначала определяется, требует ли exact task authoritative current-state mutation.

### `WRITER_NOT_REQUIRED_FOR_TASK`
Экземпляр продолжает только в уже разрешённой worker/read-only границе. Writer authority не возникает.

### `WRITER_CONTINUITY_VERIFIED`
Подтверждает только непрерывность уже существующего current-writer assignment в пределах прежней роли и authority. Новых полномочий не создаёт.

### `WRITER_ESTABLISHED`
Допустим только после всех обязательных условий Writer Gate: authority basis, pre-publication competing-writer check, exact recovery/current-state basis, отдельный writer evidence, immutable publication/readback и fresh post-publication reconciliation current-writer domain. Publication/readback или техническая доступность сами по себе этого state не создают.

### `WRITER_REQUIRED_UNVERIFIED`
Задача требует writer authority, но она не подтверждена. Authoritative mutation блокируется.

### `WRITER_CONFLICT`
Есть competing writer artifacts или handoff/race не разрешается действующим authority basis. Authoritative mutation блокируется. Победитель по commit time, last-write-wins или технической доступности не выбирается.

## 7. Exact Task Gate

После допустимого writer/worker исхода:
1. fresh preflight;
2. выбрать одну exact task либо установить её отсутствие;
3. проверить адресата, dependencies, current status и exact task authority;
4. не возобновлять historical/parked task автоматически;
5. непосредственно перед `processing_started=yes` выполнить final task revalidation: immutable task identity, current status, current recipient, dependencies и authority.

Если task superseded/withdrawn/readdressed, старый task не исполняется. Если актуальная exact task отсутствует, wake-cycle завершается `WAITING_EXACT_TASK`.

## 8. Семантические границы автоматизации

`wake_detected != wake_routed != processing_started != task_completed`

`package_present != initiation_verified`

`initiation_verified != current_writer_established`

`current_writer_established != task_authorized`

`task_dispatched != task_executed`

`result_published != result_received != result_accepted`.

Automation фиксирует последний доказанный переход и не повышает состояние по ожиданию.

## 9. Preservation pipeline и Wake pipeline

Preservation заранее создаёт пригодное состояние:
`authoritative current-writer → self-check/self-snapshot → ARH preservation-check → external publication → immutable readback → recovery registry`.

Wake использует сохранённое состояние:
`wake → continuity decision → recovery verification при необходимости → task requirements → writer check → exact task`.

Wake router не создаёт recovery state вместо current-writer/ARH и не чинит stale recovery самовольно.

## 10. Wake-cycle states

Все значения ниже являются только `wake_cycle_state`. Они не являются task/document status, delivery/receipt/acknowledgement/acceptance state и не доказывают approval или authority.

Минимально различаются:
- `TARGET_UNRESOLVED`;
- `RESUME_CONTINUITY_UNVERIFIED` → переход к initiation;
- `initiation_loaded_external_unverified`;
- `initiation_failed`;
- `WRITER_REQUIRED_UNVERIFIED`;
- `WRITER_CONFLICT`;
- `WAKE_WAITING_OPERATOR_DECISION`;
- `WAITING_EXTERNAL` — ожидание проверяемой внешней зависимости/evidence, необходимой для продолжения цикла; это не означает, что внешнее действие уже выполнено;
- `WAITING_EXACT_TASK`.

## 11. Минимальное evidence события

Для существенного перехода record содержит: entity; target instance, если известен; trigger/source event; requested task locator, если есть; continuity/mode decision; writer requirement/conclusion; initiation status, если выполнялась; `processing_started: yes/no/unknown`; next exact state/action; immutable evidence locator для значимых переходов.

Отдельный документ на каждый микропереход не требуется, если единый journal/registry даёт ту же проверяемость.

## 12. Human authority boundary

Automation не может самостоятельно утверждать approved-норму, расширять role/authority, обходить approval-required/non-delegable действия, выполнять high-impact действие только из-за успешного wake или создавать/восстанавливать secret по recovery metadata.

Automation может выполнить writer establishment/failover без отдельного решения текущего цикла только если действующий approved authority basis прямо разрешает автоматическое/standing establishment именно для этого условия и этой Сущности. Общая роль, успешный wake, verified recovery, technical availability, отсутствие доступного прежнего writer или writer artifact сами по себе такого разрешения не создают.

Если approved source резервирует решение за ОПЕРАТОРОМ либо относит действие к `approval-required`/`non-delegable`, требуется решение именно предусмотренного уполномоченного человека/контура. Ни wake/router/dispatch/initiation/writer state, ни решение другой Сущности без такого authority этот gate не заменяют.

## 13. Универсальность

Процедура применяется ко всем recovery-managed Сущностям проекта. Профильные различия определяются только ролью/authority, recovery package, exact task и human/external gates. Скрытая профильная initiation-логика не может менять общую нормативную последовательность.

## 14. Обязательные test vectors

T1: повторный wake действующего current-writer → `RESUME_FIRST` без полной initiation.

T2: новый чат после плановой замены → `INITIATION_REQUIRED` → verified recovery → отдельный Writer Gate.

T3: emergency failover → verified recovery + допустимый authority basis; никакого writer-by-availability.

T4: inbox/activation есть, resume чата не произошёл → `processing_started=no`; task не `RUNNING`.

T5: competing writer artifacts → `WRITER_CONFLICT`; authoritative mutation остановлена.

T6: recovery читается, immutable identity не проверяется → `initiation_loaded_external_unverified`.

T7: verified instance без exact task → `WAITING_EXACT_TASK`; historical queue не запускается.

T8: task требует OPERATOR/high-impact authority → `WAKE_WAITING_OPERATOR_DECISION`.

T9: already initiated worker wakes while writer unavailable → instance continuity остаётся `RESUME_FIRST`, writer/failover решается отдельно.

T10: два initiated replacement candidates одновременно устанавливают writer → post-publication reconciliation обнаруживает conflict; никакого winner-by-time/availability.

T11: task superseded после selection до processing start → final revalidation fail; старый task не исполняется.

T12: во время wake-cycle появляется более свежий recovery/current-writer evidence → stale snapshot не используется как authority; выполняется reconciliation и возврат в соответствующий gate.

## 15. Не является частью нормы реализации

Не фиксируются навечно scheduler/timer/webhook, ChatGPT adapter, конкретная JSON/JSONL schema, GitHub как единственный storage/runtime, lock/lease implementation или provider-specific resume API.

## 16. Review boundary

Этот r0.3 candidate интегрирует SHT F1-F5/T9-T12 и KAN A1-A6.

Он не изменяет active recovery canon v1.4 и не становится norm до ARH recovery-operational compatibility review, KOO integration и решения ОПЕРАТОРА.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: интегрировать process + authority fixes и передать унифицированную процедуру на recovery-operational compatibility review
СТАТУС: candidate_r03_ready_for_arh_review
