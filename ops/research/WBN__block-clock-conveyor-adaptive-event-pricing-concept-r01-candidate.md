# WBN Block Clock Conveyor + Adaptive Event Pricing

status: CANDIDATE_CONCEPT_R01
activation: NOT_AUTHORIZED
production_use: NO
subject_owner_candidate: SHD / ШАРДОВИК
recipient_candidate: KOO / КООРДИНАТОР
project_time: omitted

## 1. Смысл концепции

Использовать последовательность блоков WBN не как «часы реального времени», а как общий детерминированный логический такт для конвейера разрешённых событий проекта.

Блокчейн в этой модели не создаёт задачу, полномочие, current-writer, approval или право на производственное действие. Он только даёт всем участникам одинаковый наблюдаемый порядок тактов и может активировать уже существующее разрешённое действие по заранее утверждённому контракту.

Вторая часть концепции — сделать стоимость активационного события адаптивной к реальной загрузке конвейера. Тогда цена становится не просто платой, а регулятором дефицитного ресурса: внимания Сущностей, вычислительных слотов и пропускной способности исполнителей.

Базовая причинная цепочка:

`block height -> разрешённый activation slot -> исполнение -> проверяемый receipt -> reward / accounting -> следующий разрешённый slot`

## 2. Почему block height, а не wall-clock

Номер блока подходит как логический счётчик потому, что все участники цепи видят один и тот же порядок подтверждённых блоков.

Нельзя автоматически считать время блока временем предметного события. `block_height` и `block_timestamp` — разные типы свидетельств. Для проектного аудита блок может доказать порядок и факт попадания записи в цепь, но не заменяет внешний источник времени там, где важно реальное время события.

Следовательно:

- `block_height` = основной логический tick;
- `epoch` = диапазон блоков для статистики и регулирования;
- реальное время = отдельное свидетельство, если оно вообще нужно задаче;
- остановка цепи = остановка block-clock, а не повод молча перейти на локальный таймер.

## 3. Минимальная модель конвейера

### 3.1. Task Authorization Record

Контракт не хранит «текст задачи как приказ», а ссылку на уже разрешённое действие:

- immutable task locator;
- immutable version/hash;
- entity / recipient;
- authority class;
- допустимый activation window;
- stop conditions;
- допустимый тип результата/receipt;
- max resource budget;
- optional priority class.

Запись в контракте означает только: «это действие уже разрешено внешним governance-контуром и может быть активировано при наступлении его условий».

### 3.2. Activation Slot

Каждый разрешённый task может претендовать на слот.

Слот описывается как минимум:

- `slot_id`;
- `task_id`;
- `eligible_from_block`;
- `expire_after_block`;
- `priority_class`;
- `max_price`;
- `activation_nonce`.

`activation_nonce` нужен для защиты от повторного запуска одного и того же разрешения.

### 3.3. Executor

Фактический исполнитель остаётся off-chain или hybrid:

- watcher видит новый блок;
- читает разрешённые слоты;
- проверяет локальные канонические gates;
- запускает только уже разрешённую работу;
- возвращает receipt.

Блокчейн не расширяет роль executor и не обходит Writer Gate.

### 3.4. Receipt

Минимальный receipt должен позволять проверить:

- какой task исполнялся;
- по какой immutable версии;
- какой activation nonce использован;
- каким блоком/слотом была разрешена активация;
- результат PASS / BLOCKED / FAIL;
- locator результата;
- hash результата;
- consumed / replayable status;
- resource accounting.

Receipt не равен approval. Он доказывает факт и результат исполнения.

## 4. Block Clock

Простейший режим:

- каждый блок = один tick;
- каждые `N` блоков = epoch;
- scheduled события задаются как `block_height mod N` или как `eligible_from_block`.

Пример без привязки к конкретному интервалу блока:

- block 120001 -> scan A;
- block 120013 -> scan B;
- block 120025 -> reconciliation;
- block 120037 -> archive/preservation check.

Главное свойство: расписание выражается через блоки, а не через локальные часы сервера.

## 5. Adaptive Event Pricing

### 5.1. Что регулируем

Цена должна регулировать только конкуренцию за ограниченный activation capacity.

Цена НЕ должна:

- создавать полномочие;
- отменять stop-condition;
- покупать approval;
- давать право обойти current-writer;
- превращать более богатого участника в более «правого».

### 5.2. Минимальная статистика

Для первой версии достаточно одного главного показателя:

`utilization = accepted_activation_slots / target_capacity`

Остальные показатели сначала лучше собирать как telemetry, но не включать в цену:

- queue depth;
- oldest eligible task age;
- blocked ratio;
- fail ratio;
- receipt latency;
- executor saturation;
- missed slots.

Причина проста: если сразу включить всё, получится контракт, который регулирует сам себя по статистике, смысл которой никто уже не понимает.

### 5.3. Сглаживание

Чтобы цена не дёргалась от одного шумного блока, считать статистику по epoch или через экспоненциальное сглаживание:

`load_ema_next = alpha * utilization_now + (1 - alpha) * load_ema_prev`

где `alpha` задаёт скорость реакции.

### 5.4. Регулятор цены

Кандидат для MVP — ограниченное пропорциональное изменение:

`delta = k * (load_ema - target_load)`

`event_price_next = clamp(event_price * (1 + delta), min_price, max_price)`

Дополнительно ограничить максимальное изменение за epoch:

`abs(price_change) <= max_step`

Это защищает рынок от скачка цены из-за одного аномального периода.

Для on-chain реализации предпочтительна fixed-point арифметика без плавающей точки.

### 5.5. Что означает цена

Возможны три разных смысла, их нельзя смешивать без решения governance:

1. **WBN payment** — реальная экономическая плата за activation slot.
2. **Internal activation credits** — внутренний ресурс конвейера, не обязательно торгуемый.
3. **Hybrid** — базовый бесплатный/квотный объём плюс WBN за превышение или ускорение.

Для пилота безопаснее начинать с shadow-price: контракт считает цену, но она ещё ничего не списывает.

## 6. Priority без покупки полномочий

Можно разрешить несколько классов очереди:

- `scheduled` — штатные периодические задачи;
- `normal` — обычная разрешённая работа;
- `urgent` — уже отдельно разрешённая срочная работа;
- `maintenance` — инфраструктурные проверки;
- `recovery` — только при отдельно установленном recovery authority.

Важно: класс priority устанавливается governance-решением до попадания в рынок слотов.

Платёж может влиять на место среди задач одного допустимого класса, но не переводить normal task в emergency/recovery автоматически.

## 7. Защита от голодания и спама

Минимальные механизмы:

- max slots per task / entity / epoch;
- max price step;
- reserved capacity для scheduled/recovery классов;
- aging: давно ожидающая задача получает постепенно растущий scheduling weight;
- nonce/replay protection;
- per-authority quotas;
- circuit breaker при аномальной нагрузке;
- hard cap на activation expenditure.

Так цена регулирует перегрузку, но не превращает очередь в аукцион, где бедные задачи никогда не исполняются.

## 8. Chain stall и degraded mode

Если новые блоки перестали подтверждаться:

1. block-clock считается остановленным;
2. новые on-chain activations не считаются наступившими;
3. executor не должен самовольно переходить на wall-clock;
4. внешний watchdog может зафиксировать `CHAIN_STALLED`;
5. переход на резервный scheduler допустим только если для этого отдельно утверждён fallback-contract.

Это принципиально: резерв не должен создавать полномочие, которого не было в основном контуре.

## 9. Reorg / finality boundary

До выбора конкретного механизма WBN/TERA2 нельзя считать первый увиденный блок окончательным.

Нужно определить отдельно:

- что такое confirmed activation block;
- сколько подтверждений/какая finality достаточна;
- что делать, если activation попал в откатившуюся ветку;
- может ли receipt быть опубликован до finality activation;
- как не выполнить один task дважды после reorg.

Без этого производственная активация по block height преждевременна.

## 10. Возможная контрактная декомпозиция

### `TaskRegistry`
Хранит только разрешённые immutable task references и ограничения.

### `ConveyorScheduler`
Определяет eligibility и выдаёт activation nonce/slot.

### `CapacityOracle` или `CapacityRegistry`
Хранит утверждённую target capacity и фактическую загрузку, если она не полностью выводится из chain state.

### `ActivationPriceController`
Считает shadow/real event price по статистике epoch.

### `ReceiptRegistry`
Фиксирует проверяемые результаты.

### `RewardAccounting`
Начисляет вознаграждение только на основании допустимого receipt и утверждённых правил экономики.

Не обязательно реализовывать всё отдельными контрактами. Это логические границы ответственности.

## 11. MVP без риска

### Этап 0 — модель/симуляция

На сохранённой последовательности блоков моделировать:

- scheduled activations;
- очередь;
- utilization;
- shadow event price;
- starvation;
- burst load;
- chain stall.

Никаких реальных activation/payment.

### Этап 1 — read-only block clock

Watcher читает block height и только пишет telemetry:

`block -> eligible tasks -> would_activate`

Ничего не запускает.

### Этап 2 — manual activation

Контракт предлагает слот, но ОПЕРАТОР вручную подтверждает исполнение.

### Этап 3 — bounded auto-activation

Только для отдельного whitelist задач с уже утверждённым automatic activation authority.

### Этап 4 — shadow pricing

Цена рассчитывается, но не списывается.

### Этап 5 — реальный activation accounting

Только после статистической проверки модели и governance approval.

## 12. Метрики пилота

Проверяемые показатели:

- duplicate activation = 0;
- unauthorized activation = 0;
- activation after supersession = 0;
- activation after expiry = 0;
- same block state -> same eligibility result;
- bounded price step соблюдается;
- starvation rate;
- median / p95 queue age;
- used capacity / target capacity;
- receipts with immutable locator = 100%;
- reorg replay safety;
- chain-stall stop behavior.

## 13. Что можно сделать с экономикой дальше

После доказанного MVP можно исследовать:

- динамическую стоимость срочного слота;
- staking/bond за дорогое событие;
- возврат части стоимости при PASS;
- потерю части bond при malformed/spam activation;
- reward за полезный verified receipt;
- распределение части activation revenue майнерам/исполнителям/развитию;
- market for executor capacity;
- прогнозирование нагрузки по epoch-history;
- разные price curves для разных resource classes;
- contract-based reservation будущих slots;
- long-running task leases на диапазон блоков.

Но это второй слой. Первый должен доказать block-clock и безопасную activation semantics без денег.

## 14. Главные инварианты проекта

1. Блок не создаёт задачу.
2. Цена не создаёт полномочие.
3. Контракт не устанавливает current-writer сам по себе.
4. Receipt не равен approval.
5. Публикация в chain не равна человеческому принятию результата.
6. Historical task нельзя повторить только потому, что снова наступил похожий block condition.
7. Superseded task не активируется.
8. Chain stall не разрешает самовольный fallback.
9. Один activation nonce не исполняется дважды.
10. Экономический приоритет действует только внутри уже разрешённого governance scope.

## 15. Что должен проверить ШАРДОВИК по официальным TERA2 sources

Эта концепция намеренно не утверждает TERA2-специфику без профильной проверки.

SHD должен отдельно подтвердить по официальной документации и исходникам TERA2:

- доступность block height контрактам и/или внешнему watcher;
- модель finality/reorg;
- доступные smart-contract primitives;
- event/log mechanism;
- deterministic state transition ограничения;
- fixed-point / integer arithmetic возможности;
- стоимость и лимиты contract execution;
- способы immutable task/receipt references;
- возможности observer/node API;
- влияние shard architecture на единый logical clock;
- допустимый способ связывания activation с block state;
- нагрузку схемы на throughput.

До этой проверки все TERA2-specific implementation details имеют статус UNKNOWN.

## 16. Кандидат на первое исследование

Минимальная полезная гипотеза для SHD:

> Можно ли на WBN/TERA2 построить детерминированный read-only `Block Clock` и shadow `ActivationPriceController`, которые на каждом подтверждённом epoch выдают одинаковые `eligible_slots` и `shadow_price`, не запуская никаких Сущностей и не списывая WBN?

Если ответ PASS, появляется безопасная основа для следующего шага — manual activation pilot.

## 17. Предлагаемый следующий профильный результат

`SHD__wbn-block-clock-conveyor-feasibility-r01.md`

Он должен вернуть:

- VERIFIED TERA2 primitives;
- BLOCKED/UNKNOWN gaps;
- минимальную data model;
- proposed epoch semantics;
- proposed finality rule;
- shadow pricing simulation plan;
- один bounded lab experiment;
- стоп-условия;
- без production activation и без реальных списаний.

---

КТО: SIS / техническое сохранение по прямому указанию ОПЕРАТОРА  
ДЛЯ ЧЕГО: сохранить в информационном поле проекта концепцию WBN Block Clock Conveyor + Adaptive Event Pricing как проверяемый кандидат для последующего профильного рассмотрения  
СТАТУС: CANDIDATE_NOT_ACTIVE  
source: OPERATOR instruction + artifact WBN_block_clock_conveyor_adaptive_event_pricing_concept_r01.md, source_sha256=90f5d1f075fcb157b83639d2fea3f40bc9ad5fad2b7a7cd4a7f76222082585e2  
related_files: плановая карточка ШТАБИСТУ создаётся отдельным файлом с immutable locator этой версии  
approval_status: NOT_APPROVED_FOR_EXECUTION  
responsibility_boundary: preservation and planning signal only; no task authority, no automatic activation, no production use; SHD feasibility only under a separate exact task authority
