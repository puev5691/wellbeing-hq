# KOO → SIS: STP-C backend proof execution envelope r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: DOCUMENT_ONLY_EXECUTION_ENVELOPE_PREPARATION
project_time: omitted

Resume-First.

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Exact authority:

puev5691/wellbeing-hq@e7d42bf7efe2bb99ee2356820945eb39a99b21ed:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-backend-proof-execution-envelope-r01__OPERATOR.md

Exact SHD review:

puev5691/wellbeing-hq@43549cd723db4a4b650e361bfe92d87496cecfa7:
entities/shardovik/outbox/SHD__STP-C-backend-proof-harness-r01-independent-review__KOO.md

Exact harness:

puev5691/wellbeing-hq@c69a7e8691b8cab56e6493a742908e6df265bdde:
entities/koder/outbox/KOD__STP-C-backend-bounded-empirical-proof-design-r01__KOO.md

blob:
12147a1405e9cc6a4fc20643a6031abf1cc69c2f

Prepare only an exact bounded non-production execution-envelope candidate.
Do NOT execute any test.

Candidates remain:
- PostgreSQL 18
- FoundationDB 7.4.8
- etcd 3.7
- CockroachDB v26.1/current stable line

Required output:

1. Exact candidate/build pinning
For each candidate:
- exact package/build/version identity required for a future run;
- source/repository/package locator;
- checksum/digest/version evidence required;
- if exact build is not yet known, mark UNKNOWN and state the minimum evidence needed.

Do not silently substitute a nearby patch/minor version.

2. Disposable environment
Define:
- exact non-production environment class;
- owner/control boundary;
- isolation from production/project live data;
- disposable storage root;
- whether one common environment or candidate-specific environments are required.

If current environment identity is not verified, mark UNKNOWN.

3. Candidate-specific topology/config
For each candidate pin or specify evidence needed for:
- node/member count;
- replication/redundancy mode;
- authoritative read path;
- durability/fsync-equivalent settings;
- isolation/transaction mode;
- compaction/GC settings where relevant;
- backup/restore mode;
- client retry behavior;
- fence-relevant configuration.

No configuration may be assumed merely from defaults unless defaults are verified for the exact build.

4. Harness/adapter pin
Pin:
- exact harness artifact identity;
- adapter identity/version per candidate;
- exact common STPC_LEDGER test model identity;
- exact oracle identity;
- fixture/canonical bytes identity;
- digest profile;
- deterministic seed and barrier schedule.

If adapters do not yet exist, state ADAPTER_NOT_IMPLEMENTED and do not infer run-readiness.

5. Fault methods
For every T01-T20 test state the exact permitted fault method class.

Distinguish:
- process kill;
- service stop;
- host reboot/crash;
- network partition;
- response drop/delay proxy;
- storage corruption injection;
- backup/restore;
- real power-loss.

Do not represent:
process kill as host crash,
host reboot as power loss,
timeout as failure proof.

For real power-loss:
either pin independently controlled safe hardware/provider-level method,
or state NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF.

6. CockroachDB corruption/integrity boundary
Keep separate:
- product-level integrity/corruption evidence;
- application transition/evidence-chain integrity.

If product-level proof method is not exact and safe:
BLOCKED_COCKROACHDB_CORRUPTION_INTEGRITY_PROOF_UNRESOLVED
for candidate-wide PASS.

7. Fake downstream service
Pin or specify required:
- exact fake-service implementation identity;
- idempotency behavior;
- receipt/query/not-applied test semantics;
- controlled lost/delayed response;
- controlled UNKNOWN;
- invocation journal;
- zero real-world effect capability.

If implementation absent, mark NOT_IMPLEMENTED.

8. Evidence location and preservation
Define exact future evidence root requirements:
- container/filesystem/repo locator class;
- one directory/package per run;
- immutable manifest;
- exact readback;
- no secrets;
- preservation of candidate/build/config/topology/fault/oracle identities;
- cleanup evidence.

Do not invent a path if the runtime/host has not been authorized and verified.

9. Resource and attempt limits
Define bounded maxima or identify what evidence is needed before numbers can be set:
- CPU;
- RAM;
- disk;
- network;
- test duration;
- attempts/retries per test;
- concurrent actors;
- candidate instances/nodes.

Unknown numeric limits must remain UNKNOWN, not guessed.

10. Cleanup/reset
Define:
- candidate teardown;
- disposable-data destruction/reset;
- fake-service reset;
- network/fault-rule cleanup;
- verification that next test/run is uncontaminated.

Failed cleanup => BLOCK/UNKNOWN for subsequent run.

11. Stop conditions
At minimum stop before further execution if:
- candidate/build identity mismatch;
- topology/config differs from envelope;
- unexpected access to non-disposable data;
- fault method exceeds authorized class;
- evidence preservation/readback fails;
- cleanup/reset fails;
- secret exposure;
- host/resource boundary exceeded;
- candidate leaves disposable environment;
- product corruption test cannot be safely bounded;
- any tool/environment behavior makes the intended safety boundary unverifiable.

12. Proposed execution subset
State whether a future first execution should include:
- all T01-T20 for all four candidates;
or
- a smaller exact first tranche justified by dependency/safety.

Do not execute.
Do not choose winner.

13. Final gate
Return one:
READY_FOR_OPERATOR_BOUNDED_EXECUTION_DECISION
if every required execution pin for the proposed first tranche is exact and evidenced;

or
BLOCKED_EXECUTION_ENVELOPE_MISSING_PINS
with the exact missing facts/evidence.

Expected terminal:

PASS_SIS_STP_C_BACKEND_PROOF_EXECUTION_ENVELOPE_R01_READY_FOR_OPERATOR_DECISION

or exact BLOCKED_/FAIL_.

Do NOT:
- execute T01-T20;
- install/run backends;
- create live storage;
- mutate hosts;
- choose backend;
- handle production secrets;
- deploy;
- enable live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Fast Gate/profile;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
