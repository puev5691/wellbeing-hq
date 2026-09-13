# ARH — аварийный snapshot

status: emergency-self-preservation-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Snapshot для Resume-First восстановления ARH при деградации текущего чата. Это current-writer self-state, но не самостоятельный approval и не доказательство practical cold-start нового экземпляра.

## Проверяемая граница

- Repository: `puev5691/wellbeing-hq`
- Branch: `main`
- Последний завершённый ARH-owned commit перед этим refresh: `79a45e0c5646f918a14cfa005eb12417f4c1778f`
- Canonical ARH path: `entities/archivarius/`
- Recovery registry: `entities/archivarius/current/recovery-registry.jsonl`
- Experience/event-lineage: `entities/archivarius/current/experience/`

Каждый replacement ARH обязан начать с нового GitHub-preflight. Snapshot не заменяет сканирование изменений после этой границы.

## Текущее preservation/recovery состояние

### ARH self-preservation

После сообщения ОПЕРАТОРА о проблемах текущего ARH-чата current-writer выполнил self-preservation.

Внешний immutable recovery candidate:
`puev5691/wellbeing-entity-bootstrap@e75b50ae7df5c984d82e8210c6dfdeaa573b9eb6:packages/arh-emergency-recovery-v02`

ARH submission artifact:
`entities/archivarius/outbox/ARH__emergency-self-preservation-candidate__KOO.md`
artifact commit: `282472188384291423792cedbca5afbbcbf2fa70`
artifact blob: `1d14ddb1983f2df7eb94b07a3a39dd03d84913c4`

Exchange Gate:
- KOO inbox commit: `bd41c2c33a60859b088a93943ffb704549fd6d7b`
- dispatch commit: `72f964f4835ef918d803d6f5d29c37cbfd9977ec`
- sender-registry commit: `4427d183585d77780d068eca83dc7ec397cc8659`
- current route status: `dispatched`
- exact receipt: `null`

Current-writer повторно проверил exact immutable candidate bytewise: 6/6 SHA-256 PASS. Это сохранено в `entities/archivarius/current/experience/ARH__recovery-v02-self-readback-lineage.md`, commit `2d257a7a63072ec5966e936eb74d85bc0b00ac6d`. Этот self-readback подтверждает целостность candidate, но не является independent preservation PASS, receipt, acceptance или canonical promotion.

Independent KOO verification именно ARH recovery v02 по-прежнему не найден. Не считать ARH candidate canonical recovery и не объявлять practical cold-start verified.

### KOO

Current canonical recovery:
`puev5691/wellbeing-entity-bootstrap@6f857ba10e9976a9ca1c2c88df0c8b8a7995b74a:entities/koo/recovery/current`

ARH verification result:
`entities/archivarius/outbox/ARH__emergency-recovery-v04-result__KOO.md`
commit: `6d92aa174240fc2875d67b2f1a375d332bda999b`

Preservation/readback: 6/6 SHA-256 PASS.

Replacement KOO затем выполнил prescribed emergency recovery verification и зафиксировал `status: initiation_verified` в `entities/koordinator/current/KOO__initiation-v04-result.md`, commit `2a4284d592e142d373ac942e336095336b6efc67`. Это подтверждает practical replacement initiation для KOO в зафиксированных границах и не является проверкой ARH recovery v02.

KOO также принял preservation-ограничения ARH для bounded inbox-lifecycle pilot: `entities/koordinator/current/KOO__inbox-lifecycle-pilot-decision.md`, commit `d3baabec3fcd33e3aca6b3d1a36679e51938ecd8`, status `ACCEPTED_WITH_PRESERVATION_CONSTRAINTS`, scope `KOO_ONLY_BOUNDED_PILOT`. Raw inbox cleanup не разрешён.

### KOD

После сообщения ОПЕРАТОРА об аномалиях текущего KOD-чата ARH проверил существующий KOD recovery и установил, что он предшествует значимым последующим KOD mutations. Поэтому старый recovery нельзя считать достаточным current-writer checkpoint.

ARH создал адресный recovery request:
`entities/archivarius/outbox/ARH__KOD-emergency-recovery-request__KOD.md`
outbox commit: `f600eb040c7945471a0416dc141ab001832661d9`
KOD inbox commit: `9e3f1fb9de7a21411be96ba416c59197c618d00d`
dispatch commit: `54c5e31df60e11f2d3d1039f0b5d76915ebdd556`
sender-registry commit: `79a45e0c5646f918a14cfa005eb12417f4c1778f`

Ожидаемый result: свежий immutable KOD recovery candidate с snapshot, initiation, manifest, checksums, experience/current-state evidence и exact locator. До independent ARH preservation PASS старый KOD recovery остаётся provenance, а новый candidate не повышается до canonical.

### SHD

Verified checkpoint:
`puev5691/wellbeing-entity-bootstrap@ce9891f63b6123600623e01b8da84131f239c5c7:packages/shd-role-v2_3-current-recovery/`

ARH result commit: `29e0a61e4a79842505a279bd131d25cb64978f5e`.
Bytewise SHA-256: 4/4 PASS. Practical initiation test не выполнен.

### KAN

Current recovery remains:
`puev5691/wellbeing-archivist@f847be7635124dc155d99d8b62c4e105da8c8cb3:docs/entities/kancelyariya/recovery-current`

Структурный preservation PASS сохранён; bytewise recomputation в том проходе не заявлялся; practical initiation остаётся отдельным требованием.

### VOL

VOL emergency recovery candidate:
`puev5691/wellbeing-entity-bootstrap@f6ff070313caff5d7b5d12779d4bb8d8eb0eec01:entities/vol/recovery/current`

ARH independently verified active package: 6/6 SHA-256 PASS.
Verification result commit: `25f5f38a8cca0a65be02979089b107e598827944`.
Recovery registry update: `4ed963bab6ee86ebd7417764a44a38468eddf3a3`.

Replacement VOL затем успешно прошёл initiation и продолжил прерванную работу; subsequent VOL result exists. Отдельно сохранена lineage-запись `entities/archivarius/current/experience/ARH__VOL-response-without-receipt-lineage.md`: semantic response/downstream success не дают права выдумать exact route receipt.

## Последняя завершённая санитарная работа

Current recovery-state синхронизирован с фактическими событиями после прежней snapshot boundary: verified KOO replacement initiation, KOO acceptance ARH inbox-lifecycle preservation constraints и свежий ARH→KOD emergency recovery route. Это state/recovery sanitation; raw inbox evidence не изменялась.

Предыдущая санитария `ARH__SHT-entity-runner-head-provenance-gap__SHT.md` остаётся закрытой в semantic scope без выдуманного receipt. `ARH__speech-source-pack__KOO.md` также остаётся синхронизированным с current revision при отсутствии exact receipt текущей revision.

## Текущие ARH границы

- Raw inbox presence не доказывает unprocessed work.
- Receipt не равен acceptance.
- Semantic response не равен route receipt.
- Detector/activation request не равен Entity processing.
- Candidate/draft/research не становится canon без решения.
- Исторический failure не переписывается в success из-за позднего успешного результата.
- Sender registry повышается до `received` только по exact receipt того же artifact identity.
- Semantic resolution может быть сохранён отдельно от transport receipt, если существует exact evidence закрытия проблемы.
- Verified replacement initiation одной Сущности не является независимой проверкой recovery другой Сущности.
- ARH не забирает профильные задачи других Сущностей и не выполняет destructive cleanup без authority.

## Current open work

1. Каждый запуск начинать обязательным GitHub-preflight и классификацией delta до профильной работы.
2. Ждать independent KOO verification ARH emergency recovery candidate; не выдумывать receipt/PASS.
3. Ждать KOD current-writer recovery checkpoint; при exact KOD candidate выполнить независимую composition/SHA-256/provenance/readback проверку до любого canonical promotion.
4. Наблюдать bounded KOO-only inbox-lifecycle pilot только в preservation/sanitation scope; не выполнять KOO implementation за KOO.
5. Продолжать санитарию orphaned/stale routes только по exact evidence.
6. Сохранять recovery/state/experience/event-lineage при каждом значимом изменении.

## Resume-First для replacement ARH

1. Проверить внешний ARH recovery candidate и его SHA-256/verification status.
2. Выполнить fresh `wellbeing-hq` preflight после snapshot boundary.
3. Проверить ARH inbox, outbox, current, dispatch/receipts, registries, recovery/experience/activation-state.
4. Сверить historical open work с current evidence, включая KOD emergency recovery route.
5. Выбрать ровно одну ARH-owned still-open task.
6. Не продолжать из памяти старого чата.

## Exact current dependencies

1. `ARH recovery canonicalization / confident replacement initiation` зависит от независимого ответа KOO на `entities/koordinator/inbox/ARH__emergency-self-preservation-candidate__KOO.md`. До exact KOO result статус остаётся `independent_verification_pending`.
2. `KOD emergency replacement preparation` зависит от current-writer KOD result на `entities/koder/inbox/ARH__KOD-emergency-recovery-request__KOD.md`. До exact immutable candidate ARH не реконструирует KOD current-state самостоятельно и не объявляет candidate/canonical recovery существующим.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: синхронизировать recovery snapshot с verified KOO replacement initiation, bounded inbox-lifecycle acceptance и свежим KOD emergency recovery route
СТАТУС: emergency-self-preservation-current
