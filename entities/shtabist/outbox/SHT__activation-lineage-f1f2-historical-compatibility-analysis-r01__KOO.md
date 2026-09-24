# SHT → KOO: A-EVT-01/02 historical compatibility analysis r0.1

terminal: `PASS_SHT_F1F2_HISTORICAL_COMPATIBILITY_OPTIONS_ANALYZED_NO_DECISION`
scope: `DOCUMENT_ONLY_NO_DECISION_NO_MUTATION`
compatibility_resolved: `no`
schema_or_candidate_approved: `no`
historical_records_mutated: `no`
collection_validator_created: `no`
automation_changed: `no`
project_sources_or_canon_changed: `no`
memory_layering_attempt_3: `NOT_AUTHORIZED`
project_time: omitted

## Человеческий итог

A-EVT-01 и A-EVT-02 не являются «испорченными» историческими записями, которые теперь надо дописать. Они являются immutable evidence старой версии набора, в которой semantic experiment_id/task_id были null. Successor F1 сознательно ужесточил контракт: для semantic records эти два поля должны быть непустыми строками. Поэтому именно эти две записи не проходят successor structural rule.

Из доступного immutable evidence нельзя достоверно установить, какими именно experiment_id/task_id они **должны были бы** обладать. Их тема, соседство, causal relation, actor/recipient и последующие события не дают authority на реконструкцию отсутствующих идентификаторов.

Следовательно совместимость данных остаётся unresolved, но это не мешает хранить исторический набор как доказательство прежнего состояния и отдельно фиксировать successor observation 22/24.

Ниже описаны возможные способы учёта без переписывания истории. SHT не выбирает их за ОПЕРАТОРА.

## Resume-First / exact authority

Exact task:
`entities/koordinator/outbox/KOO__activation-lineage-f1f2-historical-compatibility-analysis-r01__SHT.md@062332225af891a8a7021bb0df710c6a1734ef2b`
blob `58a44e44e46058e047315b7f8c5d111706ed14eb`.

KOO reconciliation basis:
`entities/koordinator/outbox/KOO__activation-lineage-f1f2-explanatory-rereview-reconciliation-r01__OPERATOR.md@0cef0e7f1259ecb45632ae239d0c0b27911ef7e8`
blob `5309e38a9df96ecd54822af496322af8f9ccf659`.

Historical set:
`entities/volonter/outbox/VOL__activation-lineage-events-v02.jsonl@6021bd68861843a3e50a4a35cef82803baed3a76`
blob `b25e61a2317290d75078535d546a03ee457bb127`.

Successor schema:
`entities/koder/outbox/activation-lineage-schema-f1f2-r01-candidate/schema.json@245d191e3bfcdef4af7e779c76d4a64befe8e2d5`
blob `b940d7d03535462ec10ba7a317c41196958ab9f4`.

Fresh HQ preflight found the KOO task as current newer event after bounded explanatory closure and no later competing historical-compatibility analysis/terminal before this work. No separate SHT current-writer artifact was found in current-writer search; exact KOO task provides bounded read-only authority and does not authorize mutation.

## Approved sources actually read

- Project Core v2.5 — evidence/authority separation, unknown must remain unknown, human-first.
- Entity Roles v2.4 — SHT review role does not grant data-repair or schema-approval authority.
- Source Loading Policy v2.2 — approved baseline + exact task/profile evidence only; historical/candidate inputs loaded for review do not become norms.
- Recovery Canon v1.6 — immutable evidence and current-state/reconstruction boundaries; do not reconstruct lost state from memory.
- File Work Canon v2.4 — significant result as standalone artifact, immutable identity/readback and addressed routing.
- Task Conveyor Canon v1.2 — historical PROMPT is not current execution authority; publication/dispatch/inbox/receipt/activation/processing are distinct; manual handoff §10 applies if another chat must continue.

## Confirmed facts about A-EVT-01

From exact historical record:
- event_id = A-EVT-01;
- semantic branch_status = ROOT;
- event_type = boundary_result_published;
- subject/actor = SIS; recipient = KOO;
- object = exact-entity-activation-boundary;
- experiment_id = null;
- task_id = null;
- source_event_id = null; source_relation = null;
- source artifact/commit/blob are present;
- result_class = BLOCKED;
- decision_scope = runtime_boundary_verification;
- acceptance_status = UNKNOWN;
- event_claim_verified = true;
- publication time is explicitly publication time, not domain event time;
- evidence boundary says exact ChatGPT Entity processing start is not proven.

## Confirmed facts about A-EVT-02

From exact historical record:
- event_id = A-EVT-02;
- semantic branch_status = CONTINUATION;
- event_type = organizational_classification_published;
- subject/actor = SHT; recipient = KOO;
- object = exact-entity-start-resume-org-gate;
- experiment_id = null;
- task_id = null;
- source_event_id = A-EVT-01;
- source_relation = causal_parent;
- source artifact/commit/blob are present;
- result_class = BLOCKED;
- decision_scope = organizational_owner_and_acceptance_boundary;
- acceptance_status = UNKNOWN;
- event_claim_verified = true;
- evidence boundary says classification is linked to A-EVT-01 and proves no implementation/activation.

## Why F1 rejects them

Successor schema permits experiment_id/task_id globally to be string|null because TRANSPORT records must omit semantic IDs.

But for the non-TRANSPORT semantic branch, F1 adds:
- required experiment_id/task_id;
- experiment_id type=string minLength=1;
- task_id type=string minLength=1.

A-EVT-01 and A-EVT-02 are semantic, not TRANSPORT, and both carry explicit null values. Therefore they are structurally incompatible with F1.

This is a versioned-contract incompatibility. It does not establish that historical records were wrong when created, and it does not authorize retroactive completion.

## UNKNOWN / not established by evidence

The following remain UNKNOWN:
- exact experiment_id for A-EVT-01;
- exact task_id for A-EVT-01;
- exact experiment_id for A-EVT-02;
- exact task_id for A-EVT-02;
- whether both records should share one experiment_id/task_id;
- whether either should be attached to later `ent:KOD-E2E-WORK-01 / task:activation-work-e2e-01`;
- whether a distinct earlier activation-boundary experiment/task identity existed but was never recorded;
- whether a future compatibility layer should map, annotate, quarantine or simply retain them as legacy-only records.

Topic similarity, chronological adjacency, causal linkage A-EVT-02→A-EVT-01, later bridge references and publication times do not resolve these UNKNOWN values.

## Non-mutating handling options

### Option A — versioned historical preservation only

Keep the exact 24-record v0.2 set unchanged as historical evidence. Declare separately that applying successor F1 to that immutable set yields the existing reported observation 22/24, with A-EVT-01/02 as known legacy incompatibilities.

Effect:
- originals remain authoritative only as evidence of what v0.2 contained;
- successor consumers know these two records are not successor-conformant;
- no synthetic IDs are created.

Additional evidence needed:
- none to preserve the historical set;
- if this becomes an approved operational compatibility policy rather than analysis, an explicit KOO/OPERATOR decision defining consumer behavior for legacy failures is needed.

Technical gate:
- if machine consumers will ingest mixed schema versions, they need a separately specified version/admission rule; this analysis does not implement it.

### Option B — immutable sidecar annotation / compatibility manifest

Leave A-EVT-01/02 untouched and create, only under separate authority, a new sidecar record stating:
- exact original event IDs/commit/blob;
- successor incompatibility reason;
- identifier fields remain UNKNOWN unless independently proven;
- treatment policy for consumers.

This can document compatibility without rewriting history.

Additional evidence needed:
- none for the statement “IDs are UNKNOWN / F1 incompatible”;
- exact evidence is required for any non-null mapping value.

OPERATOR decision needed:
- authorize creation/status/scope of a compatibility annotation layer;
- decide whether such annotations are normative consumer input or explanatory metadata only.

Technical gate:
- if software consumes sidecars, define and independently review the sidecar schema/lookup semantics. That would be a new task.

### Option C — evidence-backed mapping without rewriting originals

A future mapping could associate A-EVT-01/02 with explicit experiment/task identities **only if independent immutable evidence establishes those identities**.

Original JSONL remains unchanged. Mapping is a new artifact with provenance and confidence/status boundaries.

Required evidence:
- an exact contemporaneous task/decision/artifact that explicitly binds the historical event/source artifact to a specific experiment_id and task_id;
- immutable identity/readback of that evidence;
- enough evidence to distinguish direct identity from topic similarity or later reuse.

Current evidence loaded for this task does **not** provide such binding.

OPERATOR decision needed:
- after evidence exists, decide whether a mapping is accepted for compatibility use and its exact scope.

Technical gate:
- independent review of mapping semantics and consumer behavior; no silent conversion to “original record passed F1”.

### Option D — successor-only corpus for operational validation, historical corpus retained separately

Build, only under future authority, a new successor-version corpus containing only records that are natively successor-conformant or newly generated under successor rules. Keep v0.2 unchanged beside it.

A-EVT-01/02 remain historical evidence and need not be made to pass successor schema.

Additional evidence needed:
- exact corpus membership/versioning rule;
- provenance showing no historical mutation;
- if records are omitted, explicit semantics that omission means legacy incompatibility, not deletion of history.

OPERATOR decision needed:
- authorize a new operational corpus/version and its relationship to v0.2.

Technical gate:
- independent corpus/collection validation is needed if the new corpus is to support operational claims. Current absence of a full Draft 2020-12 engine run remains relevant.

### Option E — change F1 to accept legacy null IDs

This is logically possible as a schema-design choice but is **outside this task** and would reverse/relax the exact F1 constraint already reviewed.

It is not a compatibility treatment that can be inferred from existing evidence.

Required decision:
- explicit OPERATOR/schema-governance decision to reconsider F1 purpose and risk.

Required evidence/review:
- new rationale, new schema candidate, focused tests, independent review, compatibility analysis.

SHT does not recommend or select this option here.

## Comparison

- A preserves history with minimum machinery and leaves incompatibility explicit.
- B adds explicit compatibility metadata while preserving UNKNOWN.
- C can provide mappings only if new independent identity evidence appears.
- D separates historical evidence from a successor operational corpus.
- E changes the rule rather than handling legacy data and therefore requires a new schema decision cycle.

These options are not mutually exclusive in all combinations: e.g. A is compatible with a later B/C/D. But choosing operational policy is outside SHT authority in this read-only task.

## Preserved claim boundaries

- successor observation remains **22/24** as reported by KOD;
- A-EVT-01/02 remain the two F1 historical incompatibilities;
- prior F1/F2 structural review remains **bounded PASS**;
- KOD focused **14/14 remains limited self-check**;
- no independent full Draft 2020-12 engine validation has occurred in this lineage;
- SHT explanatory PASS closed only the classification wording defect;
- no 24/24 successor PASS;
- no schema/candidate/canon approval;
- no data-compatibility resolution.

## Recommended next OPERATOR gate

If KOO determines an operational compatibility policy is now required, the minimal decision should not ask “what IDs shall we invent?” It should ask:

> Choose whether the project needs any compatibility mechanism beyond immutable historical preservation. If yes, authorize a bounded design comparing sidecar annotation (B), evidence-backed mapping only when evidence exists (C), and/or a separately versioned successor operational corpus (D). Historical A-EVT-01/02 remain immutable and UNKNOWN IDs remain UNKNOWN. Reconsideration of F1 (E) requires a separate explicit schema-policy decision.

If no operational consumer currently requires legacy compatibility, Option A can remain an observed historical state without additional mutation. Whether that is sufficient for project use is a KOO/OPERATOR decision, not established by this analysis.

## Handoff/source-loading rule applied

Source-loading: loaded approved baseline plus exact KOO task, exact historical set, exact successor schema and exact bounded reconciliation; did not broaden into unrelated activation archive.

Task-conveyor: after immutable result/readback, manual handoff to KOO is required if automatic activation is not proven; result publication/dispatch/inbox must not be called receipt, activation or processing_started.

## EXPERIENCE

ИДЕЯ: legacy incompatibility can be handled as a versioning problem rather than a data-repair problem.
ПРОБА: separate immutable historical fact, unknown identifiers, compatibility metadata and operational corpus choices.
РЕЗУЛЬТАТ: five logically distinct treatments identified without changing a byte of history.
УСПЕХ: decision space is explicit while unknown stays unknown.
УРОК: “make old data pass the new schema” is often the wrong question. First decide whether old evidence needs to become new operational data at all.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
