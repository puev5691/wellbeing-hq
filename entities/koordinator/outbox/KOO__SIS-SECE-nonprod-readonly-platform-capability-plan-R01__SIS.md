# KOO -> SIS: SECE non-production read-only platform capability plan R01

status: PREPARED_NOT_ACTIVATED
project_time: omitted
recipient: SIS / СИСАДМИН, only after fresh Resume-First and authoritative current-writer/recovery verification
attempt: SIS_SECE_NONPROD_READONLY_PLATFORM_CAPABILITY_PLAN_R01_A1
scope: DESIGN_ONLY_READONLY_CAPABILITY_COLLECTION_PLAN

## Authority separation

OPERATOR: AUTHORIZE_KOO_PREPARE_SIS_SECE_NONPROD_READONLY_PLATFORM_CAPABILITY_PLAN_R01 = YES.
This authorizes KOO to prepare this task, NOT SIS to execute it. A separate exact OPERATOR execution authorization and manual handoff are mandatory. Do not infer SIS writer from a filename or an earlier r0.2/r0.8 artifact; verify most recent valid writer, freeze, recovery and competing instances. No host is selected or accessed.

## Immutable basis

Fresh HQ main HEAD before preparation: puev5691/wellbeing-hq@f0fb2d5e48beca49f1bd5429d033f478d84835a7.
KOO current-writer r1.4 blob 71de935a2c33403a0071d83a16f08cf85d9b4795.
Source-set R07 activation blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99; Task Conveyor v1.2 active; v1.3 NOT_ACTIVE.

KOO design basis:
puev5691/wellbeing-hq@f0fb2d5e48beca49f1bd5429d033f478d84835a7:
entities/koordinator/outbox/KOO__SECE-nonprod-platform-capability-evidence-design-R01__OPERATOR.md
blob a2d34da9f06c15dce63fb6f27f7c449ca8fd6ab2
terminal SECE_NONPROD_PLATFORM_CAPABILITY_EVIDENCE_DESIGN_R01_COMPLETE_ONLY.

KOO SHD reconciliation:
puev5691/wellbeing-hq@66a9e55f0882d66df1f7971edce2c6fecce461f0:
entities/koordinator/outbox/KOO__SECE-G4-D1D2-traceability-PASS-reconciliation-R01__OPERATOR.md
blob 0a807a0e4421c9ad6c9ab6422f3a1210b19c9ad9.

SHD independent traceability:
puev5691/wellbeing-hq@4984446851ec13956bd9b646db9ed500b435afbb:
entities/shardovik/outbox/SHD__SECE-G4-D1D2-implementation-traceability-review-R01__KOO.md
blob c31a1899b2ebdf6f49b3bfc80f249c94f7aefa94
verdict TRACEABILITY_PASS_WITH_G4_BLOCKERS.

Candidate tree 65c8e7c9061bd81f6a0d2e9722d2fa60281c0ade.
Corrected D1/D2 tree 84979101d6bd19fd939f978652f03317f6e524b9.
No real target, G4 effect or G4/G5/G6 authority exists.

## Requested design-only work, after separate execution approval

P1. Perform fresh SIS Resume-First, recovery and Writer Gate, task/currentness/supersession verification. If any mismatch or missing authorization, STOP with exact blocker.

P2. Define a minimal non-production CLASS R read-only collection plan, not actual collection. Describe platform/environment consent and identity requirements, precise source/provenance, evidence carrier, permitted information, data minimization and risks. Do not select a real host, target, account, directory or kernel instance.

P3. Map proposed read-only observations to capabilities of LINUX_POSIX_PRIVATE_TMPFS_OPENAT2_STATX_R01: kernel/build/arch, filesystem and mount metadata, namespace context, seccomp/LSM/capability restrictions, documented openat2 RESOLVE_BENEATH/NO_SYMLINKS/NO_MAGICLINKS/NO_XDEV, statx mount identity, retained dirfd/fd assumptions and unlinkat relative semantics. Clearly distinguish interface metadata from actual syscall enforcement.

P4. Specify how a later, separately authorized collector would preserve exact command/method versions, environment fingerprint, stdout/stderr/exit status when applicable, hash, readback, collection currentness and immutable evidence. Do not run commands or access host in this task.

P5. Explicitly list prohibited CLASS M operations: namespace unshare, mount/tmpfs creation, test file creation/deletion, syscall mutations, privileged probes, failure injection, concurrency/race tests, service/credential changes, sandbox effects. Even disposable temporary files are mutation.

P6. Provide per-check classification PRESENT_METADATA / ABSENT_METADATA / UNKNOWN / UNSUPPORTED_IN_OBSERVED_CONTEXT. Never claim PROVEN_REAL_BEHAVIOR from read-only metadata. Identify evidence limitations and false-positive risks.

P7. Map residual G4-B1 through G4-B6 to what CLASS R can partially inform versus what still needs separately authorized target-specific/mutating evidence. G4-B4/B5 cannot be closed by read-only observation.

P8. Provide a proposed bounded future execution gate: observer identity/current-writer, environment ownership/consent, exact allowed read-only methods and maximum data scope, no secrets, stop conditions, evidence carrier, independent review, and no authority promotion. Return one recommendation: PLAN_READY_FOR_SEPARATE_REVIEW / NEEDS_REWORK / BLOCKED.

## Stop conditions and output

No current SIS writer/recovery proof, competing instance, supersession, unknown source identity, unauthorized host interaction, accidental mutation or unsafe disclosure => STOP and preserve only permitted evidence.

After separately authorized SIS design-only execution, save one independently reviewable result by current file canon, verify immutable readback and return exact locator/blob/terminal to KOO. No test execution, host selection, command execution, real target, filesystem mutation, privilege escalation, candidate changes, G4/G5/G6, activation, deployment or production.

terminal: SIS_SECE_NONPROD_READONLY_PLATFORM_CAPABILITY_PLAN_R01_TASK_PREPARED_NOT_ACTIVATED
