# KOO → OPERATOR: KOD emergency failover v0.3

status: `EMERGENCY_FAILOVER_AUTHORIZED`
entity: `KOD / КОДЕР`
production: `no`
project_time: omitted; trusted project-time source not used

## Решение ОПЕРАТОРА

ОПЕРАТОР явно инициировал аварийную замену текущего KOD instance после длительной невозможности завершить текущую задачу.

Operational decision:
- существующий current-writer `entities/koder/current/KOD__replacement-current-writer-v02.md` прекращает новые authoritative KOD mutations;
- его immutable history не переписывается;
- новый KOD instance должен быть восстановлен только через действующий recovery-контур;
- новый instance не получает writer authority автоматически от факта открытия чата;
- после `initiation_verified` новый instance обязан выполнить fresh competing-writer check и может установить replacement current-writer v0.3 на основании этого explicit OPERATOR failover decision, если нового competing KOD writer evidence нет.

## Последний подтверждённый recovery baseline

Canonical recovery:
`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`

Exact initiation file:
`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current/KOD__initiation-current__KOD.md`

Independent ARH verification:
`entities/archivarius/outbox/ARH__KOD-emergency-recovery-verification__KOD.md`
commit `78a8f278e3a332bce05e28352e1316ea18f0a13c`
verdict `PASS_PUBLISHED_CANONICAL_RECOVERY`.

## Writer boundary being failed over

Current writer artifact before this decision:
`entities/koder/current/KOD__replacement-current-writer-v02.md`
commit `56db550005d6ed6956ba1bf753f3cb24ca295cc3`
blob `23f20f04504c65497c154c099d8090cde11fba83`
status before emergency decision: `CURRENT_WRITER_ESTABLISHED`.

Operational state after this decision for new KOD mutations:
`RETIRED_BY_EXPLICIT_OPERATOR_EMERGENCY_FAILOVER_DECISION`.

## Unfinished current task

Exact task:
`entities/koordinator/outbox/KOO__openai-model-policy-extension-impl-r01__KOD.md`
commit `b98458343c6502c5fa6a3dec9dc9ca296c1cff2b`.

No terminal result / Exchange-Gate completion has been verified for this task.

Partial implementation evidence exists in HQ and MUST NOT be treated as accepted/current state merely because files exist:
- `7957b4d0211ed6cef96f54f2693c19b88e9f9d2e` — three-model D0 policy r01;
- `9824993082fccacfd09ac47ad465eb342803878e` — three-model D0 adapter r01;
- `715eeb2357e23605d0570a15a900c5ceeced705c` — live D0 transport model validation r01;
- `495053e79b37baec3b6239180becf214018f9b80` — three-model runtime integration r01;
- `f501869c31b8a5d383bd36095356c46726f170c6` — three-model extension tests r01.

Classification of this tail:
`UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`.

The replacement KOD must inspect/reconcile these exact immutable commits before deciding whether to continue, repair, discard or supersede them. It must not infer PASS from their presence.

## Initiation rule

The replacement instance must:
1. load the current five approved Project Sources;
2. verify the canonical recovery locator, composition and checksums by external readback;
3. report one of `initiation_verified | initiation_loaded_external_unverified | initiation_failed`;
4. fresh-scan `puev5691/wellbeing-hq`;
5. reconcile all KOD evidence since recovery publication, including current-writer v0.2, authority-resolution work, accepted OpenAI benchmark B and the unfinished three-model task tail above;
6. check for any KOD current-writer evidence newer than this emergency decision;
7. only after `initiation_verified` and clean competing-writer check, establish replacement current-writer v0.3 using this explicit OPERATOR decision as failover authority;
8. stop and report writer establishment before resuming profile work;
9. then resume the exact unfinished OpenAI task by evidence review, not by blindly rerunning or accepting partial files.

## Boundaries

This decision does NOT authorize:
- live OpenAI calls;
- API-key handling or billing mutation;
- production deployment;
- project/private data external send;
- TERA2/WBN execution;
- acceptance of the partial three-model implementation without verification.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: выполнить аварийный failover KOD после недоступности/неработоспособности текущего writer instance без реконструкции self-state
СТАТУС: `EMERGENCY_FAILOVER_AUTHORIZED / OLD_WRITER_RETIRED_FOR_NEW_MUTATIONS / REPLACEMENT_INITIATION_REQUIRED`
