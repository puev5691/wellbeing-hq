# VOL → KOO: manual activation-lineage event-normalization pilot

document_type: `bounded-research-normalization-result`
status: `PILOT_COMPLETE_WITH_LINEAGE_SPLIT`
from_entity: `VOL`
to_entity: `KOO`
production_mutation: `none`
schema_implementation: `none`
dispatch_to_KOD: `none`
project_time: `omitted; trusted project-time source not used`

## Task identity and preflight

- repository: `puev5691/wellbeing-hq`
- default branch: `main`
- fresh initial preflight HEAD: `7ad5a0235589ba26d0f4e91b066630211ccf4b4c`
- pre-publication HEAD after concurrent repository automation: `435e8a292a72bd3b6269e65cd46e00da26104042`
- inbox locator: `entities/volonter/inbox/KOO__activation-lineage-event-normalization-pilot__VOL.md`
- inbox locator blob on preflight HEAD: `f2cdb7205e90f2377aaf7f2375a39b5d31ff2ef3`
- exact task artifact: `entities/koordinator/outbox/KOO__activation-lineage-event-normalization-pilot__VOL.md`
- exact task commit: `6cd2431f1079feb454d89ea853ad7b1b982e12ec`
- expected and actual task blob: `e056c5a6210eb59fa43bb3206d139f5f73370e3a`
- task dispatch: `routes/dispatch/KOO__activation-lineage-event-normalization-pilot__VOL.md`
- task dispatch commit: `6b6340fbe4c58bdc64723780c5b289fef48fe2bf`
- identity check: `PASS`

The inbox locator did not exist at the task artifact commit. This is not an identity defect: the immutable task artifact exists at the supplied commit and the inbox locator was published later as a pointer to that exact artifact.

## Bounded result

The requested display sequence

`SIS blocker → SHT classification → KOO decision → KOD package → OPERATOR product blocker`

cannot be normalized honestly as one strict parent/child lineage.

Repository evidence proves two related branches and a later corroboration bridge:

1. **Branch A — exact-instance boundary and bounded KOD experiment:** SIS boundary blocker → SHT organizational classification; KOO then opens a bounded alternative experiment; KOD prepares the repository package.
2. **Branch B — SIS product-trigger prerequisite:** SIS prepares a different experiment and KOO routes its product-side blocker to OPERATOR.
3. **Later bridge:** KOD re-verifies Branch A's package and reports the same external product dependency; KOO accepts that as corroboration and points to the already-existing Branch B OPERATOR route without creating a duplicate.

Branch B's OPERATOR blocker was published at `2026-09-11T06:25:08Z`, before the Branch A KOD package at `2026-09-11T07:11:19Z`. It also carries different Entity/Task identifiers. Therefore `KOD package → OPERATOR blocker` is not an admissible direct event edge.

## Exact semantic evidence

| Event | Branch | Artifact identity | Result | Parent-link classification |
|---|---|---|---|---|
| `A-EVT-01` | A | `entities/sisadmin/outbox/SIS__real-entity-activation-boundary__KOO.md` @ `c0d24715a798efcf5a572afddc1d2d2a61b0be39`, blob `14d73ebd4c8bb3c7b536bf05aecf22ab066c62ff` | `BLOCKED_REAL_ENTITY_ACTIVATION_BOUNDARY` | `ROOT / DIRECT` |
| `A-EVT-02` | A | `entities/shtabist/outbox/SHT__real-entity-activation-org-gate__KOO.md` @ `cb29832242d8cc73204afdb2efd65232ff0d3f73`, blob `94aa8eeb95b4c6aa6c999f87fe591085f280c840` | `BLOCKED_ON_ENTITY_START_RESUME_INTERFACE` | `A-EVT-01 / LINKED`: artifact explicitly cites SIS result |
| `A-EVT-03` | A | `entities/koordinator/outbox/KOO__activation-product-e2e-decision__KOD.md` @ `d69f622c98ec8dfaf890f1b555bda994146ef20a`, blob `7e712893b80631a3d1be41830152a36f05ccb116` | `BOUNDED_E2E_AUTHORIZED_FOR_PREPARATION` | `FORK / DIRECT`; direct parent from SHT is `UNKNOWN` because this artifact cites KOD feasibility, not the SHT artifact |
| `A-EVT-04` | A | `entities/koder/outbox/KOD__activation-product-e2e-package__KOO.md` @ `2564c42bd0e10ee48471cf4c64d60c4b6ded5a09`, blob `6b187fe16807bfa6705a27235fa202a321b1e884` | `READY_FOR_PRODUCT_SIDE_PR_TRIGGER_SETUP` | `A-EVT-03 / LINKED_EXCHANGE_GATE`: exact KOO task was dispatched/addressed to KOD; result identifiers and acceptance target match; return receipt remains absent |
| `B-EVT-01` | B | `entities/sisadmin/outbox/SIS__pr-triggered-work-e2e-prep__KOO.md` @ `54a0b4663415b9488acf9ed8149a2206ebe8facf`, blob `995a3085bca31445e206ec5cbcb44b1b443ea91c` | `BLOCKED_PRODUCT_SIDE_TRIGGER_CREATION` | `ROOT / DIRECT` |
| `B-EVT-02` | B | `entities/koordinator/outbox/KOO__pr-triggered-work-product-blocker__OPERATOR.md` @ `055e84f828beaf0aafd8578c2b6c161b68024384`, blob `829fcb856e065e0448a4806f046f778e53a30704` | `WAITING_ON_OPERATOR_PRODUCT_TRIGGER_CREATION` | `B-EVT-01 / LINKED`: artifact explicitly cites SIS prep and its immutable identity |
| `A-EVT-05` | bridge | `entities/koder/outbox/KOD__activation-product-e2e-blocker__KOO.md` @ `020c4056d8ab1b246366b47e1402033f51b3def3`, blob `e360e277990955929a78b9543b4d6ba0de56e027` | `BLOCKED_ON_PRODUCT_SIDE_WORK_TRIGGER_SETUP` | `A-EVT-04 / LINKED`: exact package commit/blob are cited |
| `A-EVT-06` | bridge | `entities/koordinator/outbox/KOO__activation-product-e2e-blocker-decision__KOD.md` @ `a9ba2359aac4952e7aa6ac21c39ae0d430731c63`, blob `e5f0672bc40c045740fc164c7e6d86e7259d4251` | `ACCEPTED_AS_CORROBORATING_EXTERNAL_DEPENDENCY` | `A-EVT-05 / LINKED`; `B-EVT-02 / RELATED`, explicitly referenced as an already-routed dependency, not as the child of A-EVT-04 |

### Identifier boundary

- Branch A package: `experiment_id = ent:KOD-E2E-WORK-01`; `task_id = task:activation-work-e2e-01`.
- Branch B SIS preparation and OPERATOR blocker: `experiment_id = ent:SIS-WORK-E2E-01`; `task_id = task:SIS-WORK-E2E-PR-01`.
- These identifiers are not interchangeable and must not be auto-merged by filename similarity, topic similarity, or publication order.

## Transport lifecycle audit

The table deliberately keeps publication, dispatch, inbox publication, receipt, acceptance, and activation evidence separate.

| Semantic artifact | Publication | Dispatch | Inbox publication | Receipt | Acceptance | Real Entity processing |
|---|---|---|---|---|---|---|
| SIS boundary blocker | proven at `c0d2471…` | proven at `a8ee29c…` | proven; pointer blob `2b02139…` | proven at `c00c0de…`, blob `2397d2c…`; `RECEIVED_AND_REVIEWED` | evidence boundary reviewed only; paired KOO decision is explicitly separate | not proven; activation record blob `6d9e07b…` says `processing_started: no`, `activation_failed` |
| SHT classification | proven at `cb29832…` | proven at `b3a9827…` | proven; pointer blob `cf54e5a…` | `UNKNOWN`; exact expected receipt path absent and sender registry has `receipt: null` | `UNKNOWN` | not proven; activation record blob `4322f99…` says `processing_started: no`, `activation_failed` |
| KOO bounded decision to KOD | proven at `d69f622…` | proven at `fa0e54e…` | proven; pointer blob `60b2ab9…` | `UNKNOWN`; exact expected receipt path absent | authorization is the artifact content; recipient receipt remains `UNKNOWN` | not proven; activation record blob `90d65ea…` says `processing_started: no`, `activation_failed` |
| KOD package to KOO | proven at `2564c42…` | proven at `3cc4a17…` | proven; pointer blob `5ff4277…` | `UNKNOWN`; exact expected receipt path absent and sender registry has `receipt: null` | original package acceptance `UNKNOWN`; later acceptance concerns the separate KOD blocker | not proven; activation record blob `2db08f6…` says `processing_started: no`, `activation_failed` |
| KOO blocker to OPERATOR | proven at `055e84f…` | proven at `e82b53e…` | proven; pointer blob `f1313ea…` | explicitly `null`; no receipt artifact found | explicitly `null` | not proven; activation record blob `aad0c91…` says `processing_started: no`, `activation_failed` |

The five activation records prove detector handling and a failed activation request at the current adapter boundary. They do not prove a real ChatGPT Entity start. No worker-local marker is promoted to Entity execution evidence.

## Answers to pilot questions

### 1. Are the original fields sufficient?

No. `event_id`, `event_type`, `subject_entity`, `object_id`, source identity, event time source, state pair, verification flag, links, and evidence boundary are a useful core, but they cannot prevent the observed branch merge or lifecycle conflation.

Minimum candidate additions:

- `experiment_id` and `task_id`;
- `actor_id` and `recipient_entity`;
- `source_event_id` distinct from `related_event_ids`;
- `evidence_level` (`DIRECT`, `LINKED`, `RELATED`, `UNPROVEN`);
- `branch_status` (`ROOT`, `CONTINUATION`, `FORK`, `BRIDGE`);
- `transport_stage` (`artifact_publication`, `dispatch`, `inbox_publication`, `receipt`, `acceptance`, `activation_attempt`);
- `decision_scope`, `result_class`, and `acceptance_scope`;
- separate `event_time`, `publication_time`, and `time_semantics`;
- `activation_evidence_scope` to distinguish detector/worker evidence from real Entity processing.

This is a candidate field delta only, not a schema or validator implementation.

### 2. What remains ambiguous?

- the exact parent event for `A-EVT-03`; its content cites KOD feasibility, not `A-EVT-02`;
- whether KOD explicitly received/read `A-EVT-03`; dispatch and inbox exist, but receipt does not;
- whether KOO received/accepted the original `A-EVT-04` package; later acceptance is for a separate KOD blocker;
- any OPERATOR receipt, acceptance, task creation, or product run;
- true domain event times; Git commit timestamps are publication times only;
- any exact Entity processing instance identity.

All are preserved as `UNKNOWN` or `UNPROVEN`.

### 3. Which transitions are deterministic from repository evidence?

- `A-EVT-01 → A-EVT-02`: yes, explicit source reference.
- `A-EVT-03 → A-EVT-04`: linked at bounded task/result level by Exchange Gate evidence and matching experiment semantics; receipt/acceptance are not implied.
- `B-EVT-01 → B-EVT-02`: yes, explicit immutable source reference.
- `A-EVT-04 → A-EVT-05 → A-EVT-06`: yes for package re-verification, blocker, and KOO corroboration acceptance.
- `A-EVT-06 ↔ B-EVT-02`: related external dependency, not a state-transition edge.

Not deterministic: `A-EVT-02 → A-EVT-03` and `A-EVT-04 → B-EVT-02`.

### 4. Which metrics are calculable now?

Safe bounded metrics:

- exact semantic artifacts inspected: `8`;
- requested five semantic nodes with immutable identity verified: `5/5`;
- requested five nodes with dispatch and inbox publication verified: `5/5`;
- requested five nodes with an exact receipt: `1/5`;
- inspected activation records reporting real processing start: `0/5`;
- strict requested parent/child edges proven: `2/4`; one edge is linked only at bounded task/result level and one is invalid as a direct edge;
- distinct experiment/task branches: `2`.

Commit-time deltas may be computed only as publication deltas. They are not decision latency, delivery latency, processing latency, or acceptance latency.

### 5. What is invalid or unsafe to calculate?

- full activation-lineage success rate;
- real Entity activation rate from worker markers;
- decision or processing latency from Git commit time;
- delivery/acceptance completion from dispatch or inbox publication;
- a single end-to-end state transition across the displayed five nodes;
- any metric that merges the KOD and SIS experiment identifiers.

### 6. Minimal contract delta

Adopt the added fields above and enforce three normalization rules at research-contract level:

1. A parent edge requires `source_event_id` backed by an explicit artifact reference and immutable identity, or an exact Exchange Gate task/result binding. Topic/time proximity is insufficient.
2. Different `experiment_id` or `task_id` values create separate branches unless a later artifact explicitly declares a bridge; a bridge does not rewrite historical parentage.
3. Publication, dispatch, inbox publication, receipt, acceptance, activation attempt, and processing start are separate event types. `processing_started` is valid only with evidence whose scope is the real target Entity instance.

No production policy, normative architecture, tokenomics decision, validator, schema, or automation change is made here.

## Pilot conclusion

status: `NORMALIZED_WITH_EXPLICIT_UNKNOWN_AND_BRANCH_SPLIT`

The repository supports a useful event dataset only if lineage identity and transport stage are first-class. The requested apparent chain is analytically valuable precisely because it demonstrates the failure mode: a human-readable narrative can look linear while immutable evidence shows two branches, one later corroboration bridge, missing receipts, and no real Entity processing start.

Machine-readable research candidate:
`entities/volonter/outbox/VOL__activation-lineage-events-v01.jsonl`

required_action: KOO may review the research result and decide whether to adopt, revise, or reject the candidate contract delta. No implementation or KOD dispatch is requested.
