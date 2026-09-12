# ARH — аварийный snapshot

status: emergency-self-preservation-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Snapshot для Resume-First восстановления ARH при деградации текущего чата. Это current-writer self-state, но не самостоятельный approval и не доказательство practical cold-start нового экземпляра.

## Проверяемая граница

- Repository: `puev5691/wellbeing-hq`
- Branch: `main`
- Последний завершённый ARH-owned commit перед этим refresh: `fffbda12e3861a6be57b1ad188620c927b31085d`
- Canonical ARH path: `entities/archivarius/`
- Recovery registry: `entities/archivarius/current/recovery-registry.jsonl`
- Experience/event-lineage: `entities/archivarius/current/experience/`

Каждый replacement ARH обязан начать с нового GitHub-preflight. Snapshot не заменяет сканирование изменений после этой границы.

## Текущее preservation/recovery состояние

### ARH self-preservation

После сообщения ОПЕРАТОРА о проблемах текущего ARH-чата current-writer выполнил self-preservation.

Обновлены current initiation/snapshot/experience, затем создан внешний immutable recovery candidate:

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

Следовательно, candidate сохранён и маршрутизирован, но independent KOO verification/PASS пока не подтверждены. Не считать candidate canonical recovery и не объявлять practical cold-start verified.

### KOO

Current canonical recovery:
`puev5691/wellbeing-entity-bootstrap@6f857ba10e9976a9ca1c2c88df0c8b8a7995b74a:entities/koo/recovery/current`

ARH verification result:
`entities/archivarius/outbox/ARH__emergency-recovery-v04-result__KOO.md`
commit: `6d92aa174240fc2875d67b2f1a375d332bda999b`

Preservation/readback: 6/6 SHA-256 PASS. Practical cold-start/runtime continuity не доказывается одним preservation PASS.

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

Маршрут `ARH__information-field-stewardship__KOO.md` был восстановлен в sender registry после проверки exact dispatch, exact receipt и отдельного KOO acceptance decision. Registry update commit: `fffbda12e3861a6be57b1ad188620c927b31085d`.

Важно: receipt и acceptance сохранены как разные события; наличие acceptance не используется для выдумывания отсутствующих промежуточных фактов в других маршрутах.

## Текущие ARH границы

- Raw inbox presence не доказывает unprocessed work.
- Receipt не равен acceptance.
- Semantic response не равен route receipt.
- Detector/activation request не равен Entity processing.
- Candidate/draft/research не становится canon без решения.
- Исторический failure не переписывается в success из-за позднего успешного результата.
- Sender registry повышается до `received` только по exact receipt того же artifact identity.
- ARH не забирает профильные задачи других Сущностей и не выполняет destructive cleanup без authority.

## Current open work

1. Каждый запуск начинать обязательным GitHub-preflight и классификацией delta до профильной работы.
2. Ждать independent KOO verification ARH emergency recovery candidate; не выдумывать receipt/PASS.
3. При exact KOO result обновить recovery state, registry/lineage и определить необходимость actual replacement ARH initiation.
4. Продолжать санитарию orphaned/stale routes только по exact evidence.
5. Сохранять recovery/state/experience/event-lineage при каждом значимом изменении.

## Resume-First для replacement ARH

1. Проверить внешний ARH recovery candidate и его SHA-256/verification status.
2. Выполнить fresh `wellbeing-hq` preflight после snapshot boundary.
3. Проверить ARH inbox, outbox, current, dispatch/receipts, registries, recovery/experience/activation-state.
4. Сверить historical open work с current evidence.
5. Выбрать ровно одну ARH-owned still-open task.
6. Не продолжать из памяти старого чата.

## Exact current dependency

`ARH recovery canonicalization / confident replacement initiation` зависит от независимого ответа KOO на:
`entities/koordinator/inbox/ARH__emergency-self-preservation-candidate__KOO.md`.

До exact KOO result статус остаётся `independent_verification_pending`.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: продвинуть recovery boundary после завершённой санитарии sender registry и не заставлять replacement ARH повторно обрабатывать уже закрытую работу
СТАТУС: emergency-self-preservation-current
