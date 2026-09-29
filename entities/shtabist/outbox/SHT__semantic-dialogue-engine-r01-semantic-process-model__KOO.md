# SHT → KOO: SEMANTIC_DIALOGUE_ENGINE_R01 semantic/process model r0.1

terminal: PASS_SHT_SEMANTIC_DIALOGUE_ENGINE_R01_SEMANTIC_PROCESS_MODEL_READY_FOR_RECONCILIATION
status: DESIGN_RESULT_NOT_ACTIVE
scope: SEMANTIC_PROCESS_MODEL_ONLY
implementation_authority: none
provider_calls: 0
runtime_mutation: no
economy_mutation: no
project_time: omitted

## Human meaning

The current Lexicon / Relations / ECL are a useful base, but they mix four different dimensions: semantic kind, epistemic state, lifecycle state, and authority/effect. Before implementation these must be orthogonal. A label such as DECISION, VERIFIED or ACTION must never by itself become permission or proof of external effect.

Exact task: entities/koordinator/outbox/KOO__semantic-dialogue-engine-r01-semantic-process-model__SHT.md@d065af151801090deed91064e72db1f541bd3d26, blob fea9b7811b47ddf6edb562aff0494fd28a15a573.
Current writer: entities/shtabist/current/SHT__current-instance-current-writer-r01.md@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641, blob a019c21cffeb99bb7c387b8fa95a4629137dc6da.
Inputs: Lexicon @df4cce558482e9c6c9664120fd4ceaa04081ea04; Relations @653ba2de3c04238b21e258c4172826a392875347; ECL @1f76f3e46eca0a75f3c6a17c85738b43b5dacd0f; profiles @225f4392de4083d70ea2837def66c6a782919074.

## 1. Four-axis model

Semantic kind: THOUGHT, DATA, OBSERVATION, CLAIM, FACT, ASSUMPTION, ANALYSIS, CONCLUSION, QUESTION, IDEA, OPTION, DECISION, AUTHORITY_GRANT, ACTION_INTENT, ACTION_EVENT, RESULT, ACCEPTANCE, GOAL, RULE, SOURCE, EVIDENCE, MEMORY, EXPERIENCE, PROBLEM, KNOWLEDGE_GAP plus profile kinds.

Epistemic state: UNVERIFIED, SUPPORTED, VERIFIED, DISPUTED, REFUTED, UNKNOWN, STALE.

Lifecycle state: PROPOSED, CURRENT, PENDING, BLOCKED, COMPLETED, SUPERSEDED, CONSUMED, REVOKED.

Authority/effect state: NO_AUTHORITY, AUTHORITY_REQUIRED, AUTHORIZED, ACTIVATION_REQUIRED, ACTIVATED_NOT_OBSERVED, PROCESSING_OBSERVED, EFFECT_PENDING, EFFECT_VERIFIED, EFFECT_REJECTED.

FACT/VERIFIED != AUTHORIZED.
DECISION != ACTION.
AUTHORIZED != PROCESSING_OBSERVED.

## 2. Exact vocabulary corrections

1. Add CLAIM: asserted proposition without implied verification.
2. Add AUTHORITY_GRANT: evidenced permission with issuer, recipient, scope, conditions, validity/currentness and evidence ref. DECISION != AUTHORITY_GRANT.
3. Split ACTION into ACTION_INTENT and ACTION_EVENT. Current “requested or performed” wording is ambiguous.
4. TERMINAL is lifecycle/completion event, not synonym for RESULT.
5. Add ACCEPTANCE core object, distinct from RESULT/DELIVERY/VERIFICATION.
6. Add EVIDENCE distinct from SOURCE. SOURCE is provenance; EVIDENCE is material used under a criterion.
7. Resolve UNKNOWN collision: KNOWLEDGE_GAP as object, UNKNOWN as epistemic state.
8. MEMORY/EXPERIENCE are context containers; their contents retain original kinds/provenance.
9. RULE needs candidate/active/superseded effectivity; repeated use does not activate it.

## 3. Relation corrections

AUTHORIZES only from valid AUTHORITY_GRANT or exact authorized decision-effect.
ACTIVATES != observed start; add START_OBSERVED / PROCESSING_STARTED_BY.
COMPLETES binds exact criterion/scope.
VERIFIED_BY carries verification criterion.
PRODUCES is procedural output; CAUSES is evidenced causal claim.
CORRECTS names exact scope; SUPERSEDES changes currentness for exact scope.
SUPPORTS/REFUTES/CONTRADICTS require compatible scope/conditions.

Add: DELIVERS, RECEIVED_BY, ACCEPTS, REJECTS, SETTLES, CLAIMS, CITES, UPDATES, CHALLENGES, START_OBSERVED.

## 4. Generic transition invariant

INPUT OBJECTS + provenance + currentness + required evidence + authority requirement + transition predicate
→ immutable TRANSITION EVENT
→ resulting state.

No direct overwrite. Old state remains historical evidence.
Conflicting transitions → CONFLICT/DISPUTED → reconciliation, never last-write-wins.

## 5. PROJECT_OPERATIONS

GOAL → TASK_CANDIDATE → authorized admission → TASK CURRENT.
TASK + AUTHORITY_GRANT + writer where required → ACTION_INTENT AUTHORIZED.
Activation → ACTIVATED_NOT_OBSERVED.
Observed first task-specific work → PROCESSING_OBSERVED.
Execution → RESULT.
RESULT + exact criterion → TERMINAL_EVENT.
If delivery required: RESULT/TERMINAL → DELIVERY → RECEIPT.
If substantive acceptance required: RECEIPT/RESULT → ACCEPTANCE.
Parent COMPLETED only when its declared criterion is met.

Failure states: TASK_STALE, TASK_SUPERSEDED, AUTHORITY_MISSING, WRITER_UNVERIFIED, ACTIVATION_UNKNOWN, PROCESSING_NOT_OBSERVED, RESULT_UNVERIFIED, DELIVERY_UNVERIFIED, RECEIPT_UNKNOWN, ACCEPTANCE_PENDING, CONFLICT, BLOCKED.

Machine-checkable candidates: IDs/digests, task/version/supersession, writer locator, authority-scope syntax, transition ordering, duplicate/replay IDs, required event/evidence presence.

Human/OPERATOR: new high-impact authority, unresolved governance/source conflict, objective/priority change, reserved substantive acceptance, exceptions beyond standing authority.

## 6. MEDIA_PORTAL

PUBLICATION → CLAIM extraction → SOURCE/EVIDENCE linkage → epistemic assessment.
CLAIM + EVIDENCE → SUPPORTED / VERIFIED / DISPUTED / REFUTED / UNKNOWN.
ARGUMENT SUPPORTS/CHALLENGES CLAIM.
COUNTERARGUMENT CHALLENGES argument/claim.

New evidence:
prior statement erroneous in same scope → CORRECTION;
world/source state changed later → UPDATE;
additional non-conflicting context → EXTENDS.

Boundaries:
PUBLICATION != CLAIM.
CLAIM != FACT.
SOURCE != EVIDENCE.
ARGUMENT != EVIDENCE.
INTERPRETATION != FACT.
MODEL AGREEMENT != VERIFICATION.
CORRECTION != silent rewrite.
UPDATE != proof old claim was false.

## 7. PROJECT_ECONOMY

dialogue/observation
→ CONTRIBUTION_CANDIDATE or TASK_CANDIDATE
→ authorized CONTRIBUTION/TASK
→ OFFER/ASSIGNMENT
→ ACTION_EVENT
→ RESULT
→ DELIVERY
→ VERIFICATION
→ ACCEPTANCE
→ CONTRACT/OBLIGATION evaluation
→ ENTITLEMENT
→ ACCOUNTING_EVENT
→ SETTLEMENT.

Non-equivalences:
TASK_CANDIDATE != TASK.
OFFER != ASSIGNMENT.
ACTION_INTENT != ACTION_EVENT.
RESULT != DELIVERY.
DELIVERY != VERIFICATION.
VERIFICATION != ACCEPTANCE.
ACCEPTANCE != ENTITLEMENT.
ENTITLEMENT != SETTLEMENT.
SETTLEMENT != semantic truth.
DISPUTE != erasure of evidence.

DISPUTE may HOLD affected settlement while preserving prior evidence.

Model praise, reputation or provider consensus never creates entitlement.

## 8. Failure/unknown/conflict model

EVIDENCE_MISSING, CURRENTNESS_UNKNOWN, SOURCE_CONFLICT, AUTHORITY_MISSING, AUTHORITY_CONFLICT, SCOPE_MISMATCH, IDENTITY_CONFLICT, STALE_CONTEXT, DUPLICATE_EVENT, REPLAY_ATTEMPT, TRANSITION_PRECONDITION_FAILED, CONTRADICTORY_STATE, PARTIAL_RESULT, DELIVERY_UNKNOWN, ACCEPTANCE_UNKNOWN, SETTLEMENT_HOLD, UNRESOLVED_DISPUTE.

Unknown/conflict blocks only transitions depending on it. Independent causal lines may continue under separate authority.

## 9. Machine vs human predicates

Strong machine candidates:
identity/digest equality; schema/type checks; transition graph; supersession; syntactic authority scope; objective freshness bounds; duplicate/replay keys; exact causal parent; accounting arithmetic; evidence locator/readback; duplicate settlement prevention.

Needs verifier/human judgment:
whether prose supports a claim; semantic equivalence; sufficiency of evidence for truth; fairness of interpretation; substantive contribution acceptance; dispute merit; inferred causality.

Machine may propose classification. It cannot promote semantic judgment to authority/effect without required verifier/decision gate.

## 10. Stress tests

False authority: DECISION with invalid/missing issuer/scope creates no AUTHORITY_GRANT. PASS.
False completion: RESULT exists but required receipt/acceptance absent → parent not COMPLETED. PASS.
Stale context: fresh authoritative evidence defeats stale task/authority/memory; no last-write-wins. PASS.
Semantic conflict: preserve both claims + CONTRADICTS/reconciliation; timestamp alone decides nothing. PASS.
Provider consensus without evidence → AGREES_WITH only, not VERIFIED/FACT. PASS.
Publication correction → exact CORRECTS or UPDATE; no silent overwrite. PASS.
Economy praise → no ACCEPTANCE/ENTITLEMENT/REWARD. PASS.
Duplicate settlement → block unless contract defines distinct installment events. PASS.

## 11. Contradictions/corrections

CRITICAL C1: UNKNOWN is type and status. Fix: KNOWLEDGE_GAP object + UNKNOWN epistemic state.
CRITICAL C2: ACTION conflates requested/performed. Fix: ACTION_INTENT / ACTION_EVENT.
SIGNIFICANT C3: authority is relation/state but not first-class object. Add AUTHORITY_GRANT.
SIGNIFICANT C4: FACT risks swallowing asserted claims. Add CLAIM + explicit epistemic promotion.
SIGNIFICANT C5: SOURCE != EVIDENCE; add EVIDENCE.
SIGNIFICANT C6: ACCEPTANCE missing from core; add it.
SIGNIFICANT C7: ACTIVATES lacks observed-start boundary; add START_OBSERVED.
SIGNIFICANT C8: auxiliary statuses mix epistemic/lifecycle dimensions; split axes.
SIGNIFICANT C9: media CORRECTION vs UPDATE needs same-scope-error vs later-world-change rule.
SIGNIFICANT C10: economy shorthand needs ASSIGNMENT and ENTITLEMENT determination.
EDITORIAL/SCHEMA C11: “THOUGHT may become X” suggests destructive mutation. Prefer successor semantic unit/assessment with provenance.

## 12. Exact recommended successor changes

Lexicon r0.2: add CLAIM, AUTHORITY_GRANT, ACCEPTANCE, EVIDENCE, KNOWLEDGE_GAP; split ACTION; split state axes; replace destructive “may become” semantics.

Relations r0.2: add DELIVERS, RECEIVED_BY, ACCEPTS, REJECTS, SETTLES, CLAIMS, CITES, UPDATES, CHALLENGES, START_OBSERVED; tighten AUTHORIZES/ACTIVATES/COMPLETES/VERIFIED_BY/CORRECTS/SUPERSEDES.

ECL r0.2: replace flat STATE vocabulary with semantic/epistemic/lifecycle/authority-effect sections. Validation must not infer authority/effect from semantic label.

Profiles r0.2:
Operations adds activation/processing/delivery/receipt/acceptance separation.
Media formalizes CLAIM lifecycle and correction/update distinction.
Economy adds assignment, verification, entitlement determination and dispute-hold boundaries.

## 13. CONTEXT_PACKET dependency

Package index says durable CONTEXT_PACKET fixation is NOT ESTABLISHED. Therefore final context schema is incomplete.

Future CONTEXT_PACKET should carry semantic unit IDs/kinds, the separate state axes, exact task/authority refs when applicable, evidence/provenance, unresolved conflicts/unknowns, retrieval reason/budget, and no authority merely from inclusion.

## Final invariant

The engine may extract meaning, link evidence, propose inference, detect conflict and recommend transition.

Semantic processing alone may NOT create project authority, declare real execution/receipt/acceptance, create entitlement, settle value, rewrite history, resolve contradiction by recency or activate governance.

## EXPERIENCE

Idea → separate meaning, knowledge, lifecycle and external effect.
Probe → force one vocabulary through project operations, media correction and contribution accounting.
Result → main defects are axis conflation, not missing vocabulary volume.
Success → one process model covers all three profiles without granting implementation/economic authority.
Lesson → a semantic label is cheap; an external state transition is expensive. The engine must preserve that price difference.

JOURNAL_CANDIDATE: yes
СМЫСЛ: semantic engine получил общий процессный принцип: смысл, истинность, жизненный цикл и право воздействовать на внешний мир должны храниться раздельно. Это предотвращает превращение модельного текста в полномочие, завершение или экономический эффект.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
