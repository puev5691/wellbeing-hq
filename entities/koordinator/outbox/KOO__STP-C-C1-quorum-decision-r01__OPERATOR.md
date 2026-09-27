# KOO → OPERATOR: STP-C C1 quorum decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Exact appointed seats:

GOV = KOO
NORM = KAN
INFRA = SIS

Appointment record:
puev5691/wellbeing-hq@fc1b6ecced47bf147581e0b350cdac7bf2584453:
entities/koordinator/outbox/KOO__STP-C-C1-seats-KOO-KAN-SIS__OPERATOR.md

Established technical boundary:
the three seats are governance-diverse but remain one shared technical control/failure domain.

This quorum therefore governs decision/process diversity only.
It must not be described as cryptographic or technical threshold independence.

## Option Q2 — 2 of 3, conflict-blocking

Token:
SELECT_STPC_C1_QUORUM_Q2_2_OF_3_CONFLICT_BLOCKING

Rule:
- any two current APPROVE decisions may satisfy candidate quorum
- BUT any contradictory current REJECT blocks admission
- silence/absence is not approval
- stale/unknown currentness blocks
- no casting vote

Consequence:
- tolerates one unavailable seat when the remaining evidence is non-conflicting
- faster routine governance
- weaker against two coordinated/internal decision errors
- does not improve technical independence

## Option Q3 — role-constrained 2 of 3

Token:
SELECT_STPC_C1_QUORUM_Q3_ROLE_CONSTRAINED

Candidate rule:
- at least two approvals required;
- approvals must satisfy an explicit role-coverage rule;
- contradictory current REJECT blocks;
- silence/absence is not consent;
- stale/unknown currentness blocks.

Important:
this token selects only the Q3 family.
The exact role-coverage rule (for example which seat may never be bypassed) would require one later bounded decision.

Consequence:
- better protection against two similar-function seats deciding alone;
- more governance structure;
- slightly more operational friction.

## Option Q4 — unanimous ordinary/high-impact governance

Token:
SELECT_STPC_C1_QUORUM_Q4_UNANIMOUS

Rule:
- all three current seats must APPROVE;
- any REJECT blocks;
- any unavailable/stale/unknown seat prevents admission.

Consequence:
- strongest internal governance consensus;
- highest deadlock/availability cost;
- still no technical independence because all three share one control domain.

Emergency revoke is NOT selected by this token and remains a separate future decision.

## Deferred

Token:
DEFER_STPC_C1_QUORUM_DECISION

Use if no quorum should be selected yet.

## Not part of this gate

No:
- participant changes;
- emergency-revoke rule;
- root/signing technology;
- signer/attestor;
- credentials;
- backend/host/operator;
- Fast Gate;
- profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation.

EOM pilot remains BLOCKED.
Memory-layering attempt 3 remains NOT_AUTHORIZED.

Return exactly one token:
- SELECT_STPC_C1_QUORUM_Q2_2_OF_3_CONFLICT_BLOCKING
- SELECT_STPC_C1_QUORUM_Q3_ROLE_CONSTRAINED
- SELECT_STPC_C1_QUORUM_Q4_UNANIMOUS
- DEFER_STPC_C1_QUORUM_DECISION
