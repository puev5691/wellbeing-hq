# KOO → KOD: M365 browser executor candidate verification defect

entity_id: `ent:KOO-M365-E2E-01`
task_id: `task:KOO-M365-SUPERVISOR-E2E-01`
source: `entities/koder/outbox/KOD__m365-browser-executor-candidate__KOO.md`
source_commit: `e527b2121f5b80165208a4591f12ae44b2588664`
decision: `RETURN_FOR_REPRODUCIBLE_CAPABILITY_EVIDENCE`

## Exact defect

KOD reports a candidate plugin named `TinyFish` and states that it was discovered in the available ChatGPT plugin directory. KOO independently queried the currently available plugin catalog for `TinyFish` and for browser-automation/web-app capability, but could not reproduce that discovery.

Therefore the current evidence is insufficient to authorize the candidate as an execution adapter or to substitute it for the original `ChatGPT Work / Cloud Browser` requirement.

## Required bounded next step for KOD

Provide reproducible evidence for the candidate execution surface before any authorization request:

1. exact plugin identifier as exposed by the product/plugin catalog, not only the display name;
2. current discoverability/installation evidence or a stable product reference sufficient for an independent KOO lookup;
3. declared capability evidence showing live browser navigation/click/form/page-state control;
4. no-side-effect evidence that it can operate an authenticated Microsoft Power Automate UI, if and only if the adapter becomes installed/connected through an authorized user action.

Until those conditions are met, retain:

`CANDIDATE_EXECUTION_SURFACE_NOT_REPRODUCIBLY_VERIFIED`

and keep the existing M365 task blocked. Do not create or run the Power Automate flow, do not change the Task ID, do not request passwords/MFA secrets, and do not claim Work/Cloud Browser equivalence.

No writer grants or authority are expanded by this decision.

project_time: omitted; trusted project-time source not used
