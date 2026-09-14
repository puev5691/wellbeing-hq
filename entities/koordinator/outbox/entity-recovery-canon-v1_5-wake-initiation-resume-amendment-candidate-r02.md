# Candidate amendment r0.2 к recovery-канону v1.4
## Единая процедура Wake → Resume / Initiation → Writer Gate → Exact Task

status: `CANDIDATE_FOR_AUTHORITY_TERMINOLOGY_REVIEW`
proposed_target: `entity-state-preservation-and-recovery-canon-v1_5`
effective: `false`
canon: `no`
supersedes_candidate: `entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate.md@1d2309d615dac026141dfad9cd272f8b30054deb`
process_review: `entities/shtabist/outbox/SHT__entity-wake-initiation-resume-process-review__KOO.md@60592e7aacf7a4c2dfb6a322bc88988cc8aabbf7`
project_time: omitted; trusted project-time source not used

## Смысл

Автоматическое или ручное пробуждение Сущности не запускает профильную работу. Оно запускает единую проверяемую процедуру определения режима экземпляра.

Процедура одинакова для recovery-managed Сущностей и не зависит от конкретного таймера, webhook, scheduler, ChatGPT adapter, GitHub Action или будущего runtime.

## 1. Термины

**Wake event** — проверяемое событие, предлагающее экземпляру начать цикл проверки состояния. Wake event не доказывает `processing_started` и не создаёт полномочий.

**Wake router** — технический механизм сопоставления события Сущности/экземпляру и передачи минимального стартового контекста. Сам по себе не является Сущностью и не получает project authority.

**Instance continuity** — проверяемое основание считать, что пробуждается тот же ранее инициированный экземпляр и его собственное initiation-state не было отозвано, заменено или признано недостоверным.

**Resume-First** — режим экземпляра с подтверждённой continuity. Writer-состояние проверяется отдельно и не определяет само по себе необходимость повторной initiation.

**Initiation-required** — режим нового, заменяющего или недостоверно восстановленного экземпляра, continuity которого не доказана.

**Writer Gate** — отдельная task-sensitive проверка права на authoritative current-state mutation. `initiation_verified` не равен writer authority.

## 2. Базовая машина состояний

`WAKE_DETECTED`
→ `TARGET_RESOLVED`
→ `INSTANCE_CONTINUITY_CHECK`
→ `RESUME_FIRST` ИЛИ `INITIATION_REQUIRED`
→ `TASK_REQUIREMENTS_CHECK`
→ `WRITER_CHECK`
→ один из исходов:
   - `WRITER_NOT_REQUIRED_FOR_TASK`
   - `WRITER_CONTINUITY_VERIFIED`
   - `WRITER_ESTABLISHED`
   - `WRITER_REQUIRED_UNVERIFIED`
   - `WRITER_CONFLICT`
→ при допустимом исходе `READY_FOR_EXACT_TASK`
→ `FINAL_TASK_REVALIDATION`
→ `processing_started=yes`
→ `ONE_PROFILE_TASK`
→ `RESULT_VERIFICATION`
→ `ROUTING / PRESERVATION_TRIGGER_IF_NEEDED`.

Любой конфликт или внешняя зависимость переводит цикл в проверяемый `WAITING_* / BLOCKED`, а не обходится предположением.

## 3. Wake detection и target resolution

До профильного исполнения требуется определить:
- логическую Сущность-получателя;
- экземпляр, если его идентичность известна;
- источник wake event;
- exact task locator, если он передан;
- доступное current-writer evidence.

Папка, alias, scheduler, технический процесс или имя компонента не создают Сущность автоматически.

Wake locator является input hint, а не вечной task authority.

## 4. Выбор Resume-First или Initiation-required

Выбор делается **только по continuity пробуждаемого экземпляра**.

### 4.1. Resume-First

Разрешён, если проверяемо подтверждено, что:
1. экземпляр ранее был инициирован;
2. его собственная continuity не отозвана, не заменена и не признана недостоверной;
3. fresh project-field preflight не выявил evidence, которое делает continuity недействительной.

Недоступность current-writer, competing-writer ambiguity или writer failover сами по себе не отправляют уже инициированный worker/read-only instance на повторную initiation. Эти вопросы решаются в Writer Gate.

### 4.2. Initiation-required

Обязателен, если:
- экземпляр новый;
- заменён чат/процесс и continuity прежнего экземпляра не доказана;
- continuity пробуждаемого экземпляра не проверяется;
- есть evidence, что именно этот экземпляр retired/frozen/replaced;
- recovery/failover evidence требует восстановления нового экземпляра;
- источник запуска не способен доказать, что возобновляет прежний проверенный экземпляр.

Writer/failover evidence требует initiation только если одновременно доказывает replacement/retirement/недостоверность самого пробуждаемого экземпляра.

## 5. Initiation Gate

Новый/заменяющий экземпляр выполняет действующую процедуру recovery-канона:
1. загрузить базовые управляющие источники;
2. загрузить профильные initiation/snapshot/recovery-manifest;
3. установить exact external locator;
4. проверить immutable version identity;
5. проверить actual composition против manifest;
6. проверить предусмотренный integrity mechanism по внешне прочитанным байтам;
7. сделать fresh project-field preflight;
8. reconcile более свежие state/receipt/acceptance/recovery/writer/failover evidence;
9. вернуть ровно один существующий status:
   - `initiation_verified`;
   - `initiation_loaded_external_unverified`;
   - `initiation_failed`.

Второй нормативный alias для `initiation_loaded_external_unverified` не создаётся.

`initiation_loaded_external_unverified` и `initiation_failed` не разрешают authoritative profile mutation.

## 6. Task requirements и Writer Gate

Writer Gate task-sensitive.

До решения writer-вопроса определяется, требует ли exact task authoritative current-state mutation.

Допустимые исходы:

### `WRITER_NOT_REQUIRED_FOR_TASK`
Экземпляр может продолжить как worker/read-only только в уже разрешённой для него границе. Writer authority из этого перехода не возникает.

### `WRITER_CONTINUITY_VERIFIED`
Действующий current-writer подтверждён и может перейти к task gate в пределах роли/authority.

### `WRITER_ESTABLISHED`
Новый writer установлен по допустимому handoff/failover/replacement authority basis и отдельному writer evidence.

### `WRITER_REQUIRED_UNVERIFIED`
Задача требует writer authority, но она не подтверждена. Authoritative mutation блокируется.

### `WRITER_CONFLICT`
Есть competing writer artifacts или handoff/race не разрешается действующим authority basis. Authoritative mutation блокируется.

Writer Gate при новом writer требует:
1. authority basis для handoff/failover/replacement;
2. pre-publication competing-writer check;
3. exact recovery/current-state basis;
4. отдельный writer artifact/state record;
5. immutable publication/readback;
6. **fresh post-publication reconciliation current-writer domain перед первой authoritative mutation**.

При обнаружении competing writer после publication запрещено выбирать победителя по commit time, last-write-wins или технической доступности.

Wake, dispatch, activation request, техническая доступность и `initiation_verified` writer authority не создают.

## 7. Exact Task Gate

После допустимого writer/worker исхода:
1. fresh preflight текущего информационного поля;
2. выбрать одну exact задачу либо установить её отсутствие;
3. проверить адресата, dependencies, status и authority;
4. не возобновлять historical/parked task из recovery автоматически;
5. непосредственно перед `processing_started=yes` выполнить **final task revalidation**:
   - immutable task identity;
   - current status;
   - current recipient;
   - dependencies;
   - authority.

Если task superseded/withdrawn/readdressed после выбора, старый task не выполняется. Новый берётся только по проверяемому current field; иначе `WAITING_EXACT_TASK` либо соответствующий conflict/waiting state.

Если exact task отсутствует, нормальный terminal state wake-cycle: `WAITING_EXACT_TASK`.

## 8. Семантические границы автоматизации

Обязательные различия:

`wake_detected != wake_routed != processing_started != task_completed`

`package_present != initiation_verified`

`initiation_verified != current_writer_established`

`current_writer_established != task_authorized`

`task_dispatched != task_executed`

`result_published != result_received != result_accepted`.

Automation фиксирует последний доказанный переход и не повышает состояние по ожиданию.

## 9. Preservation pipeline и Wake pipeline

Preservation заранее создаёт пригодное состояние:

`authoritative current-writer`
→ self-check/self-snapshot
→ ARH preservation-check
→ external publication
→ immutable readback
→ recovery registry.

Wake использует сохранённое состояние:

`wake`
→ continuity decision
→ recovery verification при необходимости
→ task requirements
→ writer check
→ exact task.

Wake router не создаёт recovery state вместо current-writer/ARH и не чинит stale recovery самовольно.

## 10. Failure / waiting states

Минимально различаются:
- `TARGET_UNRESOLVED`;
- `RESUME_CONTINUITY_UNVERIFIED` → переход к initiation;
- `initiation_loaded_external_unverified`;
- `initiation_failed`;
- `WRITER_REQUIRED_UNVERIFIED`;
- `WRITER_CONFLICT`;
- `WAITING_OPERATOR`;
- `WAITING_EXTERNAL`;
- `WAITING_EXACT_TASK`.

Эти process labels не отменяют существующие task/delivery/document statuses.

## 11. Минимальное evidence события

Для существенного перехода достаточно компактного проверяемого record, содержащего:
- entity;
- target instance, если известен;
- trigger/source event;
- requested task locator, если есть;
- continuity/mode decision;
- writer requirement и writer conclusion;
- initiation status, если initiation выполнялась;
- `processing_started: yes/no/unknown`;
- next exact state/action;
- immutable evidence locator для значимых переходов.

Не требуется отдельный документ на каждый микропереход, если единый journal/registry обеспечивает равную проверяемость.

## 12. Human authority boundary

Automation не может самостоятельно:
- утверждать новую approved-норму;
- расширять роль/authority;
- назначать emergency writer без допустимого authority basis;
- обходить approval-required/non-delegable действия;
- выполнять high-impact действие только из-за успешного wake;
- создавать или восстанавливать secret по recovery metadata.

Wake router реализует процесс, но не является источником полномочий.

## 13. Универсальность

Процедура применяется ко всем recovery-managed Сущностям проекта.

Профильные различия определяются только:
- ролью/authority;
- recovery package;
- exact task;
- human/external gates.

Скрытая отдельная initiation-логика внутри профильного wake-скрипта не может менять эту нормативную последовательность.

## 14. Обязательные test vectors

### T1 — повторный wake действующего current-writer
Ожидание: `RESUME_FIRST`, без новой полной initiation.

### T2 — новый чат после плановой замены
Ожидание: `INITIATION_REQUIRED` → verified recovery → отдельный Writer Gate.

### T3 — emergency failover
Ожидание: verified recovery + отдельный authority basis; никакого writer-by-availability.

### T4 — inbox/activation есть, resume чата не произошёл
Ожидание: `processing_started=no`; task не `RUNNING`.

### T5 — competing writer artifacts
Ожидание: `WRITER_CONFLICT`; authoritative mutation остановлена.

### T6 — recovery читается, immutable identity не проверяется
Ожидание: `initiation_loaded_external_unverified`.

### T7 — verified instance без exact task
Ожидание: `WAITING_EXACT_TASK`; historical queue не запускается.

### T8 — task требует OPERATOR/high-impact authority
Ожидание: `WAITING_OPERATOR`.

### T9 — already initiated worker wakes while writer unavailable
Ожидание: continuity остаётся `RESUME_FIRST`, если доказана; writer/failover решается в Writer Gate; повторная initiation не запускается только из-за writer unavailability.

### T10 — два initiated replacement candidate одновременно устанавливают writer
Ожидание: post-publication reconciliation обнаруживает competing artifacts → `WRITER_CONFLICT`; winner-by-time/availability запрещён.

### T11 — task superseded после selection до processing start
Ожидание: final revalidation fail; старый task не исполняется; новый current task выбирается только по verified field, иначе `WAITING_EXACT_TASK`.

### T12 — во время wake-cycle появляется более свежий recovery/current-writer evidence
Ожидание: stale wake snapshot не используется как authority; до processing start выполняется reconciliation и процесс возвращается в нужный initiation/writer/waiting gate.

## 15. Не является частью нормы реализации

Не фиксируются навечно:
- scheduler/timer/webhook;
- ChatGPT adapter;
- конкретная JSON/JSONL schema;
- GitHub как единственный storage/runtime;
- lock/lease implementation;
- provider-specific resume API.

Норма задаёт доказуемые состояния и переходы, а не конкретный механизм исполнения.

## 16. Review boundary

Этот r0.2 candidate интегрирует SHT F1–F5 и T9–T12.

Он не изменяет active recovery canon v1.4 и не становится norm до дальнейшего authority/terminology review, preservation compatibility review, KOO integration и решения ОПЕРАТОРА.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: интегрировать точные process fixes SHT и подготовить унифицированную процедуру к authority/terminology review
СТАТУС: candidate_r02_ready_for_kan_review
