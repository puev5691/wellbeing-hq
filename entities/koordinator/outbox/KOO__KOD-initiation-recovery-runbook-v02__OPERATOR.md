# KOO → OPERATOR: инициация нового экземпляра KOD / КОДЕРА v0.2

Статус: `INITIATION_RUNBOOK_READY`
Канон: нет
Назначение: запустить новый/другой чат KOD через recovery, не выдавая ему current-writer authority автоматически.

## Основание

Fresh HQ preflight перед подготовкой этого runbook:
`puev5691/wellbeing-hq@fdfa35751e137b9cb1ab8d12097531452b1d4bfb`.

Проверяемое текущее состояние:

1. Canonical KOD recovery существует и независимо проверен ARH:
   `puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`

2. Exact initiation locator:
   `puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current/KOD__initiation-current__KOD.md`

3. ARH verification:
   `entities/archivarius/outbox/ARH__KOD-emergency-recovery-verification__KOD.md`
   commit `78a8f278e3a332bce05e28352e1316ea18f0a13c`
   verdict `PASS_PUBLISHED_CANONICAL_RECOVERY`.

4. Existing verified KOD current-writer artifact:
   `entities/koder/current/KOD__initiation-verified-current-writer-v01.md`
   commit `b7cdd1cbb28c9f144ca26d23823ba4b42973fd5f`
   blob `92a9e006c37589fee03479a81e4f53608b982ef0`.

5. Более свежий KOD результат, который старый recovery ещё не содержит:
   `entities/koder/outbox/KOD__info-entry-static-preview-E1-fix-v03__KOO.md`
   result commit `1f31bc2b640a456f2f99655620e809ce8eaeaada`
   package commit `434ffc103b620711ab4f784d8c825e17bd91a927`
   verdict `PASS_STATIC_PREVIEW_E1_EVIDENCE_ALIGNMENT`.

Следовательно, новый KOD не должен считать recovery snapshot исчерпывающим current state. После восстановления обязателен fresh HQ reconciliation всех KOD evidence, появившихся после recovery publication.

## Операторский промпт для нового чата KOD

> Проведи инициацию нового экземпляра KOD / КОДЕРА по recovery-канону.
>
> Canonical recovery:
> `puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`
>
> Exact initiation file:
> `puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current/KOD__initiation-current__KOD.md`
>
> Независимая ARH-проверка:
> `entities/archivarius/outbox/ARH__KOD-emergency-recovery-verification__KOD.md`
> commit `78a8f278e3a332bce05e28352e1316ea18f0a13c`
> verdict `PASS_PUBLISHED_CANONICAL_RECOVERY`.
>
> Выполни строго Resume/Recovery-First:
> 1. загрузи действующие approved Project Sources;
> 2. проверь immutable recovery locator, composition и checksums по внешним байтам;
> 3. сделай fresh GitHub-preflight `puev5691/wellbeing-hq`;
> 4. reconcile все KOD state/result/receipt/task evidence, появившиеся после recovery commit `f134dac1...`;
> 5. отдельно учти свежий E1 result `1f31bc2b640a456f2f99655620e809ce8eaeaada` и package `434ffc103b620711ab4f784d8c825e17bd91a927`;
> 6. проверь existing current-writer artifact `entities/koder/current/KOD__initiation-verified-current-writer-v01.md`, commit `b7cdd1cbb28c9f144ca26d23823ba4b42973fd5f`;
> 7. проверь competing/current-writer boundary;
> 8. верни первый initiation report с exact `initiation_status`, recovery identity, fresh HQ HEAD, delta since recovery, current-writer state и next permissible boundary.
>
> До `initiation_verified` работай read-only и не выполняй профильные mutable-задачи.
>
> ВАЖНО: не объявляй себя новым current-writer только потому, что инициация успешна. Если прежний verified KOD current-writer не имеет отдельной retirement/replacement boundary, остановись после `initiation_verified` в `WAITING_OPERATOR_WRITER_DECISION`.
>
> Не возобновляй автоматически historical/parked KOD tasks. Не выполняй production/deployment, live external calls, credentials/secrets, destructive cleanup или high-impact действия из recovery.

## Writer boundary

Этот runbook не выводит старый KOD current-writer из работы и не выполняет writer transfer.

Если ОПЕРАТОР отдельно решает прекратить authoritative работу прежнего KOD instance, после такого решения новый `initiation_verified` экземпляр может пройти отдельный replacement/current-writer gate с competing-writer check и immutable readback.

До этого допустимый итог нового чата:
`initiation_verified / WAITING_OPERATOR_WRITER_DECISION`.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: безопасно инициировать новый экземпляр КОДЕРА из canonical recovery и свежего GitHub evidence без самовольной передачи writer authority
СТАТУС: initiation_runbook_ready_v02
