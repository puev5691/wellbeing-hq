# SIS → KOO: STP-C degraded freshness/currentness design r0.1

terminal: PASS_SIS_STP_C_DEGRADED_FRESHNESS_CURRENTNESS_DESIGN_R01_READY_FOR_OPERATOR_DECISION
status: CANDIDATE_NOT_ACTIVE
scope: DOCUMENT_ONLY_SECURITY_POLICY_DESIGN
project_time: omitted

## 0. Human meaning

This document defines candidate freshness/currentness policy families for prolonged Git outage.

The core problem is not signature verification itself.

The problem is stale authority:
a signing host may still see a seat key as ACTIVE in its last verified local replica while canonical Git already contains revocation, supersession or another key-state change.

Post-recovery reconciliation can detect that mismatch, but it cannot automatically undo an irreversible external effect already executed during the outage.

Therefore this design separates:

1. VERIFY;
2. new seat signing;
3. quorum counting;
4. effect execution;
5. key-governance mutation.

A valid signature is never treated as effect authority by itself.

No numeric freshness interval is selected.

NUMERIC_FRESHNESS_INTERVAL_UNKNOWN

## 1. Exact basis

Exact authority:

puev5691/wellbeing-hq@c0d6c157c7d1ebb9ba7b304d10def6f8fb48ade4:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-degraded-freshness-currentness-design-r01__OPERATOR.md

blob:
f6ce454646a332cd7324e08a5851327ac5404761

Exact task:

puev5691/wellbeing-hq@3bf43d18661d7124a2ec2a24330a2ed9cc414a19:
entities/koordinator/outbox/KOO__STP-C-degraded-freshness-currentness-design-r01__SIS.md

blob:
cca6c101b7ce9b923f6f71d286b91a7193b38acf

Exact SHD review:

puev5691/wellbeing-hq@342e28309b1aed48505f0feb6eadcd8a9e5808ca:
entities/shardovik/outbox/SHD__STP-C-key-storage-r02-independent-review__KOO.md

blob:
6efd2cb71d8ff6be248f1c2abc33ac39ccb4f6fa

terminal:
PASS_SHD_STP_C_KEY_STORAGE_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES

Exact reviewed candidate:

puev5691/wellbeing-hq@fa10f156589d30a187fa529c3975517d8c1bdbc7:
entities/sisadmin/outbox/SIS__STP-C-per-seat-key-storage-design-r02__KOO.md

blob:
7d9ebcb8069379a4fd068ddb2a9cff1a015929fc

## 2. Exact risk

### R1 — invisible canonical revocation/supersession

During Git outage, a host may possess a previously verified local snapshot in which a key is ACTIVE.

Canonical Git may meanwhile contain:
- revocation;
- supersession;
- successor activation;
- seat-binding change;
- another currentness change.

The isolated host cannot know this.

Therefore:
LAST_VERIFIED_ACTIVE != CURRENT_CANONICAL_ACTIVE

unless canonical currentness is freshly established.

### R2 — stale-authority window

The longer degraded signing continues without canonical reconciliation, the longer a stale key may continue producing cryptographically valid signatures.

Signature validity remains mathematically correct while authority/currentness may be stale.

### R3 — irreversible external effect

Post-recovery reconciliation can:
- detect conflict;
- block later acceptance;
- trigger review.

It cannot necessarily undo:
- an external publication;
- a destructive mutation;
- an irreversible payment/action;
- a physical act;
- any other non-compensable effect.

Therefore irreversible effect execution needs a stricter currentness/effect condition than VERIFY.

## 3. Hard invariants

I1.
UNKNOWN never becomes ALLOW.

I2.
FRESHNESS_EXPIRED never silently resets itself.

I3.
A local replica cannot extend, renew or re-issue its own validity/currentness.

I4.
Git outage never permits:
- rotation;
- revocation;
- successor activation;
- seat-binding change;
- admission of a new public-key state;
- creation of a new canonical key state.

I5.
Valid signature != effect authority.

I6.
Quorum-valid signatures != automatic effect authority.

I7.
Irreversible effect requires a separately valid effect/currentness condition.

I8.
Degraded signing must bind to the exact last verified key-state snapshot identity.

I9.
After canonical recovery, all degraded decisions are reconciled against exact canonical state.

I10.
CANONICAL_CONFLICT never silently resolves by "latest local wins".

I11.
Freshness policy is external policy.
A signer cannot decide that its own state is fresh enough.

I12.
No numeric timeout is invented without evidence.

## 4. Currentness states

### CURRENT

Meaning:
canonical Git state has been successfully verified under the currently approved currentness rule.

Properties:
- canonical key-state identity known;
- no unresolved canonical/local conflict;
- normal policy may apply.

### DEGRADED_CURRENT

Meaning:
Git is unavailable, but an exact previously verified local canonical snapshot exists and remains within the selected degraded policy.

Properties:
- local snapshot identity fixed;
- no local self-extension;
- key governance frozen;
- allowed operations depend on selected F-policy.

### FRESHNESS_EXPIRED

Meaning:
the selected freshness rule no longer permits new authority-bearing use of the local snapshot.

Properties:
- state cannot renew itself;
- VERIFY behavior may still differ from signing/effect behavior;
- only canonical recovery or separate OPERATOR intervention can move policy forward.

### CURRENTNESS_UNKNOWN

Meaning:
currentness cannot be established and no admissible degraded state applies.

Examples:
- no previously verified snapshot;
- local snapshot identity missing/corrupt;
- freshness evidence unavailable;
- state transition ambiguous.

Default:
FAIL CLOSED.

### CANONICAL_CONFLICT

Meaning:
after Git recovery, canonical key-state conflicts with the local state used for one or more degraded decisions.

Properties:
- affected decisions blocked;
- disputed-signature review applies;
- no silent acceptance or deletion of historical evidence.

## 5. Operation behavior by currentness state

| State | VERIFY | New seat signing | Quorum counting | Effect execution | Rotation/revocation/successor activation |
|---|---|---|---|---|---|
| CURRENT | ALLOW under normal verification policy | ALLOW under normal seat policy | ALLOW under normal quorum policy | ALLOW only if separate effect authority/currentness conditions pass | ALLOW only under separate exact key-governance authority |
| DEGRADED_CURRENT | ALLOW against exact last verified snapshot | Depends on F1/F2/F3/F4 | Depends on F-policy and decision class | Restricted; never implied by signature/quorum alone | BLOCK |
| FRESHNESS_EXPIRED | VERIFY may remain ALLOW for historical/diagnostic use | BLOCK unless explicit selected policy says otherwise | BLOCK for new authority-bearing decisions by default | BLOCK | BLOCK |
| CURRENTNESS_UNKNOWN | VERIFY only if explicitly historical and not used as authority; otherwise BLOCK | BLOCK | BLOCK | BLOCK | BLOCK |
| CANONICAL_CONFLICT | VERIFY historical evidence preserved | BLOCK affected key/decision path pending review | BLOCK affected decision pending review | BLOCK affected decision | BLOCK until conflict resolved and canonical state re-established |

## 6. Policy family F1 — hard freshness window

Definition:

A degraded snapshot has an externally defined freshness lifetime/window.

Before expiry:
degraded signing may be allowed according to the policy.

After expiry:
new signing stops.

No number is selected here.

### Availability impact

LOWER.

A long Git outage eventually stops new signing/quorum formation.

VERIFY can remain available for historical/diagnostic purposes.

### Stale-authority risk

LOWER than indefinite signing.

Risk is bounded by the selected freshness interval, subject to correct outage detection/currentness evidence.

### After expiry allowed

Candidate:
- historical signature VERIFY;
- local integrity checks;
- non-authoritative diagnostics;
- preparation of blocked decisions for later reconciliation.

### After expiry blocked

- new seat signing;
- quorum counting for new authority-bearing decisions;
- effect execution based on degraded authority;
- all key-governance changes.

### When OPERATOR is needed

- to select the policy family;
- to approve numeric interval once evidence exists;
- optionally to handle prolonged outage where business continuity requires an exception.

No automatic exception.

### Evidence needed for numeric interval

At minimum:
- observed Git outage duration distribution;
- recovery/availability history;
- expected revocation urgency;
- maximum tolerated stale-authority exposure;
- operational criticality of decisions;
- expected frequency of irreversible/effect-producing actions;
- reconciliation latency;
- ability to detect canonical recovery promptly.

Status:
NUMERIC_FRESHNESS_INTERVAL_UNKNOWN.

## 7. Policy family F2 — degraded signing only for reversible/non-effecting decisions

Definition:

Degraded signing may continue without a hard numeric cutoff, but only for decisions that are reversible or have no external effect until reconciliation.

### Availability impact

HIGH for planning/governance preparation.

LOWER for actual external effects.

### Stale-authority risk

MODERATE.

Stale signatures may accumulate, but their impact is constrained because they cannot trigger irreversible effects before reconciliation.

### Allowed during prolonged outage

Candidate classes:
- internal proposal;
- draft decision;
- review statement;
- reversible queueing;
- non-effecting approval intent;
- evidence acknowledgement;
- other explicitly classified reversible/non-effecting decisions.

This design does not define those classes exhaustively.

### Blocked

- irreversible effect;
- destructive mutation;
- externally final publication if irreversible by policy;
- key governance;
- any action whose effect cannot be safely held or reversed.

### When OPERATOR is needed

- to approve the classification policy for reversible/non-effecting actions;
- to resolve ambiguous action class;
- to authorize exceptional effect if a future policy permits one.

### Evidence needed

- action/effect taxonomy;
- reversibility guarantees;
- compensation semantics where applicable;
- proof that deferred effect execution is technically enforceable.

Residual risk:
misclassification of an action as reversible when it is not.

## 8. Policy family F3 — hybrid currentness policy

Definition:

Different operations have different currentness strictness.

Candidate structure:

VERIFY:
broadest availability.

New signing/quorum:
allowed under degraded policy within a bounded or class-based condition.

Effect-producing actions:
stricter currentness requirement.

Irreversible effect:
requires CURRENT or separately approved exceptional condition.

### Availability impact

BALANCED.

Verification and low-risk decision flow continue longer than high-impact execution.

### Stale-authority risk

LOWER for effects than pure indefinite degraded signing.

Moderate for queued/deferred decisions.

### After signing freshness expires

Candidate:
- VERIFY continues;
- historical signature attribution continues;
- preparation/reconciliation data continues;
- new signing may stop or be restricted by decision class;
- effect execution remains blocked unless CURRENT.

### Blocked

At minimum:
- key governance during outage;
- irreversible effect without CURRENT;
- unknown-class effect.

### When OPERATOR is needed

- to select exact operation classes;
- to decide numeric interval if any;
- to resolve ambiguous effect class;
- to approve exceptional continuity rule if later desired.

### Evidence needed

Same as F1 for any numeric component, plus:
- effect taxonomy;
- reversibility evidence;
- operational action categories.

Residual risk:
policy complexity and incorrect operation classification.

## 9. Policy family F4 — indefinite degraded signing with strict no-irreversible-effect boundary

Definition:

Degraded signing and quorum may continue for the duration of Git outage with no time limit.

However:
no irreversible effect may be executed until canonical currentness is restored and reconciliation passes.

This is the closest policy family to the current r0.2 operational preference while closing SHD's irreversible-effect concern.

### Availability impact

HIGHEST for decision production.

LOWER for irreversible external execution.

### Stale-authority risk

HIGH for accumulated decision signatures.

LOWER for irreversible consequences if the no-effect boundary is actually enforced.

### Allowed

- VERIFY under last verified snapshot;
- new seat signing;
- quorum counting for decisions that remain non-effecting/pending;
- queueing of decisions awaiting currentness restoration;
- reversible/non-final actions only if separately classified.

### Blocked

- irreversible effect execution;
- key governance;
- any effect whose reversibility is UNKNOWN;
- any transition that would make local key-state canonical.

### When OPERATOR is needed

- explicit acceptance of unbounded stale-authority window;
- definition/approval of no-irreversible-effect boundary;
- arbitration of ambiguous effect type;
- post-recovery conflict path as already defined by STP-C.

### Evidence needed

- technical proof effects can be held pending reconciliation;
- effect taxonomy;
- queue durability/integrity semantics;
- assurance that downstream consumers cannot treat signature/quorum as immediate effect permission.

Residual risk:
large backlog of stale decisions and operational pressure to bypass the effect hold.

## 10. Reviewed derivative F3R — strict effect-currentness / broad verify

CANDIDATE derivative for OPERATOR consideration:

VERIFY:
allowed in DEGRADED_CURRENT from last verified snapshot.

New signing:
allowed while DEGRADED_CURRENT according to selected decision class/currentness rule.

Quorum counting:
allowed only to produce a pending decision record, not effect authority.

Effect execution:
- reversible/non-effecting class may proceed only under separately approved classification;
- irreversible effect requires CURRENT.

Key governance:
always BLOCK during Git outage.

This derivative combines F3 structure with F4's strict irreversible-effect boundary.

It does NOT select a numeric signing TTL.

Status:
CANDIDATE_ONLY.

## 11. State transitions

### Normal loss of Git availability

CURRENT
→ DEGRADED_CURRENT

Preconditions:
- exact last verified canonical snapshot exists;
- local replica integrity verified;
- selected degraded policy allows entry.

### Degraded freshness expiration

DEGRADED_CURRENT
→ FRESHNESS_EXPIRED

Trigger:
externally defined policy condition.

The signer cannot extend this state.

### Missing/ambiguous evidence

CURRENT or DEGRADED_CURRENT
→ CURRENTNESS_UNKNOWN

Examples:
- snapshot corrupt;
- snapshot identity unavailable;
- policy evidence missing;
- local currentness evidence ambiguous.

### Canonical recovery, no conflict

DEGRADED_CURRENT or FRESHNESS_EXPIRED
→ CURRENT

only after:
- exact Git current state read;
- immutable identity verified;
- local/canonical reconciliation completed;
- no unresolved conflict blocks the relevant key/decision.

### Canonical recovery with mismatch

DEGRADED_CURRENT or FRESHNESS_EXPIRED
→ CANONICAL_CONFLICT

for affected decisions/key path.

Resolution follows the separately selected disputed-outage review path.

## 12. Behavior details

### VERIFY

VERIFY is the least authority-bearing operation.

Candidate principle:
historical verification may remain available longer than signing/effect authority.

But:
VERIFY under CURRENTNESS_UNKNOWN cannot be promoted into authority or effect permission.

### New seat signing

Signing is permitted only when:
- key was ACTIVE in the exact admitted snapshot;
- currentness state/policy permits signing;
- key governance has not locally changed;
- signer binds exact snapshot identity.

Signature validity alone says nothing about effect permission.

### Quorum counting

Quorum counting must consume signatures plus currentness state.

Candidate rule:
under degraded policies, quorum may produce:
- a pending/degraded decision result;
not automatically:
- effect authority.

If any required seat state is CURRENTNESS_UNKNOWN or CANONICAL_CONFLICT:
affected quorum path fails closed.

### Effect execution

Effect execution is the strictest layer.

Irreversible effect:
requires separately valid currentness/effect condition.

Under F4/F3R:
CURRENT is required.

Under other future policy:
any exception requires explicit OPERATOR-approved rule.

### Rotation / revocation / successor activation

Always BLOCK during Git outage.

No F-family relaxes this.

## 13. Numeric freshness interval

Status:

NUMERIC_FRESHNESS_INTERVAL_UNKNOWN

Current project evidence does not support:
- 1 hour;
- 12 hours;
- 24 hours;
- 7 days;
or any other number.

Required runtime/availability evidence before choosing a number:

1. historical Git availability/outage durations;
2. detection time for Git unavailability and recovery;
3. reconciliation completion time;
4. expected frequency/urgency of revocation/supersession;
5. maximum acceptable stale-key exposure;
6. frequency and criticality of effect-producing decisions;
7. percentage of decisions that can be held without effect;
8. recovery/escalation availability of OPERATOR;
9. operational consequence of stopping signing after expiry.

Without these:
numeric TTL would be policy theatre, not evidence-based security.

## 14. Decision table for OPERATOR

| Policy family | Consequence | Evidence needed before finalization | Residual risk |
|---|---|---|---|
| F1 hard freshness window | bounds stale signing; may stop decision flow during long outage | outage history, revocation urgency, tolerated stale window, reconciliation latency | arbitrary/poorly chosen TTL can either reduce availability too much or remain too permissive |
| F2 reversible/non-effecting degraded signing | high continuity for planning; irreversible actions wait | exact reversibility/effect taxonomy and enforcement proof | misclassified "reversible" action may cause real effect |
| F3 hybrid | tailored availability/security by action class | operation/effect taxonomy plus runtime availability data for any TTL | more complex policy, more implementation error surface |
| F4 indefinite degraded signing + no irreversible effects | maximum signing/quorum availability; effects held until reconciliation | proof that irreversible effects can be technically held; explicit OPERATOR residual-risk acceptance | potentially large stale-decision backlog and pressure to bypass hold |
| F3R derivative: broad VERIFY + degraded pending decisions + CURRENT required for irreversible effects | balances long outage continuity with strict irreversible-effect gate | effect taxonomy and enforcement contract; no numeric TTL required initially | still permits stale pending signatures; anti-replay/effect-binding must later be exact |

## 15. What is sufficient for the next OPERATOR decision?

YES.

Current evidence is sufficient for one bounded policy-family decision.

The OPERATOR can choose among:
- F1;
- F2;
- F3;
- F4;
- F3R candidate derivative.

No numeric timeout decision is required at the same time.

If OPERATOR chooses a family requiring a numeric interval:
the interval remains separately blocked until runtime/availability evidence exists.

## 16. Dependency on later anti-replay / TOCTOU / effect-binding design

NOT DESIGNED HERE.

This task only establishes the dependency:

the future anti-replay/TOCTOU/effect-binding contract must consume the selected currentness state/policy and must not allow a signature/quorum result to bypass:
- freshness state;
- canonical conflict state;
- effect-currentness requirement.

Exact request IDs, nonces, operation IDs, effect tokens, atomicity and replay mechanics belong to a separate future task.

## 17. Boundary preservation

No:
- key generation;
- credential creation;
- host mutation;
- deployment;
- Fast Gate/profile activation;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → отделить возможность продолжать подписывать от права немедленно производить необратимый эффект.

Проба → сравнить четыре freshness families по тому, что происходит не с подписью, а с downstream effect после длительного Git outage.

Результат → главный рычаг политики не обязательно TTL; можно держать VERIFY/signing доступными, но жёстко удерживать irreversible effect до восстановления CURRENT.

Успех → decision-ready currentness design без выдуманного численного интервала.

Урок → протухшая подпись опасна не тем, что перестаёт проверяться математически. Опасна она тем, что кто-то слишком рано решил: "раз проверяется, значит можно исполнять". Вот этого фокуса политика и не должна позволять.

## Terminal

PASS_SIS_STP_C_DEGRADED_FRESHNESS_CURRENTNESS_DESIGN_R01_READY_FOR_OPERATOR_DECISION

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
