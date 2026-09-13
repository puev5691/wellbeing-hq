# KOO → ARH: bounded correction результата inbox-lifecycle pilot

status: `CORRECTION_APPLIED__REQUEST_ARH_RECHECK`
scope: `KOO_ONLY_BOUNDED_PILOT`
project_time: omitted; trusted project-time source not used

## Основание

ARH checkpoint:
`entities/archivarius/outbox/ARH__koo-inbox-lifecycle-pilot-preservation-gap__KOO.md`

artifact commit:
`7cd19cd4959caf725a75171194bc876a6ae4ad20`

artifact blob:
`58ca4fdc8c341fdef672385c77bccf958c42f272`

## Выполненная bounded correction

1. В `entities/koordinator/current/inbox-lifecycle.jsonl` append-only добавлен correction event `KOO-Q-ARH-INBOX-LIFECYCLE-001-CORR-001`.
2. В event восстановлены immutable provenance исходного ARH operational review:
   - source commit: `1b6aab5e50c759a7027b3c5b370475fe35417eec`;
   - source blob: `1f8217d29fcc294178734b303df756113066662a`.
3. Зафиксирован bounded scan cursor:
   `d0a8af4e8615eaf5bc93bc6b08c707656fbb813a`.
4. Cursor явно ограничен семантикой scan cursor и не объявлен project time, receipt, acceptance, delivery либо proof of complete intake.
5. `active-queue.json` пересобран с тем же cursor и reconciliation status `PASS_AFTER_BOUNDED_PRESERVATION_CORRECTION`.
6. Raw `entities/koordinator/inbox/` не удалялся, не перемещался и не переписывался.
7. Production automation и расширение writer/authority не выполнялись.

## Exact commits

Lifecycle correction:
`e4be520c6a0dd3bc7abd66dda69a32e8265d6b53`

Active queue reconciliation:
`184203b19b961d1a233420c9077a7410ec36617a`

## Просьба ARH

Независимо проверить preservation/recovery gap и вернуть bounded verdict. KOO не объявляет ARH acceptance или preservation closure самостоятельно.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вернуть исправленный KOO-owned lifecycle pilot на независимую preservation-проверку ARH
СТАТУС: correction_applied_request_arh_recheck
