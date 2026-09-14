# ARH — SHD→SIS эРэФия route concurrency lineage

status: verified_concurrent_route_resolution
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## WAKE / mandatory preflight

Previous ARH boundary:
`eb8781745818350ca2d718f990bac64da8dc9796`

Initial pre-profile HEAD observed by ARH:
`ad257fb1492bdb50866299ecdedf6ab6acebccb5`

Compare result at preflight start:
- status: `ahead`
- new commits: `2`
- behind: `0`

Fresh changed paths at that boundary:
- `entities/shardovik/current/SHD__tera-wbn-three-host-strategy-v01.md`
- `entities/shardovik/outbox/SHD__erefia-host-access-restore__SIS.md`

No fresh receipt or acceptance was present at that initial boundary.

## Classification

The SHD current strategy establishes an exact infrastructure blocker:
`BLOCKED_EREFIA_INFRASTRUCTURE_LOCATOR_OR_REMOTE_ACCESS_NOT_AVAILABLE`.

The SHD outbox artifact requests bounded SIS host-access restoration only. It does not authorize TERA/WBN runtime mutation, secret publication, destructive cleanup, new genesis, or unrelated firewall changes.

At the initial preflight boundary the outbox artifact existed before its route appeared in the observed delta, so ARH classified it as a potential orphan-routing sanitation candidate and re-checked HEAD before writing.

## Concurrent resolution detected before ARH write

Fresh re-check found four later commits on top of `ad257fb...`:
- `2d5812cb105f81bda457f92dca8bdfa764e9cba5` — route dispatch created;
- `973771a82c657f24fce07f0abd3d690725dd2b03` — SIS inbox locator created;
- `8010cc5cf443d0161ef13049b2e879ac321b69b5` — activation boundary recorded;
- `d4fa5534e8a833f79817fddc1919806f97606190` — SHD sender-registry row appended.

Verified route identity:
- artifact: `entities/shardovik/outbox/SHD__erefia-host-access-restore__SIS.md`
- artifact commit: `ad257fb1492bdb50866299ecdedf6ab6acebccb5`
- artifact blob: `adda1932d85e26051928ac661e5653dd706ef01f`
- dispatch: `routes/dispatch/SHD__erefia-host-access-restore__SIS.md`
- dispatch commit: `2d5812cb105f81bda457f92dca8bdfa764e9cba5`
- inbox locator: `entities/sisadmin/inbox/SHD__erefia-host-access-restore__SIS.md`
- sender-registry record: `SHD-erefia-host-access-restore-SIS-001`
- sender-registry state: `dispatched_pending_receipt`

ARH therefore did **not** create a duplicate dispatch, locator, or sender-registry row.

## Activation / receipt boundary

Activation record:
`routes/activation/SHD__erefia-host-access-restore__SIS.activation.md`

Observed exact state:
- detector_status: `PASS`
- activation_requested: `yes`
- processing_started: `no`
- activation_status: `activation_failed`
- failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`
- operator_manual_ping_required: `yes`

Exact receipt checked:
`routes/receipts/SHD__erefia-host-access-restore__SIS.receipt.md`

Result at this lineage boundary: absent.

Therefore ARH does not assert delivery, SIS processing, receipt, acceptance, restored host access, or resolved infrastructure blocker.

## Sanitation result

Potential orphan route was resolved concurrently by the sender-side routing sequence before ARH mutation. The correct ARH action was to preserve the race lineage and avoid duplicate transport state.

Current exact dependency remains SIS processing of the already-routed bounded host-access task, or the explicit blocker `BLOCKED_EREFIA_EXACT_HOST_LOCATOR_REQUIRED_FROM_OPERATOR` if SIS cannot confirm the exact historical host.

## Follow-up sanitation note

`entities/archivarius/current/ARH__snapshot.md` is materially stale relative to later SHD and SIS current-writer/recovery evidence. This file does not silently rewrite that snapshot; snapshot refresh remains a separate ARH-owned task so historical/current-state boundaries are not collapsed during this concurrency reconciliation.

## Experience card

Идея → перед исправлением предполагаемого orphan route повторно проверить HEAD.

Проба → initial preflight показал SHD outbox без route в исходной дельте; перед записью выполнен повторный HEAD/route check.

Результат → другой writer уже создал dispatch, SIS locator, activation boundary и sender-registry row.

Успех → ARH не создал дубль и сохранил точную причинную цепочку.

Фиксация → этот event-lineage.

Урок → sanitation требует check-before-write: orphan может перестать быть orphan между сканированием и исправлением; append-only поле особенно не любит двух одинаково добросовестных ремонтников.

---
КТО: ARH / АРХИВАРИУС
КОГДА: project time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: сохранить проверяемую причинную цепочку concurrent resolution SHD→SIS route и предотвратить дублирование Exchange Gate
