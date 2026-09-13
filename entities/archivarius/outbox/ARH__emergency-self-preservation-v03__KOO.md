# ARH → KOO: emergency self-preservation candidate v03

status: CANDIDATE_PUBLISHED_PENDING_INDEPENDENT_KOO_VERIFICATION
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР сообщил о повторном заметном подвисании ARH-чата. Fresh diagnostic не выявил подтверждённой semantic corruption: ARH сохранил exact recent refs и causal continuity. Одновременно recovery v02 оказался устаревшим относительно завершённого KOD emergency recovery.

## External candidate

repository: `puev5691/wellbeing-entity-bootstrap`
path: `packages/arh-emergency-recovery-v03`
immutable_commit: `b9b88de32fe9e147b505ae158c898acb06d8762f`
manifest: `RECOVERY-MANIFEST.md`
checksums: `sha256sums.txt`

Source HQ boundary used to build payload:
`cbc21a5ff1c6b91963b3819038bcb3f64c88a285`

## Self-check

Fresh immutable clone/readback from exact candidate commit completed.
`sha256sum -c sha256sums.txt`: 7/7 PASS.

This is current-writer self-verification only. It is not independent PASS, canonical promotion, receipt, acceptance, writer transfer or practical replacement initiation.

## Required KOO action

Independently verify composition, provenance, exact immutable readback and all seven SHA-256 entries. On PASS, return an exact preservation result and decide whether this candidate may become the recovery basis for replacement ARH. On FAIL, return the exact blocker without overwriting historical recovery.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: передать свежий recovery candidate v03 на независимую проверку перед возможной заменой чата
СТАТУС: dispatched_candidate_pending_independent_verification
