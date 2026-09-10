# ARH — experience extraction

## Роль и граница
Entity: ARH / АРХИВАРИУС. Правильное техническое имя, явно установленное ОПЕРАТОРОМ в текущем чате: `archivarius`; `arhivarius` — ошибочная форма, требующая inventory/migration перед удалением.

Подтверждённые направления в доступной истории: preservation/recovery; GitHub current-state и адресная маршрутизация; speech source-pack; continuity/experience requirements; canonical path hygiene.

Доступна история текущего экземпляра не от гарантированного начала. Полная старая история не подтверждена. Historical evidence не объявляется current truth без текущей проверки.

## Существенные эпизоды

### Semantic recovery gap
**Задача:** восстановить новый экземпляр Сущности, а не только проверить пакет.
**Evidence:** в SIS-инциденте structural checks могли пройти, но substantial working context появился после чтения authoritative snapshot; для KOO urgent START введён semantic reconstruction control.
**Неудачный заход:** считать commit/blob/SHA/composition достаточным для `initiation_verified`.
**Рабочее решение:** два gate: structural integrity + semantic/operational reconstruction.
**Lesson:** integrity verified != working state restored.
**next_time_behavior:** до verified восстановить documented decisions, artifacts, open/parked/unknown, blockers и safe next action.
**prohibited_repeat:** checksum-only initiation.
**Граница:** скрытая модель-память не реконструируется; только документированное evidence.
**Актуальность:** reusable.

### GitHub inbox как живой рабочий канал
**Задача:** определить текущую работу ARH.
**Evidence:** после указания ОПЕРАТОРА в `wellbeing-hq` обнаружилось уже существующее срочное задание KOO; затем адресные notices KOO/KOD. Commits `bf8360b523364dec36c93d3af9804252f0b6d9d5`, `a90d625b8cb192991700cfc6da98dd400098f482`.
**Неудачный заход:** пассивно ждать следующей ручной команды.
**Рабочее решение:** direct GitHub readback + hourly condition-watch значимых изменений.
**Lesson:** перед «задач нет» проверить рабочий канал.
**next_time_behavior:** activation/current-task cycle включает inbox/recent commits/dispatch/receipts.
**prohibited_repeat:** manual-courier-only workflow.
**Актуальность:** reusable.

### Candidate memory layering / log16
**Задача:** обработать новые continuity requirements.
**Evidence:** KOO/KOD явно маркируют их candidate и запрещают превращать в active canon без утверждения.
**Рабочее решение:** учитывать как вход для будущей ревизии recovery, сохраняя status/provenance.
**Lesson:** сильная идея не получает нормативный статус автоматически.
**prohibited_repeat:** silent promotion draft/candidate.
**Актуальность:** reusable.

### Адресные запросы для speech source-pack
**Задача:** получить проверяемые профильные evidence к выступлению ОПЕРАТОРА.
**Действия:** запросы доставлены прямо в inbox RED, KAN, VOL, KOD, SIS. Commits: `66187a50ff319498c4fa966d586d9c21414191b4`, `81391ac73012342b7a435ffda7d146628be5254d`, `12eccfb82756fb369d3244944b5c0af067fd2d0c`, `4deb8d02a0ceb2feb8a7e9a4083fe40f608f7677`, `c06979ab69a3e2fa0b811f70099d2db2570598ec`.
**Рабочее решение:** профильный request → addressed inbox → result/receipt → verification → source-pack.
**Lesson:** publication/dispatch/receipt/acceptance различны.
**prohibited_repeat:** считать создание файла acceptance адресатом.
**Актуальность:** reusable.

### `archivarius` / `arhivarius`
**Задача:** устранить split-state по имени ARH.
**Evidence:** GitHub подтверждает существование обоих каталогов; ОПЕРАТОР явно установил `archivarius` как правильное имя.
**Рабочее решение:** новые данные писать только в `entities/archivarius/`; перед удалением typo-path провести inventory и перенос уникальных годных данных с readback.
**Lesson:** typo в Entity path нельзя лечить слепым удалением.
**next_time_behavior:** authoritative identity → inventory → migrate → verify → retire typo-path.
**prohibited_repeat:** новые записи в `entities/arhivarius/`.
**Актуальность:** requires-current-check.

## Плантация граблей
1. **Checksum вместо восстановления.** Причина: structural verification подменяет semantic reconstruction. Anti-regression: fresh instance обязан восстановить documented operational state до verified.
2. **Пассивный ARH.** Симптом: KOO считает ARH работающим, ARH сообщает, что ждёт команду. Причина: inbox не проверен. Anti-regression: адресная задача должна обнаруживаться без ручной доставки.
3. **Два каталога одной Entity.** Причина появления typo-path: unknown. Правильный подход: canonical identity + inventory/migration/readback; не blind delete.

## Причинные решения
1. `recovery integrity без continuity → checksum-only vs semantic reconstruction → chosen: two-gate recovery → checksum-only rejected`.
2. `пассивное ожидание → manual courier vs GitHub intake → chosen: addressed GitHub + hourly watch`.
3. `двойной path → blind delete vs inventory/migrate → chosen: inventory/migrate/readback before retire`.

## Reusable procedures

### Cold-start recovery verification
1. Прочитать active sources.
2. Проверить immutable locator/version/composition/checksums.
3. Прочитать initiation/snapshot/state/handoff.
4. Реконструировать identity, decisions, artifacts, open/parked/unknown, blockers, safe next action.
5. Сверить с evidence.
6. Только после двух gate разрешать `initiation_verified`.
Stop: mismatch/missing/contradictory mandatory evidence.

### Addressed GitHub intake
1. Проверить canonical Entity path.
2. Проверить inbox/recent commits/dispatch.
3. Разделить task и notice/candidate.
4. Выполнить одну профильную задачу.
5. Результат в canonical outbox + addressed delivery.
6. Отдельно фиксировать dispatch/receipt/acceptance.

### Typo-path migration
1. Authoritative имя.
2. Inventory обоих путей.
3. Сравнение status/version/content.
4. Перенос только уникальных годных данных.
5. Readback.
6. Retire/delete typo-path только после проверки и требуемого разрешения.

## Историческое незавершённое состояние
- open: `ARH__speech-source-pack__KOO.md`, ответы RED/KAN/VOL/KOD/SIS ещё требуют current check.
- open: оценка candidate Entity Continuity/memory layering/log16 для будущей ревизии recovery.
- open: inventory/migration `entities/arhivarius/` → `entities/archivarius/`.
- parked: amendment recovery canon до отдельного утверждённого цикла.
- blocked: acceptance адресных результатов до receipt/result.
- unknown: полный состав старой истории ARH за пределами доступного контекста.

## EXTRACTION_REPORT
- История: доступная история текущего ARH-чата и реально присутствующие в ней tool/file evidence; начало целиком не подтверждено.
- Существенных эпизодов: 5.
- Граблей: 3.
- Причинных решений: 3.
- Reusable procedures: 3.
- Experience cards: 5.
- Anti-regression cases: 5.
- Существенных unknown: 4.
- Крупные направления: recovery continuity; GitHub routing; status/provenance; speech source-pack; Entity path canonicalization.
- За пределами extraction могли остаться ранние эпизоды ARH, которых нет в доступном контексте.

status: historical_experience_extraction
current_truth_claimed: no
active_sources_changed: no
project_time: generated_without_trusted_project_time
