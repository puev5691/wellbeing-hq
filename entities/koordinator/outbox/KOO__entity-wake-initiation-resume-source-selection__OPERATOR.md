# KOO — выбор источников для унификации wake / initiation / resume всех Сущностей

status: `CANDIDATE_SOURCE_SELECTION`
canon: `no`
project_time: omitted; trusted project-time source not used

## 1. Решение по нормативному дому

Не создавать отдельный общий «канон пробуждения».

Предлагаемый нормативный дом единообразной процедуры:

`entity-state-preservation-and-recovery-canon`

Следующая редакция должна включить общий раздел `Wake → Resume / Initiation → Writer Gate → Exact Task` и стать `v1.5` только после review и решения ОПЕРАТОРА.

Причина: действующий recovery-канон уже распространяется на все Сущности, определяет экземпляр, инициацию, recovery, current-writer, failover и проверяемую восстановимость. Создание второго универсального канона породит конкурирующие источники истины.

## 2. Нормативные источники, выбранные для формализации

### A. `project-instructions-core-v2_1-approved.md`

Использовать как верхнеуровневую основу для:
- различия `Сущность` / `экземпляр` / `чат`;
- правила `capability != authority`;
- запрета автоматического наследования решений прежнего чата;
- остановки при конфликте approved-источников;
- требования проверяемой инициации через внешний recovery locator;
- рабочего цикла `одна задача → одна профильная Сущность → один проверяемый результат → одна проверка → короткая фиксация`.

Не переносить в новый раздел файловую или маршрутизационную детализацию, уже принадлежащую file-canon.

### B. `source-loading-policy-v2-approved.md`

Использовать для единого порядка загрузки контекста:
1. базовые управляющие источники;
2. профильные `initiation / snapshot / recovery-manifest`;
3. внешняя recovery-проверка;
4. только затем профильные материалы конкретной задачи.

Ключевая граница: автоматическое пробуждение не является основанием загружать архив «для контекста».

### C. `entity-state-preservation-and-recovery-canon-v1_4-approved.md`

Это основной нормативный источник и цель следующей редакции.

Из него без изменения смысла сохранить:
- инициацию проходит экземпляр, а не абстрактная Сущность;
- обязательную процедуру внешней проверки recovery;
- статусы `initiation_verified`, `initiation_loaded_external_unverified`, `initiation_failed`;
- модель `несколько проверенно инициированных экземпляров → один current-writer`;
- запрет автоматического failover по одной технической доступности;
- self-snapshot current-writer и preservation-check АРХИВАРИУСА;
- фазовый барьер;
- разделение preservation/recovery ответственности;
- практический критерий recoverability.

Новый раздел должен закрыть организационный пробел между событием автоматического wake и уже описанной процедурой инициации.

### D. `entity-roles-short-v2_3-approved.md`

Использовать только для границ владельцев процесса:
- current-writer является автором собственного self-state;
- ARH владеет preservation/recovery процессом;
- SHT проектирует и ревизует жизненный цикл процесса;
- KOO управляет приоритетами/конфликтами и может инициировать checkpoint;
- SIS обеспечивает техническую инфраструктуру, но технический доступ не даёт writer/recovery authority;
- OPERATOR сохраняет человеческий authority для нормативных изменений и high-impact исключений;
- технический компонент не становится Сущностью автоматически.

Последний пункт применим к будущему wake-router/orchestrator: это технический компонент, пока отдельное решение не установит иное.

### E. `file-work-canon-universal-v2_3-approved.md`

Использовать как внешний контракт доказательности процесса:
- не путать создание, publication, delivery, receipt, acknowledgement и acceptance;
- не объявлять выполнение по факту выдачи команды;
- locator/version/readback должны быть проверяемыми;
- automation не должна имитировать `RUNNING`, если processing не доказан;
- значимый результат должен оставаться самостоятельным проверяемым артефактом.

File-canon не должен становиться нормативным домом wake/initiation state machine.

## 3. Материалы, выбранные только как test vectors / evidence

Они не являются источниками нормы и не должны цитироваться как authority для общего правила.

1. SHD replacement initiation/current-writer chain:
   - recovery correction;
   - KOO cold-start PASS;
   - `entities/shardovik/current/SHD__replacement-initiation-current-writer.md`.

2. SIS replacement chain:
   - self-preservation v02 `dfac1b1f...`;
   - KOO gate `1a6bf507...`;
   - current-writer artifact `2926908f...`;
   - first initiation result `551abc81...`.

3. Activation records с доказанной границей:
   - `activation_requested: yes`;
   - `processing_started: no`;
   - `activation_failed` при отсутствии exact Entity-chat resume.

Эти кейсы используются для проверки, что общая процедура корректно различает:
`wake request != processing != initiation != writer transfer != task execution`.

## 4. Что сознательно НЕ выбирать нормативной основой

- `KOO__orchestrator-worklist-v01.jsonl` — рабочий coordination artifact, не канон;
- конкретные SIS/SHD/KOD recovery-пакеты — профильное состояние, не общая норма;
- PWH/hashchain и другие research candidates — не относятся к authority процесса;
- старые activation/wake scripts — технические реализации и evidence;
- память прежних чатов — не источник истины.

## 5. Выделенный нормативный пробел

Действующие источники уже определяют, как инициировать новый экземпляр, но не формализуют единый переход от автоматического события пробуждения к выбору режима экземпляра.

Нужно нормативно определить:

`WAKE EVENT`
→ идентификация Сущности и экземпляра
→ проверка continuity/current-writer boundary
→ выбор `RESUME_FIRST` или `INITIATION_REQUIRED`
→ при необходимости verified recovery
→ отдельный writer gate
→ materialized exact task
→ только затем профильное исполнение.

## 6. Требование к следующей редакции

Редакция v1.5 должна устанавливать одинаковую процедуру для всех recovery-managed Сущностей и не зависеть от конкретного чата, провайдера, таймера, GitHub Action, webhook или будущего runtime.

Техническая реализация может меняться. Нормативная машина состояний должна оставаться одной.

## 7. Предлагаемый review-route

1. SHT — lifecycle/failure-state/stale-state/parallel-instance stress-review.
2. KAN — authority/terminology/normative-boundary review после SHT.
3. ARH — совместимость с preservation/recovery эксплуатацией и registry.
4. KOO — интеграция замечаний в единый v1.5 candidate.
5. OPERATOR — единственный approval gate для активации новой редакции.

До решения ОПЕРАТОРА этот материал и amendment ниже являются candidate only.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: выбрать минимальный набор действующих оснований и единый нормативный дом процедуры автоматического wake/initiation/resume
СТАТУС: candidate_source_selection
