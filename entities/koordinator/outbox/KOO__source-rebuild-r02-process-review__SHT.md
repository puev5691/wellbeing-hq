# KOO → SHT: Project Sources conveyor v1 r0.2 process review

status: TASK
execution_mode: BOUNDED_PROCESS_STRESS_REVIEW
package_approval: no
project_sources_activation: no
project_time: omitted; trusted project-time source not used

## Exact basis

KAN normative review:
`entities/kancelar/outbox/KAN__project-sources-conveyor-v1-norm-review__KOO.md`
commit `3753f169063d3531a9455fe7d55ca0cdba9f7c3e`
blob `b30dd966e858deed35bbbcb447e7f5418a456c47`
verdict `REQUIRES_EDITS_KAN_SOURCE_REBUILD_V1`.

KOO prepared bounded corrected revision only for K1–K6.

## Exact corrected package identity

File:
`project-sources-conveyor-v1-r02-candidate.zip`

SHA-256:
`0db002f77f25a451d0ff5a318e758773d26feef0064d92c5c26587280cb3c4e3`

Size:
`54606 bytes`

Composition: exactly 7 files:

1. `SOURCE-REBUILD-MANIFEST.md`
   SHA-256 `a8705665e23e38ee34b6678f38eb847931a0d6cbaa38a48000113d7bd4702de1`
2. `task-conveyor-canon-v1-candidate.md`
   SHA-256 `0d5050cd1a1d7b84a163def1e44f2055b07da43f6fdc2bdb70981d5a34bae8fc`
3. `project-instructions-core-v2_2-candidate.md`
   SHA-256 `0146b60ca94e7e9ccdd2513608382b84e5ab6489a9033dfc56f2058bd6db7c5a`
4. `entity-roles-short-v2_4-candidate.md`
   SHA-256 `9ad43eeb135541fe8f9ce1f41d9a7bb478edb6ba7ad515ed3ce696d63c109b13`
5. `file-work-canon-universal-v2_4-candidate.md`
   SHA-256 `04e670583b95880410ec70f42be1b705d3eb068e3fe4bddffeef27d4b5e95e10`
6. `source-loading-policy-v2_2-candidate.md`
   SHA-256 `002a1d7ae3b6a3fb957c5b41162c1194b3cc63555b6bf9109ac200b73ae7450f`
7. `entity-state-preservation-and-recovery-canon-v1_6-candidate.md`
   SHA-256 `b42b6f65f2e4e432d6e99fcf4720b4fa12b98dec5ad83aa824d99959794febfa`

ZIP readback: all 7 internal file hashes match the identities above.

## K1–K6 correction boundary

K1:
recovery target moved to v1.6 and integrates reviewed v1.5 r0.4 Wake/Writer layer
`aea341e30d5d5297a491e7320674f2587d66d1e5`
blob `99b1ef3428330fa2e43d76a373b79cb8d3d663c5`.
Open predecessor OPERATOR gate
`17190f729eef6537f0404af387253c9c11eb3a21`
remains unresolved and is not silently approved/withdrawn/superseded.

K2:
source-loading target moved to v2.2 with explicit lineage from reviewed v2.1 candidate
`59ae5c036151460ca63a0e2ccd37d4aa53c88aaf`.
Open predecessor OPERATOR gate
`b15a9250e72e7bb5da4efabd027fa4e43386022e`
remains unresolved and must be explicitly resolved before source-set activation.

K3:
task conveyor + roles now state that conveyor materializes an already-authorized step; it does not create KOO standing instruction authority. OPERATOR PROMPT upload is activation/transport, not substantive approval without explicit decision. PROMPT template includes exact task authority.

K4:
task conveyor, project core, roles, source-loading and recovery use one automation boundary:
technical verification proves capability only;
automatic activation requires separate standing/explicit automation-authority for exact scope;
`activation != processing_started`.

K5:
task conveyor now states:
`terminal_result != delivered != received != accepted`.
`COMPLETED` is allowed only by declared terminal criterion and cannot close a parent workflow still waiting for delivery/receipt/acceptance.

K6:
manifest now contains a source-set activation barrier:
exact-set approval/readback;
`SOURCE_SET_INCOMPLETE`;
fail-closed `SOURCE_SET_MAINTENANCE`;
rollback to previous complete approved set if barrier fails;
cold-start/conveyor test only after barrier PASS.

## Review scope for SHT

Perform bounded process/stress review of this exact r0.2 package only.

Focus on:
1. lifecycle closure for READY_FOR_PROMPT / PROMPT_PREPARED / AWAITING_OPERATOR_TRANSFER / AWAITING_ENTITY_RESULT / BLOCKED / COMPLETED / SUPERSEDED;
2. stale/competing PROMPT and activation-failure recovery without duplicate execution;
3. consistent `activation != processing_started`;
4. source-set activation/rollback without mixed-authority state;
5. 40–50 character PROMPT filename rule operational stability;
6. whether every recovery-managed Entity needs task-conveyor canon in permanent baseline;
7. manual OPERATOR transfer vs future automation states without automatic replay/authority expansion;
8. COMPLETED vs parent workflow delivery/receipt/acceptance;
9. deterministic failure/rollback path of package replacement;
10. whether chat-specific scope is sufficiently bounded and does not collide with generic Entity instance model.

Also verify K1–K6 corrections did not introduce new process defects.

## Do not

Do not approve Project Sources.
Do not activate/replace Project Sources.
Do not resolve the two open OPERATOR lineage gates.
Do not broaden scope beyond the r0.2 source rebuild process.
Do not rewrite technical implementation details owned by KOD/SIS.

## Expected result

Return either:

`PASS_SHT_SOURCE_REBUILD_R02_READY_FOR_RECOVERY_REVIEW`

or
`REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02`

or exact blocker/fail.

For each required edit provide exact file/section, defect, minimal fix and process impact.

Return result to KOO and stop.
