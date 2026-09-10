# COOP research conveyor — стоп по конфликту approved-источников

## Смысл

Launch-пакет КООРДИНАТОРА для ШТАБИСТА получен и проверен. Внутренняя контрольная сумма задания совпадает.

Профильное проектирование исследовательского технологического конвейера **не начато**, потому что в действующих approved-источниках обнаружено несовместимое правило адресной доставки, а задача прямо требует проектировать `route / receipt / acceptance` и дальнейшее отображение процесса на OSS.

По действующей core-инструкции при несовместимости двух approved-источников профильное исполнение должно быть остановлено до явного разрешения конфликта.

Статус: `BLOCKED_SOURCE_CONFLICT`.

---

## 1. Проверка входного пакета

Пакет:

`KOO__COOP-launch__SHT.tar.gz`

SHA-256 пакета:

`d6a99e9bfb008d26491c5de61c2a8789f7a71719eef2e6c5a834a1d17cda8b7a`

Состав:

- `SHT/KOO__COOP-research-conveyor__SHT.md`
- `SHT/SHA256SUMS.txt`

Внутренняя проверка:

`KOO__COOP-research-conveyor__SHT.md: OK`

SHA-256 задания:

`6203114671c08094518c7bd846fc45fd1205dbf5ab36de46af3e30d695c8287f`

Задание адресовано `SHT`, имеет `priority: P1`, требует файловый-first исследовательский процесс и отдельно требует описать отображение на OSS `request/task/route/receipt/acceptance`.

---

## 2. Конфликт

### Источник A — `project-instructions-core-v2.1`

Статус: `approved_for_active_use`.

Правило доставки:

- различаются `created → published → delivered → received → acknowledgement → accepted`;
- адресная доставка может завершаться:
  1. фактической передачей файла;
  2. проверяемой locator-based delivery существующего артефакта;
- locator-based delivery допустима при существующем артефакте, конкретном адресате, адресном dispatch, доступном locator, проверяемой версии, подтверждённом receipt и failure-mode.

SHA-256 проверенного локального источника:

`8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26`

### Источник B — `file-work-canon-universal-v2.3`

Статус: active approved-редакция.

Он прямо вводит принятую архитектурно-нормативную модель двух допустимых способов адресной доставки:

1. физическая передача файла;
2. проверяемая locator-based delivery существующего артефакта.

Также отдельно фиксирует, что publication, delivery, receipt, acknowledgement и acceptance — разные состояния.

SHA-256 проверенного локального источника:

`5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5`

### Источник C — `source-loading-policy-v2`

Статус: `approved_for_active_use`.

Раздел `5. Маршрутизация файлов` всё ещё устанавливает иной набор терминальных вариантов:

- файл фактически загружен в адресный чат; либо
- зафиксирована конкретная причина невозможности доставки и следующий шаг.

Locator-based delivery как допустимый способ завершения маршрута в этом approved-источнике отсутствует.

SHA-256 проверенного локального источника:

`2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061`

---

## 3. Почему конфликт блокирует именно эту задачу

Исследовательский конвейер должен определить:

- source-card и claim-card;
- переходы ownership;
- parallel research dispatch;
- merge конфликтующих результатов;
- evidence-matrix gate;
- failure modes;
- последующее отображение на OSS `request/task/route/receipt/acceptance`.

Следовательно, выбор нормы доставки влияет не на оформление отчёта, а на сам процесс:

- что считать `delivered`;
- когда возникает `receipt`;
- когда source-card/claim-card может перейти к следующему участнику;
- как работает файловый маршрут без ручного ОПЕРАТОРА;
- какой failure-state возникает при доступном artifact locator, но отсутствии физической загрузки в чат.

Молчаливо выбрать одну из двух approved-норм означало бы самостоятельно устранить нормативный конфликт, что ШТАБИСТУ запрещено.

---

## 4. Минимальное решение, необходимое для продолжения

Нужно одно явное решение ОПЕРАТОРА либо нормативно оформленное решение через уполномоченный контур:

### Вариант 1 — подтвердить новую норму

Зафиксировать, что раздел `5. Маршрутизация файлов` в `source-loading-policy-v2` в части способов завершения адресной доставки **superseded** более новой approved-моделью `project-instructions-core-v2.1` + `file-work-canon-universal-v2.3`, и поручить КАНЦЕЛЯРУ подготовить согласованную редакцию source-loading policy.

### Вариант 2 — сохранить физическую загрузку как обязательную

Явно установить, что для данного класса исследовательских маршрутов locator-based delivery пока не считается терминальной доставкой, несмотря на общую норму core/file canon.

Для проектируемой общей среды этот вариант создаст исключение, которое придётся явно отразить в процессе и OSS mapping.

---

## 5. Рекомендация SHT

Рекомендую **вариант 1**.

Причина: `project-instructions-core-v2.1` и `file-work-canon-universal-v2.3` согласованно и подробно вводят locator-based delivery, включая version identity, receipt и failure-mode. `source-loading-policy-v2` выглядит как негармонизированный остаток прежнего правила маршрутизации.

Но это только организационная рекомендация. Она не заменяет явного нормативного решения.

---

## 6. Следующий безопасный шаг

После явного разрешения конфликта SHT продолжает **эту же P1-задачу**, не создавая новую постановку, и готовит один результат:

`SHT__COOP-research-conveyor-v01-candidate__KOO.md`

До разрешения конфликта:

- отдельная IT-система не проектируется;
- OSS schema/API не проектируется;
- research-conveyor не объявляется готовым;
- задача не считается `PASS` или `READY`.

---

## Служебная карточка

from_entity: SHT  
to_entity: KOO  
document_type: source-conflict-stop-report  
project_scope: ШТАБ БЛАГОПОЛУЧИЯ  
topic: COOP-research-conveyor  
input_task: KOO__COOP-research-conveyor__SHT.md  
input_task_sha256: 6203114671c08094518c7bd846fc45fd1205dbf5ab36de46af3e30d695c8287f  
status: BLOCKED_SOURCE_CONFLICT  
profile_execution_started: no  
recommended_resolution: supersede source-loading-policy-v2 section 5 delivery rule by approved core-v2.1 + file-work-canon-v2.3 model, then harmonize source-loading policy  
project_time: generated_without_trusted_project_time
