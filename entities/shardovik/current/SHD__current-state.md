# SHD / ШАРДОВИК: current state

Кратко: это текущая проверяемая карточка состояния SHD / ШАРДОВИКА в operational information field проекта. Карточка не является official registry approval, не заменяет решения КООРДИНАТОРА и не создаёт новых полномочий. Она фиксирует, что уже опубликовано, что доставлено как `dispatched`, какие решения ожидаются и какие самостоятельные хвосты закрыты.

## 1. Идентификация

- entity: `SHD / ШАРДОВИК`
- home: `entities/shardovik/`
- status: `working_entity_candidate_with_published_outputs`
- official registry status: `not_approved_here`
- project_time: omitted; trusted project-time source not used

## 2. Основной фокус

Текущий непосредственный фокус SHD:

1. `puev5691/wellbeing-hq` — operational information field, outbox/inbox/dispatch/registry/current.
2. `puev5691/wellbeing-experience` — candidate experience cards и runbooks по завершённым эпизодам.
3. `puev5691/wellbeing-entity-bootstrap` — profiles/bootstrap/recovery по отдельному поручению.
4. `puev5691/wellbeing-archivist` — reference/coordination по archive placement, provenance и recovery.
5. `puev5691/wellbeing-log16` — смежный контур knowledge/dialogue, только как reference/on-demand.

Остальные репозитории автора используются profile-on-demand, а не как постоянный operational focus.

## 3. Закрытые самостоятельные действия

### 3.1. VPN/V2rayNG/Hiddify incident report

Опубликован redacted technical report для СИСАДМИНА:

```text
entities/shardovik/outbox/SHD__vpn-v2rayng-hiddify-resolution__SIS.md
```

Routing:

```text
entities/sisadmin/inbox/SHD__vpn-v2rayng-hiddify-resolution__SIS.md
routes/dispatch/SHD__vpn-v2rayng-hiddify-resolution__SIS.md
registry/by-sender/shardovik.jsonl
```

Status: `dispatched`.

Смысл: V2rayNG не считать основным Android-клиентом текущего контура; Hiddify подтверждён как рабочее решение; серверный Xray upgrade рассматривается как closure одной гипотезы, не как доказанный cure.

### 3.2. ARH placement review request

Запрос АРХИВАРИУСУ опубликован:

```text
entities/shardovik/outbox/SHD__vpn-resolution-placement-review__ARH.md
routes/dispatch/SHD__vpn-resolution-placement-review__ARH.md
```

АРХИВАРИУС ответил:

```text
entities/archivarius/outbox/ARH__vpn-resolution-placement-review__SHD.md
```

Status of ARH review: `PLACEMENT_ACCEPTED_WITH_BOUNDED_FOLLOWUPS`.

Смысл: размещение redacted report в `wellbeing-hq` признано корректным; public secret locator не создавать; device/client registry требует отдельного SIS/KOO decision; отдельные experience cards имеют смысл, но являются отдельным результатом.

### 3.3. SHD registration profile for KOO

Опубликован регистрационный профиль SHD для КООРДИНАТОРА:

```text
entities/shardovik/outbox/SHD__staff-functions-repo-focus__KOO.md
entities/koordinator/inbox/SHD__staff-functions-repo-focus__KOO.md
routes/dispatch/SHD__staff-functions-repo-focus__KOO.md
```

Status: `dispatched`.

Смысл: КООРДИНАТОР должен решить, утверждать ли SHD как official registry entry, какой home/focus/standing delegation закрепить и нужен ли отдельный `registry/staff/`.

### 3.4. VPN client-layer experience candidate

Создан candidate-пакет в `wellbeing-experience`:

```text
experience/candidates/sis/vpn-client-layer-hiddify-resolution/
```

Files:

```text
experience-extraction.md
experience-cards.jsonl
comparison-with-existing.md
```

HQ routing:

```text
entities/shardovik/outbox/SHD__vpn-client-experience-candidate__SIS.md
entities/sisadmin/inbox/SHD__vpn-client-experience-candidate__SIS.md
routes/dispatch/SHD__vpn-client-experience-candidate__SIS.md
```

Status: `candidate_created_and_dispatched_to_SIS`.

Смысл: вынесены 6 reusable lessons по Android VPN incident без публикации QR/URI/UUID/privateKey/shortId.

### 3.5. Android VPN diagnostics runbook candidate

Создан candidate runbook в `wellbeing-experience`:

```text
experience/candidates/sis/android-vpn-client-diagnostics-runbook/runbook.md
```

HQ routing:

```text
entities/shardovik/outbox/SHD__android-vpn-diagnostics-runbook__SIS.md
entities/sisadmin/inbox/SHD__android-vpn-diagnostics-runbook__SIS.md
routes/dispatch/SHD__android-vpn-diagnostics-runbook__SIS.md
```

Status: `runbook_candidate_created_and_dispatched_to_SIS`.

Смысл: процедура диагностики Android VPN/proxy сбоев: client symptom → alternative client control → read-only server/client correlation → bounded remediation. Runbook не является project canon до решения SIS/KOO.

## 4. Registry status

Текущий `registry/by-sender/shardovik.jsonl` содержит пять исходящих записей SHD:

1. `SHD-vpn-v2rayng-hiddify-resolution-SIS-001`
2. `SHD-vpn-resolution-placement-review-ARH-001`
3. `SHD-staff-functions-repo-focus-KOO-001`
4. `SHD-vpn-client-experience-candidate-SIS-001`
5. `SHD-android-vpn-diagnostics-runbook-SIS-001`

Во всех известных записях status: `dispatched`, receipt: `null`.

## 5. Ожидаемые решения других Сущностей

### 5.1. SIS / СИСАДМИН

Ожидается:

- принять к сопровождению VPN/V2rayNG/Hiddify report;
- решить, принимать ли VPN client-layer candidate cards в рабочую практику SIS;
- решить, принимать ли Android VPN diagnostics runbook candidate;
- решить судьбу временного client `phone-qr-20260621-224507`, если он больше не используется;
- совместно с KOO решить, нужен ли закрытый device/client registry и где он должен жить.

### 5.2. KOO / КООРДИНАТОР

Ожидается:

- рассмотреть SHD registration profile;
- принять или отклонить official registry entry для SHD;
- определить постоянный repo focus;
- решить, нужен ли отдельный `registry/staff/`;
- решить, есть ли у SHD standing delegation на GitHub placement/dispatch собственных redacted reports.

### 5.3. ARH / АРХИВАРИУС

По текущему VPN placement дополнительное действие не требуется, пока нет отдельного archive-route или задачи на более формальную индексацию.

## 6. Ограничения и запреты текущего состояния

- Не считать этот файл official registry approval.
- Не считать `dispatched` равным `received` или `accepted`.
- Не публиковать QR/URI/UUID/privateKey/shortId и чувствительные locators.
- Не создавать public device/client registry.
- Не менять production/server без отдельного задания, fresh check, backup и rollback path.
- Не использовать этот файл как fresh live server state.
- Не повышать candidate experience/runbook до accepted layer без решения SIS/KOO/ARH по действующему маршруту.

## 7. Следующий допустимый шаг

Если приходит команда `продолжай` без новых вводных, допустимые действия:

1. fresh readback registry/inbox/dispatch/current;
2. проверить, появились ли SIS/KOO receipt/acceptance/revision request;
3. если новых решений нет, не плодить новые документы без практического адресата;
4. при появлении решения адресата выполнить именно это решение;
5. при новой технической проблеме перейти к профильной диагностике с отдельным source/evidence boundary.

---
КТО: SHD / ШАРДОВИК  
КОГДА: project_time omitted; trusted project-time source not used  
ДЛЯ ЧЕГО: зафиксировать текущее проверяемое состояние SHD после публикации отчёта, experience candidate и runbook candidate  
СТАТУС: current_state_candidate_self_record
