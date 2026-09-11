# KOD → KOO: M365 browser executor candidate reconciliation v2

## Task continuity

- entity_id: `ent:KOO-M365-E2E-01`
- task_id: `task:KOO-M365-SUPERVISOR-E2E-01`
- previous KOO decision: `RECONCILIATION_ACCEPTED_KEEP_EXACT_BLOCKER`
- previous exact blocker: `AVAILABLE_REPRODUCIBLY_CAPABLE_AUTHENTICATED_BROWSER_CONTROL_SURFACE_FOR_POWER_AUTOMATE`

The same Task ID remains active. No replacement Task ID is created.

## New reproducible evidence

During the current KOD pass, ChatGPT plugin discovery was repeated using the available Plugin Management surface with the query:

`browser automation TinyFish web app navigation`

The current surface returned an available plugin:

- display_name: `TinyFish`
- plugin_id: `plugin_asdk_app_695325bae7348191b58ae9349a963d22`
- global status: `ENABLED`
- installation_policy: `AVAILABLE`
- installed: `false`
- declared capability: live browser session for user-directed workflows, including site navigation, clicking, form filling, page-state checks and work inside a web app.

The same discovery also returned `Opera Browser Connector` as an additional browser-surface candidate, but no capability claim is made for Power Automate from its presence alone.

This is new reproducible evidence relative to the KOO decision that closed the prior TinyFish branch because the plugin was not visible on the then-available search surface.

## What this changes

The exact blocker is no longer correctly described as "no reproducibly discoverable browser-control candidate exists".

The narrower verified state is now:

`REPRODUCIBLE_BROWSER_CONTROL_CANDIDATE_AVAILABLE_NOT_INSTALLED_NOT_AUTHENTICATED_NOT_CAPABILITY_PROBED_FOR_POWER_AUTOMATE`

This does **not** establish an authenticated browser control surface and does **not** satisfy the M365 execution dependency yet.

## Required next decision

Because KOO explicitly allowed reopening the TinyFish branch only if new reproducible evidence changed the dependency, this note returns that new evidence for review.

The next admissible stage, if KOO accepts the evidence, is bounded and side-effect free:

1. OPERATOR explicitly installs/connects the candidate plugin;
2. KOD performs only a no-side-effect capability probe;
3. verify whether an authenticated Power Automate UI can be opened/read/navigated;
4. perform no flow creation, save, run, PR creation, subscription, purchase, tenant creation or authority expansion;
5. return PASS/FAIL evidence to KOO before any architecture substitution.

## Boundaries

- TinyFish is **not** declared equivalent to ChatGPT Work / Cloud Browser.
- No Power Automate side effect was performed.
- No Microsoft password/MFA secret is requested or stored.
- No writer/adapter authority is expanded.
- Existing alarms remain enabled.

## Anti-regression

Do not silently substitute a third-party browser plugin for the KOO-required Work / Cloud Browser path. A reproducibly discoverable candidate is evidence for a new bounded probe only, not authorization to execute the M365 flow task.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать новое воспроизводимое evidence, меняющее прежний negative plugin-discovery факт, и вернуть его KOO без изменения Task ID и без внешних side effects
project_time: omitted; trusted project-time source not used
