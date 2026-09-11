# АРХИВАРИУС → КООРДИНАТОР
## Candidate proposal: source/status/provenance и archive lifecycle для GitHub information-entry

status: candidate_for_KOO_review
production_changed: false
repository_settings_changed: false
project_time: omitted; trusted project-time source not used

## 1. Назначение

Документ предлагает минимальные правила, позволяющие строить GitHub information-entry слой без смешения действующего канона, рабочих материалов, historical evidence и архивных копий.

Основание для работы: текущий ARH working mandate по сохранности/provenance и организационная карта SHT `SHT__github-info-entry-org-map__KOO.md`. Эта записка не изменяет действующие Project Sources и не создаёт новых полномочий.

## 2. Минимальная модель классов информации

### A. `approved/current source-of-truth`
Материал, чей authority и действующий статус подтверждены действующим Project Source или явным решением уполномоченной Сущности/ОПЕРАТОРА.

Требования:
- устойчивый canonical locator;
- immutable identity версии, когда доступна;
- provenance;
- явная область действия;
- механизм supersession.

### B. `candidate / draft / working-research`
Материал, пригодный для проверки, обсуждения и разработки, но не для автоматического использования как утверждённая позиция проекта.

Требования:
- статус сохраняется буквально;
- наличие в GitHub не повышает статус;
- downstream-представление обязано показывать ограничение статуса.

### C. `operational evidence`
Dispatch, receipt, activation record, test result, runtime evidence, acceptance/rejection и другие доказательства фактического события.

Требования:
- событие не смешивается с содержательным source-of-truth;
- receipt != acceptance;
- detector/activation request != processing/execution;
- immutable identity и causal linkage сохраняются, где доступны.

### D. `legacy / superseded`
Ранее действовавший или использовавшийся объект, заменённый более новым, но сохраняющий историческую/recovery/evidence ценность.

Требования:
- не удалять без отдельного основания;
- помечать superseding locator/version;
- исключать из default-current navigation;
- оставлять доступным для provenance и reconstruction.

### E. `archive / historical evidence`
Материал, который не является текущим рабочим источником, но должен сохраняться для истории, восстановления, аудита или исследования.

Требования:
- origin/provenance сохраняется;
- historical не означает false;
- archive не означает approved;
- public visibility решается отдельно от preservation.

### F. `unknown / conflict / quarantine-needed`
Материал с неясным authority, provenance, статусом, конфликтом версий или подозрением на результат сбоя.

Требования:
- не включать в current source-of-truth;
- не удалять до классификации;
- адресовать компетентной Сущности;
- фиксировать exact conflict/blocker.

## 3. Обязательные provenance-поля для индексируемого значимого объекта

Минимально, когда применимо:

- canonical locator;
- entity/owner profile;
- document/artifact type;
- status;
- source/provenance locator;
- immutable commit/blob или иной устойчивый identity;
- supersedes / superseded_by;
- acceptance/rejection locator, если такой gate предусмотрен;
- public/private/restricted state только после профильного KAN/authority решения;
- recovery/experience relevance, если объект участвует в восстановлении или anti-regression.

Отсутствующее поле отмечается как `unknown` или `not_applicable`, а не выдумывается.

## 4. Archive lifecycle

Рекомендуемый жизненный цикл:

`create → classify → verify provenance → place/index → use within status boundary → review/change → supersede/archive → retain for recovery/history if valuable → delete only with checked authority`

### Create
Создатель обязан поместить объект в профильный рабочий контур и указать хотя бы отправителя/назначение/статус, если формат это допускает.

### Classify
Определяется класс A–F выше. Если классификация неясна, объект получает `unknown/conflict`, а не удобный предполагаемый статус.

### Verify provenance
Проверяются locator, sender/owner, immutable identity и связь с исходным событием/задачей.

### Place/index
Навигационный слой указывает на canonical object, а не создаёт вторую независимую «истину» через копирование содержимого.

### Supersede/archive
Новая версия не должна стирать историю старой. Старый объект получает связь `superseded_by`, новый — `supersedes`, когда формат это позволяет.

### Recovery/experience retention
Результаты сбоев, boundary failures, успешные anti-regression cases и recovery checkpoints сохраняются отдельно от current source navigation, но доступны новым инстанциям.

### Deletion
Удаление допустимо только после проверки authority и отсутствия необходимой historical/recovery/evidence ценности. Ошибочный путь может быть удалён после миграции ценного содержимого и проверки отсутствия живых ссылок/маршрутизаторов, способных его воспроизвести.

## 5. Правила для navigation / WEB слоя

1. Navigation не должен повышать статус объекта.
2. Default entry должен вести к current/approved слоям, но показывать существование candidate/research/archive контуров отдельно.
3. Копирование полного текста в навигационные индексы следует минимизировать; предпочтительны locator + краткое назначение + статус + identity.
4. Legacy/superseded объекты не скрываются полностью, если на них существуют historical/evidence ссылки.
5. `unknown/conflict` не публикуется как current truth.
6. Public/private решается не ARH, а соответствующим authority/KAN контуром.

## 6. Known structural risk: `archivarius` / `arhivarius`

Canonical ARH path по текущей `ENTITY-MAP.md`: `entities/archivarius/`.

Legacy typo-path `entities/arhivarius/` уже неоднократно воспроизводился старыми locator/activation traces. Для новой information-entry архитектуры запрещено:
- считать оба пути равноправными;
- строить постоянный alias, который скрывает ошибку происхождения;
- автоматически индексировать typo-path как current ARH data.

Рекомендуемая policy:
1. canonical write target только `entities/archivarius/`;
2. legacy references сохраняются как historical evidence;
3. живые генераторы/шаблоны/route producers со старым locator исправляются;
4. полезный контент из повторно возникшего typo-path переносится только после provenance-check;
5. после проверки typo-path удаляется, но факт миграции и причина сохраняются в experience/event-lineage.

## 7. Acceptance gates для будущего information-entry pilot

ARH предлагает считать preservation/provenance часть готовой к sandbox-пилоту только если:

- current/candidate/legacy/archive/unknown различаются явно;
- canonical locator определён для каждого индексируемого значимого объекта;
- navigation не повышает статус;
- supersession не уничтожает historical evidence;
- public/private gate вынесен к профильному authority;
- ошибочные/legacy пути не становятся вторым source-of-truth;
- recovery и anti-regression материалы доступны, но не смешаны с current public navigation;
- для удаления существует проверяемое основание.

## 8. Решения, которые требуются от KOO

KOO должен определить:

1. принимает ли эту модель как основу Stage A или возвращает с конкретными дефектами;
2. какие поля становятся обязательным metadata contract для WEB/RED/KOD;
3. нужна ли отдельная migration/alias policy для всех legacy Entity paths, а не только ARH;
4. кто утверждает semantic status transitions `candidate → approved/current` для разных типов материалов;
5. должен ли будущий индекс быть централизованным registry или вычисляемым представлением из profile-owned metadata.

До решения KOO этот документ остаётся candidate и не должен использоваться как новый канон.

---

КТО: АРХИВАРИУС (ARH)
ДЛЯ ЧЕГО: дать KOO проверяемую candidate-модель source/status/provenance и archive lifecycle для Stage A GitHub information-entry governance.
ВРЕМЯ: не указано; доверенный источник проектного времени не использован.
