# KAN emergency replacement initiation v0.1

Новый экземпляр КАНЦЕЛЯРА проходит аварийную инициацию не как продолжение прежнего чата, а как replacement instance. ОПЕРАТОР прямо подтвердил недоступность прежнего authoritative KAN current-writer и отдельно разрешил emergency replacement на основе последнего externally verified recovery, с fresh reconciliation, без synthetic reconstruction и с отдельным Writer Gate.

Обычная инициация до этого была корректно остановлена из-за stale recovery. Текущее решение ОПЕРАТОРА не делает старый recovery свежим. Оно создаёт допустимое emergency-failover basis: replacement instance восстанавливает только подтверждённый внешний baseline, принимает текущий approved source set как более свежую внешнюю норму и **не реконструирует** потерянный профильный current-state между recovery checkpoint и аварийной заменой.

## Результат

initiation_status: `initiation_verified`
replacement_mode: `EMERGENCY_FAILOVER`
next_state: `WAITING_SEPARATE_WRITER_GATE`
writer_state: `NOT_ESTABLISHED_FOR_THIS_INSTANCE`
profile_work: `NOT_STARTED`
historical_task_replay: `FORBIDDEN`
synthetic_reconstruction: `NOT_PERFORMED`
project_time: omitted; trusted project-time source not used

## Authority basis

Прямое решение ОПЕРАТОРА в текущем чате:

- прежний authoritative KAN current-writer недоступен;
- emergency replacement KAN явно разрешён;
- basis: последний externally verified recovery;
- обязательны fresh reconciliation и запрет synthetic reconstruction;
- Writer Gate должен быть отдельным шагом.

Это exact human authority для emergency failover. Оно не является автоматическим назначением current-writer и не разрешает профильную работу до Writer Gate.

## Fresh approved source basis

Независимо проверены current approved Project Sources и их SHA-256:

- `project-instructions-core-v2_5-approved.md`
  SHA-256 `f2ad19e243e55c552b10372c4bd7ddda7f18018579527f94d69e14858303b49c`;
- `entity-roles-short-v2_4-approved.md`
  SHA-256 `d7feae524f6d1a34b0fd2a63475435e41ebe48097a191d87ca0ceeb797421530`;
- `file-work-canon-universal-v2_4-approved.md`
  SHA-256 `c7e09bb358afd9ff131158044ce3722375ab30580e240909e85afdf38ca1e08b`;
- `source-loading-policy-v2_2-approved.md`
  SHA-256 `2a410e929c8cf4daa21f9229ad300e92abbaf4ab40b4fbf3a03950cc663e719e`;
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`
  SHA-256 `82e3117570a9ecd73be2dae1279ebb3e0a2d6125556de98d5c1ede14a9236ae5`;
- `task-conveyor-canon-v1_2-approved.md`
  SHA-256 `913e88c1e4d17a07122ad9cdf680abae28fc2def0ea0740df9ce925fec22d0e7`.

Fresh activation evidence:
- Project Core v2.5 activation:
  `entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md`
  blob `0751a00489dd8f3f4ac5feeda900a22ade1b3f99`;
- task-conveyor v1.2 activation:
  `entities/koordinator/outbox/KOO__source-set-r06-activation-result__OPERATOR.md`
  blob `f1eb35b445dda92d084a00e9304e333854e19a75`.

Pending task-conveyor v1.3 is not treated as active.

## Last externally verified recovery

External recovery basis remains:

`puev5691/wellbeing-archivist@f847be7635124dc155d99d8b62c4e105da8c8cb3:docs/entities/kancelyariya/recovery-current`

Fresh immutable readback verified:

- `KAN__initiation-current__KAN.md`
  blob `37f21538113c46e95bdb06f68fd6abd209727cd4`;
- `KAN__snapshot__KAN.md`
  blob `40c08d6587510c26fc62590e975f03f7596c3c76`;
- `KAN__recovery-manifest__KAN.md`
  blob `8dda06d122136350a56ad8f1d83b12c0e45871c8`;
- `sha256sums.txt`
  blob `734c19cbdd4136a12c62158715472caec1f39853`.

Checksum table declares:
- initiation SHA-256 `4df82df55ea8798799fd62bc41724d80def9553c028cdb410eb72f671cca8ab5`;
- manifest SHA-256 `3273be2a8693258a8f526d65d0a42da49c81734fcddd1574f9aa5e48114bd0eb`;
- snapshot SHA-256 `da9484eae3ed13ab5338c7c83f5581c58844f01bb4cc6c97753aebb9148bc5cb`.

ARH independent preservation result:
`entities/archivarius/outbox/ARH__KAN-role-source-v2_3-preservation-result__KAN.md`
blob `0c82a34a3d5ff2df16a3b38f9a4ae0bfe5870095`.

Current ARH recovery registry still points KAN to exact recovery commit `f847be7635124dc155d99d8b62c4e105da8c8cb3`; no newer externally verified KAN recovery is registered.

## Stale-recovery boundary

Этот recovery authentic и externally verified, но materially stale. Он сохраняет старые source versions и профильное состояние старого checkpoint.

Предыдущий диагностический результат:
`entities/kancelar/outbox/KAN__initiation-diagnostic-stale-recovery__OPERATOR-ARH-KOO.md`
commit `ca7cf041d6b68b38f5702dc5a2ad8d89c3fd4a59`
blob `4e648b083a417278a8a6ecdca4f572379e15718b`
правильно зафиксировал ordinary initiation как `initiation_failed` до решения ОПЕРАТОРА о failover.

Emergency basis меняет допустимый режим восстановления, но **не переписывает** старый snapshot и не делает его current по содержанию.

Replacement instance принимает как confirmed:
1. устойчивую роль KAN из externally verified recovery, ограниченную current approved role-source v2.4;
2. последний externally verified recovery как rollback/recovery basis;
3. current six-source approved baseline как fresher externally verified normative layer;
4. факт недоступности predecessor writer как explicit OPERATOR decision;
5. все post-checkpoint KAN artifacts только как external evidence до отдельной exact revalidation.

Не принимается как восстановленный authoritative self-state:
- скрытая память прежнего чата;
- автоматическое продолжение post-checkpoint задач;
- inferred current status из последовательности commits;
- synthetic merged snapshot из старого recovery + новых outbox/inbox artifacts.

## Fresh HQ reconciliation

Pre-initiation HQ HEAD:
`3648e9d8df496891335a4d752127107794d6d0cd`.

Fresh inspection:
- `entities/kancelar/current/` не содержит explicit KAN current-writer artifact;
- competing replacement KAN writer evidence не обнаружено;
- текущий HEAD включает stale-recovery diagnostic и его маршрутизацию;
- более свежий externally verified KAN recovery не обнаружен;
- свежие KAN inbox/outbox/queue artifacts существуют, но являются evidence, а не automatic execution authority;
- old recovery writer-state claim относится только к historical checkpoint и не переносится на этот replacement instance.

## Restored role and limitations

Роль:
KAN / КАНЦЕЛЯР.

Current role boundary:
границы понятий, ответственности и внешних обязательств; различение факта, определения, гипотезы, нормативного предложения и обещания; короткие policy/disclaimers/regulations; без подмены профильного юриста и без бюрократии ради бюрократии.

До Writer Gate этот экземпляр:
- read-only относительно authoritative KAN current-state;
- может завершить только текущую emergency recovery procedure;
- не возобновляет исторические PROMPT/tasks;
- не принимает новые profile tasks;
- не создаёт новый self-snapshot как authoritative state.

## Единственный безопасный следующий шаг

Выполнить **отдельный Writer Gate** по уже данному явному разрешению ОПЕРАТОРА:

1. fresh pre-gate HQ reconciliation;
2. повторно проверить exact initiation result;
3. проверить отсутствие competing KAN writer;
4. подтвердить, что recovery basis и active source identities не изменились;
5. если PASS, отдельно materialize replacement KAN current-writer;
6. выполнить exact readback и post-write reconciliation;
7. остановиться без profile-work replay.

---

sender: replacement KAN instance
document_type: emergency-replacement-initiation-result
status: initiation_verified
next_state: waiting_separate_writer_gate
profile_work: not_started
project_time: omitted; trusted project-time source not used
