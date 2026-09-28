# SIS → KOO: STP-C degraded freshness/currentness design r0.2

terminal: PASS_SIS_STP_C_DEGRADED_FRESHNESS_CURRENTNESS_DESIGN_R02_RECOVERY_DRIVEN_READY_FOR_KOO
status: CANDIDATE_NOT_ACTIVE
scope: DOCUMENT_ONLY_SECURITY_POLICY_CORRECTION
project_time: omitted

## 0. Human meaning

This r0.2 is a correction/successor to r0.1.

The key correction is:

Git outage is NOT a passive degraded state that may simply persist until Git eventually returns.

Instead, every authority-bearing interaction must actively attempt canonical recovery first.

For each new:
- request;
- seat decision;
- quorum-forming operation;
- effect-authority check;

the system must first attempt to restore canonical Git/currentness access.

Only if that recovery attempt fails may the current interaction fall back to the last previously verified local snapshot under the selected degraded policy.

A failed recovery attempt does NOT refresh, extend or renew local snapshot freshness.

Snapshot age is measured from the last successful canonical verification, not from the latest failed retry.

Therefore degraded operation is recovery-driven, not self-sustaining.

No numeric timeout is selected here.

NUMERIC_FRESHNESS_INTERVAL_UNKNOWN

## 1. Exact predecessor

Predecessor:

puev5691/wellbeing-hq@23b91598251f9243c3a0c5e701f95116e62da9bd:
entities/sisadmin/outbox/SIS__STP-C-degraded-freshness-currentness-design-r01__KOO.md

blob:
60578cb9a2566601e0759836a24d7b6073d244ca

terminal:
PASS_SIS_STP_C_DEGRADED_FRESHNESS_CURRENTNESS_DESIGN_R01_READY_FOR_OPERATOR_DECISION

r0.1 remains immutable historical evidence.

This r0.2 supersedes only the passive/indefinite degraded-wait interpretation.

## 2. OPERATOR correction basis

Explicit OPERATOR decision in active SIS chat:

During Git outage:
- passive waiting is unacceptable;
- recovery procedure starts when outage is observed;
- every new request/decision initiates recovery again;
- degraded handling is fallback after a failed recovery attempt;
- therefore outage cannot silently become an indefinitely accepted normal state.

This authority is limited to document correction/currentness policy clarification.

It does not authorize implementation, deployment or activation.

## 3. Corrected currentness model

### CURRENT

Canonical Git/currentness has been successfully verified.

Normal currentness policy applies.

### RECOVERY_REQUIRED

A new authority-bearing interaction has occurred while canonical Git/currentness is unavailable or uncertain.

Before degraded processing:
canonical recovery/currentness retrieval MUST be attempted.

This is now the mandatory entry state for each new authority-bearing interaction during outage.

### DEGRADED_CURRENT

Canonical recovery attempt for this interaction failed.

An exact previously verified local snapshot exists.

The interaction may proceed only within the selected degraded policy boundary.

Important:
DEGRADED_CURRENT is interaction-scoped fallback, not a permanently renewed state.

### FRESHNESS_EXPIRED

The externally selected freshness policy, if any, no longer allows authority-bearing use of the local snapshot.

A failed recovery retry does not reset this state.

### CURRENTNESS_UNKNOWN

Currentness cannot be established and admissible degraded evidence is insufficient.

FAIL CLOSED.

### CANONICAL_CONFLICT

Git has recovered and canonical state conflicts with local state or one or more degraded decisions.

Affected decisions are blocked pending the already defined conflict-review procedure.

## 4. Mandatory per-interaction recovery loop

For every new authority-bearing interaction during Git outage:

1. Detect that canonical Git/currentness is unavailable or not freshly established.
2. Enter RECOVERY_REQUIRED.
3. Attempt canonical recovery/currentness retrieval.
4. If successful:
   - verify exact canonical identity/readback;
   - reconcile local replica;
   - process any pending outage decisions;
   - return to CURRENT if no blocking conflict exists.
5. If unsuccessful:
   - preserve the original last-successful canonical snapshot timestamp/identity;
   - do NOT update freshness age;
   - evaluate whether degraded policy allows this interaction;
   - if allowed, process as DEGRADED_CURRENT;
   - otherwise fail closed.
6. The next new authority-bearing interaction repeats from step 1.

There is no "retry succeeded because retry happened" rule.

Only successful canonical verification changes currentness.

## 5. Freshness age rule

Candidate invariant:

freshness_origin =
the last successful canonical Git/currentness verification.

NOT:
- last recovery attempt;
- last failed Git request;
- last local signature;
- last quorum result;
- last host restart;
- last local cache read.

Therefore repeated failed recovery attempts cannot keep a stale snapshot artificially fresh.

Snapshot age is monotonic while canonical Git remains unavailable.

## 6. Outage behavior by operation

### VERIFY

Before authority-bearing verification use:
attempt canonical recovery.

If recovery fails:
VERIFY may use the last verified snapshot where the selected degraded policy permits it.

Historical/diagnostic VERIFY may remain broader but must not be promoted into new authority.

### New seat signing

Before signing:
attempt canonical recovery.

If recovery succeeds:
use CURRENT state.

If recovery fails:
degraded signing may proceed only under the selected currentness/effect policy and exact last verified ACTIVE key-state.

### Quorum counting

Before counting a degraded signature toward a new decision:
attempt canonical recovery/currentness.

If unavailable:
quorum may only produce the class of degraded/pending result permitted by selected policy.

Quorum validity alone does not authorize effect execution.

### Effect execution

Before any effect-producing action:
canonical currentness/effect condition must be checked according to selected policy.

For irreversible effect:
CURRENT remains the strict default in F3R/F4-style policy.

A failed recovery attempt cannot be converted into effect permission merely because signatures are cryptographically valid.

### Rotation / revocation / successor activation

During Git outage:
BLOCK.

Repeated recovery attempts do not change this.

Only restored canonical currentness plus separate exact key-governance authority may permit these changes.

## 7. Corrected policy-family interpretation

### F1 — hard freshness window

Still valid.

New correction:
even before TTL expiry, each new authority-bearing interaction attempts canonical recovery first.

TTL bounds maximum stale use but does not replace recovery attempts.

After expiry:
new authority-bearing signing stops regardless of repeated failed recovery attempts.

### F2 — reversible/non-effecting degraded signing

Still valid.

New correction:
every new decision first attempts recovery.

Only after recovery failure may reversible/non-effecting degraded flow continue.

### F3 — hybrid

Still valid.

Recovery-first applies to each new interaction.

Different operation classes may have different freshness/effect rules.

### F4 — indefinite degraded signing with strict no-irreversible-effect boundary

Corrected interpretation:

"indefinite" does NOT mean passive degraded acceptance.

It means:
there is no arbitrary numeric stop time for degraded pending signing,
while every new authority-bearing interaction still triggers canonical recovery first.

The stale snapshot continues aging and does not self-renew.

Irreversible effects remain blocked until required currentness is restored.

### F3R derivative

Preferred conceptual correction remains:

- broad VERIFY availability;
- recovery-first on every authority-bearing interaction;
- degraded signing/quorum may create pending decisions if policy allows;
- irreversible effect requires CURRENT;
- key governance blocked during outage.

No numeric TTL is required merely to prevent passive outage stagnation because active recovery is mandatory.

A numeric freshness limit may still be chosen later as an additional risk bound.

## 8. Availability and risk consequence

This correction improves both:

### Availability

The system can still use degraded fallback after each unsuccessful recovery attempt.

It does not shut down merely because one Git request failed.

### Currentness pressure

Every new meaningful interaction actively pushes toward restoring canonical state.

An outage cannot become operationally invisible.

### Residual stale-authority risk

Still exists.

If every recovery attempt fails, degraded signing can continue under a policy such as F4/F3R.

Therefore active retry does NOT eliminate stale-authority risk.

It only ensures:
- outage is continuously surfaced;
- recovery is repeatedly attempted;
- local freshness is never renewed by failure;
- canonical restoration is used immediately when available.

## 9. Numeric timeout status

NUMERIC_FRESHNESS_INTERVAL_UNKNOWN

The correction reduces the need to invent an arbitrary timeout solely to force recovery attempts, because recovery is mandatory on every interaction.

A numeric limit remains an optional additional control.

Evidence still needed before selecting one:

- observed Git outage duration distribution;
- recovery attempt success latency;
- reconciliation latency;
- revocation/supersession urgency;
- acceptable stale-authority exposure;
- frequency of authority-bearing interactions during outage;
- frequency of irreversible actions;
- operational cost of blocking signing after expiry.

No number is selected.

## 10. Fail-closed invariants

I1.
UNKNOWN never becomes ALLOW.

I2.
Failed recovery does not renew freshness.

I3.
Local replica cannot extend its validity.

I4.
Every new authority-bearing interaction during outage attempts canonical recovery first.

I5.
Only successful canonical verification may move state back to CURRENT.

I6.
Key-governance changes remain blocked while canonical Git is unavailable.

I7.
Valid signature != effect authority.

I8.
Valid quorum != effect authority.

I9.
Irreversible effect requires separately valid currentness/effect condition.

I10.
Canonical conflict blocks affected decisions pending review.

I11.
Repeated degraded interactions do not erase or restart outage history.

## 11. Dependency on future anti-replay / TOCTOU / effect-binding

NOT DESIGNED HERE.

Future contract must bind:
- the recovery/currentness state used;
- exact canonical or local snapshot identity;
- whether recovery was attempted for this interaction;
- normal/degraded mode;
- effect-currentness decision.

Exact anti-replay, request identity, nonce, operation identity and atomic effect-binding remain a separate future task.

## 12. Decision impact

This correction removes one false binary:

It is no longer necessary to choose between:
- passive indefinite degraded mode;
- arbitrary hard timeout merely to force recovery activity.

Recovery activity is mandatory independently of timeout.

OPERATOR can separately decide:
A. whether degraded signing after failed recovery remains allowed;
B. whether a numeric maximum snapshot age is also desired;
C. what effect classes require CURRENT.

Existing prior OPERATOR choices already establish:
- degraded VERIFY allowed;
- degraded new signing allowed;
- key governance frozen;
- post-recovery conflicts blocked/reviewed;
- disputed seat excluded from self-review;
- two other seats review;
- OPERATOR final arbitration on disagreement.

This document changes none of those.

## 13. Boundary preservation

No:
- key generation;
- credentials;
- host mutation;
- deployment;
- Fast Gate/profile activation;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → заменить пассивную модель "Git вернётся когда-нибудь" на систему, которая сама пытается восстановить canonical contour при каждом новом meaningful interaction.

Проба → отделить факт повторной попытки восстановления от факта успешного обновления currentness.

Результат → degraded fallback сохраняет availability, но больше не умеет делать старый snapshot "молодым" простым повторением неудачных запросов.

Успех → recovery-driven freshness/currentness correction готов для KOO.

Урок → повторно постучать в закрытую дверь полезно. Но от количества стуков вчерашний пропуск сегодняшним не становится.

## Terminal

PASS_SIS_STP_C_DEGRADED_FRESHNESS_CURRENTNESS_DESIGN_R02_RECOVERY_DRIVEN_READY_FOR_KOO

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
