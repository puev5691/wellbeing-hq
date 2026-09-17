# RED self-snapshot r0.1

status: `CURRENT_WRITER_SELF_SNAPSHOT_READY_FOR_PRESERVATION`
entity: RED / РЕДАКТОР
project_time: omitted; trusted project-time source not used

## Назначение

Этот файл фиксирует текущее содержательное состояние РЕДАКТОРА перед возможной заменой/инициацией нового экземпляра. Это self-snapshot текущего RED writer, а не внешний backup и не подтверждение recoverability.

Последний externally verified recovery-пакет RED существует в:
`puev5691/wellbeing-entity-bootstrap:entities/red/recovery/current`

Но он относится к более раннему состоянию и не включает значимую работу, выполненную после него. Поэтому его нельзя считать достаточным current recovery без нового preservation/readback цикла.

## Текущая роль и границы

РЕДАКТОР отвечает за живой текст, читаемость, структуру, публикационные и литературные версии, ручную вычитку и редакционное преобразование материалов без подмены фактов.

RED не:
- повышает candidate/draft до approved/current;
- объявляет публикацию состоявшейся без evidence;
- меняет технический статус чужих профильных результатов;
- подменяет KOO в межконтурной маршрутизации;
- подменяет KAN/SIS/KOD/SHD в их профильном authority;
- выдумывает receipt, acceptance, deployment, billing, provider access или live API result.

## Current-state, который должен восстановить новый экземпляр

### 1. «Сначала она была выдумана» v0.3

Exact RED candidate:
- `entities/redaktor/outbox/RED__publication-snachala-ona-byla-vydumana-v03__KOO.md`
- commit `1d81c994b212ea8a00e6441136d39dd5364c6b32`
- blob `d7faa795602cec3fef40cb8c4fbb7511d55c7057`

KAN delta result:
- `PASS_DELTA`
- commit `2c858f412576539c5004777d0310e260d388c286`

KOO gate decision:
- commit `d9ce3fd253c258fae70b52533eb805fe5886cb55`

OPERATOR route exists.
Current state:
`WAITING_OPERATOR_RELEASE_DECISION`

Do not rewrite by inertia.

### 2. Public cooperation speech v0.2

Exact candidate:
- `entities/redaktor/outbox/RED__wellbeing-cooperation-speech-v02__KOO.md`
- commit `30214bc36f48d4804ffff9fc60c3a7aedb0438c1`
- blob `31034d87d67035698748339f7e0d747509da0edc`

KOO bounded acceptance exists.
OPERATOR route exists.
Current state:
`WAITING_OPERATOR_REVIEW`

Do not infer OPERATOR acceptance from inbox placement.

### 3. GitHub Information Entry

RED result:
- `entities/redaktor/outbox/RED__github-info-entry-editorial-lifecycle__KOO.md`
- commit `f900a2c79b32612347e332e99384c5b5e243b32f`
- blob `7d62a4cbb3257b46a23a94193f046988dabb1d9c`

KOO status:
`ACCEPTED_BOUNDED_STAGE_B_PREREQUISITE`

RED state:
`COMPLETED_ACCEPTED_NO_EDITORIAL_TASK_PENDING`

### 4. Русскоязычные операторские briefs

Telegram Phase 1B:
- `entities/redaktor/outbox/RED__telegram-phase1b-operator-brief-ru__KOO.md`
- commit `f1006919533f0dde2832c4b3aa65903307342f86`
- blob `23d9d5c076abcfe76444383c020e6037aa06e19c`

Multi-model:
- `entities/redaktor/outbox/RED__multimodel-operator-brief-ru__KOO.md`
- commit `6f5f00aa4f55444157cd292bf0456706196a20cd`
- blob `2b6db6de7e259d55bff8ffe4fbaf1c293982a423`

Result:
- `entities/redaktor/outbox/RED__operator-briefs-ru-result__KOO.md`
- commit `91985e74a5d70fa18c3e6db93600854b62a88340`
- blob `41a164301e32f51a3cd8fabd6cd433b4731e009a`
- verdict `PASS_RUSSIAN_OPERATOR_BRIEFS_READY`

### 5. Provider capabilities/pricing brief

- `entities/redaktor/outbox/RED__provider-capabilities-pricing-brief-r01__KOO.md`
- commit `82d3679a06763ef465d5b330cc5ec16b9af0cf25`
- blob `15760cf167bbca112e67716ffdf0ae91507a7e11`
- verdict `PASS_PROVIDER_OPERATOR_BRIEF_R01`

### 6. OpenAI account/billing activation runbook r0.1

- `entities/redaktor/outbox/RED__openai-account-billing-activation-runbook-r01__KOO.md`
- commit `b9a9a375590e1e089b3c67333432254eaa1fcb88`
- verdict `PASS_OPENAI_ACCOUNT_BILLING_ACTIVATION_RUNBOOK_R01`

Important: in RED sender registry the artifact blob remained explicitly unverified from the then-current connector readback. Do not invent a blob value from memory.

### 7. Anthropic account/billing activation runbook r0.1

- `entities/redaktor/outbox/RED__anthropic-account-billing-runbook-r01__KOO.md`
- commit `68fd91d7876564a6e00fb0b2461a1e512839cf2d`
- blob `3b0435a3250ce5424c838476720eb53e5bfb39b8`
- verdict `PASS_ANTHROPIC_ACCOUNT_BILLING_RUNBOOK_R01`

### 8. Anthropic official API contract r0.1

Exact task:
- `entities/koordinator/outbox/KOO__anthropic-official-api-contract-r01__RED.md`
- commit `4123ee9ac9870c46656d531966587ce2b7db1f09`

Exact RED result:
- `entities/redaktor/outbox/RED__anthropic-official-api-contract-r01__KOO.md`
- commit `2b7e1c573afd0baf61e7701810567d998d9ec3ce`
- blob `b9080d52d53050e25caad6c267d605ca13dd421d`
- verdict `PASS_ANTHROPIC_OFFICIAL_API_CONTRACT_R01`

Dispatch:
- `routes/dispatch/RED__anthropic-official-api-contract-r01__KOO.md`
- commit `961f1923c7c0b8d338b6b80a41905c0b99ab8a52`

KOO inbox pointer:
- commit `13d46e8ac0633e7683a57686477fcd63b05e0e0e`

Sender registry update:
- commit `53fab4c42502009d7ec19bd1799a80989362a23e`

Recipient receipt for this exact version was not verified at the time of this snapshot. Current route state must therefore be rechecked before claiming received/accepted.

## Литературный контур и память развития

Current literary plan:
- `entities/redaktor/current/RED__life-project-literary-cycle-plan.md`
- current main blob at snapshot preparation: `30b96ec0215e001a530a7974f8bb5001d876df2d`

Recovered raw literary source «Как мы строили гараж» is preserved in project information field and should remain available as early-future-imagination source. Its function in the cycle is to compare early dream of an almost omnipotent System with the later bounded architecture of Entities, verification, routing and authority limits.

The literary cycle should keep two evidence layers distinct:
- verifiable project artifact/event;
- author recollection or literary interpretation.

Do not promote recollection to GitHub fact and do not use GitHub artifacts as proof of the author's inner state.

## Опыт, который должен менять поведение нового экземпляра

Current experience corpus:
`entities/redaktor/current/experience/RED_experience-cards.jsonl`

Must restore at least these reusable lessons:

1. `RED-EXP-001` — fresh GitHub preflight before claiming idle/waiting/current state.
2. `RED-EXP-002` — old blockers are versioned dependencies and must be revalidated.
3. `RED-EXP-003` — legal/semantic tightening should remove unsupported implications without killing the public voice.
4. `RED-EXP-004` — dispatch, receipt, acceptance and downstream use are separate evidence classes.

Operational memory rule:
`task → result → receipt → decision → next gate`.

## Недавняя причинная цепочка, которую нельзя потерять

- RED moved from literary/publication work into operator-facing technical briefs without taking technical authority from SIS/KOD/KAN/SHD.
- Provider research led to an operator comparison brief and then provider-specific account/billing runbooks.
- OpenAI path was handled first, then Anthropic.
- Anthropic work split correctly into two different artifacts: account/billing activation runbook and official API contract for KOD.
- KOD synthetic Anthropic adapter explicitly did **not** prove provider API compatibility; RED official contract exists to prevent synthetic fixture semantics from silently becoming provider semantics.
- No account creation, purchase, API-key creation/reading, billing mutation or live provider call was performed by RED in those tasks.

## Preservation trigger and current recovery risk

KOO already issued an emergency preservation/recovery checkpoint for RED to ARH:
- source task commit `999542a004cd1fb4bc6364ee24c6dd8aaee47ca7`
- addressed ARH inbox commit `2f70ce273cf2b8bd4ead7ec5b26b256e5c72fec5`

At snapshot preparation time, no newer verified RED external recovery package was established in `wellbeing-entity-bootstrap`.

The current external recovery at:
`puev5691/wellbeing-entity-bootstrap:entities/red/recovery/current`
contains the older standard four-file package and therefore must be treated as the **last verified recovery**, not as a current backup of the work listed above.

## Pending / unknown

- new external backup/preservation of this snapshot: pending ARH;
- external publication + readback/verification of the replacement recovery package: pending ARH;
- recoverability of a new RED chat from the refreshed package: not yet tested;
- exact current receipt/acceptance state of recent provider artifacts: revalidate from routes/receipts before claims;
- no writer transfer is performed by this snapshot.

## Один безопасный следующий шаг

АРХИВАРИУС должен принять this self-snapshot plus initiation procedure/manifest candidate, publish a refreshed external RED recovery package, perform readback/version verification, update recovery accounting, and return exact preservation result. Only after that should a replacement RED chat perform cold-start verification and any writer handoff.

---

WHO: RED / РЕДАКТОР current writer
DOCUMENT_TYPE: self-snapshot
PURPOSE: preserve authoritative RED state, event tail and reusable experience before replacement initiation
BACKUP_STATUS: `NOT_YET_EXTERNALLY_PRESERVED`
