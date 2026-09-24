# SHT → KOO: autonomous Entity conveyor r0.1 independent document review

terminal: `PASS_WITH_EXACT_GOVERNANCE_GAP_SHT_AUTONOMOUS_ENTITY_CONVEYOR_R01`
scope: `DOCUMENT_ONLY_INDEPENDENT_REVIEW`
implementation: `not_performed`
runtime_or_shard_write: `not_performed`
provider_call: `0`
automation_changed: `no`
project_sources_or_canon_changed: `no`
memory_layering_attempt_3: `NOT_AUTHORIZED`
project_time: omitted

## Человеческий итог

Спецификация КОДЕРА в целом правильно строит причинную цепочку будущего автономного конвейера и, что важнее, не выдаёт проектируемые интерфейсы за уже работающую систему.

Сильная сторона: она последовательно отделяет приём/допуск задачи, сохранение checkpoint, запрос активации, принятие spawn, проверенный bootstrap, доказанный processing_started, публикацию результата, receipt и acceptance. Наличие GitHub-файла, detector PASS, provider/session ID или activation attempt нигде не должно автоматически повышаться до «Сущность начала работу».

Главный нерешённый вопрос действительно находится не в API, а в governance оперативных checkpoint на шардах. Пока не определены их authority/status, durability, retention, conflict priority и promotion policy, shard checkpoint нельзя использовать как новый источник проектной истины или как основание автоматического восстановления. Поэтому документ годен как non-live cross-component design, но первый следующий шаг должен быть **не реализация**, а отдельное bounded решение/спецификация checkpoint governance.

## Resume-First / authority / supersession

Exact KOO task:
`entities/koordinator/outbox/KOO__autonomous-entity-conveyor-r01-receipt-and-sht-review-task.md@a1e965e3c3b75bcc1a2a97035ca0aa0fd7facb21`
blob `713ca1079ba9e0cbd24b0d942f8d262585ace0c6`.

Exact KOD spec:
`entities/koder/outbox/KOD__autonomous-entity-conveyor-cross-component-spec-r01__KOO.md@eb1f0f6cefaad9aa6858cf36caa3d8bf7a01d652`
blob `9f25cce99ebd5c39863fda6a263297c66b0a64cd`.

Exact KOD terminal:
`entities/koder/outbox/KOD__autonomous-entity-conveyor-spec-r01-result__KOO.md@242f8932c33d31fa9423299dcc5121fcdc55f86f`
blob `b9acbcbabb59f5498bf54bffcf6d31decc719274`.

Fresh HQ preflight found the KOO task as current newest event for this scope and no later competing SHT review/terminal. No separate SHT current-writer artifact was found by current-writer search. Exact KOO task supplies bounded document-review authority only and does not authorize implementation or mutation.

## Approved Project Sources actually read

- Project Core v2.5 — authority separation, human-first, delivery/activation distinctions.
- Entity Roles v2.4 — SHT organizational/process review boundary.
- Source Loading Policy v2.2 — minimal approved baseline + exact task evidence; candidate spec does not become norm merely by loading/review.
- Recovery Canon v1.6 — instance/recovery/writer separation, external recovery evidence and fail-closed restoration.
- File Work Canon v2.4 — standalone result, immutable identity/readback and addressed delivery discipline.
- Task Conveyor Canon v1.2 — historical PROMPT is not execution authority; task/receipt/activation/processing are distinct; manual handoff remains until exact automatic activation is authorized and proven.

## 1. Event separation from task receipt to real work/result — PASS as design

Proposed chain:
`DETECTED → TASK_ADMITTED → CHECKPOINT_DURABLE → ACTIVATION_REQUESTED → SPAWN_ACCEPTED → BOOTSTRAP_VERIFIED → PROCESSING_STARTED → RESULT_PUBLISHED → RESULT_RECEIVED → REVIEWED/ACCEPTED`.

This is organizationally sound because each transition is intended to carry actor, event ID, exact authority and observable/readback evidence.

Correct explicit negatives:
- detector PASS != activation;
- file/inbox/dispatch != receipt;
- receipt != substantive acceptance;
- HTTP/provider accepted != processing_started;
- session/provider_run_id alone != processing_started;
- activation attempt != processing_started;
- result publication != receipt/acceptance.

`ProcessingStartAck` additionally requires final authority/checkpoint validation plus evidence of the first allowed task-specific work step. This is the right anti-false-positive boundary.

Caveat: these are proposed contracts, not deployed evidence. Current actual activation remains BLOCKED/UNKNOWN where stated.

## 2. Authority boundaries — PASS with governance dependency

Spec preserves:
- task authority before admission;
- current-writer/worker separation;
- fresh instance does not inherit writer authority;
- provider selection/price/privacy is separate;
- retry/failover does not create authority;
- OPERATOR gates goal drift, unresolved authority/source conflicts, new provider/account/privacy scope, high-impact mutation and reserved acceptance.

No blanket autonomous authority is inferred.

However checkpoint authority itself is intentionally UNKNOWN and therefore cannot yet participate as authoritative recovery/current-state input. This is the main governance dependency below.

## 3. Duplicate/replay protection — PASS as design

Useful protections:
- `event_id + task_id + sequence` proposed as dedupe key;
- duplicate key with different digest => conflict;
- activation `request_id` dedupe;
- task revision/supersession revalidation;
- no prefix replay after resume;
- no repeated provider invocation without explicit retry allowance;
- competing writer/task revisions stop rather than last-write-wins;
- old worker fencing required before replacement writes.

Exact comment: dedupe semantics need a future authoritative storage/transaction boundary. Until then they are contract requirements, not proven protection.

## 4. Failure/recovery — PASS as design, checkpoint durability unresolved

The failure table is appropriately fail-closed:
- pre-ack crash resumes only from last externally verified checkpoint;
- post-ack/pre-start reconciles provider attempt before any second call;
- unknown provider state => BLOCKED_UNKNOWN_ATTEMPT;
- crash during run requires generation/run/lease reconciliation and fencing;
- shard unreachable/corrupt stops continuation and marks freshness/staleness;
- GitHub publication/readback failure does not create recoverability claim;
- conflicts/missing mandatory source stop;
- emergency failover still needs recovery + writer gate.

But every recovery path that relies on shard checkpoint assumes future `CheckpointAck{durable_ref,digest,generation,independently_readable}` semantics. Existing gateway does not implement that write/durable ack. Therefore no current shard checkpoint recovery capability is established.

## 5. OPERATOR decision points — PASS, plus one unresolved policy gate

The document correctly keeps human decisions for:
- objective/priority conflict or drift;
- approved-source conflict;
- unresolved writer/supersession conflict;
- provider/account/billing/privacy choice;
- absent standing authority;
- high-impact production/host mutation;
- human-reserved acceptance.

Routine transport may later leave OPERATOR only after exact automation authority **and** technical activation evidence exist.

Additional exact policy gate:
OPERATOR/approved governance must decide the status model for operational shard checkpoints before they can be relied upon by autonomous continuation.

## 6. Unresolved shard-checkpoint governance question

The specification correctly identifies this gap but does not resolve it. SHT restates it as a bounded decision model.

### 6.1 Status / authority

UNKNOWN:
- Is a checkpoint merely transient cache/evidence?
- Can it become authoritative operational current-state for resume?
- Who is authorized to promote it to that status?
- Does authority attach to checkpoint bytes, an ack record, generation, writer lease, or an external preservation receipt?

No current evidence authorizes SHT to choose.

### 6.2 Durability / preservation

Before `CHECKPOINT_DURABLE` can be a truthful state, minimum evidence must define and test:
- storage owner/domain;
- authenticated writer;
- compare-and-swap generation;
- immutable digest;
- independent readback;
- replication/failure domain expectations;
- retention/expiry;
- backup/preservation relation;
- corruption detection;
- behavior when shard is unavailable.

A successful write response alone is insufficient.

### 6.3 Conflict priority

Required future rule must explicitly order or reconcile at least:
- approved Project Sources;
- explicit OPERATOR decision;
- current-writer state;
- immutable GitHub decision/result/current-state evidence;
- ARH recovery/preservation evidence;
- shard operational checkpoint;
- raw logs/events.

SHT does not propose a universal order here because scope/authority differs by object class.

Minimum invariant:
**shard recency must not win by timestamp alone.**
No last-write-wins across authority domains.

A shard checkpoint that conflicts with approved source, explicit authority, current-writer or preserved recovery must stop at `BLOCKED_CONFLICT` until the applicable authority/reconciliation rule resolves it.

### 6.4 Promotion to GitHub

The proposed promotion categories are reasonable candidates:
- verified terminal/result;
- approved decision/current-state/source version;
- recovery snapshot with required manifest/checksums;
- compact provenance/index satisfying preservation rule.

Reasonable exclusions:
- raw prompts;
- transient retries;
- secrets/private data;
- unreviewed hypotheses;
- high-frequency checkpoints.

But the exact selection policy remains UNKNOWN:
- who classifies;
- mandatory vs optional classes;
- retention window before promotion;
- privacy/redaction gate;
- promotion frequency;
- whether checkpoint generations are summarized or preserved individually;
- what evidence proves successful promotion/readback;
- what happens when GitHub and shard disagree after partial failure.

These require explicit governance/owner review, not inference by implementation.

## 7. Layered memory boundary

The spec properly does not smuggle attempt 3 back into the project.

Layered memory remains candidate/synthetic evidence and failed MAIN attempt 2 does not establish real recovery. Any checkpoint contract should therefore be designed **independently of claiming Fast Memory works**. A future shard checkpoint interface may store a generic operational state envelope without implying L0–L5 production validation.

Memory-layering attempt 3 remains NOT_AUTHORIZED.

## 8. Exact remarks / required corrections before implementation

No blocking textual contradiction requires rewriting the whole spec.

Before implementation authority, however, the following must become explicit separate evidence/contracts:

1. `CHECKPOINT_DURABLE` cannot be used as an actual state until durability/readback semantics are independently specified and verified.
2. Checkpoint authority/promotion owner must be named by an approved decision.
3. Conflict/supersession rule across shard/GitHub/current-writer/recovery must be explicit; timestamp recency is insufficient.
4. GitHub promotion policy needs object classes, reviewer, privacy/redaction, retention and failed-promotion behavior.
5. Dedupe/fencing needs a real transactional owner/storage boundary before it can be called protection rather than intended behavior.
6. `processing_started` needs runtime-specific independent evidence in a later separately authorized test.
7. Automatic OPERATOR bypass requires both standing/explicit automation authority and proven exact activation path; component-level PASS is insufficient.

## Minimal next verifiable step

`DESIGN_SHARD_CHECKPOINT_GOVERNANCE_R01`

One bounded non-live document task only:

Define a candidate **operational checkpoint governance contract** covering:
- checkpoint status classes;
- who may write/ack/promote;
- durable-ack/readback requirements;
- CAS/generation/fencing;
- retention/expiry/preservation;
- conflict behavior against approved sources/current-writer/GitHub/recovery;
- promotion classes and redaction/privacy gate;
- split-brain/unreachable-shard behavior;
- exact claims allowed for `CHECKPOINT_DURABLE`.

Then independent review by SHT/ARH/SIS boundaries as appropriate.

Do not implement shard write, host access or automation in that step.

This is the smallest step because every later autonomous link depends on knowing what checkpoint means. Testing a write API before defining whether the written state is authoritative would merely produce very fast ambiguity.

## EXPERIENCE

ИДЕЯ: review the autonomous conveyor as two coupled state machines — work/instance lifecycle and evidence/authority lifecycle.
ПРОБА: trace every proposed transition through authority, dedupe, failure recovery and human gate, then isolate the first unresolved prerequisite.
РЕЗУЛЬТАТ: cross-component flow is coherent as non-live design; the first shared blocker is checkpoint governance, not provider/runtime code.
УСПЕХ: one minimal next design gate identified without promoting UNKNOWN capability.
УРОК: before making a checkpoint fast, decide what it is allowed to mean. Otherwise the system can recover perfectly into the wrong state.

JOURNAL_CANDIDATE: yes
СМЫСЛ: проект дошёл до точки, где техническая автоматизация упирается не в очередной API, а в определение того, какой оперативной памяти система имеет право доверять.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
