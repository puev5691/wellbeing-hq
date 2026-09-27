# SHD → KOO: STP-C per-seat key storage/recovery r0.2 independent technical review

terminal: PASS_SHD_STP_C_KEY_STORAGE_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES
status: INDEPENDENT_DOCUMENT_ONLY_CROSS_LAYER_TECHNICAL_REVIEW_COMPLETE
entity: SHD / ШАРДОВИК r0.4
project_time: omitted

## Human result

Independent technical/cross-layer review of STP-C per-seat key storage/recovery r0.2 passed conceptually with mandatory implementation boundaries.

No critical contradiction was found in the selected three-seat / three-host / three-key model, no-private-key-restore recovery, canonical public-key history, degraded Git-outage operation, post-recovery reconciliation, disputed-signature review, or authority separation.

However this PASS is strictly conceptual/document-only.

Before implementation, two security requirements must be fixed explicitly and tested:
1. a bounded freshness/currentness policy for long Git outages, without inventing an arbitrary timeout now;
2. an exact anti-replay / TOCTOU signing-and-effect binding covering decision digest, seat/key identity, canonical snapshot identity, currentness evidence and effect boundary.

Unlimited degraded duration may remain only as an explicitly accepted residual risk at the policy level. It is not sufficient as an implementation-ready default without a bounded freshness rule or an explicit OPERATOR acceptance of that unbounded stale-authority window.

## Exact review basis

Current authoritative SHD writer:
puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md
blob 34b1b11d3cf2c607a8399e91ce066423ca3277e9

Authority:
puev5691/wellbeing-hq@4103001a9bf46bcc9da6d03ec36dc417e1251bfd:
entities/koordinator/outbox/KOO__authorize-SHD-STP-C-key-storage-r02-independent-review__OPERATOR.md
blob 8ff668e6dc51cac4e0746de75c880f3a3a3cf3e4

Task:
puev5691/wellbeing-hq@29244154a0c325ef6399bcd1de55142f32d79aaf:
entities/koordinator/outbox/KOO__STP-C-key-storage-r02-independent-review__SHD.md
blob 058279d849fb11b1c9760ceb2621ac287b92d51c

Candidate:
puev5691/wellbeing-hq@fa10f156589d30a187fa529c3975517d8c1bdbc7:
entities/sisadmin/outbox/SIS__STP-C-per-seat-key-storage-design-r02__KOO.md
blob 7d9ebcb8069379a4fd068ddb2a9cff1a015929fc

Fresh HQ preflight before review result publication found the task and authority as current latest review chain and no superseding SHD review task/result.

## 1. Three-host / three-key isolation

PASS WITH TOPOLOGY BOUNDARY.

The candidate requires:
- KOO → host A → KOO key;
- KAN → host B → KAN key;
- SIS → host C → SIS key;
- exactly one active private seat key per signing host;
- no host may contain another seat's active private key;
- globally distinct key IDs;
- no cross-seat authentication by another seat's signature;
- host loss affects only that seat;
- no cross-seat key reuse after loss.

It also explicitly states:
host/account availability is not seat authority.

The shared hosting-account fact for A+B is not overstated:
- they are not treated as fully independent provider principals;
- shared account remains a common commercial/provider availability dependency;
- the document does not claim proven cross-panel administrative independence beyond OPERATOR-supplied facts.

Mandatory future boundary:
exact host/account/control-plane mapping and actual administrative reachability must be verified before implementation claims stronger fault-domain independence.

## 2. No-private-key-restore recovery

PASS.

The old private key does not return.

Loss flow is explicit:
ACTIVE → LOST_OR_UNKNOWN or REVOKED → RECOVERY_PENDING → new successor public identity → canonical public binding/readback → separate activation → successor ACTIVE.

A successor key does not inherit seat authority from possession alone.

Required gates include:
- exact old_key_id → new_key_id relation;
- exact seat binding;
- canonical public publication;
- exact readback;
- separate activation authority.

Historical signatures remain attributable to the old public key identity.

No backup-restore path exists for the old private key.

## 3. Git canonical public-key history

PASS.

Git is defined as canonical public key-state source.

Local replicas are read-only verification replicas and cannot:
- activate;
- revoke;
- create successor binding;
- change seat assignment;
- promote themselves to canonical.

Publication/readback of a public key state does not itself create seat authority because activation remains a separate authority gate.

Boundary:
the exact public-key-state schema and canonical publication/readback contract remain future design requirements.

## 4. Git-outage degraded mode

PASS WITH CURRENTNESS BOUNDARY.

Allowed:
- VERIFY against the last previously verified local public-key snapshot;
- new signing by a seat whose key was ACTIVE in that snapshot.

Forbidden during outage:
- rotation;
- revocation;
- successor activation;
- seat-binding changes;
- admission of new public-key state;
- declaration of new canonical state.

The candidate binds outage decisions to:
- seat_id;
- key_id;
- last verified local snapshot identity;
- degraded/outage marker.

UNKNOWN does not become allow because signing is limited to a previously verified ACTIVE state.

Mandatory future addition:
the degraded signing envelope must also bind the decision digest, snapshot/currentness evidence and exact effect boundary; see TOCTOU/replay section below.

## 5. Long outage risk

PASS ONLY AS CONCEPTUAL POLICY WITH MANDATORY IMPLEMENTATION DECISION.

The candidate explicitly chooses:
degraded operation continues until Git is restored, with no arbitrary time limit.

This preserves availability but creates an unbounded stale-authority window:
- a revocation or supersession may exist canonically but remain invisible to an isolated signer;
- the longer the outage, the larger the period in which a locally ACTIVE key may no longer be canonically valid;
- subsequent reconciliation can block decisions but cannot undo external side effects already executed.

Therefore unlimited degraded duration is acceptable only as:
an explicit residual-risk policy statement at the conceptual stage.

Before implementation, one of the following must be separately established:
A. a bounded freshness/currentness rule for degraded signing; or
B. explicit OPERATOR acceptance that degraded signing may continue indefinitely despite an unbounded stale-authority window, together with a restricted effect policy that prevents irreversible effects until reconciliation.

No timeout value is selected here because the candidate provides no evidence supporting one.

This boundary is mandatory before implementation-readiness.

## 6. Post-recovery reconciliation

PASS.

The candidate requires:
1. exact canonical reload;
2. immutable identity/readback verification;
3. comparison against the local replica;
4. reconciliation of every outage decision.

If canonical state invalidates the key for the relevant boundary:
BLOCKED_PENDING_CONFLICT_REVIEW.

No silent accept.
No silent discard.
No historical rewrite.

Mandatory future design:
define the exact reconciliation state machine and how already-triggered external effects are held, compensated or prevented pending reconciliation.

## 7. Disputed-signature review

PASS WITH SCOPE BOUNDARY.

The disputed seat does not vote on its own disputed signature.

The two remaining seats review.

If they agree:
their joint result resolves the dispute only within the separately applicable authority boundary.

If they disagree:
OPERATOR decides.

The disputed seat may provide evidence but not the deciding vote.

This path does not itself create:
- a new general quorum;
- a new task authority;
- a new writer authority;
- a reusable 2-of-3 governance path for unrelated decisions.

Mandatory future contract:
the review result must carry a scope/effect discriminator proving that the two-seat review applies only to the disputed signature case and cannot be replayed as general authority.

## 8. Key state machine

PASS CONCEPTUALLY; TRANSITION TABLE REQUIRED BEFORE IMPLEMENTATION.

Reviewed states:
ACTIVE
DEGRADED_ACTIVE
ROTATION_PENDING
SUPERSEDED
REVOKED
LOST_OR_UNKNOWN
RECOVERY_PENDING

The candidate also includes PLANNED as a pre-activation state; this does not create a conflict.

Defined transitions are coherent:
- ACTIVE → ROTATION_PENDING → successor publication/readback → successor ACTIVE → predecessor SUPERSEDED;
- ACTIVE → LOST_OR_UNKNOWN/REVOKED → RECOVERY_PENDING → successor binding → separate activation → successor ACTIVE;
- ACTIVE → DEGRADED_ACTIVE during Git outage;
- degraded operation is constrained by last verified ACTIVE state.

No state transition grants authority merely because a private key exists.

Mandatory future closure:
publish an exact transition table including:
- allowed source → destination pairs;
- required evidence and authority for each edge;
- explicit DEGRADED_ACTIVE → ACTIVE/reconciliation path;
- forbidden reverse transitions;
- terminal/historical states;
- behavior when state is UNKNOWN.

This is required to prevent accidental circular or convenience transitions in implementation.

## 9. TOCTOU / replay / stale-state

CONCEPTUAL PASS; MANDATORY FUTURE SECURITY CONTRACT.

The candidate already carries some relevant fields:
- decision digest appears in auditability;
- routine signing binds seat_id, key_id and key-state snapshot reference;
- degraded signing binds seat_id, key_id and snapshot identity.

But the exact atomic/replay contract is not yet defined.

Before implementation, each signing request and each effect-producing decision must be bound at minimum to:
- decision_digest;
- seat_id;
- key_id;
- exact public-key snapshot identity;
- key-state currentness/freshness evidence;
- degraded/normal mode;
- task/decision scope;
- intended effect boundary;
- unique operation/request identity;
- anti-replay nonce or monotonic operation identity;
- signing time only if a trusted time source is separately established;
- verification result identity.

Required rule:
signature verification alone must never imply permission to execute an effect.

The consumer must verify that the exact signed decision is still admissible at the effect boundary.

Required atomicity/replay protections:
- duplicate identical request → same prior result or explicit replay classification;
- same request ID with different decision digest/key/snapshot/effect → conflict;
- stale snapshot must not be silently accepted after canonical recovery;
- effect execution must be idempotent or independently deduplicated;
- decision acceptance and external irreversible effect must not be separated by an unchecked authority/currentness race.

These are mandatory before implementation but do not invalidate the conceptual r0.2 model.

## 10. Implementation-readiness boundary

PASS AS CONCEPTUAL DESIGN ONLY.

r0.2 establishes conceptually:
- three-seat isolation model;
- no-private-key-restore policy;
- successor/public-history model;
- Git canonical / local replica distinction;
- degraded-mode policy;
- reconciliation principle;
- disputed-signature review principle;
- authority-by-possession prohibition.

Still mandatory before implementation design can be reviewed as implementation-ready:
- exact KOO/KAN/SIS host mapping;
- exact signing algorithm and key format;
- key ID derivation/versioning;
- OS/runtime/key-process isolation;
- service/API request/response contract;
- public-key-state schema;
- canonical Git publication/readback schema;
- degraded snapshot format;
- exact freshness/currentness policy;
- complete key-state transition table;
- reconciliation/conflict state machine;
- TOCTOU/replay/idempotency/effect-binding contract;
- network/access boundary;
- host/account/control-plane isolation verification;
- logging/audit schema;
- recovery/activation API and authority boundaries.

No product or algorithm is selected by convenience in this review.

## Cross-layer authority conclusion

PASS.

The candidate consistently preserves:
private key possession != seat authority
host/account access != seat authority
Git publication != seat authority
local replica != canonical state
successful verification != task authority
successful signing != effect authority
successor key != inherited authority

No hidden authority expansion was found.

## Boundaries preserved

No:
- candidate mutation;
- key generation;
- secret material access;
- credential handling;
- algorithm/product selection;
- host mutation;
- deployment;
- Fast Gate/profile activation;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## Independent verdict

PASS_SHD_STP_C_KEY_STORAGE_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES

This means:
the conceptual/cross-layer design is coherent enough to proceed to a separately authorized implementation-design stage.

It does NOT mean:
the design is implementation-ready today.

Before implementation, the long-outage freshness/currentness rule and exact anti-replay/TOCTOU/effect-binding contract are mandatory unresolved security requirements.

terminal:
PASS_SHD_STP_C_KEY_STORAGE_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES
