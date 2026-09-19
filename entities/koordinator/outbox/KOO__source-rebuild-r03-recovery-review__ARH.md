# KOO → ARH: source rebuild r0.3 recovery review

status: TASK
execution_mode: BOUNDED_RECOVERY_SOURCE_LIFECYCLE_REVIEW
project_sources_approval: no
project_sources_activation: no
operator_gates_resolution: no
historical_task_replay: none
project_time: omitted; trusted project-time source not used

## Owner

owner: ARH / АРХИВАРИУС

owner_basis:
- ARH owns preservation/recovery process, provenance, source lifecycle and recoverability review;
- SHT has already closed D1–D3 process defects;
- this task does not ask ARH to approve Project Sources or rewrite profile-owned source content.

Current ARH writer lineage:
`entities/archivarius/current/ARH__replacement-current-writer-r01.md`
establishment commit `a00b1644e840bed722e3712e78c8842959599797`
current blob `3d17b16c02e84e841d1266e3b0fcc083640b77d6`.

ARH must fresh-verify its writer/current-state before processing.

## Exact causal basis

SHT narrow recheck result:
`entities/shtabist/outbox/SHT__source-rebuild-r03-narrow-recheck__KOO.md`
commit `8949ec92965d8b8ed3835007de04a104ee402262`
blob `cd64946979a22cd30f9523246cb2811ef1f64b82`
verdict `PASS_SHT_SOURCE_REBUILD_R03_READY_FOR_RECOVERY_REVIEW`.

KOO inbox pointer:
`entities/koordinator/inbox/SHT__source-rebuild-r03-narrow-recheck__KOO.md`
status `addressed_for_processing`.
Inbox placement is not receipt, acceptance or processing evidence.

## Exact immutable candidate locator

Read the candidate directly from the shared project information field:

`puev5691/wellbeing-hq@316fe7ac638b9ed7bc422f2cbf1a720ca6197b10:entities/koordinator/outbox/source-rebuild-r03`

Boundary commit:
`316fe7ac638b9ed7bc422f2cbf1a720ca6197b10`

Boundary tree:
`e8cd47baec0be6accca0fa2968187aefa75b18ed`

Composition:
exactly 7 files.

Infofield publication result:
`entities/koordinator/outbox/KOO__source-rebuild-r03-infofield-result__KOO.md`
commit `e46e17f03ce110f6917557969ef7fd4f4a7a2be6`
blob `17bf5f78eee840c5fd61e7dd565b34ee019fe967`
verdict `PASS_KOO_SOURCE_REBUILD_R03_INFOFIELD_PUBLISHED_READY_FOR_SHT_RECHECK`.

## Exact per-file identities

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

## Review scope

Perform one bounded recovery/source-lifecycle review of this exact immutable r0.3 candidate.

### R1 — recovery lineage integrity

Verify that recovery v1.6:
- preserves reviewed v1.5 r0.4 Wake/Resume/Initiation/Writer Gate/Exact Task authority layer;
- does not silently approve, withdraw or supersede the open v1.5 OPERATOR gate;
- keeps instance continuity, writer continuity and exact task authority distinct;
- preserves no synthetic recovery reconstruction;
- preserves no historical task/PROMPT replay.

Open predecessor gate:
`17190f729eef6537f0404af387253c9c11eb3a21`.

### R2 — source-loading lineage integrity

Verify that source-loading-policy v2.2:
- has explicit lineage from reviewed v2.1 candidate;
- does not silently resolve its open OPERATOR gate;
- does not create mixed active/candidate source status.

Open predecessor gate:
`b15a9250e72e7bb5da4efabd027fa4e43386022e`.

### R3 — locator-first recoverability

Verify that locator-first activation:
- allows Entity to retrieve referenced artifacts from shared infofield by exact immutable locator;
- does not weaken provenance/version/readback requirements;
- does not convert locator presence into receipt/acceptance/task authority/processing evidence;
- remains recoverable if chat-local copies are absent;
- leaves physical transfer as fallback only when locator is unavailable or input exists outside shared infofield.

### R4 — source-set lifecycle / rollback

Verify that source-set activation barrier and deterministic rollback:
- preserve exact prior approved set identity;
- prevent mixed-authority source sets;
- deactivate newly introduced source(s) on rollback;
- require exact readback of the restored previous set before leaving maintenance;
- remain fail-closed when rollback is incomplete.

### R5 — preservation/source lifecycle

Verify:
- exact candidate provenance is recoverable from immutable infofield locator;
- superseded/candidate/approved states remain distinguishable;
- old candidate revisions can remain provenance without becoming authority;
- activation requires explicit OPERATOR decision + completed source-set activation barrier;
- no candidate file is treated as active merely because it is published in HQ.

### R6 — information-field stewardship

Verify that the new locator-first model remains compatible with ARH stewardship:
- duplicate/conflicting candidate versions remain detectable;
- immutable locator + status/provenance are sufficient to classify the object;
- no need exists to physically duplicate candidate files into reviewer chats;
- publication/readback and semantic acceptance remain separate.

## Explicit boundaries

Do NOT:
- approve Project Sources;
- activate or replace Project Sources;
- close, approve, withdraw or supersede either open OPERATOR gate;
- mutate recovery/current pointers;
- promote v1.6/v2.2/task-conveyor candidates to active;
- rewrite the package unless an exact recovery/source-lifecycle defect requires KOO correction;
- infer receipt/acceptance/processing from inbox placement or locator readability.

## Expected terminal result

Return exactly one:

`PASS_ARH_SOURCE_REBUILD_R03_RECOVERY_COMPATIBLE`

or

`REQUIRES_EDITS_ARH_SOURCE_REBUILD_R03`

or exact blocker/fail.

For each defect provide:
- exact file/section;
- recovery/source-lifecycle impact;
- minimal correction;
- whether SHT/KAN re-review is required after the change.

Address terminal result to KOO.
Stop after terminal result.
