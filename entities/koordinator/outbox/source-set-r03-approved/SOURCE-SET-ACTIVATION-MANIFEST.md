# Source-set activation manifest — r0.3 approved publication

status: APPROVED_SET_PREPARED_NOT_ACTIVATED

OPERATOR decision:
`APPROVE_SOURCE_REBUILD_R03_AND_SELECT_SUCCESSOR_LINEAGE`

Decision commit:
`c1e44243eb57ef0e667d0b9c4e93c1991cbf1899`

Reviewed candidate locator:
`puev5691/wellbeing-hq@316fe7ac638b9ed7bc422f2cbf1a720ca6197b10:entities/koordinator/outbox/source-rebuild-r03`

## Approved source set

- `entity-roles-short-v2_4-approved.md` — SHA-256 `d7feae524f6d1a34b0fd2a63475435e41ebe48097a191d87ca0ceeb797421530`
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md` — SHA-256 `82e3117570a9ecd73be2dae1279ebb3e0a2d6125556de98d5c1ede14a9236ae5`
- `file-work-canon-universal-v2_4-approved.md` — SHA-256 `c7e09bb358afd9ff131158044ce3722375ab30580e240909e85afdf38ca1e08b`
- `project-instructions-core-v2_2-approved.md` — SHA-256 `ae215f9c7bb44a1b9d525e1f78ea828cdeecd2d8487cb075dc49f4f94420c7af`
- `source-loading-policy-v2_2-approved.md` — SHA-256 `2a410e929c8cf4daa21f9229ad300e92abbaf4ab40b4fbf3a03950cc663e719e`
- `task-conveyor-canon-v1-approved.md` — SHA-256 `7c49fde826ffab59d19c4fc30ccfa6aa660454c2c09785ba9237647e4e4388a6`

## Resolved predecessor gates

- recovery v1.5 r0.4 gate → `SUPERSEDED_BY_OPERATOR_SELECTED_V1_6_R03`
  resolution commit `d07a843f57f962a02c5ee34ba8713ad08e4ef416`
- source-loading v2.1 gate → `SUPERSEDED_BY_OPERATOR_SELECTED_V2_2_R03`
  resolution commit `2fda0a3a6752f1170aee3b5968b5f493d39befc5`

## Previous complete approved set for rollback

- `project-instructions-core-v2_1-approved.md`
  SHA-256 `8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26`
- `entity-roles-short-v2_3-approved.md`
  SHA-256 `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`
- `file-work-canon-universal-v2_3-approved.md`
  SHA-256 `5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5`
- `source-loading-policy-v2-approved.md`
  SHA-256 `2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061`
- `entity-state-preservation-and-recovery-canon-v1_4-approved.md`
  SHA-256 `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda`

## Activation barrier

1. Before mutation verify the previous complete approved set is still the active baseline.
2. Enter `SOURCE_SET_MAINTENANCE`; do not start source-dependent normative work.
3. Remove/deactivate the five predecessor sources.
4. Add exactly the six approved files above.
5. Verify exact six-file identity/readback.
6. Verify all five predecessors are no longer active.
7. Only then declare `SOURCE_SET_ACTIVATED`.
8. Run cold-start/source-loading and conveyor smoke tests after barrier PASS.

## Rollback

If any activation/readback condition fails:
- restore all five predecessor approved sources with exact identities above;
- ensure `task-conveyor-canon-v1-approved.md` and every other new r0.3 source are inactive;
- read back the complete previous five-source set;
- remain `SOURCE_SET_MAINTENANCE / SOURCE_SET_INCOMPLETE` until full rollback PASS.

Approval does not equal activation.
