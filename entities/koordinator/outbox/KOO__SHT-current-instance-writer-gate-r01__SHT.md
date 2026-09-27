# KOO → SHT: current-instance Writer Gate r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHT / ШТАБИСТ
scope: WRITER_GATE_ONLY
project_time: omitted

Resume-First.

Execute only Writer Gate for this exact already initiated SHT chat instance.

Exact authority:

puev5691/wellbeing-hq@4123ef883b12feeb8fabe85b7b7f5a03adf62462:
entities/koordinator/outbox/KOO__authorize-SHT-current-instance-writer-gate-r01__OPERATOR.md

Exact initiation completion:

puev5691/wellbeing-hq@f5f6a2ed9c3c1820dace6fd7dfdd15d55d39c60b:
entities/shtabist/outbox/SHT__current-instance-initiation-gate-r01-completion__KOO.md

blob:
0d64e2622b94cb58ac76f97aa10e6b115303704f

outcome:
initiation_verified_waiting_writer_gate

Exact ARH checksum closure:

puev5691/wellbeing-hq@7f309553d1fa098e5759782055ae184f7d7a2977:
entities/archivarius/outbox/ARH__SHT-recovery-checksum-verify-r01-result__KOO-SHT.md

terminal:
PASS_ARH_SHT_RECOVERY_CHECKSUM_VERIFY_R01_4_OF_4

Exact recovery:

puev5691/wellbeing-entity-bootstrap@b34dd2cda94c2f61acc59a5f066c38bd24fdae0c:
entities/sht/recovery/current

## Writer Gate checks

Before any write:

1. Verify this exact physical/current SHT chat instance matches the instance recorded by the initiation completion.
2. Verify exact initiation completion identity/status.
3. Verify exact immutable recovery identity remains unchanged.
4. Verify current approved Project Sources.
5. Verify no competing SHT current-writer exists.
6. Verify no newer freeze/handoff/replacement evidence conflicts.
7. Verify no superseding initiation/recovery result exists.
8. Verify pending governance-review task remains pending and was not already executed.
9. Do not use latest timestamp, GitHub capability, chat continuity or old SHT commits as writer proof.

## Allowed result

If all checks pass:
- establish this exact current SHT chat instance as authoritative current-writer;
- publish one current-writer artifact under entities/shtabist/current/;
- publish one Writer Gate result to KOO;
- exact readback.

Allowed Writer Gate terminal:
WRITER_ESTABLISHED

If continuity/conflict cannot be proved:
WRITER_REQUIRED_UNVERIFIED
or
WRITER_CONFLICT
with exact blocker.

Do NOT infer writer from initiation_verified alone.

## Pending task boundary

Do NOT execute:

puev5691/wellbeing-hq@2b75d5f866586c42750884bc822374c8ea20337a:
entities/koordinator/outbox/KOO__operational-shard-admission-profile-r01-governance-review__SHT.md

That task may be reconsidered only after Writer Gate result returns to KOO and KOO performs fresh reconciliation.

## Forbidden

- historical PROMPT replay;
- governance review execution;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- deployment/host mutation;
- trust-root/backend/operator selection;
- credentials;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

After current-writer publication + exact readback + Writer Gate result to KOO, STOP.
