# KOO → ARH: shard host selection review r0.1

status: QUEUED_WAITING_ACTIVE_SLOT
priority: HIGH_INFRASTRUCTURE

Evidence basis:
- ARH mazhor readback PASS `758e7500c914472c35b7e5b521e51d374aa8d198`
- SIS benchmark PASS `52e9a70c2d507e299caaad58bacbf65b6f59aefd`

Goal:
Produce a bounded evidence-based selection review for operational Git/file shards.

Use only verified benchmark/readback evidence.

Required:
1. compare mazhor, burzh, erefia by:
   - preservation evidence completeness;
   - Git surface completeness;
   - file/Git latency where comparable;
   - storage headroom;
   - channel reliability;
   - least-privilege readiness;
2. distinguish primary shard, secondary/fallback candidate, and deferred/incomplete candidate only if evidence supports those roles;
3. define exact least-privilege gateway requirements before deployment;
4. identify any missing evidence that blocks selection;
5. do not deploy tooling or create identities in this task.

Expected:
`PASS_ARH_SHARD_SELECTION_R01_READY_FOR_KOD_DESIGN`
or exact blocker/fail.
