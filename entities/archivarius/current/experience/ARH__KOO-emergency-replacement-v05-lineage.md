# ARH experience: KOO emergency replacement v05 lineage

status: `PRESERVATION_COMPLETE_REPLACEMENT_COLD_START_PENDING`
project_time: omitted; trusted project-time source not used

## Идея

При деградации current-writer сначала использовать его собственный final self-snapshot/freeze, если он успел их опубликовать, а не реконструировать coordinator state из внешних фрагментов.

## Проба

KOO успел создать emergency self-snapshot v05, handoff freeze и exact ARH preservation task до фактической остановки normal profile work.

ARH проверил candidate composition, published-byte checksums, active-source identities, snapshot boundary, post-freeze writer evidence and secret boundary.

## Результат

Candidate `4fd0f198...` прошёл проверку.

Canonical recovery v05 опубликован атомарно:
`puev5691/wellbeing-entity-bootstrap@47eea7599619c98a2d590f38b6a7a608d4af97c8:entities/koo/recovery/current`.

Immutable readback: 7/7 exact composition PASS; checksum-covered payload: 6/6 PASS.

Old v04 canonical composition remains immutable historical provenance at `6f857ba...`.

## Успех

Atomic tree publication prevented the v05 canonical path from temporarily or finally containing a mixed v04/v05 composition. In particular, old v04 launcher and `experience/` subtree were removed from current composition while remaining in Git history.

## Ограничение

ARH did not establish replacement KOO writer-state. Replacement initiation/current-writer handoff remains a separate cold-start action under explicit OPERATOR authority.

## Урок

Recovery publication must replace the declared composition as one coherent immutable version when the previous canonical directory contains extra historical payload. Sequential overlay is unsafe because it can reproduce the same manifest/composition mismatch previously observed in SIS recovery.

Freeze + verified self-snapshot + atomic canonical publication creates a clean writer-gap: old writer cannot mutate normal current-state, while the new instance must independently pass recovery and Writer Gate before profile work.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить reusable experience аварийной замены KOO v05
СТАТУС: preservation_complete_replacement_cold_start_pending
