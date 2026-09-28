# Entity Operational Continuity Contract r0.1 — candidate

status: CANDIDATE_NOT_ACTIVE
entity: KOO / КООРДИНАТОР
scope: DOCUMENT_ONLY_CONTINUITY_MECHANISM
project_time: omitted

## 1. Человеческий смысл

Проблема, которую закрывает этот кандидат, не в том, что recovery не хранит факты. Действующие Project Sources уже требуют сохранять current-state, следующий безопасный шаг, состояние конвейера и готовый manual activation handoff.

Практический дефект возникает позже: новый экземпляр может корректно прочитать recovery, перечислить PASS-ы и всё равно завершить ответ без правильного следующего действия для человека.

Поэтому этот кандидат НЕ создаёт новый recovery-канон и НЕ дублирует Task Conveyor Canon.

Он вводит три компактных проверяемых operational objects поверх уже действующих норм:

1. CURRENT_STATE_CAPSULE — минимальный causal state конкретной Сущности;
2. CONVEYOR_HEAD — минимальный causal head КООРДИНАТОРА;
3. PRE_SEND_GATE — fail-closed проверка перед human-facing terminal result.

Дополнительно задаётся минимальный набор machine-checkable contradictions, которые должны блокировать завершение результата.

## 2. Нормативная совместимость

Этот кандидат опирается на уже действующие требования:

Project Core v2.5:
- human-facing слой обязан объяснять причинную связь;
- человек должен понимать, где проект находится и что будет следующим;
- manual activation handoff обязателен, если работа должна продолжиться в другом Entity-чате и automatic activation не доказан.

Recovery Canon v1.6:
- recovery должен сохранять результаты, от которых зависят следующие действия;
- recovery должен содержать один понятный/безопасный следующий шаг;
- при initiation replacement instance должен восстановить active/parked tails и следующий безопасный шаг;
- recovery task conveyor восстанавливает состояние конвейера, но не replay старого PROMPT.

Task Conveyor Canon v1.2:
- KOO после replacement Writer Gate выполняет fresh reconciliation;
- historical prompt != current execution authority;
- human-facing terminal result с продолжением в другом чате обязан содержать готовый АДРЕСАТ / PROMPT / ДЕЙСТВИЕ ОПЕРАТОРА;
- ОПЕРАТОР не собирает поручение из нескольких источников;
- перед выдачей PROMPT есть quality gate.

Этот кандидат только материализует эти требования в коротких объектах и проверках.

## 3. Главный принцип

Не заставлять replacement instance "помнить, как лучше".

Вместо этого:

    verified state
    -> explicit causal pointer
    -> pre-send validation
    -> human action / handoff

Результат не считается operationally complete, если causal pointer известен, но human-facing terminal result не передал его человеку в допустимой форме.

## 4. CURRENT_STATE_CAPSULE

### 4.1 Назначение

CURRENT_STATE_CAPSULE — компактное текущее causal-state summary одной Сущности.

Он не заменяет:
- self-snapshot;
- recovery package;
- current-writer artifact;
- exact task;
- authority;
- terminal result.

Он является индексом для быстрого восстановления причинной позиции и обязан ссылаться на exact evidence.

### 4.2 Минимальные поля

    entity
    capsule_status
    current_writer_ref
    current_writer_identity
    current_task_ref
    current_task_status
    last_terminal_ref
    last_terminal_status
    current_blocker
    next_allowed_transition
    next_transition_authority
    next_recipient
    operator_handoff_required
    historical_prompt_replay
    stale_or_unknown_fields
    evidence_refs

Допустимые значения unknown сохраняются явно.

### 4.3 Правила

1. Capsule не создаёт authority.
2. Capsule не создаёт writer rights.
3. Capsule не превращает candidate/pending task в current.
4. Каждое значимое утверждение должно опираться на exact locator + immutable identity либо быть UNKNOWN.
5. current_task_ref может быть NONE, если current task реально отсутствует.
6. next_allowed_transition может быть NONE только с явной причиной.
7. Если current_blocker != NONE, next_allowed_transition не должен молча перепрыгивать blocker.
8. historical_prompt_replay всегда FORBIDDEN, кроме случая, если будущий approved canon явно введёт иной режим.
9. Capsule обновляется только authorized current-writer при существенном изменении causal state.
10. ARH сохраняет и проверяет Capsule как часть recovery, но не исправляет чужой causal state.

## 5. CONVEYOR_HEAD

### 5.1 Назначение

CONVEYOR_HEAD существует только для KOO.

Это не полная очередь и не новый active-queue ledger.

Он отвечает на один вопрос:

> где сейчас верхняя причинная точка конвейера и что должно случиться дальше?

### 5.2 Минимальные поля

    head_status
    current_priority_line
    current_task_ref
    current_task_class
    last_terminal_ref
    last_terminal_class
    blocker
    next_causal_step
    next_step_authority
    next_recipient
    manual_activation_required
    active_prompt_ref
    active_prompt_status
    competing_prompt_status
    parked_lines_summary
    unknowns
    evidence_refs

### 5.3 Классы task/current state

Используются действующие conveyor-классы:

- CURRENT
- COMPLETED
- BLOCKED
- SUPERSEDED
- PAUSED
- UNKNOWN

Новый класс этим кандидатом не вводится.

### 5.4 Правила

1. CONVEYOR_HEAD не заменяет fresh reconciliation.
2. После replacement Writer Gate KOO обязан fresh-reconcile и только потом обновить CONVEYOR_HEAD.
3. Historical PROMPT не может стать active_prompt_ref без нового fresh task materialization.
4. Если current_task_class = BLOCKED, next_causal_step должен либо снимать exact blocker, либо требовать authority/decision для этого.
5. Если current_task_class = COMPLETED, next_causal_step не должен повторять completed task.
6. Если current_task_class = SUPERSEDED, active_prompt_status не может быть ACTIVE.
7. Если next_recipient != KOO и manual_activation_required = YES, human-facing terminal result обязан содержать полный handoff.
8. Если next_causal_step требует нового OPERATOR decision, terminal result обязан содержать одну точную строку решения вместо выдуманного task authority.
9. parked_lines_summary остаётся кратким. Полная история не копируется в head.

## 6. PRE_SEND_GATE

### 6.1 Назначение

PRE_SEND_GATE выполняется перед каждым human-facing terminal result, после которого:
- causal work должна продолжиться;
- требуется решение ОПЕРАТОРА;
- требуется ручная activation другого Entity-чата;
- либо заявляется, что никакого действия не требуется.

Gate проверяет не красоту ответа, а причинную полноту.

### 6.2 Обязательные проверки

    G1 HUMAN_CAUSAL_EXPLANATION
    G2 FACT_VS_UNKNOWN_SEPARATION
    G3 NEXT_CAUSAL_STEP_RESOLVED
    G4 MANUAL_HANDOFF_COMPLETE_IF_REQUIRED
    G5 OPERATOR_DECISION_EXACT_IF_REQUIRED
    G6 NONE_ACTION_JUSTIFIED
    G7 NO_OPERATOR_RECONSTRUCTION
    G8 SINGLE_OPERATOR_ACTION
    G9 NO_HISTORICAL_PROMPT_REPLAY
    G10 CURRENT_EVIDENCE_BOUND

PASS возможен только при PASS всех применимых gates.

### 6.3 Смысл gates

G1:
человек понимает, что произошло, почему важно и где остановились.

G2:
UNKNOWN, blocker, candidate, receipt, acceptance и actual execution не смешаны.

G3:
определён next causal step либо доказано, почему он пока UNKNOWN/BLOCKED.

G4:
если нужен другой Entity-chat и нет approved automatic activation, выдан полный:
АДРЕСАТ + PROMPT + ДЕЙСТВИЕ ОПЕРАТОРА.

G5:
если следующий переход требует нового решения ОПЕРАТОРА, выдана одна точная decision string с понятным смыслом и границами.

G6:
если OPERATOR_ACTION = NONE / "ничего не делать", должно быть доказано одно из:
- causal chain завершена;
- следующий переход не существует;
- следующий переход уже автоматически активирован по отдельно доказанному authority и mechanism;
- ожидание внешнего события само является текущим разрешённым состоянием и не требует ручного действия.

Иначе FAIL.

G7:
ОПЕРАТОР не должен собирать поручение из GitHub, истории чата, нескольких locators или нескольких сообщений.

G8:
human-facing terminal result заканчивается одним понятным действием ОПЕРАТОРА.

G9:
никакой historical PROMPT не используется как current execution authority.

G10:
next step / handoff / decision опираются на fresh current evidence, current-writer и applicable authority.

## 7. Machine-checkable contradictions

Следующие сочетания считаются FAIL независимо от литературного качества ответа.

### C01

    terminal = initiation_verified_waiting_writer_gate
    AND operator_action = NONE

FAIL:
CAUSE_CHAIN_DROPPED_BEFORE_WRITER_GATE_HANDOFF

Исключение:
только если Writer Gate уже отдельно автоматически активирован по доказанному approved mechanism.

### C02

    writer_status = WRITER_ESTABLISHED
    AND conveyor_reconciliation_required = YES
    AND operator_action = NONE
    AND automatic_reconciliation_activation != PROVEN

FAIL:
MISSING_POST_WRITER_CONVEYOR_HANDOFF

### C03

    next_recipient != current_entity
    AND manual_activation_required = YES
    AND prompt_complete != YES

FAIL:
MISSING_MANUAL_ACTIVATION_HANDOFF

### C04

    task_class = BLOCKED
    AND next_step repeats blocked task unchanged

FAIL:
BLOCKED_TASK_REPLAY

### C05

    task_class IN {COMPLETED, SUPERSEDED}
    AND active_prompt points_to_same_historical_task

FAIL:
HISTORICAL_PROMPT_REPLAY_CONTRADICTION

### C06

    next_step_requires_operator_authority = YES
    AND exact_operator_decision = NONE

FAIL:
MISSING_OPERATOR_DECISION_GATE

### C07

    publication_or_dispatch = YES
    AND receipt_or_processing_started inferred_without_explicit_evidence

FAIL:
DELIVERY_STATE_INFERENCE_ERROR

### C08

    operator_action = NONE
    AND next_allowed_transition != NONE
    AND automatic_activation != PROVEN

FAIL:
UNJUSTIFIED_NO_ACTION

### C09

    human_result contains next step
    AND machine state next_allowed_transition differs

FAIL:
HUMAN_MACHINE_CAUSAL_MISMATCH

### C10

    capsule evidence is stale/superseded
    AND result treats capsule as current without fresh reconciliation

FAIL:
STALE_CAPSULE_PROMOTION

## 8. Minimal lifecycle integration

### 8.1 Before planned preservation

Current-writer:
1. updates/validates self-snapshot;
2. updates CURRENT_STATE_CAPSULE;
3. if KOO — updates CONVEYOR_HEAD;
4. ensures all refs are exact;
5. ARH preserves/readbacks package.

### 8.2 Emergency failover

If predecessor unavailable:
- last preserved Capsule/Head are recovery evidence only;
- new instance does not treat them as live task authority;
- initiation restores them as causal hints;
- after Writer Gate KOO fresh-reconciles before producing new Head/PROMPT.

### 8.3 After every terminal result

Profile Entity:
- establishes exact terminal state;
- determines next transition only if within authority;
- runs PRE_SEND_GATE;
- if another Entity must act, returns ready handoff;
- if it cannot determine next step, handoff goes to KOO per existing Conveyor Canon.

### 8.4 After KOO reconciliation

KOO:
- updates CONVEYOR_HEAD;
- chooses one already authorized next step OR requests one exact OPERATOR decision;
- materializes a fresh PROMPT only if task remains current;
- runs PRE_SEND_GATE before human terminal response.

## 9. Linter behavior candidate

A future linter may consume:
- terminal metadata;
- CURRENT_STATE_CAPSULE;
- CONVEYOR_HEAD;
- materialized PROMPT metadata;
- human-facing result metadata.

Minimal output:

    PASS

or

    FAIL
    code: <contradiction code>
    field: <offending field>
    expected: <expected causal state>
    observed: <observed value>
    evidence: <exact refs>

The linter:
- does not create authority;
- does not choose policy;
- does not change files automatically;
- does not infer UNKNOWN;
- blocks "terminal complete" classification when a contradiction is found.

## 10. Example: defect that triggered this candidate

Observed pattern:

    initiation = initiation_verified_waiting_writer_gate
    writer_gate = NOT_PERFORMED
    next_allowed_transition = separate Writer Gate
    automatic_activation = NOT_PROVEN
    human operator action = "ничего не делать"

PRE_SEND_GATE result:

    G3 PASS
    G4 FAIL
    G6 FAIL
    G8 FAIL

Machine contradiction:

    C01 FAIL
    C08 FAIL

Therefore such a response may be technically correct about recovery state but cannot be accepted as operationally complete.

## 11. Minimalism / anti-bureaucracy

This candidate explicitly forbids:
- new manifest only for Capsule;
- new route-note only for Capsule;
- duplicate full queue inside CONVEYOR_HEAD;
- full transcript ingestion;
- copying all Project Sources into every PROMPT;
- new approval layer for every terminal result;
- treating Capsule/Head as authority;
- maintaining parallel truth stores.

Preferred implementation:
- one small current capsule per recovery-managed Entity;
- one small current conveyor head for KOO;
- one deterministic pre-send validator/linter;
- exact references back to existing evidence.

## 12. Deployment boundary

This candidate is DOCUMENT_ONLY.

It does NOT:
- modify Project Sources;
- modify approved Recovery/Conveyor/Core canons;
- activate Capsule/Head requirements;
- authorize KOD implementation;
- authorize automation;
- authorize automatic chat activation;
- mutate foreign current-state.

Proposed causal sequence:

1. independent KAN review for documentary/canon compatibility and minimality;
2. independent SHT stress-review of causal invariants and failure modes;
3. if both PASS, exact OPERATOR decision on bounded pilot;
4. KOD implements linter + example fixtures under separate authority;
5. pilot on one Entity replacement cycle;
6. only after evidence, decide whether to amend approved sources.

## 13. Review questions

KAN review should determine:
1. whether this candidate duplicates or conflicts with active Project Sources;
2. whether Capsule/Head are operational artifacts rather than new authority stores;
3. whether PRE_SEND_GATE can be introduced as an implementation/check layer without canon activation;
4. whether any field creates hidden current-state ambiguity;
5. whether minimal document count is preserved.

SHT review should determine:
1. whether C01-C10 cover the observed causal failure class;
2. where false PASS / false FAIL remains possible;
3. whether blocked/completed/superseded transitions are safe;
4. whether emergency failover can incorrectly promote stale Capsule/Head;
5. whether linter can remain non-authoritative and fail-closed.

## Terminal

CANDIDATE_READY_FOR_INDEPENDENT_DOCUMENT_REVIEW

No Project Source/canon activation performed.
