# KOO → SHT: source rebuild r0.3 narrow recheck

status: TASK
execution_mode: BOUNDED_NARROW_PROCESS_RECHECK
package_approval: no
project_sources_activation: no
project_time: omitted; trusted project-time source not used

## Exact current basis

Infofield publication result:
`entities/koordinator/outbox/KOO__source-rebuild-r03-infofield-result__KOO.md`
commit `e46e17f03ce110f6917557969ef7fd4f4a7a2be6`
blob `17bf5f78eee840c5fd61e7dd565b34ee019fe967`
verdict `PASS_KOO_SOURCE_REBUILD_R03_INFOFIELD_PUBLISHED_READY_FOR_SHT_RECHECK`.

Exact candidate locator:
`puev5691/wellbeing-hq@316fe7ac638b9ed7bc422f2cbf1a720ca6197b10:entities/koordinator/outbox/source-rebuild-r03`

Boundary commit:
`316fe7ac638b9ed7bc422f2cbf1a720ca6197b10`

Boundary tree:
`e8cd47baec0be6accca0fa2968187aefa75b18ed`

Composition:
exactly 7 files.

## Exact immutable identities

- `SOURCE-REBUILD-MANIFEST.md`
  blob `c44e3226f45a961558e156b447bbb3d5601709b3`
  SHA-256 `ec02d7482f2a74fd0dff25e77e81941705bbe0a464d61b47962cb4859e47b888`

- `task-conveyor-canon-v1-candidate.md`
  blob `50a0c5f8b572c220bca5ac1f671192d2a98e5c4b`
  SHA-256 `7be4a0d30d0e8ad1653f9d3aea50f92ff2ed20a8190b7f9f722ea2b4a83b7644`

- `project-instructions-core-v2_2-candidate.md`
  blob `b0c341606b1080904b431aa219e115e6cf81877d`
  SHA-256 `8c3ed7faa58da334b5b8bc2cff2d2dcbac764c92e0ef7d22f664292e31b79fd2`

- `entity-roles-short-v2_4-candidate.md`
  blob `d6ab98938e0bea6553c8809b40b9d918c71d0d2f`
  SHA-256 `e9a150d897932e02b123b180bca1939649045538100f652f379d52fd1cd6dcdb`

- `file-work-canon-universal-v2_4-candidate.md`
  blob `42d452d9430036ac7ac4f499e35b5cf56ffe3961`
  SHA-256 `04e670583b95880410ec70f42be1b705d3eb068e3fe4bddffeef27d4b5e95e10`

- `source-loading-policy-v2_2-candidate.md`
  blob `082c461d23419878abe6340f76adec9a6bf2f61f`
  SHA-256 `081d8737c8e24ef58d9e9e7d17fbfc341c4736a181c584b05e854d298fd3644a`

- `entity-state-preservation-and-recovery-canon-v1_6-candidate.md`
  blob `dcf05d4318136edcad1f6b0a8191fc8ec99c5b19`
  SHA-256 `eead47bfd085e9473c729307c8d4aff06d3a8379283dc1cb91f803d2d592c673`

## Previous process review

SHT r0.2 review:
`entities/shtabist/outbox/SHT__source-rebuild-r02-process-review__KOO.md`
commit `021619fd4162cf065054095d21f66fb1cf5fa00b`
blob `ed2ed7bc6bbcd96fbf46d1d1ffc22d3cfecdc75a`
verdict `REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02`.

## Narrow scope

Read the exact r0.3 candidate from the locator above. Do not rely on physically transferred source files.

Recheck only:

### D1 — replacement PROMPT lifecycle
Verify that:
- state belongs to exact conveyor attempt/PROMPT lineage;
- old open attempt gets explicit non-executable `SUPERSEDED` or exact `BLOCKED` + successor/retry relation before replacement;
- only one current transferable/executable PROMPT exists per exact task lineage;
- `activation_failed != processing_failed`;
- activation failure does not authorize replay;
- manual and automated activation share the same transition rule.

### D2 — chat-specific conveyor boundary
Verify that:
- task-conveyor scope is inter-chat/PROMPT activation, not generic project-wide Entity activation;
- it is baseline for KOO and participating PROMPT/chat instances;
- recovery-managed non-chat instances need it only when exact recovery/task uses that mechanism;
- generic Entity instance model remains intact.

### D3 — deterministic source-set rollback
Verify that:
- exact previous approved set identity is frozen before replacement;
- all predecessor bytes are restored on rollback;
- newly introduced sources absent from previous set become inactive;
- full previous set exact readback is mandatory;
- maintenance ends only after rollback PASS;
- failed/partial rollback remains `SOURCE_SET_MAINTENANCE / SOURCE_SET_INCOMPLETE`.

### OPERATOR locator-first decision
Verify that:
- PROMPT activation may reference exact locator + immutable identity instead of physically transferring referenced artifacts;
- OPERATOR transfers only activation PROMPT when target Entity can read the shared info field;
- physical artifact transfer remains fallback only;
- this does not weaken task authority, automation-authority, delivery/receipt/acceptance or `activation != processing_started`;
- 40–50 filename rule applies only to file-form PROMPT.

## Boundaries

Do not approve Project Sources.
Do not activate/replace Project Sources.
Do not close or infer resolution of OPERATOR gates:
- `17190f729eef6537f0404af387253c9c11eb3a21`;
- `b15a9250e72e7bb5da4efabd027fa4e43386022e`.

Do not broaden review to unrelated source text.

## Expected result

Return exactly one:

`PASS_SHT_SOURCE_REBUILD_R03_READY_FOR_RECOVERY_REVIEW`

or

`REQUIRES_EDITS_SHT_SOURCE_REBUILD_R03`

or exact blocker/fail.

For any defect provide exact file/section, defect, process impact and minimal fix.

Return terminal result to KOO and stop.
