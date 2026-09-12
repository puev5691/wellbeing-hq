# KOO emergency handoff v04

status: CURRENT_WRITER_HANDOFF_FREEZE
candidate_repository: `puev5691/wellbeing-entity-bootstrap`
candidate_path: `entities/koo/preservation/pending/emergency-initiation-v04`
candidate_ref: `99ebd990537d3b0405ff0bfcd20fdac91621b077`

Preservation task:
`entities/koordinator/outbox/KOO__emergency-recovery-v04__ARH.md`
commit: `bdff93c20d4d07106123620b8325646cba22d232`

ARH inbox:
`entities/archivarius/inbox/KOO__emergency-recovery-v04__ARH.md`
commit: `7f0323802c839814c508d6c3fdc0abc5daa87087`

Dispatch:
`routes/dispatch/KOO__emergency-recovery-v04__ARH.md`
commit: `0e1626b19a59784b948749bcd647e98140a0f8ca`

## Freeze boundary

The current KOO instance has completed its authoritative self-snapshot, external candidate publication, readback/checksum verification and addressed preservation dispatch.

After this marker, this old instance must not perform normal profile/current-state mutations.

Allowed further actions are limited to:
- verifying ARH preservation result;
- clarifying the exact handoff if ARH returns a blocker;
- reporting the emergency-initiation status to OPERATOR.

The replacement KOO must not assume current-writer authority until recovery verification and handoff conditions are satisfied.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: прекратить дальнейшие profile-mutations старого экземпляра после emergency handoff
СТАТУС: current_writer_handoff_freeze
