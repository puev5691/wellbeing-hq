# KOO → KOD: Entity operational memory + shards convergence design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: DESIGN_AND_CORRECTION_PLAN_ONLY
project_time: omitted

## Exact recovered plan

puev5691/wellbeing-hq@f13c4d4665ce0ba2f8b853f2f082b830040a2078:
entities/koordinator/current/KOO__entity-operational-memory-shards-recovered-plan-r01.md

terminal:
PASS_KOO_ENTITY_OPERATIONAL_MEMORY_SHARDS_RECOVERED_PLAN_R01

## Goal

Produce one implementation-ready convergence design that joins the existing:
- File/Artifact Service direction and its exact four known defects;
- mazhor shard gateway successor runtime r0.3;
- memory-layering isolation/recovery work and attempt-2 harness failure;
- standing fixed-IP -> Commander transport;
into one minimal synthetic pilot for Entity operational memory and replacement continuity.

Do not implement or execute attempt 3.

## Required exact inputs

Git operational shards direction:
puev5691/wellbeing-hq@87c278e5d99f102b9c148104a56e5009ab49a005:
entities/koordinator/outbox/KOO__git-operational-shards-priority-r01__OPERATOR.md

File/Artifact + shards direction:
puev5691/wellbeing-hq@b62896ff271ab0480a4ff1fcecef386a7c65b1b6:
entities/koordinator/outbox/KOO__file-artifact-git-shards-r01__PROJECT.md

File/Artifact Service independent FAIL:
puev5691/wellbeing-hq@b6849cd2aa9d45fea823b06f05d45053d968d2cb:
entities/shardovik/outbox/SHD__file-service-verify-r01__KOO.md

Mazhor shard gateway current-state reconciliation:
puev5691/wellbeing-hq@19c360d694f2274236942b9e8f4b792003a13bcd:
entities/sisadmin/outbox/SIS__mazhor-shard-gateway-option-a-current-state__KOO.md

Memory-layering isolated runtime feasibility:
puev5691/wellbeing-hq@930e90b32dddb33aad133d8303ecaa6b49348f42:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-isolated-runtime-feasibility__KOO-SHT.md

Memory-layering attempt 2 terminal:
puev5691/wellbeing-hq@7cfcfb611dd9e1a66fcb5dd2ff4e460fb8003a86:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-attempt-2-result__KOO.md

Standing transport:
puev5691/wellbeing-hq@59848480752f5096d07866e747bf894c3559270a:
entities/koordinator/current/KOO__fixed-ip-commander-standing-transport-current-r01.md

## Required output

Produce one design/result for KOO that defines:

1. Exact memory layer model
   - governance/identity;
   - operational working memory;
   - current state/checkpoint;
   - experience;
   - library/durable knowledge;
   - canonical GitHub evidence.

2. Record schemas and identity
   - immutable IDs/digests;
   - task/entity/writer binding;
   - supersession;
   - retention/expiry for operational records;
   - exact locator model.

3. Write/read flow
   - what Entity may write frequently to shard;
   - what must be sealed/verified;
   - what gets promoted to canonical GitHub;
   - when GitHub publication is required vs explicitly unnecessary.

4. Corrected File/Artifact Service successor requirements
   Must address all four exact defects from SHD review:
   - immutable MANIFEST mismatch;
   - reserved MANIFEST.json collision;
   - prior_manifest_path escape;
   - create_archive type closure.

5. Shard gateway role
   - use existing r0.3 verified runtime where compatible;
   - READ/WRITE/VERIFY/ROUTE boundaries;
   - no authority semantics;
   - fail-closed loss/mismatch behavior.

6. Replacement continuity contract
   Define exact OLD -> checkpoint -> fresh NEW flow where NEW has no transcript and must recover:
   - exact task;
   - causal cursor;
   - last verified result;
   - unresolved dependencies;
   - current operational facts;
   - required experience/library locators;
   - next already-authorized step.

7. Selective retrieval contract
   - minimum bootstrap;
   - semantic/query access to operational/library material;
   - no full archive dump by default;
   - request/read/byte accounting.

8. Non-mutating verification rule
   Prevent repetition of attempt-2 failure:
   - verifier cannot write into immutable package;
   - python bytecode disabled and/or read-only projection;
   - verification tool state separated from checked object.

9. GitHub batching contract
   Explicitly define how many classes of events remain shard-only and what events force canonical GitHub publication.
   Preserve GitHub as final project evidence without high-frequency scratch traffic.

10. Minimal synthetic E2E pilot
   Specify one small pilot that can later prove:
   - OLD produces operational memory;
   - checkpoint sealed;
   - NEW starts fresh without transcript;
   - NEW retrieves selectively;
   - NEW reconstructs state;
   - NEW continues without replay;
   - OPERATOR provides zero historical retelling;
   - GitHub receives only significant bounded publications.

11. Measurement
   Define counters for:
   - shard reads/writes;
   - GitHub reads/writes;
   - bytes;
   - recovery latency;
   - number of OPERATOR corrections/retellings;
   - replayed work count;
   - mismatches/fail-closed stops.

12. Ordered implementation plan
   Smallest next correction/build/verify steps after design approval.
   Do not authorize them yourself.

## Required explicit non-goals

- no memory-layering attempt 3 execution;
- no production Entity migration;
- no generic host mutation;
- no standing host command authority;
- no canon/Project Sources mutation;
- no automatic current-writer transfer;
- no CHECKPOINT_DURABLE claim;
- no replacement of GitHub canonical evidence;
- no secret storage in shard/memory artifacts.

## Expected terminal

PASS_KOD_ENTITY_OPERATIONAL_MEMORY_SHARDS_CONVERGENCE_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_* if an immutable dependency is missing/conflicting.

After immutable result + readback + addressed return to KOO, STOP.
