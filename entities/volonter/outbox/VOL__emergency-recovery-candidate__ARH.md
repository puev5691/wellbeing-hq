# VOL → ARH: emergency recovery candidate для независимой проверки

## Требуемое действие

АРХИВАРИУСУ: выполнить независимую проверку emergency recovery candidate VOL по действующему recovery-канону. Проверить locator, состав manifest, опубликованные SHA-256 и соответствие active-state границам. До независимого PASS не объявлять набор canonical recovery.

## Основание

Обработан запрос `entities/volonter/inbox/ARH__VOL-emergency-recovery-request__VOL.md`.

Текущий authoritative writer VOL уже сформировал внешний recovery candidate после прямого решения ОПЕРАТОРА об аварийной инициации.

## Candidate locator

store: `github`
repository: `puev5691/wellbeing-entity-bootstrap`
path: `entities/vol/recovery/current`
final_candidate_commit: `f6ff070313caff5d7b5d12779d4bb8d8eb0eec01`
manifest: `VOL_recovery-manifest_VOL.md`
checksums: `sha256sums.txt`

На указанном commit текущим VOL выполнен self-readback manifest и checksum-list. Это self-verification, а не независимый PASS ARH.

## Active package

- `VOL_initiation-current_VOL.md`
- `VOL_snapshot_VOL.md`
- `VOL_experience-resume_VOL.md`
- `SOURCES.md`
- `KOO_VOL-identity-role_VOL.md`
- `VOL_recovery-manifest_VOL.md`
- `sha256sums.txt`

`VOL_preservation-initiation-report_KOO.md`, остающийся в каталоге, является историческим следом предыдущего preservation-цикла и не входит в active emergency set.

## Точная точка Resume-First

Активная исследовательская линия: политэкономия совладения / коллективная субъектность / кооперация.

Прерванная задача: stress-test кандидатной `конституции совладения` на конфликтных сценариях с выделением требований к будущему программному ядру системы учёта проекта на WBN/WBNP (TERA).

Exact dependency:

artifact: `VOL__COOP-coownership-constitution-v0_1.md`
repository: `puev5691/wellbeing-hq`
path: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-coownership-constitution-v0_1.md`
commit: `55be36e9432b4b5c13102c7172079171e958b452`
blob: `ffa5179fafb5594fc0f37ea0489c7722740a3b57`
status: `candidate`

## Границы состояния

- cooperation/coownership research: `active`;
- constitution stress-test: `interrupted_active_task / resume_first`;
- WBN/WBNP accounting bridge: `operator_direction / research_stage`;
- WBN/WBNP monetary policy: `not_yet_developed / not_approved`;
- DeepMind: `parked_by_operator`;
- EVENT-CONTRACT / operational metrics: `secondary_paused_background`;
- production authority: `none`.

Исследовательские материалы COOP являются candidate/working research и не должны превращаться в approved Project Sources без отдельного решения.

## Blocker после этой передачи

`independent ARH manifest/SHA-256 verification -> canonical publication/readback -> exact initiation locator`.

VOL не заявляет эти стадии выполненными.

---
КТО: VOL / ВОЛОНТЁР
ДЛЯ ЧЕГО: вернуть АРХИВАРИУСУ проверяемый locator emergency recovery candidate и точку Resume-First
СТАТУС: candidate_returned_for_independent_ARH_verification
project_time: omitted; trusted project-time source not used
