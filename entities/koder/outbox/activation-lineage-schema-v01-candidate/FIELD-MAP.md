# Activation-lineage v0.1 candidate — field map

status: `CANDIDATE_FOR_ORG_REVIEW`
basis_records: 24
schema_target: one JSONL record
project_time: omitted; trusted project-time source not used

## Structural fields

| Field | Structural type / enum | Nullable | Boundary |
|---|---|---:|---|
| `event_id` | non-empty string | no | Identity shape only. Global uniqueness is cross-record. |
| `event_type` | bounded enum of 12 observed v0.2 event classes | no | v0.1 candidate intentionally has no `real_processing_start` class. |
| `subject_entity` | non-empty string | no | No authority inferred from name. |
| `object_id` | non-empty string | no | Object reference, not proof of lineage by itself. |
| `experiment_id` | string or null | yes | Required on semantic records; absent on transport records. Cross-record separation requires validator. |
| `task_id` | string or null | yes | Required on semantic records; absent on transport records. Cross-record separation requires validator. |
| `actor_id` | non-empty string | no | Actor label only. |
| `recipient_entity` | non-empty string | no | Addressing is not receipt or acceptance. |
| `source_event_id` | string or null | yes | Null iff `source_relation` is null; referenced-record existence is cross-record. |
| `source_artifact` | non-empty string | no | Locator only; actual immutable identity requires Git readback. |
| `source_commit` | 40 lowercase hex or null | yes | Null is allowed for current activation records whose commit was not loaded. Hex shape is not proof of existence. |
| `source_blob` | 40 lowercase hex | no | Shape only; actual bytes require Git readback. |
| `event_time` | RFC3339 date-time or null | yes | In current v0.2 candidate always null. Must not be inferred from Git publication time. |
| `publication_time` | RFC3339 date-time or null | yes | Loaded Git commit time only for the explicit publication-time semantic class. |
| `time_semantics` | 4-value enum observed in v0.2 | no | Controls structural null/non-null time shape; provenance/equivalence remains external evidence. |
| `previous_state` | string or null | yes | Record claim, not independent proof. |
| `new_state` | non-empty string | no | For transport event classes current exact states are structurally fixed. |
| `evidence_level` | `DIRECT | LINKED | LINKED_EXCHANGE_GATE` | no | Does not widen `verification_scope`. |
| `decision_scope` | non-empty string | no for semantic | Required on semantic records; forbidden on transport records. |
| `result_class` | non-empty string | no for semantic | Required on semantic records; forbidden on transport records. |
| `branch_status` | `ROOT | CONTINUATION | FORK | BRIDGE | TRANSPORT` | no | `TRANSPORT` triggers separate lifecycle constraints. |
| `transport_stage` | `artifact_publication | acceptance | dispatch | inbox_publication | receipt | activation_attempt` | no | Semantic and transport stage sets are structurally separated. |
| `acceptance_status` | `PROVEN | UNKNOWN | NOT_APPLICABLE` | no | `PROVEN` structurally requires non-null exact scope; all transport records are forced to `NOT_APPLICABLE`. |
| `acceptance_scope` | non-empty string or null | yes | String only when status is `PROVEN`; null otherwise. Scope must not widen cross-record. |
| `activation_evidence_scope` | non-empty string or null | yes | Describes bounded activation evidence; it is not processing evidence. |
| `evidence_boundary` | non-empty string | no | Human-readable bounded claim; future validator must not infer stronger evidence from adjacent records. |
| `source_relation` | `causal_parent | transport_predecessor | bridge_reference | null` | yes | Relation type is explicit. Current v0.2 records use causal, transport, and null; cross-branch bridges are additionally carried in `bridge_reference_event_ids`. |
| `bridge_reference_event_ids` | array of unique non-empty strings | no | Duplicate IDs within one record are rejected structurally; target existence/self-reference/append-only semantics are cross-record. |
| `event_claim_verified` | boolean | no | Verification flag for current record claim only. |
| `verification_scope` | constant `current_event_record_claim_only` | no | Prevents interpreting verification as acceptance/activation/processing proof. |

## Event-family structural separation

### Semantic records

`branch_status != TRANSPORT` requires:
- `experiment_id`;
- `task_id`;
- `decision_scope`;
- `result_class`.

Their `transport_stage` is limited to `artifact_publication` or `acceptance`; `source_relation` is limited to `causal_parent`, `bridge_reference`, or null.

### Exchange Gate / activation transport records

`branch_status = TRANSPORT`:
- permits only `dispatch`, `inbox_publication`, `receipt`, `activation_attempt`;
- forces `source_relation = transport_predecessor`;
- forces `acceptance_status = NOT_APPLICABLE`;
- forces `acceptance_scope = null`;
- forbids `experiment_id`, `task_id`, `decision_scope`, `result_class` on the transport record itself;
- forbids bridge references on the transport record.

Exact event-class state constraints in v0.1 candidate:
- `dispatch_published` → stage `dispatch`, state `dispatched`;
- `inbox_locator_published` → stage `inbox_publication`, state `addressed`;
- `receipt_published` → stage `receipt`, state `RECEIVED_AND_REVIEWED`;
- `activation_attempt_recorded` → stage `activation_attempt`, state `activation_failed`.

These constraints deliberately prevent current transport evidence from being relabeled as acceptance or real processing.

## Acceptance boundary

Structural JSON Schema can express:
- exact status enum;
- `PROVEN` requires a non-empty scope;
- `UNKNOWN`/`NOT_APPLICABLE` require null scope;
- transport lifecycle records cannot claim `PROVEN`.

JSON Schema alone cannot prove that the immutable artifact cited by a semantic acceptance event actually contains the asserted acceptance. That remains evidence readback plus future validator work.

## Time boundary

For `time_semantics = github_commit_created_at_is_publication_time_not_domain_event_time`:
- `publication_time` must be a date-time;
- `event_time` must remain null.

For the three current “timestamp not loaded/source push/activation record not loaded” semantics:
- `publication_time` remains null;
- `event_time` remains null.

A future rule that populates semantic `event_time` requires an explicit schema revision/evidence rule; v0.1 does not silently equate it with Git time.

## Bridge representation

The relation concept `bridge_reference` is retained in the relation vocabulary, but current v0.2 cross-branch bridges are represented by later records carrying `bridge_reference_event_ids` while preserving their causal parent in `source_event_id`. This allows one record to have both a causal parent and a non-causal cross-branch reference without rewriting the earlier event.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать field semantics, nullable/enum boundaries и structural/cross-record split
СТАТУС: CANDIDATE_FOR_ORG_REVIEW
