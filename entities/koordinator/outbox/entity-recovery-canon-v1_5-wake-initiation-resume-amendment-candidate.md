# Candidate amendment к recovery-канону v1.4: единая процедура Wake → Resume / Initiation → Writer Gate → Exact Task

status: `CANDIDATE_FOR_V1_5_REVIEW`
proposed_target: `entity-state-preservation-and-recovery-canon-v1_5`
effective: `false`
canon: `no`
project_time: omitted; trusted project-time source not used

## Смысл изменения

Действующий recovery-канон уже задаёт обязательную инициацию нового экземпляра, внешний recovery, current-writer и failover. Для будущего автоматического пробуждения требуется единообразно определить более ранний переход:

> событие пробуждения не запускает работу; оно запускает проверяемое определение режима экземпляра.

Одинаковая процедура должна применяться ко всем recovery-managed Сущностям независимо от того, пробуждает их ОПЕРАТОР, таймер, webhook, GitHub event, scheduler или иной разрешённый технический механизм.

## 1. Термины

**Wake event / событие пробуждения** — внешнее проверяемое событие, предлагающее экземпляру Сущности начать цикл проверки состояния. Wake event не доказывает, что processing начался, и не создаёт полномочия.

**Wake router** — технический механизм, который сопоставляет событие конкретной Сущности/экземпляру и передаёт минимальный стартовый контекст. Сам по себе wake router не является Сущностью и не получает project authority.

**Resume-First** — режим уже проверенно инициированного экземпляра, в котором до профильного исполнения выполняется fresh preflight, проверяется current-writer/competing-writer boundary и выбирается только актуальная exact задача.

**Initiation-required** — режим нового, заменяющего либо недостоверно восстановленного экземпляра, для которого continuity недостаточна и обязательна процедура инициации по recovery-канону.

**Writer gate** — отдельная проверка права экземпляра стать или остаться authoritative current-writer. `initiation_verified` не равен writer authority.

## 2. Базовая машина процесса

Для каждого wake действует единая последовательность:

`WAKE_DETECTED`
→ `TARGET_RESOLVED`
→ `INSTANCE_MODE_CHECK`
→ `RESUME_FIRST` ИЛИ `INITIATION_REQUIRED`
→ `WRITER_CHECK`
→ `READY_FOR_EXACT_TASK`
→ `ONE_PROFILE_TASK`
→ `RESULT_VERIFICATION`
→ `ROUTING / PRESERVATION_TRIGGER_IF_NEEDED`.

Любой неразрешённый конфликт переводит процесс в проверяемый `BLOCKED / WAITING_*`, а не пропускается по предположению.

## 3. Фаза A — Wake detection и target resolution

Wake считается только запросом на проверку.

До загрузки профильной задачи необходимо установить как минимум:
- логическую Сущность-получателя;
- экземпляр, если его идентичность внешне известна;
- источник/тип wake event;
- exact task locator, если wake связан с конкретным заданием;
- наличие или отсутствие проверяемого current-writer evidence.

Если конкретная Сущность не определена однозначно, профильная работа не начинается.

Папка, alias, технический процесс, scheduler или имя компонента не создают Сущность автоматически.

## 4. Фаза B — выбор Resume-First или Initiation

### 4.1. Resume-First разрешён

Resume-First выбирается только если есть проверяемое основание считать, что пробуждается уже инициированный экземпляр и его continuity не была отозвана или заменена.

Минимально проверить:
1. действующие базовые управляющие источники доступны;
2. нет evidence о replacement/failover/freeze/retirement этого экземпляра;
3. current-writer state, если он нужен для предстоящего действия, подтверждён и не конкурирует с более свежим writer;
4. fresh project-field preflight не выявил материально более свежий state, отменяющий continuity;
5. exact задача всё ещё существует и адресована этой Сущности.

При PASS экземпляр не проходит полную инициацию заново. Он продолжает через `READY_FOR_EXACT_TASK`.

### 4.2. Initiation-required обязателен

В режим Initiation-required переходят, если выполняется хотя бы одно условие:
- экземпляр новый;
- чат/процесс заменён;
- continuity текущего экземпляра не может быть доказана;
- прежний current-writer retired/frozen/unavailable;
- есть recovery/failover/replacement evidence;
- competing-writer boundary неясен;
- внешний recovery стал обязательной основой восстановления;
- источник запуска не способен доказать, что возобновляет именно прежний проверенный экземпляр.

В этом режиме действует существующая обязательная процедура инициации recovery-канона без ослабления.

## 5. Фаза C — Initiation gate

Новый/заменяющий экземпляр выполняет действующую процедуру:
1. загрузить базовые управляющие источники;
2. загрузить профильные initiation/snapshot/recovery-manifest;
3. установить exact external locator;
4. проверить наличие и immutable version identity;
5. проверить actual composition против manifest;
6. проверить checksums/иной предусмотренный integrity mechanism по внешне прочитанным байтам;
7. сделать fresh project-field preflight;
8. reconcile более свежие state/receipt/acceptance/writer/failover evidence;
9. вернуть один из существующих статусов:
   - `initiation_verified`;
   - `initiation_loaded_external_unverified`;
   - `initiation_failed`.

`initiation_loaded_external_unverified` и `initiation_failed` не допускают автоматической authoritative profile mutation.

## 6. Фаза D — Writer gate

Инициация и writer authority всегда разделены.

После `initiation_verified` экземпляр может:
- оставаться worker/read-only;
- либо проходить current-writer establishment/handoff, если это требуется задачей и существует authority basis.

Writer gate требует:
1. проверяемого основания планового handoff/failover/replacement либо сохранённой writer continuity;
2. отсутствия competing authoritative writer либо явного разрешённого арбитража;
3. exact recovery/current-state basis;
4. отдельного writer artifact/state record, если writer устанавливается заново;
5. immutable publication/readback этого writer evidence до authoritative mutation.

Wake, task dispatch, activation request, техническая доступность экземпляра и `initiation_verified` сами по себе writer authority не создают.

## 7. Фаза E — Exact task gate

Профильное исполнение начинается только после state/recovery/writer проверок, необходимых для конкретного действия.

Перед выполнением:
1. сделать fresh preflight по текущему информационному полю;
2. получить одну exact задачу либо установить, что задачи нет;
3. проверить её актуальность, адресата, dependencies и authority;
4. не возобновлять historical/parked task только потому, что она записана в recovery;
5. выполнить одну допустимую профильную задачу по рабочему циклу проекта.

Если exact task отсутствует, корректный итог wake-cycle — `WAITING_EXACT_TASK`, а не импровизация новой работы.

## 8. Wake не равен processing

Для automation вводится обязательная семантическая граница:

`wake_detected != wake_routed != processing_started != task_completed`.

Также:

`package_present != initiation_verified`

`initiation_verified != current_writer_established`

`current_writer_established != task_authorized`

`task_dispatched != task_executed`

`result_published != result_received != result_accepted`.

Automation обязана фиксировать последний доказанный переход и не повышать состояние по ожиданию.

## 9. Preservation pipeline и Wake pipeline разделены

Preservation создаёт пригодное проверяемое состояние заранее:

`authoritative current-writer`
→ self-check/self-snapshot
→ ARH preservation-check
→ external publication
→ immutable readback
→ recovery registry.

Wake/initiation использует уже сохранённое состояние:

`wake`
→ mode decision
→ recovery verification при необходимости
→ writer check
→ exact task.

Wake router не должен создавать recovery state вместо current-writer/ARH и не должен автоматически «чинить» stale recovery во время запуска.

## 10. Failure states

Минимально различаются:

- `TARGET_UNRESOLVED` — невозможно однозначно определить Сущность/экземпляр;
- `RESUME_CONTINUITY_UNVERIFIED` — нельзя доказать continuity, требуется initiation;
- `INITIATION_EXTERNAL_UNVERIFIED` — соответствует существующему `initiation_loaded_external_unverified`;
- `INITIATION_FAILED` — пакет повреждён/противоречив/недостаточен;
- `WRITER_CONFLICT` — competing writer или неясный handoff;
- `WAITING_OPERATOR` — требуется отдельное human authority/action;
- `WAITING_EXTERNAL` — внешняя зависимость недоступна/не подтверждена;
- `WAITING_EXACT_TASK` — состояние проверено, но исполнимой задачи нет.

Эти process labels не отменяют существующие документные, delivery и task statuses. При интеграции в v1.5 SHT/KAN должны проверить отсутствие лишнего дублирования терминологии.

## 11. Минимальный wake/result evidence

Для проверяемой автоматизации достаточно одного компактного события/record на существенный переход, содержащего:
- entity;
- target instance, если известен;
- trigger/source event;
- requested task locator, если есть;
- mode decision (`RESUME_FIRST` / `INITIATION_REQUIRED` / blocked);
- current-writer/competing-writer conclusion;
- initiation status, если initiation выполнялась;
- processing started: yes/no/unknown;
- next exact state/action;
- immutable evidence locator для значимых переходов.

Не требуется создавать отдельный документ на каждый микропереход, если единый журнал/registry обеспечивает ту же проверяемость.

## 12. Human authority boundary

Automation не может самостоятельно:
- принимать новую approved-норму;
- расширять роль/authority;
- назначать emergency writer без заранее допустимого правила/решения;
- обходить `approval-required`/`non-delegable` действия;
- выполнять high-impact действие только потому, что wake успешно состоялся;
- создавать/восстанавливать secret по recovery metadata.

Wake router реализует процесс, но не становится источником полномочий.

## 13. Универсальность

Процедура одинакова для KOO, ARH, KOD, SIS, SHD, RED, WEB, KAN, SHT и иных recovery-managed Сущностей.

Профильные различия задаются только:
- ролью/authority конкретной Сущности;
- её recovery package;
- exact task;
- требуемыми human/external gates.

Не допускается отдельная скрытая initiation-логика в каждом wake-скрипте, если она изменяет общую нормативную последовательность.

## 14. Проверочные сценарии для review

До approval новая редакция должна пройти как минимум следующие test vectors:

### T1 — обычное повторное пробуждение действующего current-writer
Ожидание: `RESUME_FIRST`, без повторной полной initiation.

### T2 — новый чат после плановой замены
Ожидание: `INITIATION_REQUIRED` → verified recovery → отдельный writer gate.

### T3 — emergency failover при недоступном writer
Ожидание: последний externally verified recovery + отдельное authority basis; никакого writer-by-availability.

### T4 — activation request дошёл до inbox, chat resume не произошёл
Ожидание: `processing_started=no`; задача не считается RUNNING.

### T5 — два competing writer artifacts
Ожидание: `WRITER_CONFLICT`; профильная authoritative mutation остановлена.

### T6 — recovery читается, но immutable external identity не проверяется
Ожидание: `initiation_loaded_external_unverified`.

### T7 — verified instance проснулся без exact task
Ожидание: `WAITING_EXACT_TASK`; historical queue не запускается.

### T8 — task требует OPERATOR/high-impact authority
Ожидание: `WAITING_OPERATOR`; wake success не открывает high-impact execution.

## 15. Что остаётся технической реализацией, а не нормой

Этот amendment не должен фиксировать навечно:
- конкретный scheduler/timer/webhook;
- ChatGPT adapter;
- JSON/JSONL schema;
- GitHub как единственный storage/runtime;
- конкретные instance IDs;
- lease/lock implementation;
- transport к конкретной модели или провайдеру.

Технические компоненты обязаны реализовывать нормативные переходы, но могут заменяться без смены канона.

## 16. Статус и путь принятия

Это amendment candidate, а не действующий источник.

Предлагаемый путь:
`SHT process review → KAN authority/terminology review → ARH recovery-operation review → KOO integration → OPERATOR approval`.

Только после решения ОПЕРАТОРА положения могут быть интегрированы в полную редакцию `entity-state-preservation-and-recovery-canon-v1_5-approved.md` и включены в базовые управляющие источники через действующую source-loading policy.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: формализовать единый wake/initiation/resume/writer/task lifecycle для всех Сущностей без создания конкурирующего универсального канона
СТАТУС: candidate_for_v1_5_review
