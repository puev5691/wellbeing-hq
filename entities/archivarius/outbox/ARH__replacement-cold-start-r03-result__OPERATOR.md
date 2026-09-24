# ARH replacement cold-start r0.3 — initiation result

status: initiation_verified_waiting_writer_gate
entity: ARH / АРХИВАРИУС
project_time: omitted

## Человеческий смысл

Новый физический экземпляр ARH успешно прошёл cold-start по внешнему immutable recovery без реконструкции отсутствующего состояния из памяти чатов.

Инициация подтверждена. Writer Gate не выполнялся. Профильная работа не начиналась.

KOO recovery v0.8 подтверждён как уже завершённый и не возобновляется.

## Current approved Project Sources

Проверен активный набор:
- project-instructions-core v2.5 — SHA-256 f2ad19e243e55c552b10372c4bd7ddda7f18018579527f94d69e14858303b49c
- entity-roles-short v2.4 — SHA-256 d7feae524f6d1a34b0fd2a63475435e41ebe48097a191d87ca0ceeb797421530
- file-work-canon-universal v2.4 — SHA-256 c7e09bb358afd9ff131158044ce3722375ab30580e240909e85afdf38ca1e08b
- source-loading-policy v2.2 — SHA-256 2a410e929c8cf4daa21f9229ad300e92abbaf4ab40b4fbf3a03950cc663e719e
- entity-state-preservation-and-recovery-canon v1.6 — SHA-256 82e3117570a9ecd73be2dae1279ebb3e0a2d6125556de98d5c1ede14a9236ae5
- task-conveyor-canon v1.2 — SHA-256 913e88c1e4d17a07122ad9cdf680abae28fc2def0ea0740df9ce925fec22d0e7

Latest source-set evidence:
- PASS_KOO_SOURCE_SET_R07_ACTIVATED for project core v2.5;
- source-set r0.6 confirms the other five active sources, including recovery v1.6 and task-conveyor v1.2.

The stale internal service-card fields inside recovery v1.6 are overridden for source-set status by later verified activation evidence; the exact bytes match the activated source identity.

## Fresh HQ preflight

Repository: puev5691/wellbeing-hq
branch: main
fresh HEAD before result publication:
61eea761b192b8617af6087c1c551ae54edef455

That HEAD is exactly the ARH self-recovery preservation terminal commit, so no later HQ evidence exists after the preserved recovery boundary at initiation time.

## Exact immutable ARH recovery

Locator:
puev5691/wellbeing-entity-bootstrap@3a1945ac0e954a419ac9156d14776ecdaadbe91e:entities/arh/recovery/versions/arh-recovery-r03

Composition/readback: 7/7 PASS

Git blobs:
- ARH__writer-r01-exact.md — 3d17b16c02e84e841d1266e3b0fcc083640b77d6
- ARH__initiation-current-exact.md — 67bcac3eaa0a5f2835dce8ae7af515d11975a6fe
- ARH__snapshot-base-exact.md — 8223ea771012d1cf0cc654047e51e87787879bbe
- ARH__snapshot-delta-exact.md — 318215735df0db2e516aad9c3c7f0345ab67779d
- ARH__current-frontier-r03.md — 3d68db9045b0fd894666fd14cbe81c5e8eddfa14
- ARH__replacement-initiation-r03.md — 8c84db11a02f6542dd8f36cb9a934b0f7ccb758f
- RECOVERY-MANIFEST.md — f9a7448c538e34fc044e7dc69c6d8118b1d02137

Preservation terminal:
PASS_ARH_SELF_RECOVERY_R03_PRESERVED_READY_FOR_REPLACEMENT_INITIATION
commit:
61eea761b192b8617af6087c1c551ae54edef455

## Predecessor writer

Artifact:
entities/archivarius/current/ARH__replacement-current-writer-r01.md

blob:
3d17b16c02e84e841d1266e3b0fcc083640b77d6

establishment commit:
a00b1644e840bed722e3712e78c8842959599797

OPERATOR has confirmed replacement of the degraded predecessor chat for this initiation cycle.

This initiation result does not perform or imply Writer Gate, freeze mutation, new current-writer establishment, or authoritative current-state mutation.

## Fresh reconciliation boundary

Checked at the fresh HEAD:
- entities/archivarius/current/
- entities/archivarius/inbox/
- entities/archivarius/outbox/
- routes/dispatch/
- routes/receipts/
- registry/by-sender/archivarius.jsonl

No repository commit later than the preservation terminal exists at this boundary.

Historical PROMPT/tasks remain evidence only and were not replayed.

## KOO recovery v0.8 boundary

Completed:
PASS_ARH_KOO_RECOVERY_V08_PRESERVED_READY_FOR_HANDOFF

result commit:
d46c77a7f5a685943b0aec732d75cf42c95eed9b

immutable recovery:
puev5691/wellbeing-entity-bootstrap@ef8e2c887fe95b69a99b0a0252027d9ee267ea2b:entities/koo/recovery/versions/koo-recovery-v08

Disposition:
COMPLETED / DO_NOT_RESUME / DO_NOT_REPLAY

## Terminal

initiation_verified_waiting_writer_gate

STOP before Writer Gate and before profile work.

---
КТО: replacement ARH / АРХИВАРИУС
СТАТУС: initiation_verified_waiting_writer_gate
