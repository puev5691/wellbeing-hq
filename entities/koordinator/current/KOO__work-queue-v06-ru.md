# КООРДИНАТОР — текущая рабочая очередь v0.6

Статус: актуальная сверенная рабочая очередь.  
Это рабочий документ КООРДИНАТОРА, не канон проекта.  
Проектное время не указывается: доверенный источник проектного времени в этой сверке не использовался.

## Коротко

Сейчас безопасно и полезно параллельно разбудить три Сущности:

1. **СИСАДМИН** — восстановление инфраструктурного доступа к эРэФии для продолжения WBN/TERA работ ШАРДОВИКА.
2. **КАНЦЕЛЯРИЯ** — проверка полномочий и терминологии кандидата общей процедуры Wake → Resume / Initiation → Writer Gate → Exact Task.
3. **КОДЕР** — исправление оставшегося дефекта воспроизводимости Static Preview E1.

ШАРДОВИКА сейчас отдельно будить не нужно: его текущая WBN/TERA ветка упёрлась в инфраструктурный шаг СИСАДМИНА. АРХИВАРИУС свою reconciliation-задачу по replacement SIS завершил и принят КООРДИНАТОРОМ.

## Основание свежей сверки

Fresh GitHub-preflight выполнен по `puev5691/wellbeing-hq`.

Граница перед публикацией этой очереди:
`a2dc6337730c7612890da7ab4ca9a35abeec47ab`.

Материальные изменения относительно старой v0.5:
- replacement SIS уже установлен как verified current-writer;
- ARH reconciliation replacement SIS завершена и принята KOO;
- SHD подтвердил живую WBN-ноду на эРэФии и точный SSH endpoint `194.87.107.135:2222`;
- текущий blocker SHD — инфраструктурный управляемый доступ к эРэФии для локального read-only inventory;
- KOO поставил этот шаг выше Telegram Phase1B в очереди SIS;
- SHT завершил review общей wake/initiation/resume процедуры; исправленный candidate r0.2 передан KAN;
- VOL P5 evidence scout завершён и принят: пригодного закрытого эпизода с измеренным эффектом пока нет.

## Первая параллельная волна

### 1. SIS / СИСАДМИН — текущий приоритет

Состояние: **готов к ручному пробуждению; выполнение не доказано**.

Exact input:
`entities/sisadmin/inbox/KOO__sis-current-priority-erefia-access__SIS.md`

Task commit:
`bcaeccfefb992aafab16c3c7b0678d0072c65a5e`

Activation record:
`a9779f2b6ecb8fb17ddf967a772aca4075f87a3b`

Фактически подтверждено:
- activation requested: yes;
- processing started: no;
- нужен ручной пинг ОПЕРАТОРА.

Задача:
- использовать exact host `194.87.107.135`;
- использовать SSH port `2222`;
- восстановить/подтвердить управляемый инфраструктурный доступ и Remote Desktop Commander на exact host;
- TERA/WBN runtime не менять;
- вернуть KOO и SHD проверяемый readiness result либо точный blocker.

Ожидаемый результат:
`entities/sisadmin/outbox/SIS__erefia-access-readiness__KOO.md`

Telegram Phase1B r0.4 пока остаётся **приостановлен более высоким текущим приоритетом**. Старый Phase1B task не отменён, но параллельно с эРэФией не исполняется.

### 2. KAN / КАНЦЕЛЯРИЯ

Состояние: **готова к ручному пробуждению; выполнение не доказано**.

Exact input:
`entities/kancelar/inbox/KOO__entity-wake-initiation-resume-authority-review__KAN.md`

Task commit:
`6f2d21da76b1914ba11f8accb863a9383ee4ffc4`

Candidate r0.2:
`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r02.md`
commit `bb2e9b9e5e9368a2ae34dc987e37db1fb5a3b9bc`.

Activation record:
`f7fb990b635823ea07af452d84f7d1bfe2775dec`.

Фактически подтверждено:
- activation requested: yes;
- processing started: no;
- нужен ручной пинг ОПЕРАТОРА.

Задача: только authority/terminology review кандидата r0.2. Не утверждать v1.5, не выбирать runtime/adapter/scheduler и не расширять роли.

После KAN при PASS маршрут: ARH recovery-operational compatibility review → KOO integration → решение ОПЕРАТОРА об утверждении или отклонении v1.5.

### 3. KOD / КОДЕР

Состояние: **готов к ручному пробуждению; выполнение не доказано**.

Exact input:
`entities/koder/inbox/KOO__info-entry-static-preview-E1-fix-v03__KOD.md`

Task commit:
`ed84c8c379dc1ba450310fd6be46b2fa30e30fad`

Цель: исправить только оставшийся дефект побайтовой воспроизводимости evidence Static Preview E1. Representation semantics заново не открывать.

После результата KOD:
1. fresh KOO preflight;
2. exact verification результата;
3. при PASS — новый узкий WEB recheck;
4. только затем следующий KOD lane.

Внутренняя очередь KOD строго последовательна:
1. текущий E1 fix;
2. activation-lineage schema F1/F2;
3. sender-registry sanitation.

Одновременно эти три задачи КОДЕРУ не запускать.

## Сущности, которые сейчас ждут зависимость

### SHD / ШАРДОВИК

Состояние: **ждёт SIS**.

Подтверждённое текущее направление: WBN/TERA на трёх хостах.

Текущее состояние эРэФии:
- host `194.87.107.135`;
- SSH `2222` открыт и отвечает OpenSSH;
- WBN P2P `30000` открыт;
- hosting API `8780` открыт;
- `NETWORK=WELLBEING`, `SHARD_NAME=WBN`;
- chain-defining logic `shard.js` семантически совпадает с Буржуинией;
- административный endpoint известен;
- для следующего локального read-only inventory нужен управляемый доступ/Commander.

Поэтому отдельный SHD wake сейчас не нужен. После SIS readiness-result SHD делает fresh preflight и продолжает bounded inventory/сравнение опорной пары Буржуиния ↔ эРэФия.

### WEB / ВЕБМАСТЕР

Ждёт исправленного KOD Static Preview E1 package. Старую v0.2 задачу повторно не использовать. После KOO acceptance будет создан новый exact narrow-recheck task.

### SHT / ШТАБИСТ

Review общей wake/initiation/resume процедуры завершён:
`PASS_WITH_EXACT_PROCESS_FIXES`.

Для этой ветки сейчас ждёт KAN → ARH → KOO integration. Отдельного wake ШТАБИСТУ по этой ветке нет.

Отдельно его прежняя activation-lineage schema ветка ждёт будущий KOD F1/F2 correction.

## Закрытые в текущем проходе результаты

### ARH / АРХИВАРИУС — replacement SIS reconciliation

Результат:
`PASS_SIS_REPLACEMENT_PRESERVATION_RECONCILED`.

KOO receipt:
`routes/receipts/ARH__SIS-replacement-current-writer-reconcile__KOO.receipt.md`
commit `1b89a425767b19a3d2bb155293c09d27fcb01fbf`.

Состояние: **закрыто, отдельный wake не нужен**.

### VOL / ВОЛОНТЁР — P5 evidence scout

Результат принят ограниченно:
`P5_EVIDENCE_SCOUT_ACCEPTED__NO_ELIGIBLE_CLOSED_EPISODE`.

KOO receipt:
`routes/receipts/VOL__hybrid-interaction-p5-evidence-scout__KOO.receipt.md`
commit `a2dc6337730c7612890da7ab4ca9a35abeec47ab`.

Нового VOL wake не требуется. Для будущего P5 нужен закрытый эпизод с реальными измерениями «до/после», единицей измерения и доказанным получателем эффекта.

## Ожидание ОПЕРАТОРА или внешней зависимости

### Anthropic live D0

Технический adapter/transport готов. Реальный вызов не разрешён.

Ожидается отдельно:
- account/org;
- billing/credits;
- model access;
- runtime-only API key;
- явное разрешение одного D0 live call.

До этого никаких live calls и никакого project/private data.

### Entity Runner

Состояние: внешний blocker.

Подтверждена только host/runtime readiness. Не подтверждены provider entitlement/billing, Agent ID, Environment ID, API-key validity и разрешение provider-side request.

## Отложенная маршрутизация ШКОЛЫ

Вход VOL существует:
`entities/shkola/inbox/VOL__participant-capability-testing-source__SHK.md`.

Он не включается автоматически в очередь пробуждений ШТАБА. Нужно адресно определить получателя внутри действующего контура ШКОЛЫ, а не создавать Сущность `SHK` из имени папки.

## Правила текущей очереди

1. Inbox, dispatch или activation request не означают `RUNNING`.
2. Если `processing_started: no`, в операторском документе пишется «готов к ручному пробуждению», а не «выполняется».
3. Одна Сущность-current-writer выполняет одну профильную mutable-полосу за раз.
4. После каждого результата KOO делает fresh GitHub-preflight и пересобирает конфликтный граф.
5. Исторические задачи не возобновляются автоматически.
6. Документы для ОПЕРАТОРА пишутся по-русски. Латиница остаётся только там, где она технически необходима: пути, имена файлов, commits/blobs, статусы протокола, команды, модели и идентификаторы.

---
КТО: KOO / КООРДИНАТОР  
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ актуальную и удобную русскоязычную рабочую очередь после свежей сверки информационного поля  
СТАТУС: актуальная_сверенная_очередь_v0_6
