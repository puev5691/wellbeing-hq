# ARH — SIS r0.8 planned replacement preservation review r0.1

conveyor_attempt:
ARH_SIS_R08_PRESERVATION_R01_A1

attempt_state:
AWAITING_OPERATOR_TRANSFER

project_time:
omitted

АДРЕСАТ: АРХИВАРИУС / ARH

Resume-First.

Выполни ТОЛЬКО independent preservation/recovery review exact SIS r0.8 planned-replacement preparation package и, при полном PASS входных проверок, внешнее сохранение как NEW SIS recovery delta.

Не выполняй SIS freeze/handoff, successor initiation, successor Writer Gate, R03 replay/resume, host cleanup либо production/profile work.

## 1. Exact authority basis

Этот шаг уже покрыт действующим preservation/recovery process:

- Entity Roles v2.4: ARH является профильным владельцем preservation/recovery, принимает self-snapshot/recovery packages, проверяет composition/provenance/manifest/checksums/version identity, организует external publication/readback и ведёт recovery registry.
- Recovery Canon v1.6: ARH preservation-check проверяет current-writer authorship, manifest/composition, provenance, external locator, integrity, publication/readback, secrets boundary, recovery registry и stale/recoverability.
- ОПЕРАТОР поручил current SIS r0.8 начать собственную replacement/recovery preparation и поручил KOO выполнить fresh reconciliation и создать NEW ARH activation PROMPT, если preservation покрыто approved process.
- KOO r1.2 fresh reconciliation установил: separate approval gate для этого preservation-review не требуется.

Это authority только на preservation/recovery exact package ниже.
Оно не создаёт SIS task authority, successor authority, Writer Gate authority, R03 authority, production authority или Source/canon authority.

## 2. Current writers — fresh-verify before substantive work

KOO current writer:

puev5691/wellbeing-hq@e3636b4bba46d95de215f50bd0cc5b443fffbc99:
entities/koordinator/current/KOO__replacement-current-writer-r12.md

blob:
b68e1dd2e79781f4ea8fab7e48e7456fada14c80

status:
WRITER_ESTABLISHED

terminal:
PASS_KOO_REPLACEMENT_CURRENT_WRITER_R12

SIS current writer:

puev5691/wellbeing-hq@589f57033cf025ab9f26f17c480b167d87638e1e:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r08.md

blob:
2b79f89729cf0fd6c1a3d25e273e86f0c1c01b78

status:
CURRENT_WRITER_ESTABLISHED

terminal:
PASS_SIS_R08_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

ARH current writer at task preparation:

puev5691/wellbeing-hq@afe2a1d97cba7d0d489f8e9b935cc30554ac492c:
entities/archivarius/current/ARH__replacement-current-writer-r03.md

blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

status:
WRITER_ESTABLISHED

ARH must perform its own fresh Resume-First/current-writer/supersession checks.
If ARH writer continuity is not valid/current, STOP and return exact blocker. Do not self-appoint a new writer.

## 3. Exact source package

Source:

puev5691/wellbeing-hq@26784f2e1447ab1ef8a7383e8577abe7565b42de:
entities/sisadmin/outbox/sis-planned-replacement-prep-r08-r01/

package tree:
3730a6afd337439d3c9487c12344300df9b05a79

Expected composition:
EXACTLY 5 files.

1. SIS__planned-replacement-self-snapshot-r08-r01__ARH.md
Git blob:
56807b80a80cfc9de8e5e3305b21e47fb52a4d2d
SHA-256:
d6d80d436331e384596bb9cb9e4190cd2f948d4ca5897f4b0c040722eacb289f

2. SIS__planned-replacement-initiation-draft-r01__ARH.md
Git blob:
cdbd973343df72fcf3e8e550c900765570fb643a
SHA-256:
ad25aa70de23b3d374d4973b512a0fdf40b14a87ca4a959776796924eb6ed638

3. SIS__planned-replacement-preservation-handoff-r01__ARH.md
Git blob:
f29e78401e549f2371dacd9047701476e7fa5b1b
SHA-256:
b721e92096482c7441c392367e8ff49749d909e46826ceac64691e2a6e92b747

4. RECOVERY-MANIFEST.md
Git blob:
8fcb6046c1ec373e33d4bbf36f7a3d5abef4dbda
SHA-256:
b3e063de5eb3acbb034b198fdf4f548ef9f2707157426ed5e8cbae84b85a9109

5. sha256sums.txt
Git blob:
a00a06fd04e7443da653d9a94def71a505aecead
SHA-256:
ed8fc70782b54a811d99d5d1eaaf24ef569d52e749d790760107af2169a1f7e5

sha256sums.txt declares SHA-256 for the four Markdown files.

Fresh KOO verification before task materialization:
5/5 Git blob PASS
5/5 independently computed SHA-256 PASS.

ARH must independently verify exact bytes/composition/integrity again.
KOO verification is input evidence, not a substitute for ARH preservation-check.

## 4. Recovery lineage

BASE:

puev5691/wellbeing-entity-bootstrap@6ffb05a0a2fb018717ddd6e996d4ec1c7a41ef7:
entities/sis/recovery/versions/sis-emergency-r06

PREDECESSOR DELTA:

puev5691/wellbeing-entity-bootstrap@faa13798292dd93617ef8d4c0e5e47ebaf5ce809:
entities/sis/recovery/versions/sis-planned-r07

Prior ARH preservation result:

puev5691/wellbeing-hq@0061574c3aa4fcc3eeba341e63b9cc6c972dd9a3:
entities/archivarius/outbox/ARH__SIS-planned-replacement-r07-result__KOO-OPERATOR.md

blob:
df944eb4e2b7bf00935e7134c87e36811cd018c8

terminal:
PASS_ARH_SIS_PLANNED_REPLACEMENT_R07_EXTERNALLY_PRESERVED

Existing recovery registry predecessor:

entities/archivarius/current/recovery-registry/ARH__SIS-planned-recovery-r07.md

blob at task-preparation HEAD:
97558ce2b402ac8ac2ed430a627d3ac452dcb582

Do NOT overwrite or mutate r0.6 or r0.7 recovery packages.

## 5. Exact external preservation target

Repository:
puev5691/wellbeing-entity-bootstrap

Required NEW version path:
entities/sis/recovery/versions/sis-planned-r08/

At KOO task preparation this path was absent.

Before any external write:
- fresh-read external recovery inventory;
- verify sis-planned-r08 is still absent;
- verify r0.6 and r0.7 immutable identities remain available;
- verify no newer SIS recovery successor or competing preservation exists;
- verify exact source package unchanged.

If sis-planned-r08 already exists at fresh preflight:
STOP CONFLICT.
Do NOT overwrite, merge, repair or silently choose another name.

Preserve the exact five source files byte-for-byte in this new directory.
Do not rewrite SIS self-state, initiation draft, handoff, manifest or checksum file.

After publication:
- capture exact external commit;
- verify exact external package tree;
- verify 5/5 file composition;
- verify Git blob identities;
- verify SHA-256 values;
- perform immutable readback from the external repository;
- prove external bytes match the accepted source package.

## 6. Recovery registry

Only after successful external publication + immutable readback create the NEW registry record:

entities/archivarius/current/recovery-registry/ARH__SIS-planned-recovery-r08.md

Do not alter predecessor registry records to pretend they are r0.8.

Registry must include at minimum:
- source package exact locator/commit/tree;
- source SIS writer locator/blob;
- base r0.6 locator;
- predecessor r0.7 locator;
- new external r0.8 locator;
- external commit/tree/version identity;
- 5/5 composition result;
- checksum/readback result;
- stale/recoverability notes;
- explicit boundary that SIS r0.8 remains current-writer until a later separately authorized freeze/handoff/replacement transition.

If registry target already exists unexpectedly:
STOP CONFLICT before overwrite.

## 7. Current R03 boundary — preservation only, no reinterpretation

KOO current execution-state after consuming the newer SIS self-snapshot tail:

entities/koordinator/current/execution-evidence/SIS_SECE_D1D2_PUBLICFETCH_R03_A1.md

blob:
0de830e289a3a15c3994a59686694b18168fe74a

accepted_current_version:
R08_SELF_SNAPSHOT_TAIL_CONSUMED_V3

Current proven facts:

- SIS r0.8 current chat technically available = YES;
- target identity verified;
- Python 3.12.3 observed;
- exact disposable workspace created;
- bare repo.git created;
- anonymous exact commit acquisition succeeded;
- fetched commit = b32c3bdefa01c036e78a9e4d60fc2a78fd86418c;
- resolved package tree = 7807b3f5d43fe62b344f8ab6f6947aea98e33af7;
- later workspace observation = repo.git only;
- CHECKPOINT_DURABLE = NOT_CREATED;
- package materialization = NOT_PERFORMED at snapshot boundary;
- Python package workload = NOT_EXECUTED;
- R03 terminal result = NOT_CREATED;
- R03 cleanup = NOT_PERFORMED;
- R03 profile execution after replacement-preparation instruction = NOT_CONTINUED.

Current classification:
BLOCKED

blocker:
PLANNED_REPLACEMENT_PRESERVATION_PENDING_R03_NONTERMINAL

ARH may preserve these facts only as SIS current self-state/recovery evidence.

ARH MUST NOT:
- manufacture CHECKPOINT_DURABLE;
- manufacture R03 PASS/BLOCKED/FAIL;
- resume/replay R03;
- perform host cleanup;
- mutate KOO R03 current-state;
- infer workspace current existence beyond snapshot evidence.

## 8. Experience preservation

The self-snapshot contains bounded repeatable lessons with provenance.

Required minimum:
preserve them unchanged inside the externally preserved recovery package.

Optional archival extraction is allowed only if ARH fresh-verifies an already established archival learning/experience contour and its write authority.
If no exact approved destination is verified, do not invent one; report:
EXPERIENCE_PRESERVED_IN_RECOVERY_PACKAGE_ONLY.

Any extracted lesson must retain:
- source self-snapshot locator/blob;
- factual status;
- no upgrade from observed experience to approved norm;
- no secrets.

## 9. Forbidden effects

Do NOT perform:

- SIS predecessor freeze;
- SIS handoff;
- successor SIS initiation;
- successor SIS Writer Gate;
- R03 replay/resume;
- R03 host/workspace cleanup;
- simulator activation/use/deploy;
- production mutation;
- provider/OpenAI/Telegram calls;
- Project Source/canon mutation;
- KOO current-state mutation;
- SIS profile current-state rewrite;
- historical PROMPT/task replay;
- automatic next Entity activation.

No technical capability or recovery publication creates any of those authorities.

## 10. STOP conditions

STOP with exact BLOCKED/FAIL if any of the following occurs:

- ARH current-writer/continuity cannot be verified;
- KOO r1.2 writer mismatch/supersession;
- SIS r0.8 writer mismatch/supersession;
- source package commit/path/tree mismatch;
- composition != exact 5 files;
- any Git blob mismatch;
- any SHA-256 mismatch;
- manifest/checksum inconsistency;
- secrets/private credentials detected;
- external r0.6 or r0.7 lineage mismatch;
- sis-planned-r08 already exists;
- competing/newer SIS recovery successor exists;
- external publication would require overwriting predecessor data;
- external write capability/authority is unavailable;
- immutable external readback cannot be completed;
- recovery registry target conflicts;
- completion would require any forbidden effect or broader authority.

Do not repair source bytes.
Do not broaden authority.
Do not guess through a conflict.

## 11. Required terminal result

Create exactly one preservation result:

entities/archivarius/outbox/ARH__SIS-planned-replacement-r08-result__KOO-OPERATOR.md

Allowed terminal:

PASS_ARH_SIS_PLANNED_REPLACEMENT_R08_EXTERNALLY_PRESERVED

or

BLOCKED_ARH_SIS_PLANNED_REPLACEMENT_R08_PRESERVATION

or

FAIL_ARH_SIS_PLANNED_REPLACEMENT_R08_PRESERVATION

PASS requires simultaneously:

- source writer authorship verified;
- exact source package 5/5 PASS;
- exact Git blobs PASS;
- exact SHA-256 verification PASS;
- external NEW sis-planned-r08 publication PASS;
- exact external readback PASS;
- external package identity/version recorded;
- recovery registry r08 update PASS;
- stale/recoverability notes explicit;
- predecessor r0.6/r0.7 unchanged;
- forbidden effects NONE.

Result must return KOO + OPERATOR:

- exact source package locator/commit/tree;
- exact new external recovery locator;
- exact external commit;
- exact external package tree;
- all external file blobs;
- checksum/readback matrix;
- recovery registry locator/commit/blob;
- experience preservation disposition;
- stale/recoverability notes;
- exact terminal;
- explicit statement that SIS r0.8 freeze/handoff, successor initiation and Writer Gate remain NOT_PERFORMED;
- explicit statement that R03 replay/resume/cleanup remain NOT_PERFORMED.

After immutable result publication/readback:
RETURN exact result locator + commit + blob to KOO + OPERATOR.
Then STOP.

Do not initiate replacement SIS.
Do not freeze SIS r0.8.
Do not continue R03.
