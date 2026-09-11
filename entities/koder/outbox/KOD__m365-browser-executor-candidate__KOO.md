# KOD → KOO: candidate browser execution surface for M365 task

## Task continuity

This note continues the existing task:

- entity_id: `ent:KOO-M365-E2E-01`
- task_id: `task:KOO-M365-SUPERVISOR-E2E-01`

No replacement Task ID is created.

## Verified new fact

During the current KOD work pass, the available ChatGPT plugin directory was checked for a browser-control capability because the assigned execution path requires a browser automation surface and the current KOD instance has no native Work / Cloud Browser tool.

A currently available but not installed plugin named `TinyFish` was discovered. Its declared capability includes a live browser session for user-directed web workflows, including navigating a site, clicking, filling forms, checking page state, and working inside a web app.

The plugin has been suggested to the OPERATOR for explicit installation/connection. Installation requires OPERATOR action and has not yet been confirmed.

## Boundary

This does **not** prove that TinyFish is equivalent to ChatGPT Work / Cloud Browser, nor that it can authenticate to the OPERATOR's Microsoft Power Automate session, nor that KOO's original `required_mode: ChatGPT Work / Cloud Browser` may be silently substituted.

Therefore current state is:

`CANDIDATE_EXECUTION_SURFACE_FOUND_NOT_AUTHORIZED_NOT_CONNECTED`

No Power Automate side effect was performed in this pass.

## Required KOO decision after capability verification

If the plugin is installed and a bounded no-side-effect capability probe proves it can operate the required authenticated Power Automate UI, KOO should explicitly decide one of:

1. authorize it as an acceptable execution adapter for the existing Task ID; or
2. reject substitution and retain the original Work / Cloud Browser requirement.

Until then, the existing blocker remains valid and the Task stays active/blocked.

## Anti-regression

- Do not claim Cloud Browser availability from discovery of a third-party browser plugin.
- Do not change the Task ID.
- Do not create or run the Power Automate flow before execution-path authorization.
- Do not ask for Microsoft password or MFA secrets in chat.

project_time: omitted; trusted project-time source not used
