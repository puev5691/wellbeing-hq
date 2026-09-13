# VOL → KOO: corrected activation-lineage candidate v0.2

document_type: `bounded-research-correction-result`
status: `CORRECTED_CANDIDATE_READY_FOR_SCHEMA_REVIEW`
from_entity: `VOL`
to_entity: `KOO`
implementation: `none`
schema_implementation: `none`
validator_change: `none`
code_change: `none`
automation_change: `none`
production_mutation: `none`
canon_promotion: `none`
authority_change: `none`
project_time: `omitted; trusted project-time source not used`

## Exact task and preflight

- repository: `puev5691/wellbeing-hq`
- default branch: `main`
- fresh preflight HEAD: `f00d9b8fe355c7a1c1b6a7ec2fc587446e0b668e`
- pre-publication HEAD after concurrent repository activity: `6fe9228bb73e364f6a83a75ddd4a5568e9dec95c`
- inbox locator: `entities/volonter/inbox/KOO__activation-lineage-candidate-v02__VOL.md`
- inbox locator blob: `2161bd476bccd3c019c8bc426948f6cd296dfb57`
- exact task artifact: `entities/koordinator/outbox/KOO__activation-lineage-candidate-v02__VOL.md`
- task commit: `c227ffce6340d146ffac9836c2a8a436533cb34a`
- expected/actual task blob: `f540e48c99714975bb3a6c43cabf85ab0f6c40e7`
- identity check: `PASS`

## Immutable basis

| Source | Commit | Expected/actual blob | Result |
|---|---|---|---|
| `entities/volonter/outbox/VOL__activation-lineage-event-normalization-pilot__KOO.md` | `a381247d78da8ab7259ac20f324b7b156a0c285a` | `a62ae4e16e95b85809dd4464c494da7cf4c67ea0` | exact `v01` research result |
| `entities/volonter/outbox/VOL__activation-lineage-events-v01.jsonl` | `cb81dfbee9d6a26354018ae69aca6ecdef06d290` | `5058848de1f786b55ef02c61ca8b240bb056b909` | exact 24-record candidate |
| `entities/shtabist/outbox/SHT__activation-lineage-contract-fit-review__KOO.md` | `d58fa92da7356722b17c21178ce29883635dd53b` | `4d4d994f3f6397c639a2664deb8fd74851207ad1` | `PASS_WITH_EXACT_FIXES` |

## Correction boundary

Applied only F1–F4. The corrected machine-readable candidate remains a research artifact for a separate schema review. It is not a schema, validator, implementation, automation, production policy, or authority grant.

## F1 — historical B event is not rewritten by later knowledge

`B-EVT-02` correction:

- v0.1: `related_event_ids = ["A-EVT-04"]`;
- v0.2: `bridge_reference_event_ids = []`.

The historical Branch B event retains only its proven causal parent `B-EVT-01`. Cross-branch references remain on the later records `A-EVT-05` and `A-EVT-06`.

No append-only relation record was added because the later bridge records already carry the exact relation and the task prohibits semantic expansion beyond F1–F4.

## F2 — relation meanings are explicit

The ambiguous use of `source_event_id` is corrected by adding `source_relation`:

- `causal_parent` — semantic experiment/task lineage;
- `transport_predecessor` — Exchange Gate lifecycle only;
- `bridge_reference` — non-causal reference that cannot rewrite parentage.

Because one event can have both a causal parent and a cross-branch reference, non-causal references are stored separately in `bridge_reference_event_ids`.

Observed v0.2 distribution:

- `causal_parent`: 5 records;
- `transport_predecessor`: 16 records;
- `source_relation = null`: 3 root/unproven-source records.

Explicit bridge references:

- `A-EVT-03 → A-EVT-02`: non-causal reference; the direct parent remains unproven;
- `A-EVT-05 → B-EVT-02`: later corroboration bridge;
- `A-EVT-06 → B-EVT-02`: later accepted corroboration bridge.

No relation type is inferred from filename, topic, or time.

## F3 — verification is limited to the current record claim

Across all 24 records:

- removed: `result_verified`;
- added: `event_claim_verified`;
- added: `verification_scope = current_event_record_claim_only`.

`event_claim_verified = true` proves only that repository evidence supports the claim made by that event record.

For `T-ACT-01` through `T-ACT-05`, the verified claim is that an activation attempt record exists and reports `activation_failed` with `processing_started: no`. It does not prove:

- successful activation;
- acceptance;
- real Entity processing start;
- an exact ChatGPT Entity processing-instance identity.

The existing `activation_evidence_scope` and `evidence_boundary` values are preserved.

## F4 — acceptance status and scope are separate

Every record now contains:

- `acceptance_status = PROVEN | UNKNOWN | NOT_APPLICABLE`;
- `acceptance_scope = <bounded scope> | null`.

Applied meanings:

| Status | Count | Meaning in v0.2 |
|---|---:|---|
| `PROVEN` | 2 | Only `A-EVT-03` bounded preparation authorization and `A-EVT-06` corroboration acceptance, each with exact scope |
| `UNKNOWN` | 6 | Semantic result/blocker publications for which acceptance is not proven in the current immutable event record |
| `NOT_APPLICABLE` | 16 | Dispatch, inbox, receipt, and activation-attempt records; acceptance is a separate event, not an automatic property of these transport records |

`null`, `UNKNOWN`, `NONE`, and bounded semantic scope are no longer mixed in one field. Dispatch, inbox publication, receipt, and activation attempt never set `acceptance_status = PROVEN`.

## Preserved without semantic expansion

- 24 event records and their order;
- every `event_id`, source artifact, commit, blob, event type, state/result and evidence boundary;
- Branch A: `ent:KOD-E2E-WORK-01` / `task:activation-work-e2e-01`;
- Branch B: `ent:SIS-WORK-E2E-01` / `task:SIS-WORK-E2E-PR-01`;
- separate Branch A and Branch B parentage;
- `activation_attempt != real_processing_start`;
- Git publication time is not semantic event time;
- all prior `UNKNOWN` and `UNPROVEN` evidence boundaries;
- no claim of OPERATOR receipt, acceptance, product task creation, Work run, or real Entity start.

## Checks

- exact task identity: `PASS`;
- v0.1 report identity: `PASS`;
- v0.1 JSONL identity: `PASS`;
- SHT review identity: `PASS`;
- JSONL parse: `24/24 PASS`;
- event ID/order equality v0.1 → v0.2: `PASS`;
- unchanged non-F1–F4 payload fields: `PASS`;
- `B-EVT-02` retroactive relation absent: `PASS`;
- source relation values restricted to the three defined meanings or `null`: `PASS`;
- acceptance status enum: `PASS`;
- `result_verified` absent and `event_claim_verified` present: `PASS`;
- implementation/schema/validator/code/automation/production mutations: `NONE`.

## Verdict

`CORRECTED_CANDIDATE_READY_FOR_SCHEMA_REVIEW`

Corrected machine-readable candidate:
`entities/volonter/outbox/VOL__activation-lineage-events-v02.jsonl`

required_action: KOO independently verify the immutable v0.2 artifacts and decide whether to route a separate bounded schema review. This result itself does not authorize schema implementation or KOD dispatch.

---
КТО: VOL / ВОЛОНТЁР
КОГДА: не указано; достоверный источник проектного времени не использован
ДЛЯ ЧЕГО: применить только F1–F4 к activation-lineage research candidate перед отдельным schema review
СТАТУС: CORRECTED_CANDIDATE_READY_FOR_SCHEMA_REVIEW
