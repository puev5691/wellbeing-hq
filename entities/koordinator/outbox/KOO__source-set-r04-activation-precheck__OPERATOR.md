# KOO → OPERATOR: source-set activation barrier precheck r0.4

status: BLOCKED_BEFORE_SOURCE_SET_ACTIVATION
verdict: `BLOCKED_KOO_SOURCE_SET_R04_ACTIVATION_BARRIER: CHECKSUM_METADATA_MISMATCH_AND_PROJECT_SOURCE_MEMBERSHIP_MUTATION_UNAVAILABLE`
project_time: omitted; trusted project-time source not used

## Что произошло

KOO выполнил fresh GitHub-preflight и независимо перечитал exact KAN materialization:

Terminal result:
`entities/kancelar/outbox/KAN__manual-activation-handoff-materialization-r01__KOO.md`
commit `351cb92af598bc3852db6b1ebb69b3e8e5847c6a`
blob `ef4d0adfce4c3d3bb507c1c6f1f9f4ebaea6bb9c`
verdict `PASS_KAN_MANUAL_ACTIVATION_HANDOFF_READY_FOR_KOO_SOURCE_SET_BARRIER`.

KAN source-set manifest:
`entities/kancelar/outbox/manual-activation-handoff-r01/SOURCE-SET-MANIFEST.md`
commit `c20badfb6c4920f7e85b119fed8108d3d0a367c2`
blob `a4711b2e43f81978a06947128693c72bcce21eca`.

Requested activation unit:
- `project-instructions-core-v2_3-approved.md`;
- `task-conveyor-canon-v1_1-approved.md`;
with four existing active sources unchanged.

## Что это означает

Partial activation is forbidden and was not performed.

The exact Git commits/blobs of both successors are readable and internally stable, but the SHA-256 values written in the KAN SOURCE-SET-MANIFEST do not match the exact Git blob bytes.

The mismatch is exactly one missing final LF in each published blob:
- hashing the exact Git blob gives the actual SHA below;
- hashing the same content plus one final `\n` gives the SHA written by KAN.

This is checksum metadata inconsistency, not a semantic text difference, but the source-set activation barrier is an exact-byte integrity boundary and KOO will not silently ignore it.

Additionally, the current ChatGPT tool surface exposes Project Sources for reading but provides no capability to attach/detach/replace Project Source membership. Therefore KOO cannot truthfully complete the final active-payload replacement/readback step from this chat.

## Exact independent readback

### Successor 1 — project core v2.3

Path:
`entities/kancelar/outbox/manual-activation-handoff-r01/project-instructions-core-v2_3-approved.md`

Commit:
`6286962c6218072d174f87e2a040687719fbe3a6`

Git blob:
`e51054d57c583bbbecc79716e1d5543e686efbd8`

Actual Git blob SHA-256:
`b115daa61782441e3b336dbedda216e4ea0b088fae12b374681a1069414d258e`

KAN manifest SHA-256:
`5d6fceee3d667e761996cae160ba19060f4a2f054901d4700d29f1b8f22ee75c`

Relation:
KAN value equals SHA-256 of exact Git text plus one final LF.

Blob identity readback:
PASS.

Semantic text readback:
PASS for the published Git blob.

### Successor 2 — task conveyor v1.1

Path:
`entities/kancelar/outbox/manual-activation-handoff-r01/task-conveyor-canon-v1_1-approved.md`

Commit:
`6d13d7ffcfb837492ed999c904a5f5bcc210b0a0`

Git blob:
`0ff3d3f74d5793ea72cc9e84fffc64f01e8455ab`

Actual Git blob SHA-256:
`904c4a89a459ab159758a50ae6cc56be25b988514388bd201a9872ad4a56e6d8`

KAN manifest SHA-256:
`9eb9befd114bcf45b11fe1b419d104f290ccda2eb0b2fdc69b9971d493e1080b`

Relation:
KAN value equals SHA-256 of exact Git text plus one final LF.

Blob identity readback:
PASS.

Semantic text readback:
PASS for the published Git blob.

## Four unchanged sources

These exact active-source identities remain unchanged and independently match the prior approved r0.3 publication:

1. `entity-roles-short-v2_4-approved.md`
   - blob `1772339cb74dae8550bfbd2e33401c34a929e911`
   - SHA-256 `d7feae524f6d1a34b0fd2a63475435e41ebe48097a191d87ca0ceeb797421530`
   - PASS

2. `file-work-canon-universal-v2_4-approved.md`
   - blob `e9c29d62057f34e4f771d6057a36d9b7f72e74c2`
   - SHA-256 `c7e09bb358afd9ff131158044ce3722375ab30580e240909e85afdf38ca1e08b`
   - PASS

3. `source-loading-policy-v2_2-approved.md`
   - blob `69eb657f260a019f76e8e707c880ea88c1dfa0bf`
   - SHA-256 `2a410e929c8cf4daa21f9229ad300e92abbaf4ab40b4fbf3a03950cc663e719e`
   - PASS

4. `entity-state-preservation-and-recovery-canon-v1_6-approved.md`
   - blob `233117e1c9509d730e1f5ec532b1cabe3f786609`
   - SHA-256 `82e3117570a9ecd73be2dae1279ebb3e0a2d6125556de98d5c1ede14a9236ae5`
   - PASS

Unchanged-source readback:
`4/4 PASS`.

## Current active predecessors

Until complete barrier PASS:

- active core remains `project-instructions-core-v2_2-approved.md`
  SHA-256 `ae215f9c7bb44a1b9d525e1f78ea828cdeecd2d8487cb075dc49f4f94420c7af`;

- active conveyor remains `task-conveyor-canon-v1-approved.md`
  SHA-256 `7c49fde826ffab59d19c4fc30ccfa6aa660454c2c09785ba9237647e4e4388a6`.

Supersession is NOT yet recorded as effective.

## Scope clarification

The exact successor pair in this source-set implements the mandatory post-terminal manual activation handoff:
`АДРЕСАТ + PROMPT + ДЕЙСТВИЕ ОПЕРАТОРА`
while automatic exact Entity-chat resume is unavailable.

This source-set does not by itself materialize the earlier broader general human-readable-results candidate section
`что произошло → что это означает → что теперь возможно, разрешено или требуется`.
That broader candidate remains a distinct normative lineage unless separately materialized/approved.

## Minimal OPERATOR resolution

KOO does not require any return to RED for semantic evidence.

To preserve the exact source commits explicitly named by OPERATOR, the minimal checksum resolution is:

`ACCEPT_ACTUAL_GIT_BLOB_SHA256_FOR_SOURCE_SET_R04`

Meaning:
- use the two exact Git commits/blobs named above;
- treat KAN manifest SHA fields as checksum-metadata error caused by a missing final LF;
- use the actual Git blob SHA-256 values established by KOO independent readback;
- do not change semantic source bytes.

After this decision, the only remaining non-automatable barrier step is Project Sources membership replacement as one bounded maintenance operation:
- replace core v2.2 with exact core v2.3;
- replace conveyor v1.0 with exact conveyor v1.1;
- leave the other four active sources unchanged;
- do not resume normative source-dependent work between the first and second replacement;
- then signal KOO for active-payload readback.

Alternative:
`REQUIRE_KAN_SOURCE_SET_CHECKSUM_MANIFEST_CORRECTION`
keeps activation blocked until KAN republishes checksum metadata; no RED re-review is required because source semantics are unchanged.

## Barrier accounting

new source semantic readback: PASS 2/2
new source Git blob identity: PASS 2/2
new source manifest SHA-256 identity: FAIL 0/2
unchanged sources: PASS 4/4
partial activation performed: 0
Project Sources membership mutation performed by KOO: 0
mixed-set authority declared: NO
source-set activation declared: NO

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: exact source-set activation barrier precheck
СТАТУС: BLOCKED_BEFORE_SOURCE_SET_ACTIVATION
