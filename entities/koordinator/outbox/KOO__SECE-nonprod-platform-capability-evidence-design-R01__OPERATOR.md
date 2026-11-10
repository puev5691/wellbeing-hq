# KOO -> OPERATOR: SECE non-production platform capability evidence design R01

status: DESIGN_ONLY_COMPLETE
project_time: omitted
authority: AUTHORIZE_KOO_PREPARE_SECE_NONPROD_PLATFORM_CAPABILITY_EVIDENCE_DESIGN_R01 = YES
scope: DESIGN_OF_READ_ONLY_CAPABILITY_EVIDENCE_GATE_ONLY

## Human meaning

SHD independently confirmed that the R02 implementation statically traces corrected D1/D2 without a newly proven mandatory code defect. G4 still cannot proceed: real platform primitive semantics, exact target ownership/isolation, object continuity, cleanup and separate G4 authority are unproven. This document defines what a narrow non-production capability evidence step could establish without implying that a machine, namespace or target has been selected or that any command may run.

## Exact basis and currentness

Fresh main HEAD before design: puev5691/wellbeing-hq@66a9e55f0882d66df1f7971edce2c6fecce461f0.
KOO writer r1.4 blob 71de935a2c33403a0071d83a16f08cf85d9b4795.
Active source-set R07 activation blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99.
Task Conveyor v1.2 active; v1.3 NOT_ACTIVE.

KOO traceability reconciliation:
puev5691/wellbeing-hq@66a9e55f0882d66df1f7971edce2c6fecce461f0:
entities/koordinator/outbox/KOO__SECE-G4-D1D2-traceability-PASS-reconciliation-R01__OPERATOR.md
blob 0a807a0e4421c9ad6c9ab6422f3a1210b19c9ad9.

SHD independent traceability:
puev5691/wellbeing-hq@4984446851ec13956bd9b646db9ed500b435afbb:
entities/shardovik/outbox/SHD__SECE-G4-D1D2-implementation-traceability-review-R01__KOO.md
blob c31a1899b2ebdf6f49b3bfc80f249c94f7aefa94
verdict TRACEABILITY_PASS_WITH_G4_BLOCKERS.

Candidate tree 65c8e7c9061bd81f6a0d2e9722d2fa60281c0ade.
Corrected D1/D2 design tree 84979101d6bd19fd939f978652f03317f6e524b9.

## Evidence objective and separation

Only intended future observation: identify exact kernel, filesystem, mount/namespace, platform interface availability and evidence provenance that could support a later G4 proposal for the LINUX_POSIX_PRIVATE_TMPFS_OPENAT2_STATX_R01 profile.

Two distinct classes:

CLASS R — READ-ONLY OBSERVATIONS (future separately authorized step):
- documented kernel/version/architecture and feature interfaces, including provenance and scope;
- read-only filesystem/mount/namespace descriptions, without selecting an SECE effect target;
- existing API capability metadata, permission/feature visibility and environmental restrictions;
- provenance of evidence carrier, observation method, readback and hashes;
- negative or unknown results treated as UNKNOWN/BLOCKED, never interpreted as feature support.

CLASS M — MUTATING OR TARGET-SPECIFIC PROOFS (NOT within CLASS R):
- unshare/create mount namespace, mount tmpfs, create or unlink objects, attempt race/failure injection, alter process privileges or sandbox policy;
- actual openat2 creation, unlinkat deletion, retained-fd continuity, target isolation, foreign-writer exclusion and rollback;
- even a temporary probe file or a disposable target constitutes mutation and needs separate scope/authority.

A read-only observation can show presence of an interface or declared kernel capability; it cannot by itself prove enforcement of all flags under actual target-specific race conditions.

## Minimum evidence fields for a future CLASS R package

- authorized observer role/instance/current-writer/recovery and exact task attempt;
- explicitly authorized environment reference and consent/ownership for observation, without implying SECE target selection;
- immutable environment fingerprint and collection boundaries (kernel release/build/arch, mount/filesystem metadata if accessible, namespace identifiers, relevant security controls);
- exact observation methods and versions, inputs, stdout/stderr/exit status if commands later approved, immutable hashes and readback;
- privilege level and restrictions (seccomp, containers, LSM, capabilities) as observable, distinguishing unknown from absent;
- interface evidence for openat2 RESOLVE_BENEATH/NO_SYMLINKS/NO_MAGICLINKS/NO_XDEV, statx mount identity, retained fd/dirfd assumptions, unlinkat relative behavior; static interface metadata is NOT proof of runtime enforcement;
- source provenance, currentness and explicit uncertainty per finding;
- no credentials, secrets, personal data, or uncontrolled host inventory in evidence;
- separate security review of the proposed observation plan before execution where required.

## Gate checks / fail-closed rules

R0: fresh task/currentness/authority/Writer Gate and supersession.
R1: exact observer/environment scope, owner consent, read-only methods and bounded data classification.
R2: provenance and immutable versions for evidence method/tool/platform fingerprint.
R3: no filesystem writes, namespace creation, mount, syscall mutation, privilege escalation or effect.
R4: readback/hash and provenance sufficient for independent documentary review.
R5: distinguish PRESENT_METADATA, ABSENT_METADATA, UNKNOWN, UNSUPPORTED_IN_OBSERVED_CONTEXT and PROVEN_REAL_BEHAVIOR; CLASS R must never claim PROVEN_REAL_BEHAVIOR.
R6: report remaining G4-B1 through G4-B6 blockers separately and no authority promotion.
R7: on ambiguous environment, insufficient access, untrusted metadata, accidental mutation or evidence identity drift: STOP, preserve evidence and return blocker; do not expand scope.
R8: independent review and KOO reconciliation before any next decision.

## Options

Option A (recommended): prepare an addressed bounded design-only task for SIS (system administrator profile) to specify a read-only capability evidence collection plan, environment consent/identity requirements, data minimization and stop conditions. SIS is not authorized to run probes by this document. Subsequent execution authorization must be separate and target/environment-specific.

Option B: request SHD independent review of this design before tasking SIS; more conservative but adds an intermediate documentary step. Needs separate task preparation and execution authority.

Option C: stop at static traceability milestone; preserve current NO_GO_G4 and do nothing further.

## Current verdict and next decision

Current G4 readiness: NO_GO_G4_REAL_SANDBOX_EXECUTION.
Real environment/host: NOT_SELECTED.
Real SECE sandbox target: NOT_SELECTED.
Real syscall/target evidence: NOT_COLLECTED.
Candidate: NOT_ACTIVATED.
G4/G5/G6 authority: NOT_CREATED.

Recommend Option A with explicit separate preparation permission:

AUTHORIZE_KOO_PREPARE_SIS_SECE_NONPROD_READONLY_PLATFORM_CAPABILITY_PLAN_R01 = YES

If approved KOO may PREPARE only a SIS design-only addressed task, not execute it or select a host/target. SIS would be asked to propose methods, exact read-only boundary, environment evidence requirements, risks and blockers. Later execution requires a separate OPERATOR decision and manual handoff. No tests, commands, mutation, activation, deployment or G4/G5/G6.

terminal: SECE_NONPROD_PLATFORM_CAPABILITY_EVIDENCE_DESIGN_R01_COMPLETE_ONLY
