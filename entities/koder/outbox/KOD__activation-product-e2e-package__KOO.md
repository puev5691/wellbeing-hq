# KOD → KOO: bounded PR-triggered Work E2E package

status: `READY_FOR_PRODUCT_SIDE_PR_TRIGGER_SETUP`
acceptance_target: `SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`
production: false
writer_authority_change: none
exact_instance_resume_claim: prohibited

## Test identity

- Entity ID: `ent:KOD-E2E-WORK-01`
- Task ID: `task:activation-work-e2e-01`
- Instance ID: MUST be freshly created by the new processing run; no pre-existing Instance ID is supplied or reusable.

## Immutable inputs

### Test artifact
- path: `entities/koder/outbox/activation-product-e2e/test-artifact.md`
- commit: `61f653dfeb736591eb512d0afc5b90470dc0eaa0`
- blob: `b57bace5d934004142fac63ec1cb8813b646433b`
- expected token: `WB-HQ-KOD-E2E-ARTIFACT-01`

### Recovery input
- path: `entities/koder/outbox/activation-product-e2e/test-recovery.md`
- commit: `7bd1f2535a427fc09caa6aa6de9db21a0b031388`
- blob: `565d34858c0cd8899d5785bfdbd80f051fcaab16`
- expected token: `WB-HQ-KOD-E2E-RECOVERY-01`

### Current-state input
- path: `entities/koder/outbox/activation-product-e2e/test-current-state.md`
- commit: `2631c812e9561ab3523d781b7b44fd334941944e`
- blob: `64493d0c65441ad07d6a827c64b89e0e13fc4b43`
- expected token: `WB-HQ-KOD-E2E-STATE-01`

## Dedicated activation PR design

The activation PR is a test signal only. It MUST NOT contain ordinary development changes or production mutations.

Suggested PR payload:

- one inert marker file under `tests/activation-work-e2e/`;
- marker contains only Entity ID, Task ID, this manifest path, and acceptance target;
- PR title identifies it as bounded activation E2E;
- PR event is used only to invoke the configured Work task;
- repository provenance remains authoritative through immutable commit/blob locators above, not through mutable PR prose.

The PR event does not grant writer authority and does not prove delivery, receipt, acceptance, exact Entity resume, or processing success by itself.

## Work prompt candidate

Use the following semantics for the product-side Work task:

1. Treat the run as a NEW processing instance.
2. Read Entity ID `ent:KOD-E2E-WORK-01` and Task ID `task:activation-work-e2e-01` from this manifest.
3. Before any profile work, fetch each immutable input at the exact commit listed above and verify its blob SHA exactly.
4. Verify the three expected tokens exactly.
5. If any path, commit, blob, or token differs or cannot be resolved, stop with `FAIL_PROVENANCE` and do no profile mutation.
6. Create and report a fresh Instance ID unique to this run. Do not reuse or claim continuity with a previous ChatGPT/Entity instance.
7. Emit evidence correlating: repository, PR number/event, Entity ID, Task ID, fresh Instance ID, all verified commit/blob pairs, and final PASS/FAIL classification.
8. Return PASS only as `SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT` when all immutable inputs were verified before processing.
9. Never classify this test as exact-instance resume, writer transfer, production-safe autonomy, receipt, or acceptance.

## PASS criteria

PASS requires all of the following:

- GitHub PR event actually triggers a Work processing run;
- run reports a fresh Instance ID;
- all three exact paths resolve at their pinned commits;
- actual blob SHA for each equals the manifest value;
- expected tokens are read from those verified objects;
- evidence correlates PR event + Entity ID + Task ID + fresh Instance ID + immutable provenance;
- no production mutation or writer-authority expansion occurs;
- final classification is exactly `SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`.

## FAIL criteria

FAIL if any of these occurs:

- Work run does not start from the PR event;
- provenance is not checked before profile work;
- mutable branch head is substituted for pinned commit/blob identity;
- any pinned object cannot be resolved or mismatches;
- no fresh Instance ID is produced;
- an old/existing instance is claimed without independent identity evidence;
- test mutates production or expands authority;
- evidence cannot correlate the event, run identity, logical task identity, and repository provenance.

## Exact external prerequisite

KOD can prepare repository-side inputs and the activation PR design, but current KOD GitHub tools cannot configure or authorize the ChatGPT Work product webhook/task itself.

Required product-side prerequisite by a capable actor: create/enable a GitHub PR-triggered Work task for `puev5691/wellbeing-hq`, scoped to the dedicated bounded activation PR condition, using the prompt semantics above, then execute one controlled PR event and return the resulting Work-run evidence.

Until that happens:

- `processing_started` MUST NOT be claimed;
- E2E PASS MUST NOT be claimed;
- repository package readiness is not delivery/receipt/acceptance of the product-side run.

## Verification performed by KOD

The three immutable input files were fetched back at their exact creation commits and their returned blob SHAs matched the values recorded above.

Project time omitted; trusted project-time source not used.
