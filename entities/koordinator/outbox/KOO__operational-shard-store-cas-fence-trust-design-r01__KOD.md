# KOO → KOD: operational shard store CAS/fence/trust design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: DOCUMENT_ONLY
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@5d9916df3f3e3c320a64e7396db6e6640f39eae8:
entities/koordinator/outbox/KOO__authorize-KOD-operational-shard-store-design-r01__OPERATOR.md

Recovered program plan:
puev5691/wellbeing-hq@f13c4d4665ce0ba2f8b853f2f082b830040a2078:
entities/koordinator/current/KOO__entity-operational-memory-shards-recovered-plan-r01.md

Convergence design:
puev5691/wellbeing-hq@e90b9bd65e569d97e7497122c80808759dc4ce9e:
entities/koder/outbox/KOD__entity-operational-memory-shards-convergence-design-r01__KOO.md

Independent architecture review/blocker:
puev5691/wellbeing-hq@a9ea81332d2e9164bb836984fe8989567bbfa46d:
entities/shtabist/outbox/SHT__entity-operational-memory-shards-convergence-independent-review-r01__KOO.md

Verified File/Artifact Service r0.2:
KOD package:
puev5691/wellbeing-hq@b5218dc8c074108b80d7e97f537fe5faf0d9a8e2:
entities/koder/outbox/file-artifact-service-correction-r02

SHD independent PASS:
puev5691/wellbeing-hq@d5e9ee10d89fe3e498529824cd7354a469ce99e5:
entities/shardovik/outbox/SHD__file-artifact-service-r02-independent-reverify__KOO.md

Existing shard gateway current-state evidence:
puev5691/wellbeing-hq@19c360d694f2274236942b9e8f4b792003a13bcd:
entities/sisadmin/outbox/SIS__mazhor-shard-gateway-option-a-current-state__KOO.md

Important current boundary:
gateway r0.3 is READ/VERIFY only.
Do not silently convert it into WRITE/CAS/store authority.

## Required design

Produce one implementation-ready document defining:

1. Operational record model
- immutable record bytes;
- record_id/content digest;
- entity_id;
- task_id/task_version;
- writer_id/writer_epoch or equivalent fence;
- parent_digest/generation;
- state classification;
- source/evidence refs;
- no secrets.

2. CAS/current-pointer model
- immutable objects separate from mutable/current pointer;
- compare-and-swap semantics;
- expected previous pointer/generation;
- idempotency;
- concurrent writer conflict;
- no last-write-wins.

3. Writer fence/trust model
- what external authority proves writer legitimacy;
- how stale/frozen writer is rejected;
- how replacement writer fence changes;
- shard never creates writer authority.

4. Read/write/verify boundaries
- operational scratch;
- sealed operational state;
- checkpoint candidate;
- canonical promotion candidate;
- exact behavior for READ / WRITE / VERIFY / ROUTE;
- authority semantics = none.

5. Failure model
- shard unavailable;
- object missing;
- CAS conflict;
- digest mismatch;
- stale writer fence;
- task/version mismatch;
- Git/shard mismatch;
- partial write;
- pointer without object;
- object without pointer;
- recovery from loss.

6. Retention/expiry
- define required fields/policy hooks;
- keep undecided RPO/RTO/retention as UNKNOWN/policy inputs;
- do not invent numeric policy.

7. Promotion boundary
- when shard-only state is sufficient;
- when File/Artifact Service sealing is required;
- when GitHub canonical publication/readback becomes mandatory;
- publication != receipt/acceptance/current-state.

8. File/Artifact Service integration
- exact input/output contract with verified r0.2;
- sealing/readback responsibilities;
- no hidden GitHub publish authority inside service.

9. Existing gateway compatibility
- what can reuse r0.3 READ/VERIFY;
- what requires a successor component;
- no WRITE enablement by interpretation.

10. Security/trust boundary
- no credentials/secrets in operational records;
- exact locator provenance;
- no arbitrary path traversal;
- no shard content promoted by name/recency alone;
- fail closed.

11. Minimal implementation plan
- smallest build sequence after design approval;
- independent reviewers for each stage;
- exact first implementation gate;
- no implementation authority in this task.

12. Review matrix
Include adversarial cases for:
- concurrent writers;
- stale writer;
- duplicate idempotency key conflicting bytes;
- lost pointer;
- corrupt object;
- divergent Git/shard state;
- superseded task;
- frozen Entity;
- missing canonical anchor at replacement boundary.

## Explicitly preserve blocker

EOM-SHARD-PILOT-R01 remains BLOCKED because it causally overlaps unauthorized memory-layering attempt 3.

Do not redesign or execute that pilot in this task.

## Expected terminal

PASS_KOD_OPERATIONAL_SHARD_STORE_CAS_FENCE_TRUST_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_* / FAIL_*.

After immutable design + readback + result to KOO, STOP.

Do NOT:
- implement store;
- enable shard WRITE;
- deploy;
- mutate hosts;
- use Commander host action;
- execute EOM pilot;
- execute memory-layering attempt 3;
- claim CHECKPOINT_DURABLE;
- mutate Project Sources/canon/current-writer.
