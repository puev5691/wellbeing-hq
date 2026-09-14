# КООРДИНАТОР — текущая рабочая очередь v0.6

Статус: актуальная сверенная рабочая очередь.  
Это рабочий документ КООРДИНАТОРА, не канон проекта.  
Проектное время не указывается: доверенный источник проектного времени в этой сверке не использовался.

## КАК ЭТИМ ПОЛЬЗОВАТЬСЯ ОПЕРАТОРУ

ОПЕРАТОР **не читает inbox Сущности, не сверяет commit вручную и не пересказывает задачу**.

Штатное ручное пробуждение до появления автоматического exact-chat resume:

> открыть чат нужной Сущности → вставить готовый короткий промпт из этой очереди → перейти к следующему чату.

Всё остальное делает сама Сущность по Resume-First: fresh GitHub-preflight, чтение своего exact inbox, проверка актуальности задачи и возврат результата через Exchange Gate.

Отдельная компактная карточка пробуждений:
`entities/koordinator/current/KOO__operator-wake-card-v01-ru.md`

## Сейчас будить: готовые промпты

### СИСАДМИН

> Продолжай по Resume-First. Сделай fresh GitHub-preflight `puev5691/wellbeing-hq`. Текущий приоритет KOO уже лежит в твоём inbox: `KOO__sis-current-priority-erefia-access__SIS.md`. Обработай только его и верни результат через Exchange Gate. Не возобновляй Telegram Phase1B параллельно.

### КАНЦЕЛЯРИЯ

> Продолжай по Resume-First. Сделай fresh GitHub-preflight `puev5691/wellbeing-hq`. Обработай текущий exact input `KOO__entity-wake-initiation-resume-authority-review__KAN.md` из своего inbox. Только authority/terminology review, без утверждения нормы и без выбора реализации. Верни результат KOO через Exchange Gate.

### КОДЕР

> Продолжай по Resume-First. Сделай fresh GitHub-preflight `puev5691/wellbeing-hq`. Обработай текущий exact input `KOO__info-entry-static-preview-E1-fix-v03__KOD.md` из своего inbox. Выполни только E1 fix, не захватывай следующие KOD lanes. Верни результат KOO через Exchange Gate.

Этого достаточно. Если задача уже адресована в GitHub, длинный операторский промпт является аварийным исключением, а не штатной процедурой.

## Коротко о текущей обстановке

Сейчас безопасно и полезно параллельно разбудить три Сущности:

1. **СИСАДМИН** — инфраструктурный доступ к эРэФии для продолжения WBN/TERA ветки ШАРДОВИКА.
2. **КАНЦЕЛЯРИЯ** — проверка полномочий и терминологии кандидата общей процедуры Wake → Resume / Initiation → Writer Gate → Exact Task.
3. **КОДЕР** — исправление оставшегося дефекта воспроизводимости Static Preview E1.

ШАРДОВИКА сейчас отдельно будить не нужно: его WBN/TERA ветка ждёт инфраструктурный шаг СИСАДМИНА. WEB ждёт KOD. ШТАБИСТ по wake/initiation/resume review уже отработал.

## Основание сверки

Fresh GitHub-preflight выполнен по `puev5691/wellbeing-hq` перед формированием этой очереди; после неё информационное поле продолжает изменяться, поэтому каждый пробуждённый экземпляр обязан начинать со своего fresh preflight.

Подтверждённые существенные состояния:
- replacement SIS установлен как verified current-writer;
- ARH reconciliation replacement SIS завершена и принята KOO;
- SHD подтвердил живую WBN-ноду на эРэФии и SSH endpoint `194.87.107.135:2222`;
- текущий блокирующий шаг SHD передан SIS;
- KOO поставил эРэФию выше Telegram Phase1B в очереди SIS;
- SHT завершил review общей wake/initiation/resume процедуры; candidate r0.2 передан KAN;
- VOL P5 evidence scout принят: доказательно пригодного закрытого эпизода с измеренным эффектом пока нет.

## Подробности активных полос

### SIS / СИСАДМИН

Exact input:
`entities/sisadmin/inbox/KOO__sis-current-priority-erefia-access__SIS.md`

Task commit:
`bcaeccfefb992aafab16c3c7b0678d0072c65a5e`

Activation record:
`a9779f2b6ecb8fb17ddf967a772aca4075f87a3b`

Доказано: activation requested = yes, processing started = no. Поэтому до ручного wake задача не считается RUNNING.

Задача ограничена инфраструктурным доступом к exact host `194.87.107.135:2222`; TERA/WBN runtime не менять. Telegram Phase1B приостановлен более высоким текущим приоритетом.

### KAN / КАНЦЕЛЯРИЯ

Exact input:
`entities/kancelar/inbox/KOO__entity-wake-initiation-resume-authority-review__KAN.md`

Task commit:
`6f2d21da76b1914ba11f8accb863a9383ee4ffc4`

Candidate r0.2:
`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r02.md`
commit `bb2e9b9e5e9368a2ae34dc987e37db1fb5a3b9bc`.

Activation record:
`f7fb990b635823ea07af452d84f7d1bfe2775dec`.

Задача: только authority/terminology review. После PASS маршрут: ARH recovery-operational review → KOO integration → решение ОПЕРАТОРА.

### KOD / КОДЕР

Exact input:
`entities/koder/inbox/KOO__info-entry-static-preview-E1-fix-v03__KOD.md`

Task commit:
`ed84c8c379dc1ba450310fd6be46b2fa30e30fad`

Цель: только Static Preview E1 fix. После PASS создаётся новый узкий WEB recheck. Следующие KOD lanes выполняются строго последовательно: activation-lineage F1/F2, затем sender-registry sanitation.

## Сейчас не будить

- **SHD / ШАРДОВИК** — ждёт SIS по эРэФии.
- **WEB / ВЕБМАСТЕР** — ждёт KOD E1 result и новый exact task.
- **SHT / ШТАБИСТ** — по общей wake/initiation/resume ветке отработал; ждёт KAN → ARH → KOO.
- **VOL / ВОЛОНТЁР** — P5 evidence scout закрыт bounded-result.
- **ARH / АРХИВАРИУС** — предыдущая SIS replacement reconciliation закрыта; новые ARH→KOO policy/evidence входящие обрабатывает KOO отдельно, они не превращаются автоматически в wake-задачу ARH.

## Внешние и человеческие ворота

### Anthropic live D0

Технический adapter/transport готов, но real live call не разрешён. Нужны account/org, billing/credits, model access, runtime-only API key и отдельное разрешение одного D0 вызова.

### Entity Runner

Остаётся внешний blocker: provider entitlement/billing, Agent ID, Environment ID, API-key validity и provider-side authority не подтверждены.

## Правила текущей очереди

1. Inbox, dispatch или activation request не означают `RUNNING`.
2. `processing_started: no` означает только готовность к wake.
3. Одна Сущность-current-writer ведёт одну mutable-полосу за раз.
4. После результата KOO делает fresh preflight и пересобирает очередь.
5. Исторические задачи не запускаются автоматически.
6. Операторские документы пишутся по-русски.
7. **ОПЕРАТОРУ выдаётся готовый короткий wake-промпт. Ручной пересказ already-addressed задачи не является штатной обязанностью ОПЕРАТОРА.**
8. Длинный операторский prompt допустим только для аварийной инициации/recovery, когда обычной адресной continuity недостаточно.

---
КТО: KOO / КООРДИНАТОР  
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ рабочую очередь, которую можно применять без ручного диспетчерского труда  
СТАТУС: актуальная_операторская_очередь_v0_6
