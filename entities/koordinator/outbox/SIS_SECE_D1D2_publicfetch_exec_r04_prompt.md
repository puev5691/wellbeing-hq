# SIS — SECE D1+D2 public-Git exact execution proof r0.4

conveyor_attempt:
SIS_SECE_D1D2_PUBLICFETCH_R04_A1

attempt_state:
AWAITING_OPERATOR_TRANSFER

execution_evidence_profile:
CHAT_INFOFIELD_EXECUTION_EVIDENCE_PROFILE_R01

profile_applicability_reason:
EXACT_TASK_REQUIRES_DURABLE_PROGRESS_EVIDENCE

project_time:
omitted

АДРЕСАТ: СИСАДМИН / SIS r0.9

Resume-First.

Выполни только one NEW bounded independent execution-proof attempt R04 for the exact immutable SECE D1+D2 candidate.

R04 is a NEW attempt. R03 is historical NONTERMINAL / DO_NOT_REPLAY and must not be resumed, reused or cleaned by this task.

## Exact authority

puev5691/wellbeing-hq@8db9a474b2f77d1f9522dd071f2ab5dd5e356109:
entities/koordinator/outbox/KOO__authorize-SIS-SECE-D1D2-publicfetch-R04__OPERATOR.md

blob:
a7c5880a76da9a98f9d37c5c42761322b751566a

decision:
AUTHORIZE_SIS_SECE_R01_D1D2_P552203_PUBLIC_GIT_FETCH_EXEC_R04 = YES

## Current SIS writer

puev5691/wellbeing-hq@1de10d5d61430fae49f8e27bccbd655c3ed2c972:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r09.md

blob:
285bf0fd28d6b617f582ad10f0dada6cc7e899ff

status:
CURRENT_WRITER_ESTABLISHED

terminal:
PASS_SIS_R09_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Active priority

entities/koordinator/current/KOO__semantic-entity-control-engine-r01-priority-decision__OPERATOR.md

blob:
d0521905627b306a4888261a9d414148ac64f265

decision:
SEMANTIC_ENTITY_CONTROL_ENGINE_R01_PRIMARY_PRIORITY = YES

## R03 predecessor attempt

attempt:
SIS_SECE_D1D2_PUBLICFETCH_R03_A1

facts:
- NONTERMINAL / DO_NOT_REPLAY;
- processing_started = YES;
- anonymous exact commit acquisition = SUCCEEDED;
- fetched commit = b32c3bdefa01c036e78a9e4d60fc2a78fd86418c;
- resolved package tree = 7807b3f5d43fe62b344f8ab6f6947aea98e33af7;
- CHECKPOINT_DURABLE = NOT_CREATED;
- package materialization = NOT_PERFORMED_AT_SNAPSHOT_BOUNDARY;
- Python workload = NOT_EXECUTED;
- terminal result = NOT_CREATED;
- cleanup = NOT_PERFORMED.

Do not infer any R03 checkpoint or terminal.

## Exact target and workspace

hostname:
p552203.kvmvps

device_id:
830038a0-232b-4d83-b52d-0e9973126165

R04 workspace:
/data/wellbeing-lab/tmp/sece-d1d2-publicfetch-r04-a1

Existing project repository:
/data/wellbeing-lab/repos/wellbeing-hq

The existing project repository must not be modified.

Before any R04 workspace creation or network action, verify the exact target/device and that the R04 workspace does not already exist.

## Exact immutable candidate

repository:
puev5691/wellbeing-hq

only permitted network source:
https://github.com/puev5691/wellbeing-hq.git

exact candidate commit:
b32c3bdefa01c036e78a9e4d60fc2a78fd86418c

exact package path:
entities/koder/outbox/sece-r01-offline-simulator-implementation-static-d1d2-r02/

exact package tree:
7807b3f5d43fe62b344f8ab6f6947aea98e33af7

declared package identity:
f2ff196fa8463834b08fc44d636de1aa2527db873fa38f490858a9be5688e4a1

candidate status:
OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

Expected:
24 package files;
21 SHA256SUMS payload entries.

Key Git blobs:
- SHA256SUMS: e948075bbb08a2d78654c2e3446d94001b59f64f
- MANIFEST.md: da896e89dc5a6961a4d5ffd77bdc485857ae3fe6
- PACKAGE-IDENTITY.txt: 805c38795db17adb4a09f50fb2823021b71b9102
- sece_simulator.py: e7b89c948c4e672c5b682408ce790670dfcdad5c
- run_offline_tests.py: 37b6f9e655e55d9f4be59a87052cc354ff38a328
- d1d2_tests.py: e4858197c67b4a2f8aaa275642610e5005605b92
- anti_cheat_regression_tests.py: 29ab8609955d22c8785004332df4a0a9c5d3856d
- architecture_tests.py: 6e24ba6424e99659e36c8385df34c30b608558ca
- correction_tests.py: af58242a1d988856016cdf8556dbf14faba51663

SHA256SUMS SHA-256:
86c7691d0ddc31dc15898df2015512fc5b349fa0d51b168ce3444a735eb74d2d

## Required execution sequence

1. Fresh-check task, authority, SIS writer, SECE priority and supersession.

2. Before first host/network action, create immutable positive PROCESSING_STARTED evidence for:
SIS_SECE_D1D2_PUBLICFETCH_R04_A1

Bind:
- exact R04 task locator/blob;
- accepted initial execution-state blob/version;
- target/device;
- authority;
- writer.

Read back PROCESSING_STARTED before continuing.

3. Verify:
- exact device identity;
- Python >= 3.12;
- R04 workspace absent;
- public source reachable anonymously;
- interactive credential prompting disabled.

4. Create only the fixed R04 disposable workspace and a disposable Git repository/object database inside it.

5. Acquire only enough anonymous public Git objects from the exact source to establish:
commit b32c3bdefa01c036e78a9e4d60fc2a78fd86418c
and package tree 7807b3f5d43fe62b344f8ab6f6947aea98e33af7.

6. Materialize only the exact package into R04 workspace.

Verify before Python:
- 24-file composition;
- exact key blobs;
- SHA256SUMS Git blob;
- SHA256SUMS own SHA-256;
- payload verification 21/21 PASS;
- MANIFEST and PACKAGE-IDENTITY both declare the expected package identity.

After exact materialization PASS, create and read back CHECKPOINT_DURABLE for this exact R04 prefix. Python execution must still be NOT_STARTED at checkpoint.

7. Run only:

python3 -m py_compile sece_simulator.py schema_tools.py fixture_runner.py run_offline_tests.py schema_minimum_tests.py correction_tests.py architecture_tests.py anti_cheat_regression_tests.py d1d2_tests.py

python3 -I -B run_offline_tests.py

python3 -I -B fixture_runner.py

Record Python version, exit codes and bounded stdout/stderr evidence.

8. Establish the required runtime gates:

SCHEMA_VALIDATION_PASS=YES
FIXTURE_CATALOG_54_OF_54_VALID=YES
TOTAL_FIXTURES_PASS=54/54
INPUT_COMPLETENESS_EXECUTION_PASS=15/15
BINDING_DERIVATION_PASS=15/15
CONTRACT_ID_TEST_VECTORS_PASS=YES
TRACE_ID_TEST_VECTORS_PASS=YES
TRACE_SCHEMA_PASS=YES
ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED=13/13
ORACLE_SEPARATION_TEST_PASS=YES
NO_FIXTURE_ID_BRANCHING_TEST_PASS=YES
NO_HIDDEN_BINDING_MAPPING_TEST_PASS=YES
NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS=YES
DETERMINISM_TESTS_PASS=YES
NO_SIDE_EFFECT_TESTS_PASS=YES
NEXT_GATE_RULE_END_TO_END_PIPELINE_FIXED=YES
STATICVALIDATOR_TRANSFORMATION_PROXY_REMOVED=YES
ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION=YES
DESIGN_INTERFACE_MAPPING_COMPLETE=22/22

Missing marker = NOT_PROVEN.

9. After terminal evidence is durably captured, remove only the R04 workspace if exact ownership/safety is proven. Otherwise leave it inert and record CLEANUP_DEFERRED_FOR_SAFETY.

## Boundaries / STOP

Permitted effects are limited to:
- fixed R04 disposable workspace;
- one anonymous public exact-commit Git acquisition;
- exact package materialization;
- exact offline tests;
- evidence fixation;
- safe cleanup of R04 workspace only.

STOP BLOCKED/FAIL if:
- target/writer/authority/priority/currentness mismatches;
- R04 workspace pre-exists;
- authentication/credentials are requested;
- direct exact-commit acquisition is unavailable;
- continuation requires full clone, branch/main sync, git pull, alternate remote or authenticated Git;
- commit/tree/blob/hash/composition mismatch occurs;
- Python < 3.12;
- any required workload or runtime marker fails;
- any broader authority is required.

Not authorized:
- R03 resume/replay/cleanup or workspace reuse;
- modification of existing project repo/worktree/object database;
- candidate modification;
- package installation;
- service start/enable/restart;
- simulator activation/use/deploy;
- production host/service/storage mutation;
- provider/model/API/Telegram calls;
- credential/secrets access;
- Project Source/canon mutation;
- role/recovery/current-writer mutation;
- automatic SHD rereview.

## Required result

Create:

entities/sisadmin/outbox/SIS__SECE-r01-D1D2-p552203-publicfetch-exec-r04__KOO.md

Allowed terminal:
PASS_SIS_SECE_R01_D1D2_P552203_PUBLIC_GIT_FETCH_EXEC_R04
or
BLOCKED_SIS_SECE_R01_D1D2_P552203_PUBLIC_GIT_FETCH_EXEC_R04
or
FAIL_SIS_SECE_R01_D1D2_P552203_PUBLIC_GIT_FETCH_EXEC_R04

PASS requires exact acquisition/materialization/hash checks, all three Python workloads exit 0, all required runtime gates PASS, and forbidden effects NONE.

Result must include:
- exact authority/task/attempt;
- PROCESSING_STARTED evidence;
- CHECKPOINT_DURABLE evidence if reached;
- target/workspace/source/commit/tree;
- materialization/integrity verification;
- Python version and command exits;
- runtime gate matrix;
- side-effect accounting;
- cleanup outcome;
- candidate NOT_ACTIVATED;
- next-gate classification only.

After immutable publication/readback:
RETURN KOO exact result locator + commit + blob.
Then STOP.
