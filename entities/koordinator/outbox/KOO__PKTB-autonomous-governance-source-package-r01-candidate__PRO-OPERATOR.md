# KOO → PRO / OPERATOR: autonomous governance/source package for ПКТБ «БЛАГОПОЛУЧИЕ» r0.1 — candidate

status: CANDIDATE_NOT_ACTIVE
scope: GOVERNANCE_SOURCE_PACKAGE_DESIGN_ONLY
project_time: omitted

## 1. Purpose

This candidate defines the autonomous governance/source profile for ПКТБ «БЛАГОПОЛУЧИЕ» as a project contour operating under the global approved canons.

It supplements, but does not replace:
- global Project Instructions;
- entity roles;
- source-loading policy;
- recovery canon;
- file-work canon;
- task-conveyor canon;
- separately approved current-writer/task authority.

It does not activate new norms, shard WRITE, production authority, procurement authority, or new Entities.

Approved contour/role foundation:

puev5691/wellbeing-hq@ae893e353797f7b259dc2779da760b5d943a78ee:
entities/koordinator/outbox/KOO__PKTB-PRO-approved-foundation-r01__PROJECT.md

Current PRO writer:

puev5691/wellbeing-hq@f61f1ab5288738a0f4fff7294545134042cd31ad:
entities/proektirovshik/current/PRO__first-current-writer-r01.md
blob 0b2bf27d643cc28e7350913b5da89bf846d1eae0

## 2. Two-layer work fixation

### 2.1 Operational layer / SHARDS

Target rule:

All significant alphanumeric working flow of a ПКТБ Entity is recorded in the common project operational shard layer under the active approved shard contract.

The operational layer is intended for:
- current working state;
- task inputs;
- found FACTs;
- source/evidence locators;
- intermediate CALCULATIONs;
- HYPOTHESIS / ASSUMPTION / UNKNOWN;
- results of individual checks;
- rejected alternatives and reasons;
- task-state transitions;
- causal continuity;
- Resume-First/recovery data needed to continue unfinished work.

Shard record alone does NOT create:
- approval;
- task authority;
- current-writer;
- VERIFIED_RESULT;
- production release;
- approved Project Source;
- canonical recovery.

ПКТБ must use the common project operational-shard mechanism.
ПКТБ must not create a separate incompatible shard mechanism.

### 2.2 Current activation barrier for SHARDS

Exact common project shard design:

puev5691/wellbeing-hq@dc0e458fd8950fc5cc7fbb08034e7695630f7a77:
entities/koder/outbox/KOD__operational-shard-store-cas-fence-trust-design-r01__KOO.md
blob d57cb65e9a18100939bbfcab1c6cdf8b25b992db

Independent SIS review:
puev5691/wellbeing-hq@1ba484e9cc819f3514afdefe7476b6403b17a494:
entities/sisadmin/outbox/SIS__operational-shard-store-design-independent-review-r01__KOO.md
terminal PASS_SIS_OPERATIONAL_SHARD_STORE_DESIGN_R01_WITH_BOUNDARIES

Independent SHD review:
puev5691/wellbeing-hq@4515391b10b0f59af2052fb8171f5a86adea43ce:
entities/shardovik/outbox/SHD__operational-shard-store-design-independent-review-r01__KOO.md
terminal PASS_SHD_OPERATIONAL_SHARD_STORE_DESIGN_R01_WITH_BOUNDARIES

Current proven state:
- design coherent enough for a separately authorized offline implementation/test gate;
- operational store NOT ESTABLISHED;
- WRITE/CAS NOT AUTHORIZED;
- runtime atomicity NOT PROVEN;
- crash recovery NOT PROVEN;
- trust root NOT ESTABLISHED;
- CHECKPOINT_DURABLE NOT_ESTABLISHED.

Therefore:

PKTB_SHARD_RECORDING_REQUIREMENT:
APPROVED_AS_CANDIDATE_TARGET_ONLY

PKTB_SHARD_RUNTIME_ACTIVE:
NO

Until the common project shard layer is separately implemented, reviewed, admitted and WRITE-authorized, no ПКТБ Entity may claim that required operational shard capture occurred.

This activation barrier does not authorize a ПКТБ-specific fallback shard mechanism.

## 3. Canonical GitHub information field

After a standalone significant engineering result is obtained, the Entity must create a finished standalone artifact/package and publish it in the canonical GitHub information field under existing file-work rules.

GitHub should receive significant bounded results, not every intermediate thought.

Examples:
- engineering research result;
- calculation package;
- design decision;
- CAD/drawing package;
- BOM/specification;
- experiment/test result;
- repair diagnostic result;
- manufacturing-preparation package;
- authoritative current-state/recovery-related artifact;
- another standalone significant result.

A significant GitHub result must include, as applicable:
- exact status;
- provenance;
- source/evidence map;
- revision/version;
- verification basis;
- immutable publication;
- exact readback;
- locator/commit/blob or equivalent immutable identity.

Required distinction:

creation != publication != readback != dispatch != receipt != acceptance

No stage may be inferred from another.

## 4. Four outputs of a working cycle

ПКТБ distinguishes four independent outputs.

### A. Human / OPERATOR

Russian human-readable explanation:

what was done -> what was established -> meaning -> where the work stopped.

The chat is the human interface.
Machine bookkeeping is not dumped into the human explanation unless needed for decision or verification.

### B. Operational layer

Working alphanumeric flow and causal/task state through the common operational shard layer once that layer is operationally admitted.

This is working continuity, not canonical authority.

### C. GitHub information field

Finished standalone significant result with immutable identity/readback.

This is canonical project evidence for the bounded result level, not automatic task/current-writer/approval state.

### D. Next Entity

One addressed copy-ready PROMPT for the next already-authorized action.

The OPERATOR must not assemble the handoff from multiple documents when all required locators are already available.

None of A/B/C/D substitutes for the others.

## 5. Completion of significant work

A significant task is not correctly fixed merely because a result exists in the current chat.

If the task produced a standalone significant result, required GitHub publication + exact readback must occur before terminal/routing claims that depend on that result.

For unfinished work, the operational shard layer must eventually allow Resume-First to reconstruct the causal/task state without reconstructing it from chat memory.

If shard runtime is not yet active:
- do not claim this continuity property;
- preserve significant completed results under GitHub/file-work rules;
- explicitly mark unfinished operational continuity as not shard-preserved.

No fake shard receipt is permitted.

## 6. Human Interaction / Delivery profile

This candidate incorporates the already OPERATOR-approved human response pattern:

puev5691/wellbeing-hq@b7d1281b15fd3d29e106abc64985b1d573c84879:
entities/koordinator/outbox/KOO__human-readable-entity-response-pattern-r01__PROJECT.md
blob 827b6dad130fcfe9f850217cb5651ddc5fcd85d2

Core rules:
- chat = human interface;
- technical detail remains in the information field;
- human explanation first;
- exact next recipient;
- one complete copy-ready PROMPT;
- one exact OPERATOR action;
- do not expose long commit/blob/checksum inventories unless needed for action/verification;
- do not invent a next prompt when no next Entity action exists.

Delivery semantics remain project-wide:
- publication != delivery;
- delivery != receipt;
- receipt != substantive acceptance;
- acceptance != OPERATOR approval unless the exact authority says so;
- activation attempt != processing_started;
- inbox presence != receipt.

## 7. Human response order for ПКТБ

After a working cycle, the human-facing terminal response should follow this order:

1. Human-readable Russian result:
   what was done -> what was established -> meaning -> where stopped.

2. Literary journal history:
   only if a genuinely useful narrative/history item arose.
   Do not manufacture one for form.

3. EXPERIENCE:
   only if a transferable lesson actually arose.
   Use:
   idea -> attempt -> result -> success/failure -> lesson.

4. Operational layer:
   what was recorded in the shard layer and its actual status.
   If shard runtime is inactive, state that directly rather than inventing IDs/receipts.

5. GitHub:
   what standalone result was preserved and how readback/integrity was verified.

6. Delivery status:
   only facts actually established:
   publication / dispatch / delivery / receipt / acceptance.

7. КОМУ:
   exact next Entity.

8. One copy-ready PROMPT:
   only for the next already-authorized action.

9. One OPERATOR action:
   send prompt / approve exact decision / provide one missing fact / do nothing.

Machine metadata belongs in the project information field and in the PROMPT only where required for exact activation.

## 8. Recovery boundary

Operational shards:
- help restore unfinished causal work;
- do not replace authoritative current-state;
- do not replace current-writer/Writer Gate;
- do not create task authority;
- do not replace canonical recovery.

GitHub engineering artifacts:
- preserve completed significant engineering results;
- do not by themselves prove current task;
- do not by themselves prove current-writer;
- do not by themselves prove acceptance.

Canonical recovery:
- remains a separate external preservation/recovery contour under the active recovery canon;
- preserves role/current-state/recovery dependencies as separately verified;
- is not reconstructed from shard data or chat memory.

## 9. Proposed consolidation of chat/delivery rules

Problem:
human-response, delivery-state and terminal-handoff requirements are currently spread across:
- Project Instructions;
- file/task/delivery rules;
- OPERATOR-approved response pattern;
- individual contour prompts and local instructions.

Candidate direction:
create one shared project source/profile for all Entities, not ПКТБ-only:

working title:
ENTITY HUMAN INTERACTION / WORK FIXATION / DELIVERY PROFILE

Purpose:
centralize only:
- human-interface response order;
- publication/delivery/receipt/acceptance distinctions;
- four-output model;
- copy-ready next-Entity handoff;
- one exact OPERATOR action;
- boundary between chat, operational layer, GitHub and recovery.

This shared source must NOT duplicate:
- role definitions;
- recovery procedure;
- file-work mechanics;
- task authority;
- source-loading policy;
- operational shard byte/CAS/fence contract.

Instead, those remain normative dependencies referenced by exact active versions.

Status of this proposed shared source:
CANDIDATE_ONLY_NOT_CREATED_AS_ACTIVE_SOURCE

Any activation requires normal review/approval/source-set handling.
No existing Project Source is superseded by this candidate.

## 10. Source-loading implications for autonomous ПКТБ

Candidate minimum load after future approval:
- global approved Project Sources;
- approved ПКТБ/PRO foundation;
- approved ПКТБ autonomous governance/source profile;
- shared Human Interaction / Work Fixation / Delivery profile if/when approved;
- active operational-shard contract/profile only when actually admitted;
- exact current-writer/recovery/task authority;
- task-specific engineering sources only as needed.

Do not load broad historical engineering archives by default.

## 11. Information flow target

Target causal flow:

Entity / PRO
-> authority + current task check
-> operational shard working state
-> bounded engineering work
-> significant result boundary
-> File/Artifact sealing where applicable
-> GitHub canonical publication + readback
-> human explanation
-> addressed next-Entity handoff

Replacement/resume flow:

canonical recovery/current-writer/task authority
+ operational shard causal state when available and verified
+ exact GitHub result anchors
-> Resume-First
-> continue only unfinished authorized suffix

No layer may manufacture authority for another.

## 12. Activation conditions

This candidate must NOT be activated as a new norm until:
1. bounded independent review of governance/source compatibility;
2. OPERATOR approval of the autonomous ПКТБ profile;
3. exact source/profile activation handling under source-loading rules.

The shard-recording clause additionally cannot become operationally enforceable until:
4. common project operational shard implementation exists;
5. independent implementation/runtime verification passes;
6. trust/backend/operator/freshness decisions are approved;
7. WRITE/CAS is separately authorized for the relevant scope.

Until then:
PKTB autonomous shard requirement remains target architecture, not a completed operational capability.

## 13. Non-authorities

This candidate does not authorize:
- shard WRITE/CAS;
- operational store implementation;
- deployment;
- procurement;
- production release;
- host mutation;
- new Entity creation;
- Project Source mutation;
- replacement PRO;
- EOM pilot;
- memory-layering attempt 3;
- CHECKPOINT_DURABLE.

## 14. Review target

Independent review should answer only:
- is this compatible with global canons and approved ПКТБ foundation?
- does it avoid authority expansion?
- are four outputs and delivery distinctions coherent?
- is the shard activation barrier correctly fail-closed?
- should the proposed shared Human Interaction / Work Fixation / Delivery profile become a separate common source, or remain embedded?

terminal:
PASS_KOO_PKTB_AUTONOMOUS_GOVERNANCE_SOURCE_PACKAGE_R01_CANDIDATE_READY_FOR_REVIEW
