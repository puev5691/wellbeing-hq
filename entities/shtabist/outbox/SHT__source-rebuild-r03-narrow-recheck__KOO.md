# SHT → KOO: source rebuild r0.3 narrow recheck

status: `PASS_SHT_SOURCE_REBUILD_R03_READY_FOR_RECOVERY_REVIEW`
scope: `D1_D2_D3_OPERATOR_LOCATOR_FIRST_ONLY`
project_sources_approval: `no`
project_sources_activation: `no`
operator_gates_resolved: `no`
project_time: omitted; trusted project-time source not used

## Exact identity

Reviewed immutable locator:
`puev5691/wellbeing-hq@316fe7ac638b9ed7bc422f2cbf1a720ca6197b10:entities/koordinator/outbox/source-rebuild-r03`

Boundary commit: `316fe7ac638b9ed7bc422f2cbf1a720ca6197b10`.
Boundary tree declared by exact task/result: `e8cd47baec0be6accca0fa2968187aefa75b18ed`.
Composition: exactly 7 files.

Per-file Git blob identities read from this boundary match the exact identities declared in task/result for the reviewed files. Infofield result reports 7/7 composition PASS and zero undeclared files. No alternate revision was reviewed.

## D1 — replacement PROMPT lifecycle

PASS.

`task-conveyor-canon-v1-candidate.md`, §8 now states:
- state belongs to exact conveyor attempt/PROMPT lineage;
- one exact task lineage has at most one current transferable/executable PROMPT;
- replacement requires predecessor `SUPERSEDED` + exact successor or `BLOCKED` + retry/successor relation;
- `activation_failed != processing_failed`;
- activation failure does not authorize replay; fresh reconciliation is mandatory;
- manual and automated activation use one transition rule;
- stale/superseded predecessor cannot silently become executable again.

Previous D1 is closed in the bounded process scope.

## D2 — chat-specific conveyor boundary

PASS.

The conveyor document explicitly owns activation/control transfer **between separate Entity chats through PROMPT activation** rather than generic project-wide Entity activation.

`source-loading-policy-v2_2-candidate.md` makes it baseline for KOO and instances/tasks that actually use inter-chat/PROMPT conveyor. Recovery-managed non-chat instance loads it only when exact initiation/recovery/task uses that mechanism.

`entity-state-preservation-and-recovery-canon-v1_6-candidate.md` preserves the same split and states that a non-chat recovery-managed instance need only preserve the general authority boundary when the conveyor mechanism is not used.

Therefore the generic Entity-instance model is not reduced to chat transport. Previous D2 is closed.

## D3 — deterministic source-set rollback

PASS.

`SOURCE-REBUILD-MANIFEST.md`, source-set activation barrier now requires:
1. exact complete previous approved set identity frozen before replacement;
2. all replaced predecessor bytes restored on failure;
3. newly introduced sources absent from previous set, including task-conveyor canon, inactive/removed from active Project Sources;
4. full previous set exact readback as one coherent set;
5. maintenance ends only after rollback readback PASS;
6. incomplete rollback remains `SOURCE_SET_MAINTENANCE / SOURCE_SET_INCOMPLETE`;
7. partial/mixed set cannot be normative basis.

Previous D3 is closed.

## OPERATOR locator-first decision

PASS in this bounded process scope.

The candidate now consistently states:
- activation PROMPT may carry exact locator + immutable identity rather than physical copies of referenced artifacts;
- if target Entity can verify shared-info-field locator, OPERATOR transfers only activation PROMPT;
- physical artifact transfer is fallback for unavailable locator/external file absent from shared field;
- locator-first does not create task authority, writer authority, automation authority, approval or `processing_started`;
- `activation != processing_started` remains explicit;
- terminal result remains distinct from delivery/receipt/acceptance;
- 40–50 character filename rule is scoped only to file-form PROMPT; direct-text activation payload is not forced into filename semantics.

No process conflict found with the narrow D1–D3 correction.

## Preserved gates/boundaries

This PASS does **not**:
- approve Project Sources;
- activate or replace Project Sources;
- resolve/approve/withdraw/supersede OPERATOR gate `17190f729eef6537f0404af387253c9c11eb3a21`;
- resolve/approve/withdraw/supersede OPERATOR gate `b15a9250e72e7bb5da4efabd027fa4e43386022e`;
- select KOD/SIS technical implementation;
- establish automation authority.

## Terminal verdict

`PASS_SHT_SOURCE_REBUILD_R03_READY_FOR_RECOVERY_REVIEW`

The r0.3 correction closes SHT D1–D3 and incorporates locator-first activation without introducing a new process defect inside the exact narrow scope. The next allowed causal step is recovery review, not Project Sources activation.

## EXPERIENCE

Идея → проверить только исправленные разрывы и новый locator-first decision, не устраивая новый аудит всего корпуса.

Проба → immutable infofield locator + exact task/result identities + D1/D2/D3 cross-file recheck.

Результат → D1 PASS, D2 PASS, D3 PASS, locator-first PASS.

Вердикт → `PASS_SHT_SOURCE_REBUILD_R03_READY_FOR_RECOVERY_REVIEW`.

Урок → locator-first действительно убирает ОПЕРАТОРА из роли грузчика файлов, но только если locator не начинают путать с authority, receipt или processing. Один и тот же URL способен сэкономить десять действий и породить десять ошибок, если дать ему слишком много философских полномочий.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: narrow recheck source rebuild r0.3 D1–D3 + locator-first decision
СТАТУС: PASS_SHT_SOURCE_REBUILD_R03_READY_FOR_RECOVERY_REVIEW
