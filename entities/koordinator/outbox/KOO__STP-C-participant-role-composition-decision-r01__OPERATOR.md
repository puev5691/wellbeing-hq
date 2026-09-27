# KOO → OPERATOR: STP-C participant-role composition model decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

## What this decision does

Select only the abstract role-composition model for future STP-C approval seats.

This decision does NOT:
- appoint actual participants;
- prove their independence;
- select quorum;
- select root/signing technology;
- create credentials;
- select attestor/backend/host/operator;
- activate a trust profile;
- authorize live WRITE/CAS;
- deploy anything.

Exact reviewed basis:
puev5691/wellbeing-hq@1f8f6d17a9b28710ff2fc9445635991a539e1121:
entities/kancelar/outbox/KAN__STP-C-governance-model-r01-independent-review__KOO.md
blob 986cbdc37aeacbd1c4061f24803580e111e8c105

Exact candidate:
puev5691/wellbeing-hq@622addc16bd8efa8736f3332dd31cee0e7b5dcb1:
entities/shtabist/outbox/SHT__STP-C-multiparty-governance-model-design-r01__KOO.md
blob 4191acf5ced6066397c5c734f9246b2098bcb46e

Boundary B1 applies to every option:
before actual appointment, an independence map is still required:
seat -> principal -> credential custody -> runtime -> admin/control/failure domain -> conflict-of-interest.

## Option C1 — governance/coordination + normative/process + infrastructure/security

Meaning:
three role classes:
- governance/coordination;
- normative/process;
- infrastructure/security.

Consequence:
- compact three-seat structure;
- three different review perspectives;
- possible overlap between governance and normative/process must later be proven acceptably independent.

Evidence still required:
- B1 independence map;
- conflict-of-interest analysis;
- availability/failure-domain analysis.

Decision token:
SELECT_STPC_C1_GOV_NORM_INFRA

## Option C2 — human/non-delegable governance + independent organizational/normative review + infrastructure/security

Meaning:
one seat class is explicitly human/non-delegable governance, plus:
- independent organizational/normative review;
- infrastructure/security.

Consequence:
- preserves direct human participation in high-impact trust changes;
- human availability becomes an intentional bottleneck.

Evidence still required:
- B1 independence map;
- exact boundary of human/non-delegable seat;
- outage/emergency behavior;
- conflict-of-interest analysis.

Decision token:
SELECT_STPC_C2_HUMAN_NORM_INFRA

## Option C3 — governance/coordination + normative/process + independent technical verifier

Meaning:
three role classes:
- governance/coordination;
- normative/process;
- independent technical verifier.

Consequence:
- keeps approval structure centered on governance + independent evidence checking;
- infrastructure/operator role is not itself an approval seat by default;
- verifier independence and evidence completeness become critical.

Evidence still required:
- B1 independence map;
- verifier independence proof;
- B2 decision-set completeness design;
- availability/failure-domain analysis.

Decision token:
SELECT_STPC_C3_GOV_NORM_VERIFIER

## Option C4 — four-seat model

Meaning:
four role classes:
- governance/coordination;
- normative/process;
- infrastructure/security;
- independent verifier.

Consequence:
- strongest separation potential;
- highest coordination/deadlock cost;
- later role-constrained quorum may avoid requiring all four for every ordinary approval, but no quorum is selected here.

Evidence still required:
- B1 independence map across all four seats;
- availability/deadlock analysis;
- conflict-of-interest map;
- verifier independence proof.

Decision token:
SELECT_STPC_C4_GOV_NORM_INFRA_VERIFIER

## Defer

If none can be selected meaningfully before a factual independence map exists:

DEFER_STPC_ROLE_COMPOSITION_PENDING_B1_INDEPENDENCE_MAP

This is a valid bounded decision.
It means KOO must first obtain a document-only B1 independence-map candidate before asking again.

## Current non-decisions

Quorum: NOT SELECTED
Emergency revoke rule: NOT SELECTED
Authentication root: NOT SELECTED
Attestor/signer: NOT SELECTED
Backend/host/operator: NOT SELECTED
Profile activation: NO
Fast Gate: NOT ACTIVE

## OPERATOR response

Return exactly one:
- SELECT_STPC_C1_GOV_NORM_INFRA
- SELECT_STPC_C2_HUMAN_NORM_INFRA
- SELECT_STPC_C3_GOV_NORM_VERIFIER
- SELECT_STPC_C4_GOV_NORM_INFRA_VERIFIER
- DEFER_STPC_ROLE_COMPOSITION_PENDING_B1_INDEPENDENCE_MAP
