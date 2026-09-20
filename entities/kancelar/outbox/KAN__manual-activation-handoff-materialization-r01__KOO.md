# KAN → KOO: manual activation handoff canonical materialization r0.1

status: `PASS_KAN_MANUAL_ACTIVATION_HANDOFF_READY_FOR_KOO_SOURCE_SET_BARRIER`
active_source_mutations: `0`
source_successors_materialized: `2`
project_time: omitted; trusted project-time source not used

## Что произошло

RED передал точную нормативную поправку:

`entities/redaktor/outbox/RED__manual-activation-handoff-amendment-r01__KAN-KOO.md`

commit:
`6c5bac16ae7fc72d5ad4c1831e5537e0e424848a`

blob:
`813ab8fa97f2c12284c06a746c908e963f270dc1`.

ОПЕРАТОР в текущем KAN task явно утвердил смысл поправки:

> пока automatic exact Entity-chat orchestration фактически отсутствует, каждый human-facing terminal result, после которого работа продолжается в другом Entity-чате, должен выдавать готовый блок `АДРЕСАТ + PROMPT + ДЕЙСТВИЕ ОПЕРАТОРА`.

KAN выполнил fresh GitHub-preflight, проверил действующие approved sources и материализовал минимальный successor source-set без изменения active Project Sources.

## Что это означает

Нормативная поправка совместима с действующей моделью authority и task conveyor.

Она не создаёт task authority:
- исполнившая Сущность может дать следующий профильный PROMPT только в пределах уже существующего authority;
- если authority выбрать следующий шаг отсутствует, применяется safe fallback на KOO;
- KOO выполняет fresh Resume-First reconciliation и выбирает только уже авторизованный допустимый шаг.

Она также не смешивает:
- artifact routing;
- chat activation;
- `processing_started`.

Publication / inbox / dispatch / receipt остаются доказательствами файлового маршрута, но не заменяют фактическую ручную активацию другого Entity-чата.

## Проверка недублирования

### project-instructions-core

Изменение требуется.

Active `project-instructions-core-v2_2-approved.md` уже устанавливает, что manual Entity-chat activation выполняется через готовый PROMPT и что GitHub publication/inbox/dispatch не доказывают activation.

Но core не устанавливает обязательность готового post-terminal handoff в каждом human-facing terminal result.

Поэтому добавлена только cross-cutting obligation и safe fallback на KOO.

### task-conveyor-canon

Изменение требуется.

Active `task-conveyor-canon-v1-approved.md` уже требует от KOO готовый activation payload, но §10 относится в первую очередь к KOO после подготовки шага.

Новая версия:
- распространяет handoff requirement на terminal result любой участвующей Сущности;
- задаёт exact блок `АДРЕСАТ / PROMPT / ДЕЙСТВИЕ ОПЕРАТОРА`;
- закрепляет safe fallback на KOO;
- фиксирует, что routing/receipt/PROMPT creation сами по себе handoff не заменяют.

### entity-roles-short

Изменение **не требуется**.

Active `entity-roles-short-v2_4-approved.md` уже говорит:
- ОПЕРАТОР получает от KOO готовый PROMPT и не реконструирует задачу из GitHub/очереди/locator;
- KOO выполняет fresh reconciliation, выбирает следующий уже авторизованный шаг и отдаёт готовый activation payload.

Повторение нового полного post-terminal алгоритма в roles добавило бы дублирование, но не новую responsibility/authority.

Поэтому proposed RED `entity-roles-short-v2_5` в этот bounded source-set не включён.

### Остальные approved sources

Без изменений:
- `file-work-canon-universal-v2_4-approved.md`;
- `source-loading-policy-v2_2-approved.md`;
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`.

Поправка не меняет file delivery, source loading, recovery, current-writer или preservation semantics.

## Материализованный successor source-set

Directory:

`entities/kancelar/outbox/manual-activation-handoff-r01/`

### 1. Project core successor

Path:

`entities/kancelar/outbox/manual-activation-handoff-r01/project-instructions-core-v2_3-approved.md`

commit:

`6286962c6218072d174f87e2a040687719fbe3a6`

blob:

`e51054d57c583bbbecc79716e1d5543e686efbd8`

SHA-256:

`5d6fceee3d667e761996cae160ba19060f4a2f054901d4700d29f1b8f22ee75c`

Exact text readback:

`PASS`.

Status inside source:
`approved / active only after source-set activation barrier PASS`.

### 2. Task conveyor successor

Path:

`entities/kancelar/outbox/manual-activation-handoff-r01/task-conveyor-canon-v1_1-approved.md`

commit:

`6d13d7ffcfb837492ed999c904a5f5bcc210b0a0`

blob:

`0ff3d3f74d5793ea72cc9e84fffc64f01e8455ab`

SHA-256:

`9eb9befd114bcf45b11fe1b419d104f290ccda2eb0b2fdc69b9971d493e1080b`

Exact text readback:

`PASS`.

Status inside source:
`approved / active only after source-set activation barrier PASS`.

### 3. Source-set manifest

Path:

`entities/kancelar/outbox/manual-activation-handoff-r01/SOURCE-SET-MANIFEST.md`

commit:

`c20badfb6c4920f7e85b119fed8108d3d0a367c2`

blob:

`a4711b2e43f81978a06947128693c72bcce21eca`

SHA-256:

`da31a7846f5d90ee0489c878b5e5d5a61b055500b9d7946b40b7be41aff5feda`

Exact text readback:

`PASS`.

## Activation boundary

Эти два successor source являются одним bounded activation unit.

До KOO source-set activation barrier:
- current active core остаётся `project-instructions-core-v2_2-approved.md`;
- current active conveyor остаётся `task-conveyor-canon-v1-approved.md`;
- materialized successors ещё не считаются active Project Sources.

KOO должен:
1. fresh-reconcile exact identities;
2. проверить оба source SHA-256/readback;
3. провести source-set activation barrier как один unit;
4. не активировать только один из двух;
5. после PASS зафиксировать новые active source identities и supersession:
   - core v2.2 → v2.3;
   - conveyor v1.0 → v1.1;
6. вернуть human-facing terminal result.

## Scope boundary

В этот materialization не включены:
- previous broader RED operator-interface decision-packet amendment;
- human-readable event journal;
- изменения roles;
- изменения file-work/source-loading/recovery;
- automatic orchestrator implementation.

Это исключено намеренно как scope expansion.

## Terminal result

`PASS_KAN_MANUAL_ACTIVATION_HANDOFF_READY_FOR_KOO_SOURCE_SET_BARRIER`

next_owner:
`KOO / source-set activation barrier`

manual_activation_required:
`yes, unless exact KOO chat is activated by an independently verified authorized mechanism`

---

sender: KAN
recipient: KOO
document_type: manual-activation-handoff-canonical-materialization
operator_approved_scope: yes
active_source_mutations: 0
project_time: omitted; trusted project-time source not used
