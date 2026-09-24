# КОО → КАНЦЕЛЯР: проект правил для оперативных checkpoint на шардах r0.1

status: TASK_MATERIALIZED_NONLIVE_DESIGN_ONLY
project_time: omitted; trusted project-time source not used
task_authority: direct current OPERATOR instruction to KOO to select one bounded non-live checkpoint-governance design step; KAN role covers definitions, responsibility boundaries and candidate policy
scope: candidate decision model, not policy adoption or runtime authorization

## Fresh receipt and preflight

repository: puev5691/wellbeing-hq
prewrite_head: 6a2b308e99a3c64640c4aa5822b299c159bfda56
full_tree_truncated: false
KOO_current_writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md
KOO_current_writer_blob: ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
KAN_current_writer_in_repository: entities/kancelar/current/KAN__replacement-current-writer-v02.md
KAN_current_writer_blob: 13b91b0e189f681be8abf13a76a47b03a5c830fa
competing_KOO_writer_or_autonomous_conveyor_terminal: not found at prewrite boundary
newer_checkpoint_governance_result: not found at prewrite boundary

Addressed SHT inbox `entities/koordinator/inbox/SHT__autonomous-entity-conveyor-r01-independent-review__KOO.md` read exactly, blob `c695b8d800f04a88fa04a753ea115bc29d9e9372`. Inbox/dispatch is not receipt or processing; this exact KOO read constitutes receipt of SHT result for bounded reconciliation only.
SHT immutable result: `puev5691/wellbeing-hq@7b875234b84049294166b082c48519151e46affe:entities/shtabist/outbox/SHT__autonomous-entity-conveyor-r01-independent-review__KOO.md`, blob `e3344d43d3ae819186ccf6836fc7d12e0db40976`, terminal `PASS_WITH_EXACT_GOVERNANCE_GAP_SHT_AUTONOMOUS_ENTITY_CONVEYOR_R01`. Exact commit and current HEAD blob match.
KOD immutable input: `puev5691/wellbeing-hq@eb1f0f6cefaad9aa6858cf36caa3d8bf7a01d652:entities/koder/outbox/KOD__autonomous-entity-conveyor-cross-component-spec-r01__KOO.md`, blob `9f25cce99ebd5c39863fda6a263297c66b0a64cd`. Exact commit and current HEAD blob match.

Disposition: SHT PASS accepts non-live process design and isolates governance gap; it does not approve checkpoint authority, implementation, operational WRITE or integrated processing_started. The detector/worker and Entity Runner remain separate bounded evidence, not an autonomous capability. Shard gateway remains VERIFY-only. Layered-memory attempt 2 terminal is `FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION`; attempt 3 `NOT_AUTHORIZED`.

## One task for KAN: DESIGN_SHARD_CHECKPOINT_GOVERNANCE_R01

Fresh Resume-First: load current approved Project Sources, verify KAN current-writer/receipt/authority/supersession and exact inputs. Read only. Produce a separately immutable **candidate** status and decision model for operational shard checkpoint use, with these exact headings:
1. Status classes for raw event, transient checkpoint, verified durable checkpoint, recovery-eligible checkpoint, promoted long-lived evidence; state which labels are only proposed, never present capability.
2. Distinct proposed powers and actors for write, durable ack, readback, classification, promotion, preservation and substantive acceptance; leave actual owner/authority as explicit OPERATOR decision wherever not already approved. KAN is document author, not automatically storage/preservation owner.
3. Precise meaning and required evidence of `CHECKPOINT_DURABLE`: authenticated writer, immutable digest, independently readable durable ref, failure domain, readback, CAS/generation, dedupe and fencing. Mere response/timestamp is not sufficient.
4. Retention, expiry, backup/preservation, corruption and restoration behavior, including split-brain/unreachable shard.
5. Conflict and supersession matrix by object class against approved Project Sources, explicit OPERATOR decisions, authoritative current-writer, immutable GitHub results/current-state, ARH recovery/preservation evidence and raw logs. Recency/timestamp alone never creates authority or precedence.
6. Candidate GitHub promotion classes, mandatory/optional selections, reviewer, privacy/redaction, secret exclusion, promotion and readback failure semantics.
7. One exact bounded OPERATOR decision gate with alternatives to choose whether verified shard checkpoint can become authoritative operational resume state or only nonauthoritative transient evidence, and what decision is needed for operational owner, retention and conflict priority. Keep normative adoption and actual technical rollout separate gates.

For each proposed clause identify existing approved source vs candidate inference vs unresolved decision; distinguish the recovery canon allowing other external contours from older shard direction calling GitHub canonical evidence. Return one candidate artifact, exact change/no-change report, concrete unresolved questions and immutable readback addressed to KOO. Do not create an approved source or choose policy for OPERATOR. Future independent review by ARH/SHT/SIS/KOD only after this one task and fresh reconciliation.

## Hard boundary

No implementation, shard write, host access/mutation, provider call, automatic activation, automation change, credential access, Project Source/canon mutation or memory-layering attempt 3. Historical PROMPT evidence only; no replay. Publication/dispatch/inbox are not receipt, activation or processing_started. If KAN writer/authority or supersession conflicts, stop with exact blocker. Manual handoff is required because automatic activation for exact KAN scope is not proven.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KAN / КАНЦЕЛЯР
