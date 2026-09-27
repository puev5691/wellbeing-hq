# KOO → SHT: STP-C B1 factual independence map r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHT / ШТАБИСТ
scope: DOCUMENT_ONLY_FACTUAL_DEPENDENCY_AND_CONFLICT_MAP
project_time: omitted

Resume-First.

Exact OPERATOR order decision:

puev5691/wellbeing-hq@4eff701b0c4bc47db2a80ffbaf99dae17cb09814:
entities/koordinator/outbox/KOO__STP-C-order-independence-map-before-composition__OPERATOR.md

Exact KAN review basis:

puev5691/wellbeing-hq@1f8f6d17a9b28710ff2fc9445635991a539e1121:
entities/kancelar/outbox/KAN__STP-C-governance-model-r01-independent-review__KOO.md
blob 986cbdc37aeacbd1c4061f24803580e111e8c105

Exact STP-C candidate:

puev5691/wellbeing-hq@622addc16bd8efa8736f3332dd31cee0e7b5dcb1:
entities/shtabist/outbox/SHT__STP-C-multiparty-governance-model-design-r01__KOO.md
blob 4191acf5ced6066397c5c734f9246b2098bcb46e

Current SHT writer:

puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da

Build only the B1 independence map needed before OPERATOR chooses a participant-role composition.

For each relevant candidate seat/role class that can be supported by current verified project evidence, map:

- seat / role class;
- candidate principal/entity class;
- who can authorize it;
- credential custody, if known;
- runtime/execution boundary, if known;
- admin/control domain, if known;
- failure domain, if known;
- who can technically impersonate/control/disable it, if established;
- conflicts of interest;
- whether independence from each other candidate seat is:
  VERIFIED_INDEPENDENT
  VERIFIED_SHARED_DOMAIN
  PARTIALLY_INDEPENDENT
  UNKNOWN
  NOT_APPLICABLE
- exact evidence locator for every non-UNKNOWN claim.

At minimum consider role classes already present in the STP-C model:
- human/non-delegable governance / OPERATOR-class;
- governance/coordination / KOO-class;
- normative/formal review / KAN-class;
- organizational/process / SHT-class where applicable;
- infrastructure/security / SIS-class;
- independent technical verifier class;
- signer/attestor class only as a separate future capability, not an approval seat unless separately selected;
- publisher/mutation-service classes only for conflict/control analysis, not as approval seats.

Required outputs:

1. Human-readable independence matrix.
2. Conflict-of-interest map.
3. Shared-control/failure-domain map.
4. List of UNKNOWN technical facts that prevent a trustworthy C1/C2/C3/C4 choice.
5. Minimum next evidence request, if needed, identifying the correct Entity for each missing technical fact.
6. State whether the existing evidence is already sufficient to make a meaningful composition choice.

Critical rule:
different role names, chats, keys, or files do NOT prove independence.

Do not invent:
- credential ownership;
- runtime placement;
- host/admin control;
- failure-domain separation;
- technical isolation.

If those facts are unavailable, mark UNKNOWN and return the minimum exact evidence needed.

Do NOT:
- select C1/C2/C3/C4;
- appoint actual participants;
- select quorum;
- select emergency revoke policy;
- select root/signing technology;
- create credentials;
- select attestor/backend/host/operator;
- activate profile;
- activate Fast Gate;
- authorize live WRITE/CAS;
- deploy;
- claim CHECKPOINT_DURABLE;
- activate Project Source;
- unblock EOM pilot;
- authorize memory-layering attempt 3.

Expected terminal:

PASS_SHT_STP_C_B1_INDEPENDENCE_MAP_R01_READY_FOR_OPERATOR_DECISION

if evidence is sufficient,

or

BLOCKED_SHT_STP_C_B1_INDEPENDENCE_MAP_R01_MISSING_EVIDENCE

with exact missing evidence and next owner.

After immutable result + exact readback + return KOO, STOP.
