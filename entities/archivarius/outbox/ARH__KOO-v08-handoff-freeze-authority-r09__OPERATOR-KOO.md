# OPERATOR → KOO: handoff/freeze authority for r0.9 replacement

status: CURRENT_WRITER_HANDOFF_FREEZE_AUTHORIZED
entity: KOO / КООРДИНАТОР
project_time: omitted

## Human meaning

ОПЕРАТОР явно принял решение:

AUTHORIZE_KOO_V08_HANDOFF_FREEZE_FOR_R09_REPLACEMENT

Текущий authoritative KOO writer v0.8 с этого решения заморожен для новых authoritative profile/current-state mutations.

Исторические bytes и provenance writer v0.8 сохраняются и не переписываются.

Это решение разрешает только следующий replacement cold-start по independently preserved recovery r0.9.
Оно не устанавливает нового writer и не разрешает профильную работу.

## Predecessor writer

artifact:
entities/koordinator/current/KOO__replacement-current-writer-v08.md

establishment commit:
9781aeff09d868ade3f3e1a28f28014d23512386

blob:
ca7ed0ed4e539dcdbe783e122cea409a77ab10cd

disposition:
FROZEN_FOR_NEW_AUTHORITATIVE_PROFILE_CURRENT_STATE_MUTATIONS_PENDING_R09_REPLACEMENT

## Preservation basis

ARH result:
entities/archivarius/outbox/ARH__KOO-self-preservation-r09-result__KOO-OPERATOR.md

commit:
4e3bafce6e5bf70a426d474ddf5037531bc47552

blob:
018e29fc096254d7c1211afdeab32449f59c25a6

terminal:
PASS_ARH_KOO_SELF_PRESERVATION_R09_EXTERNALLY_PRESERVED

Exact immutable recovery:
puev5691/wellbeing-entity-bootstrap@ab4c7ad12db9760fe825d2a93b6467499e1a09f4:entities/koo/recovery/versions/koo-recovery-r09

composition:
5/5 PASS

external readback:
5/5 PASS

## Authority boundary

Authorized:
- new physical KOO may perform replacement cold-start initiation against exact recovery r0.9;
- fresh HQ/source/recovery reconciliation is mandatory;
- historical task/PROMPT replay is forbidden.

Not authorized by this decision:
- Writer Gate;
- profile/routing work;
- memory-layering attempt 3;
- provider/Telegram/host/credential mutation;
- automation mutation;
- Project Sources/canon mutation.

Required replacement initiation terminal:
- initiation_verified_waiting_writer_gate
or
- exact BLOCKED_* / FAIL_*.

Replacement instance must STOP before Writer Gate and profile work.

---
КТО: OPERATOR / authority recorded by ARH
СТАТУС: CURRENT_WRITER_HANDOFF_FREEZE_AUTHORIZED
