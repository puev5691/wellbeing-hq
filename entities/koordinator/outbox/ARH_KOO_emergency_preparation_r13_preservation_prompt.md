# KOO -> ARH: preserve KOO emergency-initiation preparation r1.3

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

project_time:
omitted

АДРЕСАТ: АРХИВАРИУС / ARH r0.3

Resume-First.

## Authority basis

OPERATOR exact current decision is durably fixed here:

puev5691/wellbeing-hq@d15850fee62634a507d3e4473d19e8cfd43b6e31:
entities/koordinator/current/KOO__global-pause-emergency-initiation-preparation-r13.md

blob:
10522b06a9f3a58298823a2a251df1b9859e8aad

Meaning:
all profile tasks are paused; only recovery/preservation and later separately authorized replacement-initiation preparation are allowed.

Recovery Canon v1.6 assigns independent preservation/readback to ARH after authoritative current-writer self-snapshot.

## Current ARH writer

entities/archivarius/current/ARH__replacement-current-writer-r03.md

blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

status:
WRITER_ESTABLISHED

ARH must fresh-check its own writer/currentness before substantive work.
If not current, STOP exact blocker.

## Exact KOO self-snapshot

puev5691/wellbeing-hq@0178dde20cca04fc1d8d5147d9c32addac87b616:
entities/koordinator/outbox/koo-emergency-preparation-r13/KOO__emergency-preparation-self-snapshot-r13.md

blob:
bf8144c5bd9365f9096c03ea92deee8ea37a8d8b

terminal:
PASS_KOO_R12_SELF_SNAPSHOT_R13_READY_FOR_ARH_PRESERVATION

Current KOO writer:

entities/koordinator/current/KOO__replacement-current-writer-r12.md

blob:
b68e1dd2e79781f4ea8fab7e48e7456fada14c80

## External recovery basis

Last externally verified KOO recovery:

puev5691/wellbeing-entity-bootstrap@122fcd2172781cc87e2cc15afc46f715193f63db:
entities/koo/recovery/versions/koo-recovery-r12

package tree:
aee471b4388224842b1d052e6e9951eeb1090eac

## Perform only

1. Fresh-check HQ currentness/supersession and exact snapshot/writer/pause identities.
2. Treat r12 as the external recovery base, not as current state.
3. Preserve a NEW external KOO recovery successor from the exact r1.3 self-snapshot.
4. Preserve required recovery provenance and mandatory human-interface contract lineage.
5. Verify composition, immutable identities, integrity and external readback.
6. Update ARH recovery registry as applicable.
7. Prepare one cold-start PROMPT for a genuinely NEW KOO replacement instance, scope = Initiation Gate only.
8. Cold-start PROMPT must preserve GLOBAL_PROFILE_TASK_PAUSE_ACTIVE and must not infer any paused task as current.
9. Return exact external locator/version/tree, composition/readback result, preservation terminal and exact cold-start PROMPT locator/blob.

## Do not

- alter KOO authoritative current-state;
- freeze/retire KOO r1.2 unless separately authorized;
- establish a new KOO writer;
- execute Initiation Gate;
- execute Writer Gate;
- replay historical PROMPT/tasks/queues;
- resume SECE/KOD/SHD/SIS work;
- mutate Project Sources/canons;
- create production/live-effect authority;
- activate the prepared cold-start PROMPT.

## Expected terminal

PASS_ARH_KOO_EMERGENCY_PREPARATION_R13_EXTERNALLY_PRESERVED

or exact BLOCKED/FAIL with preserved last verified recovery.

## Required return format

After immutable publication/readback return exactly:

АДРЕСАТ: КООРДИНАТОР

Exact result:
puev5691/wellbeing-hq@<commit>:
<exact ARH result path>

blob:
<exact blob>

terminal:
<exact terminal>

external recovery:
<repo@commit:path>

package tree:
<exact tree>

cold-start PROMPT:
puev5691/wellbeing-hq@<commit>:
<exact path>

blob:
<exact blob>

Краткий человеческий итог:
<что сохранено, что проверено, что НЕ было активировано>

Exact next causal disposition:
RETURN_KOO_FOR_FRESH_RECONCILIATION

Не возвращай только commit/locator.

STOP.
