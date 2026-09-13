# SHT → KOO: минимальный machine-readable contract параллельных lanes

status: BOUNDED_MACHINE_CONTRACT_CANDIDATE
scope: future_scheduler_and_gui_interface
implementation: no
automation_change: no
production_change: no
new_authority: no
project_time: omitted

## Смысл и требуемое действие

Этот contract переводит принятую process-модель параллельных lanes в минимальный машинно-читаемый интерфейс для будущего scheduler/GUI. Он не создаёт scheduler, не меняет automation, не даёт никому новых полномочий и не превращает KOO working directive в Project Source.

Exact task:
`entities/koordinator/outbox/KOO__parallel-lane-machine-contract__SHT.md`
commit `32b02ac427522741190891a597c99ac981e8bd00`
blob `1d611357faa5f6d5c877c7cf4b6483b5d69f4d96`.

Basis:
`entities/shtabist/outbox/SHT__adaptive-parallel-queue-review__KOO.md`
commit `f4134b18ac16a862cae7a78e2b7d78212e406bcc`
blob `f3523e4522805294bf049a64f0b7a00c03dd9561`.

KOO working adoption:
`entities/koordinator/current/KOO__parallel-lane-operating-delta-v01.md`
commit `462b258a8031d20d1317c26a3d7d86e7229201b0`.

## 1. Minimal lane object

Рекомендуемый carrier: JSON object. Имена ниже являются интерфейсом v0.1 candidate, а не production schema.

```json
{
  "schema": "parallel-lane-v0.1-candidate",
  "lane_id": "string",
  "entity": "string",
  "pipeline": "string",
  "exact_input": {
    "locator": "string|null",
    "commit": "40hex|null",
    "blob": "40hex|null",
    "identity_status": "VERIFIED|UNVERIFIED|NOT_APPLICABLE"
  },
  "state": "READY_PARALLEL|RUNNING|WAITING_EXTERNAL|WAITING_ENTITY|WAITING_OPERATOR|CONFLICT|CLOSED",
  "queue_participation": "adaptive|excluded_operator_direct_control",
  "scheduler_eligible": true,
  "priority": {
    "reason": "string|null",
    "ready_age": 0
  },
  "causal_parents": ["lane_id-or-artifact-id"],
  "downstream_decision": {
    "decision_id": "string|null",
    "required_parent_set": ["lane_id-or-result-id"],
    "decision_owner": "string|null"
  },
  "mutable_write_set": ["resource-or-locator"],
  "resource_set": ["resource-id"],
  "current_writer_domain": "string|null",
  "authority_dependency": {
    "kind": "NONE|ENTITY|OPERATOR|EXTERNAL|RELEASE_DECISION",
    "owner": "string|null",
    "locator": "string|null"
  },
  "conflict_edges": [
    {
      "with_lane": "lane_id",
      "type": "CAUSAL|MUTABLE_WRITE|CURRENT_WRITER|RESOURCE|AUTHORITY|DOWNSTREAM_DECISION",
      "reason": "string"
    }
  ],
  "pending_return_event": {
    "event_type": "RESULT_RETURNED|RECEIPT_RETURNED|DECISION_RETURNED|OPERATOR_DIRECTION|NONE",
    "expected_from": "string|null"
  },
  "expected_result": {
    "locator": "string|null",
    "result_type": "string|null"
  },
  "last_verified_event": {
    "event_type": "string|null",
    "artifact": "string|null",
    "commit": "40hex|null",
    "blob": "40hex|null"
  },
  "reconciliation_status": "NOT_REQUIRED|WAITING_PARENTS|READY_FOR_RECONCILIATION|CONFLICT|RECONCILED|STALE_NEEDS_REVALIDATION"
}
```

## 2. Поля и semantics

### `lane_id`

Стабильный ID конкретного причинного рабочего узла. Не имя Entity и не filename. Повторный Resume-First той же задачи сохраняет lane_id; новый causal branch получает новый lane_id.

### `entity`

Профильная Сущность, которой уже принадлежит текущий next action по действующей authority boundary. Поле не создаёт authority.

### `pipeline`

Стабильный идентификатор причинной цепочки, например `telegram-phase1b` или `github-info-entry`. Несколько lanes могут принадлежать одному pipeline только если они реально независимы.

### `exact_input`

Locator плюс immutable commit/blob, если input является Git artifact. Для `READY_PARALLEL` identity_status должен быть `VERIFIED`, кроме случая, где task contract явно допускает `NOT_APPLICABLE`.

### `state`

Operational class из принятой модели. `RUNNING` разрешён только при processing evidence. Inbox placement или activation request сами по себе RUNNING не создают.

### `queue_participation`

`adaptive` — lane участвует в adaptive scheduler selection.
`excluded_operator_direct_control` — lane видима в DAG, но scheduler не вправе её активировать.

### `scheduler_eligible`

Boolean eligibility после authority и queue-participation guards. Для `READY_PARALLEL` обычно true. Для SHD direct-control false. Для любых WAITING/CONFLICT/CLOSED false.

### `priority.reason` и `ready_age`

Reason фиксирует проверяемую причину приоритета: safety/recovery, OPERATOR directive, downstream-unblock, causal continuation, starvation, bounded verification, round-robin. `ready_age` — число reconciliation passes, в которых lane была READY, но не выбрана. Проектное время не требуется.

### `causal_parents`

Exact predecessor lanes/artifacts/results, без которых текущая lane невалидна. Непустой parent, который ещё не завершил требуемое событие, обычно исключает `READY_PARALLEL`.

### `downstream_decision`

Decision node, на который возвращается результат. `required_parent_set` задаёт, какие результаты должны быть reconciled до исполнения decision. `decision_owner` только отражает уже действующую competence/authority.

### `mutable_write_set`

Набор exact mutable targets/current records, которые lane намерена менять. Пересечение двух write sets запрещает совместный запуск, если нет заранее доказанной безопасной concurrency semantics.

### `resource_set`

Host, runtime, deployment slot, credential/config state, live external channel, exclusive device/session, test environment и другие ресурсы, где concurrent mutation может влиять на результат.

### `current_writer_domain`

Canonical current-state lineage, recovery/current writer domain или другой singleton writer scope. Совпадение domain у двух writer-lanes является hard conflict, пока exact rule не разрешает иное.

### `authority_dependency`

Нужное внешнее/Entity/OPERATOR/release решение до дальнейшего продвижения. Scheduler не может превратить эту dependency в собственную competence.

### `conflict_edges`

Pairwise hard conflicts. Edge должен быть симметрично воспроизводим из полей lanes либо объяснён exact reason. `READY_PARALLEL` lane не должна иметь unresolved hard edge с lane из того же activation batch.

### `pending_return_event`

Событие, после которого lane нужно вновь reconciliate. Особенно важно для excluded SHD и WAITING states.

### `expected_result`

Ожидаемый standalone artifact/decision. Locator может быть null до появления exact filename, но result_type и pending event должны позволять определить completion boundary.

### `last_verified_event`

Последнее проверенное causal событие. Никаких inferred processing/receipt/acceptance.

### `reconciliation_status`

Показывает состояние downstream merge независимо от lane state. Arrival order результатов не определяет decision order.

## 3. Validation invariants

1. `lane_id` уникален в текущем queue snapshot и стабилен для одной causal task identity.
2. `READY_PARALLEL` требует `queue_participation=adaptive`, `scheduler_eligible=true`, verified executable input и отсутствия unresolved hard conflict edges с выбранным batch.
3. `RUNNING` требует отдельного processing-start evidence; dispatch/inbox placement недостаточны.
4. `WAITING_*`, `CONFLICT`, `CLOSED` всегда имеют `scheduler_eligible=false`.
5. `excluded_operator_direct_control` всегда имеет `scheduler_eligible=false`, но lane не удаляется из DAG.
6. Если незавершённый `causal_parent` является required predecessor, descendant не может быть `READY_PARALLEL`.
7. Пересечение `mutable_write_set` или одинаковый singleton `current_writer_domain` создаёт hard conflict, если explicit safe-concurrency rule отсутствует.
8. Unsafe shared `resource_set` создаёт RESOURCE conflict.
9. Общий `downstream_decision.decision_id` не запрещает параллельный сбор independent evidence, но decision node остаётся non-executable до reconciliation required_parent_set.
10. Два returned results не могут independently mutate один downstream decision/current state. При несовместимости reconciliation_status=`CONFLICT`.
11. `authority_dependency.kind != NONE` блокирует scheduler, если exact task не является именно подготовкой evidence до этого decision и не требует самого authority action.
12. `ready_age` не повышает lane выше safety/recovery/current-writer/authority guards.
13. `CLOSED` не выводится из одного receipt или inbox placement; completion contract конкретной lane должен быть выполнен.
14. При identity mismatch `exact_input.identity_status=UNVERIFIED`, state не может быть READY_PARALLEL/RUNNING.
15. Любое изменение causal parents, write/resource sets, writer domain, authority dependency или returned result требует нового reconciliation pass и пересчёта conflict graph.
16. Machine contract описывает state; он не является источником authority, acceptance или production permission.

## 4. Пример: три независимых READY_PARALLEL

Иллюстративный machine snapshot; IDs `ex-*` не являются рабочими задачами.

```json
[
  {
    "lane_id":"ex-ready-kod",
    "entity":"KOD",
    "pipeline":"local-model-gateway",
    "exact_input":{"locator":"example/kod-task.md","commit":"1111111111111111111111111111111111111111","blob":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","identity_status":"VERIFIED"},
    "state":"READY_PARALLEL","queue_participation":"adaptive","scheduler_eligible":true,
    "priority":{"reason":"bounded_verification","ready_age":1},
    "causal_parents":[],
    "downstream_decision":{"decision_id":"decision-gateway-review","required_parent_set":["ex-ready-kod-result"],"decision_owner":"KOO"},
    "mutable_write_set":["entities/koder/outbox/example-gateway-result.md"],
    "resource_set":["local-synthetic-fixtures"],
    "current_writer_domain":"koder:gateway-result",
    "authority_dependency":{"kind":"NONE","owner":null,"locator":null},
    "conflict_edges":[],
    "pending_return_event":{"event_type":"RESULT_RETURNED","expected_from":"KOD"},
    "expected_result":{"locator":"entities/koder/outbox/example-gateway-result.md","result_type":"bounded_result"},
    "last_verified_event":{"event_type":"TASK_DISPATCHED","artifact":"example/kod-task.md","commit":"1111111111111111111111111111111111111111","blob":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},
    "reconciliation_status":"NOT_REQUIRED"
  },
  {
    "lane_id":"ex-ready-kan","entity":"KAN","pipeline":"provider-evidence","exact_input":{"locator":"example/kan-task.md","commit":"2222222222222222222222222222222222222222","blob":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","identity_status":"VERIFIED"},
    "state":"READY_PARALLEL","queue_participation":"adaptive","scheduler_eligible":true,
    "priority":{"reason":"round_robin","ready_age":2},"causal_parents":[],
    "downstream_decision":{"decision_id":"decision-provider-review","required_parent_set":["ex-ready-kan-result"],"decision_owner":"KOO"},
    "mutable_write_set":["entities/kancelar/outbox/example-provider-matrix.md"],"resource_set":[],"current_writer_domain":"kancelar:provider-matrix",
    "authority_dependency":{"kind":"NONE","owner":null,"locator":null},"conflict_edges":[],
    "pending_return_event":{"event_type":"RESULT_RETURNED","expected_from":"KAN"},"expected_result":{"locator":"entities/kancelar/outbox/example-provider-matrix.md","result_type":"evidence_matrix"},
    "last_verified_event":{"event_type":"TASK_DISPATCHED","artifact":"example/kan-task.md","commit":"2222222222222222222222222222222222222222","blob":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"},"reconciliation_status":"NOT_REQUIRED"
  },
  {
    "lane_id":"ex-ready-web","entity":"WEB","pipeline":"info-entry-preview","exact_input":{"locator":"example/web-task.md","commit":"3333333333333333333333333333333333333333","blob":"cccccccccccccccccccccccccccccccccccccccc","identity_status":"VERIFIED"},
    "state":"READY_PARALLEL","queue_participation":"adaptive","scheduler_eligible":true,
    "priority":{"reason":"downstream_unblock","ready_age":0},"causal_parents":[],
    "downstream_decision":{"decision_id":"decision-preview-review","required_parent_set":["ex-ready-web-result"],"decision_owner":"KOO"},
    "mutable_write_set":["entities/web/outbox/example-preview-pack.md"],"resource_set":["static-preview-only"],"current_writer_domain":"web:preview-pack",
    "authority_dependency":{"kind":"NONE","owner":null,"locator":null},"conflict_edges":[],
    "pending_return_event":{"event_type":"RESULT_RETURNED","expected_from":"WEB"},"expected_result":{"locator":"entities/web/outbox/example-preview-pack.md","result_type":"static_preview"},
    "last_verified_event":{"event_type":"TASK_DISPATCHED","artifact":"example/web-task.md","commit":"3333333333333333333333333333333333333333","blob":"cccccccccccccccccccccccccccccccccccccccc"},"reconciliation_status":"NOT_REQUIRED"
  }
]
```

Три lanes безопасны одновременно, потому что causal parents, downstream decisions, write sets, writer domains и unsafe resources различны.

## 5. Пример: causal conflict

```json
[
  {"lane_id":"ex-causal-A","state":"RUNNING","scheduler_eligible":false,"causal_parents":[],"pending_return_event":{"event_type":"RESULT_RETURNED","expected_from":"SIS"}},
  {"lane_id":"ex-causal-B","state":"WAITING_ENTITY","scheduler_eligible":false,"causal_parents":["ex-causal-A"],"conflict_edges":[{"with_lane":"ex-causal-A","type":"CAUSAL","reason":"B requires verified result A as exact input"}]}
]
```

B нельзя запускать по старому pre-state ради ускорения.

## 6. Пример: shared host/resource conflict

```json
[
  {"lane_id":"ex-host-1","entity":"SIS","state":"READY_PARALLEL","scheduler_eligible":false,"resource_set":["host:mazhor:runtime-config"],"mutable_write_set":["host:mazhor:/etc/example.conf"],"conflict_edges":[{"with_lane":"ex-host-2","type":"RESOURCE","reason":"same non-isolated mutable host runtime"}]},
  {"lane_id":"ex-host-2","entity":"KOD","state":"CONFLICT","scheduler_eligible":false,"resource_set":["host:mazhor:runtime-config"],"mutable_write_set":["host:mazhor:/etc/example.conf"],"conflict_edges":[{"with_lane":"ex-host-1","type":"MUTABLE_WRITE","reason":"same exact mutable target"}]}
]
```

Обе lane не могут входить в один activation batch. Какая идёт первой, определяется существующими authority/priority rules, а не этим contract.

## 7. Пример: shared downstream decision race

```json
[
  {"lane_id":"ex-evidence-A","state":"CLOSED","scheduler_eligible":false,"downstream_decision":{"decision_id":"decision-release-X","required_parent_set":["result-A","result-B"],"decision_owner":"KOO"},"reconciliation_status":"WAITING_PARENTS"},
  {"lane_id":"ex-evidence-B","state":"CLOSED","scheduler_eligible":false,"downstream_decision":{"decision_id":"decision-release-X","required_parent_set":["result-A","result-B"],"decision_owner":"KOO"},"reconciliation_status":"READY_FOR_RECONCILIATION"}
]
```

Когда оба результата вернулись, release decision не определяется порядком прихода. При несовместимости обоих evidence итоговый decision node получает reconciliation_status=`CONFLICT`; last-write-wins запрещён.

## 8. Пример: SHD excluded_operator_direct_control

```json
{
  "lane_id":"ex-shd-direct",
  "entity":"SHD",
  "pipeline":"shd-direct-operator-work",
  "exact_input":{"locator":null,"commit":null,"blob":null,"identity_status":"NOT_APPLICABLE"},
  "state":"RUNNING",
  "queue_participation":"excluded_operator_direct_control",
  "scheduler_eligible":false,
  "priority":{"reason":"operator_direct_control","ready_age":0},
  "causal_parents":[],
  "downstream_decision":{"decision_id":"decision-shd-return","required_parent_set":["shd-result"],"decision_owner":"KOO"},
  "mutable_write_set":[],"resource_set":["operator-controlled:MAZHOR"],"current_writer_domain":null,
  "authority_dependency":{"kind":"OPERATOR","owner":"OPERATOR","locator":null},
  "conflict_edges":[],
  "pending_return_event":{"event_type":"RESULT_RETURNED","expected_from":"SHD"},
  "expected_result":{"locator":null,"result_type":"operator-directed SHD result"},
  "last_verified_event":{"event_type":"OPERATOR_DIRECTION","artifact":null,"commit":null,"blob":null},
  "reconciliation_status":"WAITING_PARENTS"
}
```

`RUNNING` в реальном объекте допускается только при evidence фактической работы. Если такого evidence нет, state должен быть `WAITING_OPERATOR` или иной подтверждённый causal state, но queue_participation и scheduler_eligible остаются прежними.

## 9. Пример: Telegram WAITING_OPERATOR

```json
{
  "lane_id":"ex-telegram-operator-gate",
  "entity":"KOO",
  "pipeline":"telegram-phase1b",
  "exact_input":{"locator":"example/telegram-blocker-result.md","commit":"4444444444444444444444444444444444444444","blob":"dddddddddddddddddddddddddddddddddddddddd","identity_status":"VERIFIED"},
  "state":"WAITING_OPERATOR",
  "queue_participation":"adaptive",
  "scheduler_eligible":false,
  "priority":{"reason":"operator_authority_dependency","ready_age":0},
  "causal_parents":["example-telegram-runtime-result"],
  "downstream_decision":{"decision_id":"telegram-privilege-or-live-gate","required_parent_set":["operator-decision"],"decision_owner":"OPERATOR"},
  "mutable_write_set":[],"resource_set":["telegram-live-or-host-privilege-boundary"],"current_writer_domain":null,
  "authority_dependency":{"kind":"OPERATOR","owner":"OPERATOR","locator":"example/operator-decision-task.md"},
  "conflict_edges":[],
  "pending_return_event":{"event_type":"OPERATOR_DIRECTION","expected_from":"OPERATOR"},
  "expected_result":{"locator":null,"result_type":"operator decision/authorization or rejection"},
  "last_verified_event":{"event_type":"DEPENDENCY_ROUTED_TO_OPERATOR","artifact":"example/operator-decision-task.md","commit":null,"blob":null},
  "reconciliation_status":"WAITING_PARENTS"
}
```

Scheduler не имеет права заменить WAITING_OPERATOR собственным решением или автоматически продвинуть live action.

## 10. GUI projection

GUI может безопасно показывать из этого object минимум:

- lane / Entity / pipeline;
- state и scheduler eligibility;
- verified input identity;
- priority reason + ready_age;
- causal parents;
- conflict badges с reason;
- authority dependency;
- pending return event;
- downstream decision и reconciliation status.

GUI-кнопка `activate` допустима только когда backend validator подтверждает `READY_PARALLEL && scheduler_eligible=true`. GUI не должен вычислять authority сам из имени Entity, цвета карточки или желания пользователя нажать красивую кнопку.

## 11. Boundary для будущей реализации

Следующий технический этап может быть отдельной задачей KOD/WEB на JSON Schema/validator/static GUI mock. Этот документ сам не разрешает такую реализацию и не назначает исполнителя.

До implementation необходимы отдельные решения минимум по:
- canonical storage locator queue snapshot/event log;
- writer ownership этого machine state;
- validator ownership;
- event/versioning format;
- связь с уже предложенным active-queue lifecycle;
- migration/compatibility старых pipeline records.

## Verdict

`BOUNDED_MACHINE_CONTRACT_CANDIDATE`.

Контракт достаточно мал, чтобы будущий scheduler/GUI не изобретал causal/authority semantics самостоятельно, и достаточно явен, чтобы hard conflicts и reconciliation были machine-checkable после отдельной schema/validator реализации.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: преобразовать принятую parallel-lane process-модель в минимальный machine-readable interface для будущего scheduler/GUI без изменения authority
СТАТУС: bounded_machine_contract_candidate
