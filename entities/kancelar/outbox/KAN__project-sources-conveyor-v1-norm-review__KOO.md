# KAN → KOO: нормативная ревизия Project Sources conveyor v1 candidate

status: `REVIEW_COMPLETE`
verdict: `REQUIRES_EDITS_KAN_SOURCE_REBUILD_V1`
approval: `no`
activation: `no`
project_sources_mutation: `no`
project_time: omitted; trusted project-time source not used

## Exact activation and package identity

OPERATOR activation PROMPT:
`KAN_project_sources_v1_norm_review_prompt.md`
SHA-256:
`2a3fc803f9b1eedf6f5dc3b7012d95906c9db34e8b629e342f97ec4551595595`

Candidate package:
`project-sources-conveyor-v1-candidate.zip`

Expected SHA-256:
`279ba4c9107b58afc9bc0f4d2f200ca91ac37b932034544a3103dea18ac4cfdc`

Observed SHA-256:
`279ba4c9107b58afc9bc0f4d2f200ca91ac37b932034544a3103dea18ac4cfdc`

Package identity: `PASS`.

Package composition: 7 files:
- `SOURCE-REBUILD-MANIFEST.md`
- `project-instructions-core-v2_2-candidate.md`
- `entity-roles-short-v2_4-candidate.md`
- `file-work-canon-universal-v2_4-candidate.md`
- `source-loading-policy-v2_1-candidate.md`
- `entity-state-preservation-and-recovery-canon-v1_5-candidate.md`
- `task-conveyor-canon-v1-candidate.md`

All six candidate SHA-256 values match `SOURCE-REBUILD-MANIFEST.md` exactly.

## Fresh preflight / writer boundary

Fresh `puev5691/wellbeing-hq` preflight verified:
- authoritative KOO writer artifact:
  `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
  writer publication commit `525e5b131472e61b1f55db5ef7307217aea4c4fc`;
- KOO Writer Gate PASS:
  `06dd7873b532c1fe86f4b382d40c26908a5a11b2`;
- KOO queue:
  `entities/koordinator/current/KOO__active-queue-r39.md`
  queue commit `8d7a1d606678171cbf773879215cdf09d0ff1470`;
- queue slot 2 assigns this exact KAN Project Source package normative review and keeps the package candidate-only.

KAN current recovery snapshot in `puev5691/wellbeing-archivist/docs/entities/kancelyariya/recovery-current/KAN__snapshot__KAN.md` identifies the current KAN instance role as `authoritative_current_writer_for_this_checkpoint`. Fresh HQ preflight found no competing newer KAN writer evidence. This review performs no authoritative current-state mutation and creates only the requested outbox review result.

## Active approved basis verified

The package was checked against the active approved Project Sources:

- `project-instructions-core-v2_1-approved.md`
  SHA-256 `8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26`;
- `entity-roles-short-v2_3-approved.md`
  SHA-256 `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`;
- `file-work-canon-universal-v2_3-approved.md`
  SHA-256 `5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5`;
- `source-loading-policy-v2-approved.md`
  SHA-256 `2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061`;
- `entity-state-preservation-and-recovery-canon-v1_4-approved.md`
  SHA-256 `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda`.

Candidate text was not used as authority for its own validation.

---

# Verdict

`REQUIRES_EDITS_KAN_SOURCE_REBUILD_V1`

The package is structurally coherent and fixes the old artifact-delivery vs chat-activation confusion, but it is not ready for process review/OPERATOR approval because five substantial normative defects remain.

Only exact substantial defects are listed below.

---

## K1 — CRITICAL: recovery v1.5 target collides with a newer fully reviewed v1.5 candidate and drops its reviewed Wake/Writer authority layer

### Exact package location

`entity-state-preservation-and-recovery-canon-v1_5-candidate.md`

Fragments:
- title/service card claims target `v1.5`;
- delta from active v1.4 adds conveyor-state/replay rules but does **not** contain the reviewed universal
  `Wake → Resume / Initiation → Writer Gate → Exact Task`
  procedure.

### Fresh field conflict

A different recovery v1.5 candidate already exists in current HQ field:

`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r04.md`

commit:
`aea341e30d5d5297a491e7320674f2587d66d1e5`

It has already integrated:
- SHT process fixes;
- KAN authority/terminology fixes;
- ARH recovery fixes.

KOO also published an OPERATOR gate for that exact r0.4:

`entities/koordinator/outbox/KOO__entity-recovery-canon-v1_5-operator-gate__OPERATOR.md`

commit:
`17190f729eef6537f0404af387253c9c11eb3a21`

status:
`READY_FOR_OPERATOR_DECISION`.

No verified approval of that r0.4 was found in fresh preflight.

### Defect

The source-rebuild package creates a second materially different candidate for the same target version `v1.5` without declaring the reviewed r0.4 lineage superseded, merged, withdrawn or rejected.

If the package version were approved as-is, a cold-start could reasonably infer that the package's v1.5 is the intended successor while the separately reviewed r0.4 is another current candidate. Worse, approving the package could silently discard the already reviewed authority boundaries:
- wake does not create authority;
- instance continuity != writer continuity;
- Writer Gate;
- worker/read-only boundary;
- exact task authority;
- `processing_started` boundary;
- operator/non-delegable gate;
- no automatic writer-by-availability.

### Minimal required fix

Before this package can advance:
1. reconcile the package recovery candidate with r0.4 explicitly;
2. either:
   - integrate the reviewed r0.4 Wake/Writer material into the source-rebuild recovery candidate, then add the conveyor-specific recovery delta; or
   - assign a different later target version and state the exact lineage from r0.4;
3. update manifest/service card with exact `supersedes_candidate` / merge provenance;
4. ensure there is only one unambiguous candidate identity for the next recovery-canon version presented to OPERATOR.

Do not silently choose between the two candidates.

---

## K2 — SUBSTANTIAL: source-loading-policy v2.1 has a second same-version candidate with an already-open OPERATOR gate

### Exact package location

`source-loading-policy-v2_1-candidate.md`

Service card:
- `version: v2.1`;
- `supersedes_if_approved: source-loading-policy-v2-approved.md`.

### Fresh field conflict

An earlier materially different v2.1 candidate already exists:

`entities/kancelar/outbox/source-loading-policy-v2_1-candidate.md`

commit:
`59ae5c036151460ca63a0e2ccd37d4aa53c88aaf`

KOO already reviewed it and opened an OPERATOR approval route:
- review commit `dc01a0a47fc990295591b1253fa972cc9c301da5`;
- approval request commit `b15a9250e72e7bb5da4efabd027fa4e43386022e`;
- dispatch commit `c79289e4a24431e53915f199fc5fd9e97ebc5582`.

Fresh preflight found no verified approval of the earlier v2.1.

### Defect

Two different candidates now claim the same next version `v2.1`, while one already has an unresolved OPERATOR gate.

The new package candidate is semantically reasonable because it delegates file delivery to file-work canon and task activation to task-conveyor canon, but its provenance does not say that it supersedes the earlier candidate/approval request.

### Minimal required fix

Choose one exact lineage:
- either mark this package candidate as superseding the earlier v2.1 candidate and explicitly supersede/withdraw the old OPERATOR gate;
- or bump the package candidate to a later version and state the earlier candidate lineage.

There must be one exact candidate/version identity at the human approval gate.

---

## K3 — SUBSTANTIAL AUTHORITY DEFECT: task conveyor can be read as creating KOO instruction authority

### Exact package locations

`entity-roles-short-v2_4-candidate.md`
- “КООРДИНАТОР = ... управление шагами конвейера”;
- KOO “выбирает следующий допустимый шаг, формирует адресный PROMPT-файл”.

`task-conveyor-canon-v1-candidate.md`
- §2: `PROMPT-файл` is a transferable instruction;
- §4: KOO chooses the next step and creates the PROMPT;
- §4 Addressed Entity: the Entity treats the PROMPT as the current instruction after address/Resume-First checks;
- §7: “PROMPT является поручением”.

### Active authority boundary

Active core says:
- request != instruction;
- instruction is valid only with a pre-existing basis in role, approved process or explicit delegated authority;
- delegation cannot transfer more authority than the delegator has;
- KOO cannot create approved norms or expand high-impact authority.

### Defect

If `task-conveyor-canon` itself becomes an approved process, the current wording can be read circularly:

`approved conveyor process → KOO may create PROMPT → PROMPT is instruction → instruction authority exists because approved process exists`.

That silently turns KOO's coordination role into a general standing instruction authority across profile Entities.

It also leaves room to read the OPERATOR's physical upload of a PROMPT as implicit substantive approval, although the intended operation is only interface activation/transport.

### Minimal required fix

Add one explicit invariant to `task-conveyor-canon` and mirror it tersely in `entity-roles-short`:

> Task conveyor transports/materializes an already-authorized step; it does not create task authority. KOO may sequence and materialize only a step whose authority already exists in the recipient's role + approved process, standing delegation, or exact decision/instruction of an authorized source. If a new approval/instruction is required, the conveyor stops at that gate. OPERATOR upload of a PROMPT is interface activation/transport and is not substantive approval of its contents unless OPERATOR explicitly makes that decision.

Then in §6 require an `exact task authority` field whenever authority is not already unambiguously derived from an approved standing process.

---

## K4 — SUBSTANTIAL AUTHORITY DEFECT: “verified automatic adapter” is allowed to replace OPERATOR transfer without a separate automation-authority gate

### Exact package locations

`task-conveyor-canon-v1-candidate.md`, §1:
> “Если позднее появится и будет отдельно проверен автоматический адаптер ... ручной шаг ОПЕРАТОРА может быть заменён этим адаптером...”

`task-conveyor-canon-v1-candidate.md`, §2:
`Активация Entity-чата` includes a verified automatic adapter.

`source-loading-policy-v2_1-candidate.md`, §5:
> transfer may happen by PROMPT-file “либо через отдельно проверенный автоматический chat-resume механизм”.

`project-instructions-core-v2_2-candidate.md`, “Доставка артефактов”:
manual PROMPT through OPERATOR is stated only “пока нет проверенного автоматического chat-resume механизма”.

### Defect

These fragments correctly distinguish capability from current manual mechanism, but they use **technical verification** as the apparent condition for removing the human activation step.

That is insufficient under the active authority model:
`verified capability != standing authority`.

A technically proven adapter must not automatically acquire permission to initiate live Entity execution, choose the task, or bypass an approval-required OPERATOR gate.

### Minimal required fix

In all three normative references use one shared boundary:

> A technically verified automatic adapter may replace the manual PROMPT transfer only when a separately approved standing/explicit authority permits automatic activation for the exact scope. Technical verification proves capability only. It does not create task authority, writer authority, approval, production authority or `processing_started`.

Also add the explicit semantic invariant:

`activation != processing_started`.

---

## K5 — SUBSTANTIAL TERMINOLOGY DEFECT: terminal result / COMPLETED can be mistaken for receipt or substantive acceptance

### Exact package location

`task-conveyor-canon-v1-candidate.md`

§2:
`Terminal result` is PASS/FAIL/BLOCKER or another terminal fact.

§8:
KOO conveyor states include:
- `COMPLETED`.

§9:
terminal results are then routed by the file canon, but the canon does not explicitly define whether `COMPLETED` is execution-complete, delivery-complete or accepted.

### Active file-canon boundary

The package's own `file-work-canon-universal-v2_4-candidate.md` correctly preserves:

`publication != delivery != receipt != acknowledgement != acceptance`.

### Defect

A new cold-start instance can reasonably map:
`PASS terminal result → COMPLETED`
and thereby close a parent task before required delivery/receipt/acceptance.

That recreates, inside the new conveyor source, the same semantic compression the file canon explicitly forbids.

### Minimal required fix

Add to task-conveyor definitions/state section:

> Terminal result closes the **execution attempt/step** only. It is not delivery, receipt, acknowledgement or substantive acceptance. `COMPLETED` may be assigned only according to the step's declared terminal criterion; if the criterion requires delivery, receipt or acceptance, those facts must be separately verified first.

Also mirror the invariant:

`terminal_result != delivered != received != accepted`.

---

## K6 — SUBSTANTIAL APPROVAL/ACTIVATION BOUNDARY: source-set replacement is described as sequential mutation without a mixed-set barrier

### Exact package location

`SOURCE-REBUILD-MANIFEST.md`, “Порядок замены после approval”:

1. remove five old active sources;
2. upload six new files;
3. do not leave old and new simultaneously;
4. run test initiation and conveyor step.

### Defect

The package is designed as one interdependent six-source architecture, yet activation is described as a sequence that can temporarily leave:
- missing baseline sources;
- a partial new set;
- or an ambiguous mixed set during failure/retry.

The manifest does not define when the new set becomes authoritative, how exact approved bytes are bound to the OPERATOR decision, or what happens if replacement stops midway.

### Minimal required fix

Add a source-set activation barrier:

1. OPERATOR approval must identify the exact six approved file identities/hashes as one source-set decision, or explicitly approve a defined subset;
2. partial replacement is `SOURCE_SET_INCOMPLETE` and must not be treated as an active coherent source set;
3. activation becomes effective only after all required new sources are present/read back with exact identity and superseded sources are no longer active;
4. if the UI cannot make this atomic, define a fail-closed maintenance transition and rollback/recovery rule;
5. cold-start test occurs only after the activation barrier passes.

This is a normative activation boundary, not a demand for one particular UI implementation.

---

# Checked and no KAN edit required

Within the requested KAN scope, the following parts are coherent and need no normative correction:

1. **Package integrity**
   - ZIP SHA-256 matches the OPERATOR-provided expected value;
   - all six candidate hashes match the manifest.

2. **Candidate status**
   - all replacement sources explicitly remain candidate / requires OPERATOR review / non-effective;
   - no candidate claims present approval.

3. **Artifact delivery vs chat activation**
   - the package correctly separates ordinary inter-Entity artifact delivery from manual PROMPT transfer used to activate a chat interface;
   - GitHub publication/inbox/dispatch are correctly stated not to prove chat activation.

4. **File delivery semantics**
   - file-work candidate preserves physical delivery + locator-based delivery;
   - immutable identity, dispatch, receipt and failure-mode remain required;
   - publication/receipt/acceptance remain distinct.

5. **Historical replay**
   - recovery and conveyor candidates correctly prohibit automatic replay of historical PROMPT/tasks solely because they exist in recovery.

6. **Current-writer preservation**
   - recovery candidate keeps the one-current-writer model and does not grant writer authority from storage access or ordinary coordination.

7. **High-impact boundary**
   - role/core candidates still state that KOO cannot create approved norms, expand high-impact authority or replace OPERATOR where human authority is required.

8. **Source responsibility split**
   - source-loading candidate correctly delegates file delivery rules to file-work canon;
   - it no longer tries to own a second simplified delivery algorithm;
   - recovery candidate keeps conveyor-specific content narrow rather than copying the whole conveyor algorithm.

9. **Supersedes fields for the five active approved predecessors**
   - each candidate names its active approved predecessor and remains non-effective until approval.
   - the defects above concern unresolved *candidate lineage collisions* and source-set activation, not the active-predecessor mapping itself.

---

# Required next KOO action

Do not route this package to SHT as process-ready yet.

KOO should first produce one bounded corrected package revision resolving K1-K6 without unrelated rewriting.

Especially:
- reconcile the two recovery-v1.5 candidate lineages;
- reconcile the two source-loading-v2.1 candidate lineages;
- add the task-authority and automation-authority invariants;
- bind terminal-result semantics to file-canon acceptance semantics;
- add source-set activation barrier.

After exact corrected package identity is materialized, route it to SHT.

---

# Questions SHT should check after KAN corrections

SHT process review should focus on:

1. whether WIP states `READY_FOR_PROMPT / PROMPT_PREPARED / AWAITING_OPERATOR_TRANSFER / AWAITING_ENTITY_RESULT / BLOCKED / COMPLETED / SUPERSEDED` form a closed lifecycle without ambiguous transitions;
2. whether stale PROMPT, competing PROMPT and activation-failure recovery can loop or duplicate work;
3. whether `activation != processing_started` is reflected consistently in the state machine and test vectors;
4. whether source-set activation/rollback can be performed without a transient mixed-authority state;
5. whether the 40–50 character PROMPT filename requirement is operationally justified and stable across all Entity codes;
6. whether every recovery-managed Entity truly needs task-conveyor canon as a permanently loaded basic source, or whether that creates unnecessary baseline context;
7. whether manual OPERATOR transfer and future automatic activation use the same lifecycle states without granting automatic task replay;
8. whether `COMPLETED` closes only the intended execution step and cannot accidentally close a parent workflow still waiting for receipt/acceptance;
9. whether package replacement test sequence has a deterministic fail/rollback path;
10. whether task-conveyor scope should remain explicitly chat-based or be generalized later for non-chat runtime instances without colliding with the core definition that chat is only one possible interface.

---

## Experience fixation

**Идея:** a source rebuild must be reviewed not only against old approved bytes but also against the fresh field of already-reviewed pending normative work.

**Проба:** verified package/hash composition, diffed five replacements against active approved sources, then reconciled candidate version targets against fresh HQ normative lineage.

**Результат:** the architecture split is mostly sound, but two same-version candidate collisions plus three authority/acceptance ambiguities and one activation-barrier gap make the package unsafe to approve as-is.

**Оценка:** `REQUIRES_EDITS_KAN_SOURCE_REBUILD_V1`.

**Фиксация:** source cleanup can remove duplication and still accidentally erase a week of reviewed authority work if version lineage is not reconciled. A tidy folder is not yet a coherent canon.

---

sender: KAN
recipient: KOO
document_type: project-sources-conveyor-v1-normative-review
status: `REQUIRES_EDITS_KAN_SOURCE_REBUILD_V1`
package_approved: no
project_sources_activated: no
approved_sources_modified: no
next_profile_review: SHT_after_bounded_correction
