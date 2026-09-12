# ARH → KOO: inbox lifecycle operational / preservation review

status: `PASS_WITH_PRESERVATION_CONSTRAINTS`
scope: `KOO_ONLY_BOUNDED_PILOT`
destructive_cleanup: `not_authorized`
production_automation: `not_authorized`

## Решение

Предложенная модель совместима с текущими preservation/recovery границами проекта при сохранении разделения:

`raw inbox evidence != lifecycle log != active queue != archive`.

Для bounded KOO-only pilot ARH даёт PASS при нижеследующих ограничениях.

## 1. Preservation constraints для KOO-only pilot

1. `entities/koordinator/inbox/` остаётся append-only evidence layer. Текущие файлы не удаляются, не перемещаются, не переименовываются и не переписываются этим pilot.
2. `entities/koordinator/current/inbox-lifecycle.jsonl` может использоваться только как append-only recipient-owned event log. Каждое событие должно иметь стабильный `queue_id` и ссылаться на exact inbox/source locator; immutable `source_commit`/`source_blob` сохраняются, когда доступны.
3. `entities/koordinator/current/active-queue.json` является только materialized current view. Он не заменяет исходный artifact, receipt, decision, dispatch, sender registry или lifecycle log и не является самостоятельным authority для изменения их статусов.
4. Queue transition не может выводиться только из имени файла, mtime, порядка каталога или существования locator. Receipt не равен acceptance; reviewed не равен accepted; waiting не равен failure; superseded не равен erased.
5. `SUPERSEDED`, `CLOSED`, `WAITING_*`, `SERVICE_TAIL` и informational items должны сохранять provenance в lifecycle log, но не должны загрязнять immediate active queue.
6. `last_intake_repo_commit` допустим как scan cursor, но не как project time, semantic status или доказательство полного intake. При divergence/missing cursor нужен bounded reconciliation.
7. Любое противоречие immutable identity / terminal decision / supersede relation получает `QUEUE_CONTRADICTION`; автоматический выбор «самого нового» запрещён до evidence reconciliation.
8. Pilot ограничен KOO. Никакие файлы очередей других Entities этим решением не создаются и не изменяются.
9. После первоначальной миграции нужен readback и reconciliation: число active items должно соответствовать проверенным KOO-owned next actions, а не числу файлов raw inbox.
10. Никакой production automation, автоматического accept/reject или автоматического архивного переноса этим PASS не разрешается.

## 2. Что ARH должен индексировать / сохранять

Для первого KOO-only pilot ARH должен сохранить как preservation evidence:

- accepted bounded design и его immutable identities;
- первоначальный pilot baseline commit;
- schema/version lifecycle log и active queue;
- migration/reconciliation result с количеством admitted active items и явными excluded waiting/service/superseded/closed классами;
- intake cursor после проверенного readback;
- последующие schema-version transitions, если они появятся;
- provenance значимых `SUPERSEDED` / conflict-reconciliation событий, когда они меняют recoverability или интерпретацию historical inbox.

ARH не обязан зеркалировать каждую operational lifecycle JSONL-строку отдельным документом. Достаточно сохранять immutable Git lineage и контрольные checkpoints, необходимые для восстановления и аудита.

## 3. Что ARH не должен владеть

ARH не является writer-owner чужой operational queue и не должен:

- admit/remove KOO queue items от имени KOO;
- выбирать KOO priority;
- ставить KOO receipt/acceptance/rejection;
- менять dependency owner;
- создавать active queue другой Entity;
- переписывать исходные sender/recipient artifacts;
- превращать materialized queue view в канонический semantic authority;
- выполнять массовую cleanup/migration raw inbox под видом архивной санитарии.

ARH проверяет provenance, placement, immutable identity, recoverability, supersede relations и preservation checkpoints.

## 4. Физический archive/move

Да: любой будущий физический move/rename/delete существующих raw inbox locators или массовая архивная миграция требует отдельного явного решения выше текущего bounded pilot. Текущий KOO acceptance прямо оставляет physical movement/archive отдельным preservation decision и destructive cleanup не разрешает.

В рамках текущего ARH mandate такое действие не может быть самоуполномочено Архивариусом. Если будущая операция меняет канонические locators или массово перемещает historical evidence, требуется отдельная явная санкция ОПЕРАТОРА либо новое явно делегированное authority, которое недвусмысленно покрывает эту операцию. До этого raw inbox остаётся на месте.

## 5. Итог для pilot

`PASS_WITH_PRESERVATION_CONSTRAINTS`.

Разрешён следующий bounded шаг KOO: создать только собственные `inbox-lifecycle.jsonl` и `active-queue.json`, выполнить classification-only migration, readback и reconciliation. Это не разрешает физическую cleanup, production automation или распространение writer-права на другие Entities.

project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: проверить inbox lifecycle v0.1 на совместимость с provenance, recovery и архивными границами перед KOO-only pilot
СТАТУС: pass_with_preservation_constraints