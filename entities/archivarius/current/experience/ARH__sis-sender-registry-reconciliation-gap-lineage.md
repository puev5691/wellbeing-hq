# ARH experience/event-lineage — SIS sender-registry reconciliation gap

status: CURRENT_EVENT_LINEAGE
project_time: omitted; trusted project-time source not used
canon_promotion: no
authority_change: no

## Trigger / preflight boundary

Previous ARH completion boundary:
`c09a8f11db3ddb3c8e5f26345ad240ccaeb150d0`

Pre-profile-work HEAD:
`f6e0df3dd54d70cf03034efe3d548afd882901c5`

Fresh compare: 32 commits ahead, no new ARH-owned inbox/outbox/current mutation before this run.

Relevant new exact evidence:
- SIS result: `entities/sisadmin/outbox/SIS__telegram-phase1b-authorized-tooling-path-result__KOO.md`;
- source commit `488909ed0c42f709c3d23805c51967a2f82ac432`;
- source blob `44031aac4c5c96eb9268de2fd67235da37dd5824`;
- SIS sender-registry row remained `status=dispatched`, `receipt=null`;
- exact KOO receipt exists: `routes/receipts/SIS__telegram-phase1b-authorized-tooling-path-result__KOO.receipt.md`;
- receipt blob `87e676c60119803cd6703c5be2c5d4c5f517d6d6`;
- bounded result `WAITING_OPERATOR_EXACT_HUMAN_ACTION_RECEIVED`.

External dependency preserved by that receipt:
`sudo /home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once.sh`

No evidence in this lineage says that the OPERATOR has executed that command.

## ARH sanitation result

Artifact:
`entities/archivarius/outbox/ARH__sis-sender-registry-reconciliation-gap__SIS.md`

Artifact commit:
`023e22da0e0d7424bcf817b8b8714d3ea9b455eb`

Artifact blob:
`dec348a711811e6f851a0b3099222174ad3bad52`

Finding scope:
- newest current-delta SIS sender-registry row only;
- exact receipt-state reconciliation only;
- append-only correction requested from SIS writer-domain;
- no bulk reconciliation of older SIS rows;
- no production/live Telegram/public webhook authorization.

## Exchange Gate route

Dispatch:
`routes/dispatch/ARH__sis-sender-registry-reconciliation-gap__SIS.md`

Gate-v1 dispatch commit:
`cffdb4d2240b2ea36395b22b4f5765838d713917`

Gate-v1 dispatch blob:
`5a498b5040b9a9aa64793dc222ea57d5cc3011f3`

Recipient inbox pointer:
`entities/sisadmin/inbox/ARH__sis-sender-registry-reconciliation-gap__SIS.md`

Inbox pointer commit:
`e3f9757fbf25e10036fd50084c394457d134e796`

Inbox pointer blob:
`1f0cb8998029441477bcb1ae5f5c83114142070d`

ARH sender registry update:
`registry/by-sender/archivarius.jsonl`
commit `4875b54b3309423c0e781b8f659195bda6564b17`
blob `152643dfb0c9b4be70d8b97152a1336632e5673e`.

Current sender state for this route:
- `status: dispatched`;
- `receipt: null`;
- `acceptance: null`.

No receipt or acceptance for this ARH → SIS sanitation route is inferred.

## Activation boundary

Automatic activation evidence exists:
`routes/activation/ARH__sis-sender-registry-reconciliation-gap__SIS.activation.md`

It records:
- `detector_status: PASS`;
- source commit `e3f9757fbf25e10036fd50084c394457d134e796`;
- `activation_requested: yes`;
- `processing_started: no`;
- `activation_status: activation_failed`;
- failure reason `exact_entity_chat_resume_not_supported_by_current_adapter`;
- manual OPERATOR ping required by the adapter boundary.

This activation record is not delivery, processing, receipt or acceptance.

## Preservation rule

Until new exact evidence appears:
1. keep original SIS sender row as historical dispatched state;
2. require SIS-owned append-only reconciliation, not ARH mutation of SIS journal;
3. keep the Phase 1B human sudo action as external dependency;
4. keep ARH sanitation route in `dispatched` state;
5. do not infer processing from activation detector PASS.

## Experience card

Идея → newest sender-registry rows must reconcile with later exact receipts.
Проба → compare current-delta SIS registry identity against exact KOO receipt.
Результат → one stale `dispatched/receipt:null` state found for the authorized Phase 1B tooling-path result.
Успех/неудача → finding and Exchange Gate route created successfully; recipient processing is not proven because activation failed before processing start.
Фиксация → artifact + gate-v1 dispatch + SIS inbox pointer + ARH sender registry + this lineage.
Урок → receipt closure and human execution are separate events; neither should be promoted by adjacency.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную цепочку sanitation finding, Exchange Gate и failed activation без выдумывания SIS processing
СТАТУС: CURRENT_EVENT_LINEAGE
