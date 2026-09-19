# KOO → KOO: source rebuild r0.3 bounded correction

status: TASK
execution_mode: BOUNDED_CANDIDATE_INTEGRATION
processing_started: no
project_sources_activation: no
operator_gates_resolution: no
project_time: omitted; trusted project-time source not used

## Owner

owner: KOO / КООРДИНАТОР
owner_basis:
- current KOO is integrator of the existing source-rebuild lineage;
- KAN completed normative review;
- SHT completed process/stress review;
- this task only integrates exact reviewed corrections into candidate bytes;
- approval/activation remains outside KOO authority.

## Exact lineage

Current r0.2 package:
`project-sources-conveyor-v1-r02-candidate.zip`

SHA-256:
`0db002f77f25a451d0ff5a318e758773d26feef0064d92c5c26587280cb3c4e3`

KAN review:
`entities/kancelar/outbox/KAN__project-sources-conveyor-v1-norm-review__KOO.md`
commit `3753f169063d3531a9455fe7d55ca0cdba9f7c3e`
verdict `REQUIRES_EDITS_KAN_SOURCE_REBUILD_V1`.

SHT process review:
`entities/shtabist/outbox/SHT__source-rebuild-r02-process-review__KOO.md`
commit `021619fd4162cf065054095d21f66fb1cf5fa00b`
blob `ed2ed7bc6bbcd96fbf46d1d1ffc22d3cfecdc75a`
verdict `REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02`.

Inbox pointer:
`entities/koordinator/inbox/SHT__source-rebuild-r02-process-review__KOO.md`
status `addressed_for_processing`.
Inbox placement is not receipt, acceptance or processing evidence.

## Exact correction scope: D1–D3 only

### D1 — replacement PROMPT lifecycle

Target:
`task-conveyor-canon-v1-candidate.md`, lifecycle/WIP/failure sections.

Required invariant:
1. state belongs to one exact conveyor attempt / PROMPT lineage, not ambiguously to task and artifact at once;
2. before a replacement PROMPT becomes current/transferable, the prior open attempt MUST receive a non-executable disposition:
   - `SUPERSEDED`, or
   - exact `BLOCKED` with explicit successor/retry relation;
3. at most one current transferable/executable PROMPT may exist for one exact task lineage;
4. `activation_failed != processing_failed`;
5. activation failure never authorizes automatic replay;
6. replacement requires fresh reconciliation of task identity, authority, inputs and processing evidence;
7. manual and automatic activation use the same transition rule;
8. stale/superseded predecessor cannot become executable again without a new explicitly authorized transition.

Add the minimal transition table needed to make these states deterministic:
`READY_FOR_PROMPT / PROMPT_PREPARED / AWAITING_OPERATOR_TRANSFER / AWAITING_ENTITY_RESULT / BLOCKED / COMPLETED / SUPERSEDED`.

Do not redesign the whole conveyor.

### D2 — chat-specific conveyor vs generic Entity instance

Targets:
- `task-conveyor-canon-v1-candidate.md`;
- `source-loading-policy-v2_2-candidate.md`;
- `entity-state-preservation-and-recovery-canon-v1_6-candidate.md`;
- only if required for consistency, terse matching references in core/roles.

Required boundary:
1. task-conveyor canon governs inter-chat/PROMPT activation and KOO ownership of that conveyor;
2. it is mandatory baseline for KOO and for Entity instances/tasks that actually use this PROMPT/chat mechanism;
3. recovery-managed non-chat instances do not need full conveyor canon as permanent baseline unless their exact recovery/task uses that mechanism;
4. non-chat instances must still preserve the boundary reference:
   activation mechanism does not create authority, writer state or processing_started;
5. service-card scope must not claim generic project-wide Entity activation;
6. do not generalize this candidate into Work/worker/runtime orchestration beyond proven scope.

### D3 — deterministic source-set rollback

Target:
`SOURCE-REBUILD-MANIFEST.md`, source-set activation barrier.

Required rollback transaction:
1. before replacement, freeze exact identity of the full previous approved source set;
2. on activation failure, restore every replaced predecessor byte/version;
3. every newly introduced source absent from previous set, including task-conveyor canon, MUST be inactive/removed from active Project Sources;
4. perform exact readback of the complete previous approved set as one coherent set;
5. transition out of `SOURCE_SET_MAINTENANCE` only after full rollback readback PASS;
6. if any rollback element fails or remains ambiguous, state remains
   `SOURCE_SET_MAINTENANCE / SOURCE_SET_INCOMPLETE`;
7. no normative work/cold-start proceeds from an incomplete rollback state.

## Mandatory preserved boundaries

Do not approve or activate Project Sources.

Do not close, supersede, withdraw or infer resolution of these open OPERATOR gates:

Recovery v1.5 r0.4:
`17190f729eef6537f0404af387253c9c11eb3a21`.

Source-loading-policy v2.1:
`b15a9250e72e7bb5da4efabd027fa4e43386022e`.

Do not silently select old or new candidate lineage.

Preserve:
- task authority boundary;
- automation-authority boundary;
- `activation != processing_started`;
- `terminal_result != delivered != received != accepted`;
- source-set activation barrier;
- no historical replay.

## Required output of correction step

Prepare one new candidate revision r0.3 with:
- new exact ZIP identity;
- exact composition and per-file SHA-256;
- explicit provenance from r0.2 + SHT result;
- change log limited to D1–D3;
- no unrelated rewrite;
- status candidate only.

After materialization/readback:
fresh-reconcile and route the exact r0.3 package to the next review required by the existing process.

Do not execute this correction in the same routing turn.
