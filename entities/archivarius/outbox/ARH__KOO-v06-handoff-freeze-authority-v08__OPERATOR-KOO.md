# OPERATOR → KOO: handoff/freeze authority for replacement from v0.6 using recovery v0.8

status: CURRENT_WRITER_HANDOFF_FREEZE_AUTHORIZED
entity: KOO / КООРДИНАТОР
project_time: omitted

## Человеческий смысл

ОПЕРАТОР явно разрешил перейти к replacement-инициации нового физического KOO по externally verified recovery v0.8.

Текущий authoritative KOO writer v0.6 с этого решения не должен выполнять новые authoritative profile/current-state mutations.

Исторические bytes writer v0.6 сохраняются как provenance и не переписываются.

## Predecessor writer

artifact:
entities/koordinator/current/KOO__replacement-current-writer-v06.md

blob:
90edff69b20879231fda8b882cbb172173e456f0

establishment commit:
525e5b131472e61b1f55db5ef7307217aea4c4fc

disposition:
FROZEN_FOR_NEW_AUTHORITATIVE_PROFILE_MUTATIONS_PENDING_REPLACEMENT

## Recovery basis

terminal:
PASS_ARH_KOO_RECOVERY_V08_PRESERVED_READY_FOR_HANDOFF

result commit:
d46c77a7f5a685943b0aec732d75cf42c95eed9b

immutable recovery:
puev5691/wellbeing-entity-bootstrap@ef8e2c887fe95b69a99b0a0252027d9ee267ea2b:entities/koo/recovery/versions/koo-recovery-v08

composition:
8/8 PASS

## Authority boundary

This decision:
- authorizes replacement cold-start initiation only;
- does not establish a new current-writer;
- does not perform Writer Gate;
- does not authorize historical task/PROMPT replay;
- does not authorize memory-layering attempt 3;
- does not authorize provider/Telegram/external host mutation.

Replacement instance must return:
initiation_verified_waiting_writer_gate
or exact blocker,
then STOP before Writer Gate/profile work.

---
КТО: OPERATOR / authority recorded by ARH
СТАТУС: CURRENT_WRITER_HANDOFF_FREEZE_AUTHORIZED
