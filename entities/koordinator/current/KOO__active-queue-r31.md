# KOO current active queue r0.31

status: CURRENT_QUEUE

## RECOVERY ACTIVE — SIS PRESERVATION VERIFY

SIS self-preservation:
`318032c4185c46cabce288cf6abe86ec051de819`

External candidate:
`puev5691/wellbeing-entity-bootstrap@c195f023a5ad955105995de9f1c772e8cd85833d:entities/sis/preservation/pending/self-preservation-current-writer-v03`

Current candidate state:
`candidate_not_canonical`

ARH verification task:
`4c78d8d9d5272081f92eba76f8886c96e0654f13`

ARH inbox:
`b238f829a23df38c7922cd83398954f7d39b3a2a`

Current SIS writer v0.1 remains authoritative until ARH preservation verdict and explicit KOO freeze/replacement transition.

No new SIS profile work is to be assigned during this preservation stage.

## NEXT CONDITIONAL — SIS REPLACEMENT INITIATION

Condition:
`PASS_ARH_SIS_PRESERVATION_R03_READY_FOR_REPLACEMENT_INITIATION`

Then:
1. KOO records freeze/retirement of old SIS writer for new authoritative mutations;
2. KOO authorizes replacement cold-start;
3. new SIS verifies recovery package and current approved sources;
4. new SIS returns `initiation_verified_waiting_writer_gate` or exact blocker;
5. separate Writer Gate establishes replacement current-writer;
6. only then reconcile and resume profile tasks.

## PRESERVED SIS OPEN STATE

OpenAI cost matrix remains blocked/waiting on verified Astra clean runtime chain.
Original matrix:
`512cad6059a4911ee16fb6012a9e05366dc3b547`

Previous SIS blocker:
`8139700f5f31523073d7bbe3ee93e393308d0775`

KOD clean Astra package has since appeared:
`627b4ffa136de996598c64bde4fb3d87c6cbce16`

Replacement SIS must fresh-reconcile independent reverify/staging before any provider call.

Shard gateway plan task was assigned before preservation:
`2857e5601a9d156c9f03594db9db3da740013426`

Do not assume it completed unless terminal evidence appears.

## OPERATIONAL TAIL

Temporary Telegram credential file fact preserved by SIS:
`/tmp/telegram_bot_token` on burzh, mode 0600.
Contents not read and not included in recovery.
Cleanup/rotation remains separate future work.

## POLICY

Preservation candidate != canonical recovery.
Preservation PASS != writer handoff.
Initiation != writer authority.
