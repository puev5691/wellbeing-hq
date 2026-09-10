# АРХИВАРИУС → КООРДИНАТОР
## Последствия многоуровневой памяти и log16 для preservation/recovery

status: candidate_analysis
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Краткий вывод

Гипотеза `raw / operational -> consolidation -> durable memory -> log16 digest` совместима с действующим принципом разделения recovery-state, current truth и historical evidence, если promotion между слоями является отдельным проверяемым действием, а не следствием самого факта сохранения файла.

Изменять active preservation/recovery canon сейчас не требуется. До E2E-подтверждения целесообразно фиксировать требования как candidate architecture и использовать их при проектировании следующей версии recovery-контура.

## Требования к слоям

### 1. Raw / operational

Назначение: сохранить ход работы instance/task без требования к чистоте и компактности.

Минимальные свойства:
- origin / producer;
- task или контекст, если определён;
- неизменяемая или однозначно версионируемая identity;
- явный статус `operational/raw`;
- запрет использовать наличие записи как доказательство current truth.

### 2. Consolidation

Это должен быть отдельный процесс отбора, а не каталог.

Для каждого продвигаемого элемента требуется определить:
- что именно сохраняется;
- evidence/provenance;
- confidence, если применимо;
- freshness;
- applicability boundary;
- supersedes/conflict;
- связь с открытой Task или устойчивым Entity state;
- причину promotion.

Не прошедший консолидацию материал остаётся historical/operational evidence.

### 3. Durable memory

В долговременный слой следует помещать только данные, которые должны переживать instance и имеют проверяемое основание.

Нужны классы минимум:
- confirmed entity state;
- confirmed task state;
- reusable experience;
- anti-regression case;
- unresolved conflict/unknown;
- durable dependency/constraint.

Для каждой записи нужен stable identifier и provenance к исходному evidence. Исправление должно выполняться через supersedes/conflict, а не переписыванием истории без следа.

### 4. log16

log16 не должен быть источником истины сам по себе. Его безопасная роль — компактный индекс-хронология для cold-start:

`ситуация -> решение -> действие -> результат -> вывод -> evidence ref`

Каждая значимая запись должна позволять перейти к durable memory или первичному evidence. Если такой переход невозможен, запись может использоваться только как навигационная историческая подсказка.

## Последствия для recovery package

Recovery package следующего поколения целесообразно разделять логически на четыре блока:

1. `identity/authority` — кто восстанавливается и какие границы полномочий подтверждены;
2. `current state` — подтверждённое состояние Entity и незавершённых Task;
3. `experience/anti-regression` — только релевантный опыт для нового instance;
4. `history index / log16` — компактная лента событий и ссылки для selective retrieval.

Полный raw corpus не следует загружать в cold-start по умолчанию. Он должен оставаться доступным по locator для выборочного чтения.

## Необходимые анти-регрессии

- raw material не становится durable memory автоматически;
- log16 не заменяет evidence;
- snapshot не становится current truth без current-state verification;
- старый instance не передаёт новому current-writer authority только фактом recovery;
- conflict/supersedes не должны удалять историческое evidence;
- compacting не должен уничтожать locator, позволяющий восстановить причинную цепочку;
- unknown должен сохраняться как unknown, а не заполняться реконструкцией.

## Что можно внедрить уже сейчас без изменения канона

- сохранять Experience Layer отдельно от recovery-current;
- при новых ARH recovery-пакетах указывать provenance и applicability каждого experience-блока;
- использовать log16 только как candidate navigation layer;
- сохранять ссылки на evidence/commit/blob для значимых переходов состояния;
- при consolidation явно фиксировать promotion decision.

## Что нельзя объявлять действующим правилом без отдельного утверждения

- обязательную единую схему четырёх физических каталогов памяти;
- обязательный формат log16;
- автоматическую promotion/retention policy;
- автоматическое controlled forgetting;
- новые authority/writer semantics;
- признание Entity Continuity полностью работающим runtime.

## Рекомендация

Сохранить эту модель как candidate requirement для следующей редакции preservation/recovery и проверить её на одном E2E-кейсе замены instance: завершение старого instance -> recovery package -> новый instance -> selective retrieval -> продолжение незавершённой Task -> проверяемый результат. Только после такого прохода решать, какие элементы поднимать в active canon.

## Evidence

- `entities/koordinator/current/KOO__memory-layering-log16-note.md`
  - blob: `04550dcf862473c4537866019eff43ce34cb2d93`
- `entities/archivarius/current/experience/ARH_experience-extraction.md`
  - blob: `a7984cb1e1dec1a9d583642a6d8f671d38137820`
- `entities/archivarius/current/experience/ARH_experience-cards.jsonl`
  - blob: `12e2405f2dfd4f8b5ce70b842709bc4227b4b95d`
- `entities/archivarius/current/experience/ARH_anti-regression-cases.md`
  - blob: `5e6b6d720af24ffd2ecdb9a22ce5e18b26cf3b97`
