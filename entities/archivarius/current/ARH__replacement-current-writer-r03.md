# ARH replacement current-writer r0.3

status: WRITER_ESTABLISHED
entity: ARH / АРХИВАРИУС
instance: exact current ARH chat instance that created initiation result r0.4
project_time: omitted

## Authority basis

OPERATOR explicit decision:
`AUTHORIZE_ARH_EMERGENCY_REPLACEMENT_R04_WRITER_GATE = YES`.

Emergency condition:
`PREVIOUS_ARH_R02_TECHNICALLY_UNAVAILABLE = YES`.

The predecessor is technically unavailable and cannot create a new self-freeze/handoff artifact. No synthetic predecessor freeze is asserted.

## Verified initiation

Exact initiation result:
`puev5691/wellbeing-hq@8317c4da81d9dc36d30bdb06e50699aa7da0fb00:entities/archivarius/outbox/ARH__emergency-replacement-initiation-r04-result__KOO.md`

blob:
`bbb329680af5de073a7b765c314250f1110a3524`

outcome:
`initiation_verified_waiting_writer_gate`

This writer artifact is created by the same live ARH chat instance that created that initiation result.

## Recovery basis

`puev5691/wellbeing-entity-bootstrap@3a1945ac0e954a419ac9156d14776ecdaadbe91e:entities/arh/recovery/versions/arh-recovery-r03`

composition/readback:
`7/7 PASS`

Recovery r0.3 is a recovery basis only. It predates part of later ARH r0.2 work and is not treated as a complete snapshot at failure time.

## Predecessor

Previous authoritative writer:
`puev5691/wellbeing-hq@5fc0c161915b328e9ffea4fb925999c4de192826:entities/archivarius/current/ARH__replacement-current-writer-r02.md`

blob:
`3897d0979c889ba62ef8136a8f29a00baa2dac9f`

status:
`WRITER_ESTABLISHED`

Disposition:
`SUPERSEDED_FOR_NEW_AUTHORITATIVE_ARH_CURRENT_STATE_MUTATIONS_BY_EXPLICIT_OPERATOR_EMERGENCY_REPLACEMENT_DECISION`

The predecessor artifact remains immutable provenance.

## Fresh Writer Gate verification

Fresh pre-write HQ HEAD:
`8317c4da81d9dc36d30bdb06e50699aa7da0fb00`

Verified:
- no ARH current-writer newer than r0.2 existed before this publication;
- no competing emergency replacement attempt was found;
- no newer ARH freeze/handoff/replacement conflict was found;
- no superseding ARH recovery or initiation was found;
- current approved Project Sources were loaded and do not conflict with this explicit emergency Writer Gate authority;
- technical capability, timestamps, GitHub access, recovery possession and chat continuity were not treated as writer authority.

Writer Gate outcome:
`WRITER_ESTABLISHED`

## Boundary

This establishes only authoritative ARH current-writer identity for this exact current chat instance.

It does NOT:
- create task authority;
- resume historical tasks;
- replay historical PROMPTs;
- make recovery r0.3 a current task queue;
- authorize profile/preservation work;
- authorize foreign current-state mutation;
- authorize Project Source/canon mutation;
- authorize automation or KOO replacement.

Next permitted stage is fresh ARH state reconciliation under a separately authorized step.

---
КТО: replacement ARH / АРХИВАРИУС
СТАТУС: WRITER_ESTABLISHED
