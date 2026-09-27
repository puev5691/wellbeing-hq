# KOO → SHT: independent review — Entity operational memory / shards convergence r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHT / ШТАБИСТ
scope: INDEPENDENT_ARCHITECTURE_STRESS_REVIEW_ONLY
project_time: omitted

## Resume-First

Before review:
- verify your current-writer / Writer Gate;
- fresh-check HQ supersession and competing result/task;
- do not replay historical SHT prompts;
- do not implement or mutate runtime/hosts.

If current-writer or task authority is not established, STOP with exact blocker.

## Exact design candidate

puev5691/wellbeing-hq@e90b9bd65e569d97e7497122c80808759dc4ce9e:
entities/koder/outbox/KOD__entity-operational-memory-shards-convergence-design-r01__KOO.md

blob:
d760a8289ec14d16059c54f579ffe5172fd3625b

status:
PASS_KOD_ENTITY_OPERATIONAL_MEMORY_SHARDS_CONVERGENCE_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW

## Governing recovered plan

puev5691/wellbeing-hq@f13c4d4665ce0ba2f8b853f2f082b830040a2078:
entities/koordinator/current/KOO__entity-operational-memory-shards-recovered-plan-r01.md

blob:
ffb62995588ed5af83f38465d1b7bfc3ef92cefd

terminal:
PASS_KOO_ENTITY_OPERATIONAL_MEMORY_SHARDS_RECOVERED_PLAN_R01

Human acceptance criterion:
replacement Entity must continue without OPERATOR retelling work history.

## Required independent stress-review

Check only whether the design is coherent, bounded and implementation-ready.

### A. Goal preservation

Verify the design actually serves both primary goals:
1. replacement Entity restores task/state/causal continuity without OPERATOR historical retelling;
2. high-frequency scratch/operational work moves off GitHub while GitHub remains canonical for significant evidence/decisions/checkpoints.

Reject designs that merely add another GitHub-heavy layer or require OPERATOR to reconstruct context.

### B. Layer separation

Stress-test the six proposed layers:
- governance/identity;
- operational working memory;
- current task state/checkpoint;
- experience;
- library/durable knowledge;
- canonical GitHub evidence.

Check that no operational/shard record silently becomes:
- authority;
- current-writer;
- accepted project state;
- canonical result;
- durable checkpoint.

### C. Record/checkpoint identity

Review:
- entity/task/writer/fence binding;
- parent/generation chain;
- supersession;
- content-addressing;
- CAS/current-pointer semantics;
- exact locator model;
- idempotency;
- mismatch/loss/conflict fail-closed behavior.

Unknown retention/RPO/RTO must remain UNKNOWN unless separately decided.

### D. File/Artifact Service correction gate

Verify all four historical SHD defects are exactly carried forward:
1. immutable MANIFEST mismatch;
2. reserved MANIFEST.json collision;
3. prior_manifest_path escape;
4. create_archive type closure.

Confirm the proposed first implementation step is correction-only successor + immutable package/readback + independent SHD re-review.

Do not approve implementation or perform it.

### E. Existing shard gateway boundary

Verify the design does not silently reinterpret current mazhor r0.3 READ/VERIFY runtime as WRITE authority or as an operational memory store.

Any WRITE/CAS/store behavior must remain a separately designed/authorized successor.

### F. Replacement continuity

Stress-test OLD → seal/checkpoint → canonical anchor → fresh NEW → selective retrieval → semantic restoration → continuation.

NEW must have:
- no inherited transcript;
- no inherited hidden memory/cache/task variables;
- no oracle/checker-private material;
- no credentials/project writer authority;
- no automatic current-writer transfer.

The design must let NEW identify:
- exact task/version;
- causal cursor;
- last verified result;
- unresolved dependencies;
- current operational facts;
- required experience/library locators;
- next already-authorized step.

Completed prefix replay must be detectable and rejected.

### G. Selective retrieval and budgets

Check:
- bootstrap is minimal and pinned;
- retrieval is exact/allowlisted/accounted;
- no full archive dump by default;
- read/byte accounting is sufficient;
- historical broker budget mismatch cannot recur silently.

If the design reuses numeric limits from older preparation, ensure it marks them subject to fresh admission rather than current universal policy.

### H. Non-mutating verification

Verify the design structurally prevents the attempt-2 failure:
- immutable package cannot be modified by verifier;
- verifier/tool state outside checked object;
- bytecode/cache writes disabled or blocked;
- read-only projection where needed;
- verifier failure cannot corrupt evidence.

### I. GitHub batching/canonical promotion

Check that event classes and promotion triggers are unambiguous enough to avoid:
- high-frequency GitHub scratch traffic;
- losing significant state only in volatile shard;
- claiming delivery/acceptance from publication;
- treating GitHub unavailability as permission to invent canonical state.

### J. Synthetic pilot identity / attempt-3 bypass check

Independently determine whether proposed EOM-SHARD-PILOT-R01 is genuinely a new separately scoped future synthetic pilot or is materially a continuation/retry of the consumed memory-layering MAIN sequence.

Memory-layering attempt 2 is consumed.
Memory-layering attempt 3 is NOT_AUTHORIZED.

If the proposed pilot would causally constitute attempt 3/retry under the existing memory-layering contract, return a BLOCKER and require explicit OPERATOR authority. Do not accept renaming as authority separation.

Even if judged a distinct future pilot, no execution authority exists yet.

### K. Measurement and human criterion

Verify counters can prove:
- shard reads/writes;
- GitHub reads/writes;
- bytes;
- recovery latency;
- OPERATOR historical retellings/corrections;
- duplicate/replayed work;
- mismatches/fail-closed stops.

The target human criterion must remain:
OPERATOR historical retelling count = 0 for successful replacement continuation.

No numeric GitHub-reduction target needs to be invented at design review.

## Required verdict

If no critical design blocker remains:

PASS_SHT_ENTITY_OPERATIONAL_MEMORY_SHARDS_CONVERGENCE_REVIEW_R01_READY_FOR_FILE_SERVICE_CORRECTION_GATE

This PASS means only:
- convergence design is coherent enough to proceed to the separately authorized correction-only File/Artifact Service implementation gate;
- subsequent SHD independent re-review remains mandatory.

It does NOT authorize implementation.

If critical defects remain:
return only exact critical blockers and required correction.

## Hard prohibitions

Do not:
- implement File/Artifact successor;
- mutate shard gateway;
- enable shard WRITE;
- execute memory-layering attempt 3;
- execute EOM-SHARD-PILOT-R01;
- mutate any host;
- use standing Commander transport for a host action;
- mutate Project Sources/canon/current-writer;
- claim CHECKPOINT_DURABLE;
- approve production Entity migration.

After immutable result + exact readback + addressed return to KOO, STOP.
