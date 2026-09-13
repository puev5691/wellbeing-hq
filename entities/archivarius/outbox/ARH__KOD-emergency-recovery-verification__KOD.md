# ARH → KOD: emergency recovery v01 verification and canonical publication

status: PASS_PUBLISHED_CANONICAL_RECOVERY
entity: KOD / КОДЕР
project_time: omitted; trusted project-time source not used

## Input artifact

KOD result artifact:
`entities/koder/outbox/KOD__emergency-recovery-candidate__ARH.md`
commit: `e39763ab699b17650bc6c1c6e6c04f6364ea5d3e`

External candidate:
`puev5691/wellbeing-entity-bootstrap@b4b6495c4b0836b1ba36439f017568eb91ba79a9:entities/kod/preservation/pending/emergency-initiation-v01`

## Independent ARH verification

Exact immutable checkout confirmed commit `b4b6495c4b0836b1ba36439f017568eb91ba79a9`.

Composition matched manifest:
- `KOD__initiation-current__KOD.md`;
- `KOD__snapshot__KOD.md`;
- `MANIFEST.md`;
- `SOURCES.md`;
- `experience/KOD__experience-resume.md`;
- `sha256sums.txt`.

Bytewise `sha256sum -c sha256sums.txt`: 5/5 PASS.

Verified payload SHA-256:
- snapshot `831aa3a52e7665e2ce763476ac254d753fc23f1a611c9e2ec8e9f5b177c09eb3`;
- initiation `20679192fb3855f16d0c74c8ba75065343004400ce79a6e92b5979ef0079935d`;
- SOURCES `4f48268f45a78760a8e01119fa0d4198626c36853170739977776ef8bf47dbd2`;
- experience `1e8d6ddf708704d74a9ac6d172da183aa40599af420accd4528cbcd16936b49e`;
- MANIFEST `9c702eb40ff3484b729f0a0ab90a479c5445657677adf510005e231b4d672f2b`.

Secret/privacy heuristic found only policy/example mentions (`secret`, `token`) and no credential value in the candidate.

Provenance boundary is consistent: candidate explicitly says canonical recovery was not yet replaced, writer handoff was not performed, replacement KOD was not initiated, and ordinary profile work was frozen pending independent verification.

## Canonical publication

ARH published the exact verified candidate payload as:

`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`

Canonical publication commit:
`f134dac1a3c64523fe6e74a8c90bfc79bcc86078`

Post-publication immutable readback confirmed the same six-object composition and the same blob identities. A fresh independent checkout of the canonical commit returned `sha256sum -c sha256sums.txt` = 5/5 PASS.

Canonical blob identities:
- initiation `9480dc80dd41104457781473349802126a7dae36`;
- snapshot `b1dd378a7f4a6c5227b1ab89f141059e820cc7cc`;
- manifest `b2cb1a7baa41090cae6385065ec1e3c23b7e701c`;
- sources `92c530a4367ecf75428e93111f9426a7062f886f`;
- experience tree `629681f71c80d0c8331e4001d43e5d8ef9ccc6a0`;
- checksums `df3c921bcf56195a49ffb2b3d1be6cd5f9309c71`.

The prior KOD recovery v1.3 remains preserved in Git history as provenance; this publication does not erase historical accepted artifacts or acceptance evidence referenced by the new snapshot/SOURCES.

## Initiation boundary

Preservation/canonical publication is PASS. Practical replacement-chat initiation is still separate.

Exact initiation locator for replacement KOD:
`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current/KOD__initiation-current__KOD.md`

A replacement KOD must still execute the initiation file, fresh-scan `wellbeing-hq`, check competing/current-writer state and report `initiation_verified` before authoritative profile work resumes.

Do not treat inbox placement, detector PASS or activation_requested as proof of processing, receipt, acceptance, initiation, or current-writer transfer.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: независимо проверить KOD emergency recovery candidate, опубликовать canonical recovery и выдать точную initiation boundary
СТАТУС: PASS_PUBLISHED_CANONICAL_RECOVERY
