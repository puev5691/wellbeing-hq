# KOO current active queue r1.10

status: CURRENT_QUEUE
project_time: omitted

## Replacement preparation

Current KOO v0.6 remains authoritative writer.
Replacement preservation has started because OPERATOR observed chat degradation/context exhaustion.

External recovery candidate v0.7:
puev5691/wellbeing-entity-bootstrap@7c18028e23a1c4954de304ff3ac6b1358537f987:
entities/koo/preservation/pending/self-preservation-current-writer-v07

KOO self-readback:
PASS.

ARH preservation task:
entities/koordinator/outbox/KOO__recovery-v07-preserve__ARH.md
commit ee5fc33f6a7f3ee4042ac192a99243a5950340b7

ARH inbox:
4b98216a276677119d8169d36dcc0366ab45f7bd

Automatic activation:
failed; manual ARH activation required.

Do NOT freeze KOO v0.6 before ARH preservation/readback PASS.

## Priority work preserved

1. Booster: SIS r0.2 reverify PASS; host-update/readiness gate awaiting OPERATOR approval.
2. Fast memory: old memory-layering branch requires fresh reconciliation; no old PROMPT replay.
3. Telegram facilitator: verified core/bridge/semantic-input foundations; requires fresh reconciliation.
4. task-conveyor v1.3: pending OPERATOR decision, not active.
5. KAN bounded working-circle request: pending, explicitly non-preempting.

## Next causal step

ARH independent preservation/canonicalization of KOO recovery v0.7.
After ARH PASS:
- publish KOO v0.6 CURRENT_WRITER_HANDOFF_FREEZE;
- prepare replacement initiation PROMPT;
- new instance performs verified initiation;
- separate Writer Gate establishes replacement writer.
