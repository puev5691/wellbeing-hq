# KOO → ARH: WEB emergency preservation and replacement preparation r0.1

status: TASK
execution_mode: FAST_PATH
priority: EMERGENCY_CONTINUITY

## Trigger

OPERATOR reports WEB chat degradation:
- browser view appears completed;
- application remains stuck in thinking;
- continued production use of that WEB instance is to be frozen;
- project work must continue through preservation and replacement initiation.

Freeze record:
`entities/koordinator/outbox/KOO__WEB-chat-degradation-freeze-r01__OPERATOR.md`
commit `ef4026629a9ef890e4de64abdeebfd205cb15324`.

## Normative basis

Use current approved:
- entity state preservation/recovery canon v1.4;
- universal file-work canon v2.3;
- current project instructions.

Do not reconstruct WEB current-state from memory.

## Known historical continuity evidence

WEB continuity candidate:
`entities/webmaster/outbox/web-continuity-preservation-candidate-r01/`

package commit:
`f4d45cc977b0c8f0e16e61ce39cd7ce264261411`

package tree:
`db75c67da241a234ab61802a7533ec58703b5a1b`

result:
`ad17a39a781a91d3b19591fca8500532551f8417`

verdict:
`PASS_WEB_CONTINUITY_CANDIDATE_READY`

Boundary:
this package is candidate-only, NOT canonical recovery and NOT initiation_verified.

## Fresh WEB development evidence that must be preserved

Accepted/reviewed chain includes at least:

- WEB portal assembly r0.1 package:
  `entities/webmaster/outbox/public-info-portal-site-assembly-r01/`
  commit `d78b7c549d92f51f1b485b02469a65f8272e6f2b`
  tree `5d3abebe1bf8493a0268606696982d26003d4131`;

- WEB result:
  `573eef0c5b3fc20599795e11baf22f55c982d731`
  verdict `PASS_WEB_PUBLIC_INFO_PORTAL_SITE_ASSEMBLY_R01_READY_FOR_REVIEW`;

- RED public-safe/editorial review:
  `8484b16dbb6d46833af4096f8f9b5f8e442aec1a`
  verdict `PASS_RED_PUBLIC_INFO_PORTAL_EDITORIAL_REVIEW_R01`;

- current WEB presentation refinement r0.2 task:
  `entities/koordinator/outbox/KOO__public-info-portal-presentation-r02__WEB.md`
  commit `37f051ac7fc01ecb0a96b8d15891aa549e22764e`;

- corresponding WEB inbox pointer:
  commit `6248aa22078d1ac3860b0ccd2751840899c996fd`.

At KOO freeze boundary, no GitHub terminal result for r0.2 is claimed. Preserve it as pending/unknown active dependency unless fresh evidence proves otherwise.

## Required ARH procedure

### A. External coordination checkpoint

1. Freshly verify WEB current writer / current markers / relevant recovery state.
2. If current authoritative WEB writer is still usable, require/create authoritative WEB self-snapshot through that writer.
3. If current writer is unavailable/unusable:
   - record failure-state explicitly;
   - do NOT author or reconstruct a WEB self-snapshot;
   - preserve the latest externally verified recovery/current-state as last confirmed state.

### B. Preservation package

Build a recovery package suitable for replacement initiation containing, as applicable:
- current WEB initiation file;
- latest authoritative self-snapshot OR explicit missing-snapshot failure-state;
- role/authority/constraints;
- mandatory current sources;
- accepted results and exact artifact references;
- active/pending task r0.2 as exact dependency;
- open questions / known UI degradation;
- current portal work state;
- experience / lessons from degraded instance and previous continuity candidate;
- manifest;
- checksums / immutable identities;
- external recovery locator;
- one safe next step.

### C. External preservation

Use the approved external recovery contour if available.
Verify:
- repository/path/ref;
- manifest;
- checksums;
- immutable commit/blob identities;
- readback.

Do not claim external preservation if locator/readback cannot be verified.

### D. Replacement preparation

Prepare, but do not silently execute:
- replacement WEB initiation runbook/instruction;
- exact recovery locator and expected version identity;
- expected initiation status conditions;
- current-writer handoff/failover boundary;
- first safe task after initiation.

The replacement must not claim completion of the r0.2 presentation task unless a verified terminal artifact exists.

### E. Experience capture

Record concise lessons:
- degradation symptom pattern;
- browser/app state divergence;
- why GitHub terminal evidence outranks UI impression;
- need for earlier preservation trigger if similar divergence reappears;
- what worked/did not work in previous WEB continuity candidate.

## Boundaries

Do not:
- invent WEB self-state;
- mark r0.2 completed without GitHub result;
- modify portal source/status;
- deploy or publish;
- transfer current-writer automatically;
- alter canonical recovery/current pointers before verified package/readback;
- read/copy secrets.

## Expected terminal

One of:

`PASS_ARH_WEB_RECOVERY_PACKAGE_READY_FOR_REPLACEMENT_INITIATION_R01`

or exact:
`BLOCKED_* / FAIL_*`.

Return to KOO through Exchange Gate and stop.
