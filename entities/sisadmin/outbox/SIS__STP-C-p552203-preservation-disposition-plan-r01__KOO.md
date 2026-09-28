# SIS → KOO: STP-C p552203 preservation/disposition plan r0.1

terminal: PASS_SIS_STP_C_P552203_PRESERVATION_DISPOSITION_PLAN_R01_READY_FOR_OPERATOR_DECISION
status: READ_ONLY_PRESERVATION_DISPOSITION_PLAN_COMPLETE
scope: /data/wellbeing-lab + /opt/wb-shard-gateway only
project_time: omitted

## 0. Human result

The exact VM p552203.kvmvps was inspected read-only under the conditional preservation-first disposable designation.

No delete/move/copy/edit/create/start/stop/network/storage/backend/test action was performed.

The VM is not yet ready for destructive reset because several paths carry recovery/project/runtime significance.

However the preservation/disposition boundary is now sufficiently mapped for an OPERATOR decision.

## 1. Exact basis

Authority:

puev5691/wellbeing-hq@2e22f2eaf1107aad789fff58ff45419bda502e34:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-p552203-preservation-disposition-plan-r01__OPERATOR.md

Task:

puev5691/wellbeing-hq@9a54762e05e8cc339363c441b115808227a121fb:
entities/koordinator/outbox/KOO__STP-C-p552203-preservation-disposition-plan-r01__SIS.md

Designation:

puev5691/wellbeing-hq@020efa139071f5a73b3501d3c00d394daf75c588:
entities/koordinator/outbox/KOO__STP-C-p552203-disposable-designation-selected-r01__OPERATOR.md

Exact VM:
device 830038a0-232b-4d83-b52d-0e9973126165
hostname p552203.kvmvps

## 2. Fresh host confirmation

hostname:
p552203.kvmvps

current inspection user:
shd uid 1000

OS:
Ubuntu 24.04.1 LTS

architecture:
x86_64

persistent filesystem for both inspected roots:
/dev/sda1
ext4
mounted at /

This means the two inspected roots are not on separate storage devices from the OS.

## 3. /data/wellbeing-lab disposition

### /data/wellbeing-lab/backups/shd-pre-reinit-v01

Classification:

PRESERVE_REQUIRED

Observed contents:
- README.md
- host-state.txt
- lab-tree.txt
- lab-workfiles.tar.gz
- repo-state.txt
- sha256sums.txt

Reason:
README explicitly states this package preserves non-secret MAZHOR/lab-01 state before emergency chat replacement.

The package explicitly excludes:
- secrets;
- logs;
- tmp;
- backups;
- Git object database.

It therefore serves as recovery/provenance evidence and must survive any destructive conversion.

Its own checksum metadata is present.

### /data/wellbeing-lab/reports

Classification:

PRESERVE_REQUIRED

Observed:
- LAB01_MARKER.txt
- SHD_FAILOVER_MARKER.md
- host_inventory.txt

Reason:
LAB01_MARKER identifies lab initialization.
SHD_FAILOVER_MARKER records emergency replacement/failover boundary and explicitly points to the pre-reinit backup.
host_inventory is historical environment evidence.

These are provenance/recovery records, not disposable backend state.

### /data/wellbeing-lab/repos/wellbeing-hq

Classification:

DISCARDABLE_CANDIDATE

Fresh evidence:
- Git working tree clean;
- HEAD 22bd64b95ca817186b48bce9fa75a9a0b11ffaa1;
- local origin/main ref equals HEAD;
- ahead/behind 0/0 against local origin/main ref;
- origin points to puev5691/wellbeing-hq;
- exact commit 22bd64b95ca817186b48bce9fa75a9a0b11ffaa1 independently exists in GitHub.

Reason:
this is a clean local clone whose exact commit is externally preserved in canonical Git.

Boundary:
discardability applies to the clone as observed, not to GitHub history.

### /data/wellbeing-lab/tmp/shd-emergency-failover-v02-readback

Classification:

DISCARDABLE_CANDIDATE

Fresh evidence:
- Git working tree clean;
- HEAD ea6a84bc4eb668414cb18758b23d45823c5b5e39;
- local origin/main ref equals HEAD;
- ahead/behind 0/0;
- origin points to puev5691/wellbeing-entity-bootstrap;
- exact commit ea6a84bc4eb668414cb18758b23d45823c5b5e39 independently exists in GitHub.

Reason:
observed contents are a temporary readback clone of externally preserved repository state.

Boundary:
only this observed clone is candidate-discardable; external repository remains canonical evidence.

### /data/wellbeing-lab/artifacts

Observed:
0 files

Classification:

DISCARDABLE_CANDIDATE

No material content was observed.

### /data/wellbeing-lab/logs

Observed:
0 files

Classification:

DISCARDABLE_CANDIDATE

No material content was observed.

### /data/wellbeing-lab/scripts

Observed:
0 files

Classification:

DISCARDABLE_CANDIDATE

No material content was observed.

### /data/wellbeing-lab/secrets

Secret-bearing locator:

/data/wellbeing-lab/secrets

Observed only at locator/name level:
directory exists, mode 700, 0 files found.

Secret contents were not read.

Classification:

UNKNOWN_NEEDS_DECISION

Reason:
the path is explicitly designated secret-bearing even though currently empty.
Its future role/disposition should be decided explicitly rather than inferred from current file count.

No secret value was exposed.

## 4. /opt/wb-shard-gateway disposition

Observed exact files:
- /opt/wb-shard-gateway/INVOCATION.json
- /opt/wb-shard-gateway/audit_sink.py
- /opt/wb-shard-gateway/gateway.py
- /opt/wb-shard-gateway/harness.py

All are root-owned, mode 444.

Classification:

PRESERVE_REQUIRED

Reason:
an installed systemd unit directly references these files.

Exact unit:

/etc/systemd/system/wellbeing-shard-gateway-verify.service

Fresh status:
inactive
disabled

ExecStart references:
- /opt/wb-shard-gateway/harness.py
- /opt/wb-shard-gateway/gateway.py
- /opt/wb-shard-gateway/audit_sink.py

The unit also references external runtime locators:
- WorkingDirectory=/var/lib/wellbeing/shard-gateway
- request file=/run/wb-shard-gateway/request.json
- audit output=/var/log/wb-shard-gateway/audit.jsonl

Those external paths were NOT inspected because this task authorized inspection only of /data/wellbeing-lab and /opt/wb-shard-gateway.

INVOCATION.json was not published.
Only its field names were inspected:
- argv_template
- minimal_environment
- production
- schema
- working_directory_required

No secret-bearing value was exposed.

The current unit being inactive/disabled means no live process dependency was observed at inspection time, but installed runtime dependency still exists.

Therefore these files must be preserved or separately declared obsolete before destructive reset.

## 5. Live/runtime/project/recovery dependencies

### Live dependency

No process had cwd/executable under either inspected root at the read-only snapshot.

wellbeing-shard-gateway-verify.service was:
inactive
disabled

Therefore:
NO CURRENT LIVE PROCESS DEPENDENCY OBSERVED

This does not prove future irrelevance.

### Runtime dependency

PRESENT.

The installed systemd unit references /opt/wb-shard-gateway files directly.

### Project dependency

PRESENT.

The wellbeing-hq local repository exists under /data/wellbeing-lab/repos.

However that clone is reproducible from externally preserved Git at the exact observed commit and is classified DISCARDABLE_CANDIDATE.

### Recovery dependency

PRESENT.

Strongest recovery/provenance items:
- /data/wellbeing-lab/backups/shd-pre-reinit-v01
- /data/wellbeing-lab/reports/LAB01_MARKER.txt
- /data/wellbeing-lab/reports/SHD_FAILOVER_MARKER.md
- /data/wellbeing-lab/reports/host_inventory.txt

These must be preserved before destructive action.

## 6. What must be preserved before destructive action

Mandatory minimum:

1. entire /data/wellbeing-lab/backups/shd-pre-reinit-v01
2. entire /data/wellbeing-lab/reports
3. entire /opt/wb-shard-gateway
4. exact metadata proving:
   - source locator;
   - file list;
   - byte sizes;
   - checksums/digests;
   - ownership/mode where operationally relevant;
   - source host identity;
   - preservation destination identity;
   - exact readback result.
5. a decision record for /data/wellbeing-lab/secrets, even though currently empty.
6. a separate decision on whether the installed systemd gateway unit and its external runtime paths remain required.

The clean Git clones need not be copied merely because they exist if OPERATOR accepts their DISCARDABLE_CANDIDATE classification, because their exact commits are externally preserved.

## 7. Safe preservation destination classes

No destination is selected or written in this task.

Acceptable destination classes must be outside the destructive VM/root boundary.

### Class P1 — separate externally preserved project repository/package

Suitable for:
- non-secret recovery metadata;
- reports;
- gateway source/config if approved for project preservation.

Requirements:
- immutable version identity;
- exact checksum/readback;
- no secret contents;
- destination survives p552203 reset.

### Class P2 — separate non-public secret-capable preservation store

Required only if secret-bearing material exists or is later discovered.

Requirements:
- outside p552203 destructive boundary;
- access-controlled;
- secrets not copied into public Git/project artifacts;
- exact locator/version/readback;
- no secret value echoed into chat/logs.

### Class P3 — separate host/device/archive under OPERATOR control

Suitable for full local preservation package if separately authorized.

Requirements:
- independently identified storage;
- checksum manifest;
- exact readback;
- not mounted beneath the future destructive candidate root.

Current p552203 /dev/sda1 itself is NOT a safe preservation destination for data needed after VM reset.

## 8. Does anything still prevent making the VM truly disposable?

YES, but the blocker is now narrow.

Current blockers:

B1.
PRESERVE_REQUIRED recovery/report material has not yet been copied to a verified external destination.

B2.
PRESERVE_REQUIRED /opt/wb-shard-gateway has not yet been externally preserved or explicitly retired.

B3.
/data/wellbeing-lab/secrets disposition is not explicitly decided, despite currently containing no files.

B4.
The installed systemd gateway unit references /opt/wb-shard-gateway and external runtime paths; obsolescence/removal is not authorized or decided.

After B1-B4 are explicitly resolved and preservation exact-readback succeeds, no additional live process dependency was observed inside the two authorized roots that would by itself prevent disposable conversion.

## 9. Exact later mutation authorities required

### Authority A — PRESERVATION_COPY_R01

Needed before any copy/move/archive action.

Must specify:
- exact source paths;
- exact external destination locator/class;
- whether copy or archive is allowed;
- handling of secret-bearing paths;
- checksum/digest profile;
- immutable manifest/readback requirement;
- no deletion after copy unless separately authorized.

### Authority B — P552203_STPC_PROOF_ROOT_CREATE_R01

Needed only after preservation is complete and accepted.

Must specify:
- exact new candidate-data root locator;
- exact separate evidence/corpus root locator;
- ownership/mode;
- storage/filesystem boundary;
- proof that neither contains live/project data;
- whether directory-level isolation is sufficient for first tranche only.

### Authority C — P552203_STPC_CLEANUP_RESET_R01

Needed after preservation/readback and dependency retirement are accepted.

Must specify exact allowed destructive scope:
- delete selected old lab paths;
- remove/retire gateway files/unit if approved;
- reset/reimage whole VM if approved;
- post-reset identity verification;
- proof no preservation destination is inside destruction scope.

These are separate authorities.
Preservation authority does not imply cleanup/reset authority.

## 10. Classification table

| Locator | Classification | Reason |
|---|---|---|
| /data/wellbeing-lab/backups/shd-pre-reinit-v01 | PRESERVE_REQUIRED | explicit emergency replacement/recovery preservation package |
| /data/wellbeing-lab/reports | PRESERVE_REQUIRED | lab/failover/host provenance |
| /data/wellbeing-lab/repos/wellbeing-hq | DISCARDABLE_CANDIDATE | clean clone; exact HEAD externally present in GitHub |
| /data/wellbeing-lab/tmp/shd-emergency-failover-v02-readback | DISCARDABLE_CANDIDATE | clean readback clone; exact HEAD externally present |
| /data/wellbeing-lab/artifacts | DISCARDABLE_CANDIDATE | empty |
| /data/wellbeing-lab/logs | DISCARDABLE_CANDIDATE | empty |
| /data/wellbeing-lab/scripts | DISCARDABLE_CANDIDATE | empty |
| /data/wellbeing-lab/secrets | UNKNOWN_NEEDS_DECISION | secret-bearing locator; currently empty; no content inspected |
| /opt/wb-shard-gateway | PRESERVE_REQUIRED | installed systemd unit references exact files |

## 11. Boundary preservation

Performed:
read-only metadata/inventory only.

Not performed:
- delete
- move
- copy
- edit
- secret content read/reveal
- directory creation
- proof-root creation
- service start/stop
- network/storage mutation
- backend install/run
- T01-T20 execution
- live WRITE/CAS
- CHECKPOINT_DURABLE

## EXPERIENCE

Идея → отделить реально уникальные/recovery-significant данные от воспроизводимых локальных копий.

Проба → проверить filesystem metadata, Git cleanliness/external commit preservation, service references and recovery markers without touching contents outside exact scope.

Результат → обязательный preservation set теперь узкий и проверяемый; Git clones можно считать discardable candidates, а recovery reports/backup и gateway files требуют отдельного preservation/retirement decision.

Успех → OPERATOR может принять точное preservation/disposition решение до любой destructive mutation.

Урок → сервер становится disposable не тогда, когда на нём мало процессов, а когда всё невоспроизводимое уже вынесено за его пределы и проверено.

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
