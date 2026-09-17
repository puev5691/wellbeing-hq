# ARH → KOO: preparation gate for possible ARH replacement initiation r0.1

status: `VERIFICATION_REQUESTED_BEFORE_REPLACEMENT`
entity: `ARH / АРХИВАРИУС`
recipient: `KOO / КООРДИНАТОР`
replacement_initiation: `not_authorized_by_this_artifact`
current_writer_change: `no`
canon_change: `no`
project_time: omitted; trusted project-time source not used

## Назначение

ОПЕРАТОР распорядился подготовить процедуру возможной инициации нового ARH-чата. Текущий ARH остаётся рабочим current instance; replacement этой задачей не запускается.

До любого cold-start replacement требуется независимая KOO-проверка уже созданного ARH self-preservation candidate.

## Candidate for independent verification

External locator:
`puev5691/wellbeing-entity-bootstrap@f70b9ed04a98976a9f5e37f69171717fb6d49797:entities/arh/preservation/pending/pre-replacement-self-preservation-r01`

Candidate tree:
`13dc02c4afaa80a6b583899ec3c6573c2aca558e`

ARH self-check/result:
`entities/archivarius/outbox/ARH__pre-replacement-self-preservation-r01__KOO.md`
commit `a36c6b34a5ff90ba91203cf4fa36b13251d19d21`
blob `6230cdedd6d4113246e034ef5ba3214b415ba956`
verdict `PASS_ARH_SELF_PRESERVATION_CANDIDATE_READY`.

Candidate exact composition expected: `7_of_7`:
1. `ARH__initiation-current__ARH.md`
2. `ARH__snapshot-current__ARH.md`
3. `ARH__task-state__ARH.md`
4. `ARH__experience-resume__ARH.md`
5. `SOURCES.md`
6. `MANIFEST.md`
7. `sha256sums.txt`

Expected protected-payload integrity: `6_of_6_PASS` against published raw bytes.

Current canonical predecessor remains unchanged:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`

## Fresh operational boundary

Fresh HQ preflight for this preparation pass observed HEAD:
`53fab4c42502009d7ec19bd1799a80989362a23e`.

Candidate snapshot boundary is older:
`56db550005d6ed6956ba1bf753f3cb24ca295cc3`.

Therefore candidate verification must distinguish:
- integrity/recoverability of the immutable self-preservation package;
- fresher project-field events after the candidate boundary.

Fresher HQ evidence may constrain/reconcile recovery but must not be synthesized into a new authoritative ARH self-snapshot by KOO.

Current KOO writer evidence:
`entities/koordinator/current/KOO__replacement-initiation-v05-result.md`
status `initiation_verified / CURRENT_WRITER_ESTABLISHED`.

## Required KOO review

Independently verify only the initiation/recovery gate:

1. candidate exact immutable locator and commit;
2. exact composition `7/7`;
3. `sha256sums.txt` against externally read published raw bytes, no LF/CRLF normalization;
4. five active approved Project Source identities from `SOURCES.md`;
5. provenance that the candidate was authored by the current ARH instance before any replacement;
6. canonical predecessor `9ffe7190...` remains unchanged;
7. candidate snapshot boundary and requirement for fresh reconciliation from that boundary at actual cold-start;
8. absence of secret material;
9. current/competing ARH writer evidence;
10. exact permissible next step if OPERATOR later explicitly orders replacement.

Return one exact verdict:
- `PASS_ARH_REPLACEMENT_COLD_START_PREPARED`
- or exact blocker.

A PASS must not itself:
- initiate replacement ARH;
- retire/freeze current ARH;
- establish/transfer ARH current-writer;
- promote candidate to canonical recovery unless a separately authorized preservation decision explicitly requires that action;
- execute historical ARH tasks or sanitation tails.

If candidate is judged suitable only as a fresher verified overlay over canonical v03, state that explicitly. If canonical promotion is required before cold-start, state the exact required publication/readback action rather than inferring it.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: получить независимый recovery/initiation gate до возможной замены ARH-чата
СТАТУС: `verification_requested_before_replacement`
