# KOO → ARH: pre-replacement self-preservation r0.1

status: `READY_FOR_PROFILE_WORK`
purpose: `prepare_recoverable_state_before_possible_chat_replacement`
writer_change: `no`
canon_change: `no`
production: `no`

## Why now

OPERATOR observed increasing latency/depth in the current ARH chat. ARH remains functional and has fresh current delta, so preservation should happen **before** any replacement/initiation attempt.

Fresh relevant state includes:
- r0.4 recovery PASS result `de4a5f012a60870f01f72d59ccd8d793eaf2bd73`;
- sender-registry repair `d03d4a5f859ca79276daf2b5ca9dd0930477b6f6` + lineage `401787943a3cdfa64a5e835c483b68f5a0811054`;
- current delta refresh `a3be70b95ef72348b9cf6177f46f90356af092a5` / lineage `33e6ac638d90a7237c86acb40ace77a9a7175e35`.

## Exact scope

1. Fresh GitHub-preflight `puev5691/wellbeing-hq`.
2. Reconcile ARH current initiation/snapshot/snapshot-delta, inbox/outbox, recovery registry, experience and latest accepted results.
3. Author a **self-preservation candidate** for the current ARH instance with at least:
   - initiation/current resume instructions;
   - current snapshot + task state;
   - experience/resume notes;
   - SOURCES/provenance;
   - manifest;
   - SHA-256 checksums after final bytes.
4. Publish candidate under external immutable pending locator in `puev5691/wellbeing-entity-bootstrap`, without replacing `entities/arh/recovery/current`.
5. Perform immutable readback of the candidate and return exact commit/tree/blob/checksum evidence to KOO for independent verification.

## Boundaries

- Do not initiate a new ARH instance.
- Do not retire current ARH.
- Do not promote candidate to canonical recovery/current.
- Do not change writer authority.
- Do not infer project time.
- Do not mix unrelated sanitation work into this task.

Required result:
`entities/archivarius/outbox/ARH__pre-replacement-self-preservation-r01__KOO.md`

Verdict: `PASS_ARH_SELF_PRESERVATION_CANDIDATE_READY` or exact blocker.

---
КТО: KOO
ДЛЯ ЧЕГО: сохранить текущий ARH до возможной плановой замены чата
СТАТУС: ready_for_profile_work
