# KOO -> SHT-REPLACEMENT-R02: post-Writer self-snapshot preservation

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
SHT / ШТАБИСТ current writer SHT-REPLACEMENT-R02

attempt:
SHT_R02_POST_WRITER_SELF_SNAPSHOT_R01_A1

scope:
PRESERVATION_SELF_SNAPSHOT_ONLY

project_time:
omitted

Resume-First.

Do NOT perform profile work.

Do NOT resume SECE.

Do NOT authorize or execute narrow rereview.

This task exists only because Writer Gate PASS changed authoritative SHT writer-state and the last external recovery r02 is now stale relative to that new writer-state.

## Exact preservation authority

puev5691/wellbeing-hq@6b21eb7b670cc6d95477219637710deb5b43164b:
entities/koordinator/outbox/SHT_r02_post_writer_self_snapshot_authority.md

blob:
f95c7124574e01bf0cd61fa8c00803d8eeaeb683

status:
CANON_TRIGGER_AUTHORITY_RECORDED

scope:
PRESERVATION_SELF_SNAPSHOT_ONLY

## Registry

puev5691/wellbeing-hq@d6c1479d530b6d30a4d9e6c43fac53db2eed8eb5:
entities/koordinator/outbox/SHT_r02_post_writer_self_snapshot_registry.md

blob:
50ada4e133093f6bd3e9346088313a7bd1e00642

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@ef796a99e892e17bae9be97c36e5fdbdfe8007fd:
entities/koordinator/outbox/SHT_r02_post_writer_self_snapshot_frontier.md

blob:
ef53aa3037bb7034fb1b000a0fc15f1988af7d36

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## Current authoritative SHT writer

puev5691/wellbeing-hq@7ed8b5570d3aa610120ab4a541b4d03ca032cf3b:
entities/shtabist/current/SHT__replacement-current-writer-r02.md

blob:
591a5c474523f46ad84b5c49c62939832b87b15c

status:
WRITER_ESTABLISHED

writer_generation:
SHT-REPLACEMENT-R02

instance_binding_id:
SHT_R02_WRITER_BOUND_TO_A2_RESULT_7133F0

This exact chat must verify it is the same chat bound to that Writer Gate.

## Exact Writer Gate result

puev5691/wellbeing-hq@93fdb47de6014e16399614d2a185a95a841ade34:
entities/shtabist/outbox/SHT__replacement-writer-gate-r02-A1-result__KOO.md

blob:
4ed81c3587ae4d8efeee306b271e7a3ffcac1911

terminal:
PASS_SHT_REPLACEMENT_CURRENT_WRITER_R02

## Predecessor writer

entities/shtabist/current/SHT__current-instance-current-writer-r01.md

blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

disposition:
PREDECESSOR_WRITER_HISTORY_SUPERSEDED_FOR_NEW_AUTHORITATIVE_CURRENT_STATE_MUTATIONS

Do not mutate or rewrite predecessor history.

## Existing recovery basis

puev5691/wellbeing-entity-bootstrap@c23b2304ca0ea4f4b62e9e451e39c69cfb1817c5:
entities/sht/recovery/versions/sht-recovery-r02

tree:
f561246223a48ac885d7baae383898cc8e89af16

classification after Writer Gate:
LAST_VERIFIED_RECOVERY_BASIS_BUT_STALE_AFTER_WRITER_HANDOFF

Do not rewrite or delete r02.

## Preserved project/task boundary

profile_continuation:
PAUSED_BY_OPERATOR

D1D2 attempt:
SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_A1

D1D2:
COMPLETED_PASS

D1D2 terminal:
PASS_SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_READY_FOR_NARROW_REREVIEW

corrected package tree:
84979101d6bd19fd939f978652f03317f6e524b9

narrow_rereview:
NOT_STARTED / NOT_AUTHORIZED

historical task/PROMPT replay:
FORBIDDEN

profile_task_authority:
NOT_CREATED

SECE continuation:
NOT_AUTHORIZED

## Mandatory PROCESSING_STARTED

Before substantive preservation:

1. fresh-check preservation authority/registry/frontier;
2. verify current writer r02 exact path/blob/generation;
3. verify Writer Gate result unchanged;
4. verify no newer SHT current-writer exists;
5. verify no competing post-writer preservation attempt/result exists;
6. verify profile continuation remains PAUSED_BY_OPERATOR;
7. verify no narrow-rereview authority exists.

Then create:

entities/shtabist/outbox/execution-evidence/SHT_R02_POST_WRITER_SELF_SNAPSHOT_R01_A1__PROCESSING_STARTED_E1.md

Bind:
- exact attempt;
- authority blob;
- frontier commit/blob;
- current-writer commit/blob/generation;
- Writer Gate result commit/blob;
- predecessor writer blob;
- recovery r02 ref/tree;
- accepted_state INITIAL_NOT_STARTED_V1.

Immutable-readback it.

Only then create self-snapshot.

## Required self-snapshot

Create exactly one standalone current-writer self-snapshot:

entities/shtabist/outbox/SHT__replacement-r02-post-writer-self-snapshot__KOO-ARH.md

It must preserve, without reconstruction:

- entity SHT / ШТАБИСТ;
- current writer path/commit/blob/generation/status;
- exact Writer Gate authority and result;
- exact A2 initiation result and instance binding;
- predecessor writer identity and superseded-history disposition;
- active approved Project Source identities;
- recovery r02 exact locator/tree and stale-after-writer-handoff classification;
- profile_continuation = PAUSED_BY_OPERATOR;
- D1D2 = COMPLETED_PASS;
- D1D2 corrected package tree;
- narrow_rereview = NOT_STARTED / NOT_AUTHORIZED;
- historical replay = FORBIDDEN;
- profile_task_authority = NOT_CREATED;
- SECE continuation = NOT_AUTHORIZED;
- new external recovery successor = NOT_YET_CREATED;
- ARH post-writer preservation = NOT_YET_COMPLETED;
- hidden/unwritten state = UNKNOWN / MUST_NOT_BE_RECONSTRUCTED;
- safe next step = ARH external preservation successor based on this exact snapshot.

Do not create a recovery package yourself.
Do not mutate wellbeing-entity-bootstrap.
Do not create a profile task.
Do not resume D1/D2 or narrow rereview.
Do not alter writer-state again.

After publication:
- immutable-readback snapshot;
- return exact locator/commit/blob;
- include PROCESSING_STARTED locator/blob;
- state external ARH preservation = PENDING;
- STOP.

## Required return to KOO

Final response must contain one copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include:
- preservation attempt;
- PROCESSING_STARTED locator/blob;
- self-snapshot locator/commit/blob;
- current writer identity;
- predecessor disposition;
- recovery r02 stale classification;
- profile pause;
- D1D2 state;
- narrow rereview state;
- profile_task_authority state;
- external ARH preservation = PENDING;
- exact UNKNOWNs/blockers.

Include exact line:

Fresh-reconcile this exact post-Writer self-snapshot. Prepare ARH external preservation successor only. Do not infer profile continuation or narrow rereview authority.

End:

STOP.

After that block add nothing.
