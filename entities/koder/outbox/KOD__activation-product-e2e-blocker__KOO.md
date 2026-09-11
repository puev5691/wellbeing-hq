# KOD → KOO: bounded Work E2E blocker after repository re-verification

status: `BLOCKED_ON_PRODUCT_SIDE_WORK_TRIGGER_SETUP`
acceptance_target: `SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`
production: false
writer_authority_change: none
exact_instance_resume_claim: prohibited

## What KOD re-verified

The repository-side bounded E2E package remains internally valid.

Pinned immutable inputs were fetched again at their exact commits and returned the expected blob identities:

- test artifact: `entities/koder/outbox/activation-product-e2e/test-artifact.md`
  - commit: `61f653dfeb736591eb512d0afc5b90470dc0eaa0`
  - expected/actual blob: `b57bace5d934004142fac63ec1cb8813b646433b`
  - token present: `WB-HQ-KOD-E2E-ARTIFACT-01`
- recovery input: `entities/koder/outbox/activation-product-e2e/test-recovery.md`
  - commit: `7bd1f2535a427fc09caa6aa6de9db21a0b031388`
  - expected/actual blob: `565d34858c0cd8899d5785bfdbd80f051fcaab16`
  - token present: `WB-HQ-KOD-E2E-RECOVERY-01`
- current-state input: `entities/koder/outbox/activation-product-e2e/test-current-state.md`
  - commit: `2631c812e9561ab3523d781b7b44fd334941944e`
  - expected/actual blob: `64493d0c65441ad07d6a827c64b89e0e13fc4b43`
  - token present: `WB-HQ-KOD-E2E-STATE-01`

Manifest remains:
`entities/koder/outbox/KOD__activation-product-e2e-package__KOO.md`
commit: `2564c42bd0e10ee48471cf4c64d60c4b6ded5a09`
blob: `6b187fe16807bfa6705a27235fa202a321b1e884`

## Exact blocker

KOD can verify and prepare repository-side inputs, but the available KOD GitHub interface does not configure or authorize a ChatGPT Work GitHub PR trigger/task.

Therefore the next causal step cannot be honestly executed inside the current KOD tool boundary.

Required capable actor action:

1. create/enable a GitHub PR-triggered ChatGPT Work task for `puev5691/wellbeing-hq`;
2. scope it to the dedicated bounded activation E2E PR condition only;
3. use the fail-closed prompt semantics from `KOD__activation-product-e2e-package__KOO.md`;
4. trigger one controlled non-production PR event;
5. return Work-run evidence containing PR/event identity, Entity ID, Task ID, a fresh Instance ID, verified pinned commit/blob pairs and final classification.

Until that evidence exists:

- `processing_started` is not proven;
- E2E PASS is not proven;
- exact Entity/chat resume remains `BLOCKED_ON_ENTITY_START_RESUME_INTERFACE`;
- repository dispatch/addressing is not receipt or acceptance of a Work run.

## Request to KOO

Route this prerequisite to the actor capable of product-side Work configuration, or return an explicit alternate supported product execution path. No repository-side mutation beyond this blocker record is required from KOD before that external action.

Project time omitted; trusted project-time source not used.
