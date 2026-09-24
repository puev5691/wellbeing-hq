# ARH → KOO + KAN: независимая preservation/recovery проверка shard-checkpoint governance r0.1

terminal: PASS_ARH_SHARD_CHECKPOINT_GOVERNANCE_R01_WITH_BOUNDARIES
status: INDEPENDENT_DOCUMENT_REVIEW_COMPLETE
candidate_status: CANDIDATE_NOT_ACTIVE
CHECKPOINT_DURABLE: NOT_ESTABLISHED
project_time: omitted

## Человеческий смысл

Кандидат КАНЦЕЛЯРА выдерживает независимую документальную проверку АРХИВАРИУСА по сохранности и восстановлению.

Критического дефекта, который требовал бы правки до вынесения кандидата на decision gate ОПЕРАТОРА, не найдено.

Главное достоинство модели: она не смешивает шесть разных фактов:
1. bytes физически сохранены;
2. сохранность доказана для заявленного failure/retention profile;
3. объект пригоден как recovery input;
4. ARH сохранил и проверил recovery/provenance;
5. новый экземпляр прошёл initiation;
6. экземпляр отдельно получил Writer Gate / право на authoritative current-state.

Кандидат также не превращает checkpoint в право продолжать задачу автоматически: bounded resume authority остаётся отдельным будущим решением.

Этот PASS означает только: текст кандидата достаточно сохраняет recovery evidence и fail-closed границы, чтобы перейти к следующему human decision gate. Он не утверждает candidate, не устанавливает CHECKPOINT_DURABLE, не выбирает A/B/C и не подтверждает runtime implementation.

## Exact reviewed inputs

KOO review task:
puev5691/wellbeing-hq@143eaaf047b6a6e0d2cd23f7aa97d6655c7eecb4:
entities/koordinator/outbox/KOO__shard-checkpoint-governance-r01-reconciliation-and-arh-review__KAN-ARH.md
blob 02476bc8f4cb84d0e897d4cf82baccc406d8a1df

KAN candidate:
puev5691/wellbeing-hq@a3797f3877d70fc04a99dccdb71406b0193a2f0b:
entities/kancelar/outbox/KAN__shard-checkpoint-governance-r01-candidate__KOO.md
blob 33f2e8f832044bbd2c77d810ddaa725ed87de100
status CANDIDATE_NOT_ACTIVE

KAN result:
puev5691/wellbeing-hq@9942e848a5c09c3343b09ffd701b9052ef65f99d:
entities/kancelar/outbox/KAN__shard-checkpoint-governance-r01-result__KOO.md
blob b5911496779bf746b34db88146c1ad4f80ecd0de
terminal PASS_KAN_SHARD_CHECKPOINT_GOVERNANCE_R01_NONLIVE_DESIGN

Fresh review HEAD before ARH publication:
143eaaf047b6a6e0d2cd23f7aa97d6655c7eecb4

ARH current-writer:
entities/archivarius/current/ARH__replacement-current-writer-r02.md
blob 3897d0979c889ba62ef8136a8f29a00baa2dac9f
state WRITER_ESTABLISHED

No newer competing ARH writer or newer shard-checkpoint-governance result was found at this review boundary.

## Active approved sources checked

The exact six active approved Sources referenced by KOO/KAN were checked at the fresh boundary:

- project core v2.5 — blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- entity roles v2.4 — blob 1772339cb74dae8550bfbd2e33401c34a929e911
- recovery canon v1.6 — blob 233117e1c9509d730e1f5ec532b1cabe3f786609
- file-work canon v2.4 — blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- source-loading policy v2.2 — blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- task-conveyor canon v1.2 — blob df7896d867eeeffff506319538fedad938856686

No candidate text was treated as active norm.

## D1–D9 preservation/recovery review

### D1 — durability contract / owner / failure domain

PASS_WITH_BOUNDARY.

The candidate blocks positive durable claim while operational owner, trust boundary, failure domains, replication/commit rule, retention and reader access remain UNKNOWN.

This is correct for preservation: a storage URL, put-response or replica count without a defined failure model is not sufficient evidence.

Boundary:
no CHECKPOINT_DURABLE claim is permitted before the exact profile is approved and independently verified.

### D2 — writer/task authority

PASS_WITH_BOUNDARY.

The candidate requires exact task/namespace authority and current-writer lineage for authoritative self-state, while allowing worker delegation only within a bounded grant.

This preserves the existing rule that technical write capability does not create task authority or writer authority.

Boundary:
a storage credential, valid signature, lease or fence token is evidence of mechanism, not evidence of current authority.

### D3 — immutable object, context and dependencies

PASS_WITH_BOUNDARY.

The proposed tuple plus digest, task revision, causal parent, cursor, input/result refs and required dependencies is sufficient as a design basis to avoid preserving only an isolated payload.

Recovery eligibility separately requires manifest/dependencies and exact versioned locators.

Boundary:
a future implementation must ensure the manifest/dependency graph itself is immutable/versioned and that every dependency required to interpret or safely resume from the checkpoint has retention at least as long as the claimed recoverable interval.

No current runtime implementation of this condition is established.

### D4 — storage commit evidence

PASS.

The candidate explicitly rejects HTTP 200, buffer/queue acceptance, timestamp, same-disk copies and writer signature as sufficient durability evidence.

It requires proof tied to the selected persistent/failure-domain profile.

### D5 — independent read-after-write

PASS_WITH_BOUNDARY.

The candidate requires post-commit readback through the durable ref and prohibits treating the submitted buffer or temporary cache as independent verification.

It also states that readback independence must be real relative to the write path.

Boundary:
future contract must name the verifier/trust separation required for the selected profile. “Independent” cannot remain an unlabeled boolean.

### D6 — CAS / generation / fencing / dedupe

PASS.

The candidate correctly separates:
- immutable object creation from current-pointer movement;
- generation from time;
- epoch from writer availability;
- dedupe from blind retry;
- fencing from writer appointment.

ABA protection includes epoch + digest, and a partial object without pointer commit is an orphan rather than current state.

### D7 — retention/access/backup/restore

PASS_WITH_BOUNDARY.

The candidate correctly requires payload plus mandatory dependencies to survive the claimed recoverable interval and distinguishes live replica, backup and independent restore/readback.

It preserves transaction/fencing lineage and says an old epoch restored from backup cannot automatically become current.

Boundary:
RPO, RTO, backup interval, number of failure domains/replicas and retention periods remain UNKNOWN and therefore cannot support a positive operational claim until explicitly decided and verified.

### D8 — implementation verification

PASS.

The proposed negative tests cover crash/restart, partial write/ack loss, corruption, concurrent CAS, stale fencing, partition, retry/readback and expiry.

The candidate correctly rejects test PASS from a different deployed version/config as sufficient evidence.

This review does not execute those tests.

### D9 — object-specific provenance and current validity

PASS.

The candidate requires the full immutable evidence set, checks for mismatch/revocation and requires the durability contract to still be applicable for the exact object.

This prevents a historical PASS from being silently reused after contract/authority/retention changes.

## Manifest, dependency and restore integrity

PASS_WITH_BOUNDARIES.

The model preserves the important rule that recovery does not consist only of checkpoint bytes. A usable recovery object requires:
- exact manifest/composition;
- dependency graph;
- authoritative provenance;
- source/task revisions;
- retention/access availability;
- required keys/ACL availability where permitted;
- transaction/fencing lineage;
- digest/readback evidence.

A restored backup is not promoted directly to current. It is first restored to an isolated location, checked for digest/lineage and reconciled against current writer/epoch/authority.

This is compatible with ARH preservation: ARH may verify preservation/recovery composition but does not author another Entity's self-state or appoint its writer.

## Shard failure and split-brain

PASS.

The candidate is fail-closed:

- unreachable shard -> UNAVAILABLE; do not reconstruct missing state;
- split-brain / different heads -> BLOCKED_CONFLICT; preserve both branches and provenance;
- same generation with different digest/parent -> integrity branch conflict, not “pick newest”;
- timestamp or replica count alone cannot resolve semantic authority;
- old writer remaining alive does not transfer authority by availability;
- stale writer must be fenced, but fencing itself does not appoint a new writer.

This is sufficient document-level protection against last-write-wins and split-brain promotion.

## Unknown external side effect

PASS.

The candidate explicitly states that if an external effect may have happened and its outcome is unknown, the checkpoint does not authorize repeating it.

Required state is independent reconciliation of the effect before retry/resume.

Therefore checkpoint cursor semantics do not falsely promise exactly-once behavior for the external world.

## GitHub selection, editing and recovery evidence

PASS_WITH_CRITICAL_BOUNDARY.

The proposed MANDATORY / CONDITIONAL / OPTIONAL / EXCLUDE_BY_DEFAULT classes do not by themselves lose recovery-critical evidence because the candidate includes two essential safeguards:

1. an index/pointer never substitutes for substantial bytes that are unavailable or expired;
2. if sanitization/redaction destroys evidence required for recovery, the public derivative is explicitly insufficient for recovery.

A redacted object is correctly treated as a derivative with its own digest rather than as the exact original checkpoint.

Important boundary for any later adoption:
GitHub selection/editing may reduce the **public/long-lived representation**, but it must never destroy the last permitted copy of evidence required for:
- exact task/current cursor reconstruction;
- dependency interpretation;
- external-effect reconciliation;
- writer/epoch/fence provenance;
- recovery manifest validation;
- conflict/split-brain diagnosis.

If privacy prevents GitHub publication of required evidence, the correct result is not “evidence omitted and recovery still PASS”; it is a permitted non-public preservation locator or WAIT_PRIVACY_REVIEW / recovery limitation.

Therefore GitHub promotion and ARH recovery preservation remain different operations.

## Six distinct states that must remain separate

The candidate is acceptable only while the following distinctions remain explicit:

1. DURABLE_BYTES
   exact bytes survived the approved durability profile.

2. BOUNDED_TASK_RESUME_AUTHORITY
   an independently authorized exact task/cursor may continue in the allowed scope.

3. RECOVERY_ELIGIBLE
   the durable object has the exact manifest/dependencies/provenance/access needed to be considered by the approved recovery process.

4. ARH_PRESERVED
   ARH independently verified preservation/provenance/composition. This does not create self-state or authority.

5. INITIATION_VERIFIED
   a new physical instance actually performed the recovery initiation checks.

6. WRITER_ESTABLISHED
   a separate Writer Gate established authoritative writer status.

None of these states implies the next one automatically.

This separation is consistent with the active recovery canon and is the main preservation condition of this PASS.

## A / B / C boundary

ARH does not choose A, B or C.

Documentary result:

- A is preservation-safe because it creates no new resume authority domain.
- B is documentarily possible only if the OPERATOR gate explicitly fills exact scope, owners/actors, failure profile, retention/backup/restore, conflict rules, privacy/read/promotion boundaries and normative effectivity. A bare “choose B” is insufficient.
- C retains current boundaries and creates no operational authority.

Even after A/B normative adoption, implementation/test/deployment remains a separate authorization and evidence chain.

## Exact remaining UNKNOWN inputs

The candidate correctly leaves these unresolved rather than inventing defaults:

- A/B/C selection;
- operational owner;
- write/ack/readback/classification/promotion principals;
- exact storage trust and failure domains;
- replication/quorum/transaction boundary;
- epoch/fence issuer and durable lineage;
- numeric retention/TTL/RPO/RTO/backup cadence;
- outage/backlog limits;
- privacy/read scope and promotion reviewer;
- delete/hold/release authority;
- exact normative adoption/effectivity path.

These UNKNOWN values are not defects in this candidate because the document is explicitly a decision candidate and blocks operational authority until they are resolved.

## No required candidate correction

No minimum text correction is required before the OPERATOR decision gate.

If option B is later selected, the filled decision card must be reviewed as a new exact input before any claim of operational task-resume authority or implementation rollout.

## Hard boundary / current truth

candidate: CANDIDATE_NOT_ACTIVE
CHECKPOINT_DURABLE: NOT_ESTABLISHED
operational_owner: NOT_ASSIGNED
operational_resume_authority: NOT_GRANTED
A/B/C: NOT_SELECTED
memory-layering attempt 3: NOT_AUTHORIZED
implementation verification: NOT_PERFORMED
shard write: NOT_PERFORMED
host/secrets/provider access: NOT_PERFORMED
automatic activation / automation change: NOT_PERFORMED
Project Sources/canon mutation: NONE

Publication of this review does not approve the candidate.
Dispatch/inbox do not prove receipt, activation, processing_started or acceptance.

## Terminal

PASS_ARH_SHARD_CHECKPOINT_GOVERNANCE_R01_WITH_BOUNDARIES

Next causal gate:
GATE_SHARD_CHECKPOINT_STATUS_AND_ACCOUNTABILITY_R01

Only the authorized human decision contour may select A/B/C and fill the required accountability card.

---
КТО: ARH / АРХИВАРИУС
КОМУ: KOO / КООРДИНАТОР + KAN / КАНЦЕЛЯР
СТАТУС: PASS_ARH_SHARD_CHECKPOINT_GOVERNANCE_R01_WITH_BOUNDARIES
