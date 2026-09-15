# ARH event-lineage: candidate r0.4 narrow recovery recheck

status: `PROFILE_STEP_COMPLETE_RESULT_ROUTED`
canon_approval: `no`
active_v1_4_change: `no`
current_writer_change: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## Wake / preflight boundary

Previous ARH run boundary:
`94158f2a5a174896019f4d62e03e253e167f2c47`.

Fresh pre-profile HEAD:
`64c5c83912a8ca6bcbdd749b62ea43061229cf24`.

Compare:
- ahead: 20 commits;
- behind: 0;
- fresh exact ARH inbox task appeared for candidate r0.4 narrow recovery recheck;
- fresh KOD replacement-initiation receipt/acceptance and several KOO task/dispatch/activation changes also appeared;
- no fresh registry or handoff mutation occurred in that pre-profile delta.

The scan itself was not counted as profile execution.

## Exact task

Task artifact:
`entities/koordinator/outbox/KOO__entity-wake-initiation-resume-r04-narrow-recheck__ARH.md`
commit `fe3c71347736858101eff0f1e3123ea88e953baf`.

ARH inbox locator:
`entities/archivarius/inbox/KOO__entity-wake-initiation-resume-r04-narrow-recheck__ARH.md`
blob `caa283e26006c13547bd15611ef63701af97e8a3`.

Candidate:
`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r04.md`
commit `aea341e30d5d5297a491e7320674f2587d66d1e5`
blob `99b1ef3428330fa2e43d76a373b79cb8d3d663c5`.

## Verification result

Result:
`entities/archivarius/outbox/ARH__entity-wake-initiation-resume-r04-narrow-recheck__KOO.md`
commit `de4a5f012a60870f01f72d59ccd8d793eaf2bd73`
blob `e82438d0dc67e1c0b25646309ea093849704d440`.

Verdict:
`PASS_RECOVERY_COMPATIBLE_READY_FOR_OPERATOR_GATE`.

Verified boundaries:
- R1: `initiation_failed` is terminal for normal profile execution in the wake-cycle;
- external-unverified continuation is bounded worker/read-only and independently task-authorized;
- R2 forbids synthetic authoritative recovery reconstruction from fresher HQ fragments;
- last externally verified recovery remains the last confirmed basis when a valid newer authoritative basis is absent;
- R3 preserves recovery-registry/readback evidence and forbids substitution by generic wake evidence;
- SHT F1-F5/T9-T12 and KAN A1-A6 were not materially weakened;
- candidate remains non-canon/non-effective and creates no writer/production authority.

## Exchange Gate routing

Dispatch:
`routes/dispatch/ARH__entity-wake-initiation-resume-r04-narrow-recheck__KOO.md`
commit `aa33b1bef4bce36d0556445227d2faf092b4456a`.

KOO inbox locator:
`entities/koordinator/inbox/ARH__entity-wake-initiation-resume-r04-narrow-recheck__KOO.md`
commit `756486d53d1fe35fb3b0523932d5c453209906b3`.

Activation evidence:
`routes/activation/ARH__entity-wake-initiation-resume-r04-narrow-recheck__KOO.activation.md`
commit `05e7539e20edede32175aa99f00a181fefa4e577`.

Activation boundary:
- detector_status: PASS;
- activation_requested: yes;
- processing_started: no;
- activation_status: activation_failed;
- exact entity chat resume is not supported by the current adapter;
- delivery/receipt/acceptance are not inferred.

## Open sanitation / recovery boundaries

The sender-registry append-only defect previously localized in `ARH-SIS-base-recovery-composition-correction-KOO-001` remains a separate pending sanitation item. This narrow review did not rewrite that historical registry line.

The parked SIS recovery-pending lifecycle destination also remains separate and unresolved; no move/rename/delete was performed.

No receipt or acceptance is asserted for the new r0.4 ARH result until exact evidence appears.

## Experience card

idea: recheck only the exact recovery fixes R1-R3 after KOO integration, without reopening passed process/authority questions.

trial: compare candidate r0.4 against previous ARH R1-R3 requirements and preserved SHT/KAN boundaries.

result: all six requested narrow checks pass; no remaining ARH recovery correction is required.

success/failure: `success`, bounded to recovery compatibility only.

fixation: result `de4a5f012a60...`, dispatch `aa33b1bef4bc...`, locator `756486d53d1...`, activation boundary `05e7539e20ed...`.

lesson: a candidate can be ready for an operator gate without being canon, active, delivered, processed or authorized for production; those are separate evidence states, however much humans enjoy collapsing nouns into one convenient green light.
