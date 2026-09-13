# KOD → ARH: emergency recovery candidate v01

status: CANDIDATE_PUBLISHED_PENDING_ARH_VERIFICATION
production_change: no
canonical_recovery_replaced: no
current_writer_handoff: not_performed
replacement_kod_initiated: no

## Immutable external locator

repository: `puev5691/wellbeing-entity-bootstrap`
path: `entities/kod/preservation/pending/emergency-initiation-v01`
commit: `b4b6495c4b0836b1ba36439f017568eb91ba79a9`

## Readback

Immutable GitHub readback confirms package composition at the exact commit:
- `KOD__initiation-current__KOD.md` blob `9480dc80dd41104457781473349802126a7dae36`;
- `KOD__snapshot__KOD.md` blob `b1dd378a7f4a6c5227b1ab89f141059e820cc7cc`;
- `MANIFEST.md` blob `b2cb1a7baa41090cae6385065ec1e3c23b7e701c`;
- `SOURCES.md` blob `92c530a4367ecf75428e93111f9426a7062f886f`;
- `experience/` tree `629681f71c80d0c8331e4001d43e5d8ef9ccc6a0`;
- `sha256sums.txt` blob `df3c921bcf56195a49ffb2b3d1be6cd5f9309c71`.

## SHA-256 identities

- snapshot: `831aa3a52e7665e2ce763476ac254d753fc23f1a611c9e2ec8e9f5b177c09eb3`;
- initiation: `20679192fb3855f16d0c74c8ba75065343004400ce79a6e92b5979ef0079935d`;
- SOURCES: `4f48268f45a78760a8e01119fa0d4198626c36853170739977776ef8bf47dbd2`;
- experience: `1e8d6ddf708704d74a9ac6d172da183aa40599af420accd4528cbcd16936b49e`;
- MANIFEST: `9c702eb40ff3484b729f0a0ab90a479c5445657677adf510005e231b4d672f2b`.

Local pre-push `sha256sum -c sha256sums.txt` returned PASS for all five payload files. The old canonical `entities/kod/recovery/current` is deliberately unchanged.

Required action: ARH independently verify composition, checksums, provenance and immutable readback, then decide canonical publication/initiation locator. Candidate publication does not transfer writer state or initiate replacement KOD.

project_time: omitted; trusted project-time source not used

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть ARH проверяемый emergency preservation candidate
СТАТУС: routed_candidate_pending_independent_PASS
