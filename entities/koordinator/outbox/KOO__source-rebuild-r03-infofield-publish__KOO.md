# KOO → KOO: publish source rebuild r0.3 to project info field

status: TASK
execution_mode: BOUNDED_INFOFIELD_PUBLICATION
processing_started: no
project_sources_activation: no
project_time: omitted; trusted project-time source not used

## Exact basis

Integration result:
`entities/koordinator/outbox/KOO__source-rebuild-r03-integration-result__KOO.md`
commit `5488c79e626f9ab4085a14b864e4a5ed7e536eaf`
blob `a6269282611bd382e2977cd21174ee1f2d4204a8`.

Local exact package:
`project-sources-conveyor-v1-r03-candidate.zip`

SHA-256:
`2c0327f8fdeb5a1f47da2bf9cdb74892b19ebf1e2edfd0c899dd3af043003b4c`

Composition:
7 files, local readback 7/7 PASS.

## Goal

Make the exact r0.3 candidate bytes readable to project Entities from the shared project information field by verified locator, so future review requires only an activation PROMPT with exact locator/identity and no physical transfer of referenced source files.

Preferred GitHub location:

`entities/koordinator/outbox/source-rebuild-r03/`

Required published set:
- `SOURCE-REBUILD-MANIFEST.md`
- `task-conveyor-canon-v1-candidate.md`
- `project-instructions-core-v2_2-candidate.md`
- `entity-roles-short-v2_4-candidate.md`
- `file-work-canon-universal-v2_4-candidate.md`
- `source-loading-policy-v2_2-candidate.md`
- `entity-state-preservation-and-recovery-canon-v1_6-candidate.md`

## Required verification

1. publish exact candidate bytes only;
2. establish one immutable boundary commit/ref containing the complete 7-file set;
3. read back every file from that boundary;
4. verify SHA-256 against integration result;
5. verify exact composition 7/7 and no undeclared files;
6. publish compact package locator/result with boundary commit/tree and per-file blob identities;
7. do not activate Project Sources;
8. do not alter/resolve open OPERATOR gates.

Expected result:

`PASS_KOO_SOURCE_REBUILD_R03_INFOFIELD_PUBLISHED_READY_FOR_SHT_RECHECK`

or exact blocker/fail.

After PASS:
fresh-reconcile and route narrow SHT recheck using locator-only referenced inputs.
