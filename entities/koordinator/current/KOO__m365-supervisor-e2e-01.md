# KOO: Microsoft 365 supervisor E2E-01

## Цель

Проверить минимальный внешний контур замены внутренних ChatGPT-будильников:

`Microsoft Power Automate Recurrence → GitHub CreatePullRequest → ChatGPT Work PR-trigger → recovery/checkpoint → profile processing`.

Тест не выключает действующие ChatGPT automations до полного E2E PASS.

## Test identity

- entity_id: `ent:KOO-M365-E2E-01`
- task_id: `task:KOO-M365-SUPERVISOR-E2E-01`
- production: `no`
- writer_authority_change: `none`

## Prepared GitHub input

repository: `puev5691/wellbeing-hq`
base: `main`
head: `m365/activation-e2e-koo-01`
marker:
`tests/activation-m365-e2e/KOO__m365-supervisor-e2e-01.md`
marker_commit: `ea0ebdae5125a9bd9321827f549f1f5c85e9d80e`

KOO intentionally did NOT create the pull request. The first PR for this test must be created by Microsoft Power Automate GitHub connector so that event provenance is independently observable.

## Power Automate configuration

Flow type: Scheduled cloud flow.

Trigger:
- `Recurrence`
- test cadence: one hour
- timezone: explicitly configured in Power Automate; do not infer project time from it.

Action:
- connector: `GitHub`
- operation: `CreatePullRequest`
- repository owner: `puev5691`
- repository name: `wellbeing-hq`
- title: `[E2E] M365 activation KOO 01`
- head: `m365/activation-e2e-koo-01`
- base: `main`
- body: include `ent:KOO-M365-E2E-01`, `task:KOO-M365-SUPERVISOR-E2E-01`, marker commit `ea0ebdae5125a9bd9321827f549f1f5c85e9d80e`
- draft: `false`

Microsoft documentation classifies the GitHub connector for Power Automate as Standard. The CreatePullRequest action is currently documented as preview.

## Stage A PASS

PASS only if:
1. a Power Automate run is visible in run history;
2. that run reports successful GitHub `CreatePullRequest`;
3. the corresponding PR actually exists in `puev5691/wellbeing-hq`;
4. PR head/base and marker commit match this checkpoint;
5. no OPERATOR-created PR is substituted for the Microsoft-generated event.

If tenant/work-account authentication or GitHub connection cannot be completed, classify exact blocker; do not retry signup blindly.

## Stage B: ChatGPT Work

After Stage A PASS, configure one bounded ChatGPT Work event-triggered task for the test PR event.

The Work run must treat itself as a NEW processing instance and must first restore:
- Entity ID;
- Task ID;
- this checkpoint;
- immutable recovery/current-state locators;
- unfinished causal chain.

The Resume-First Gate applies before profile work.

PASS target:
`SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT_AND_TASK_CHECKPOINT`.

Exact existing-chat resume is not required and must not be claimed.

## Current checkpoint

task_status: ACTIVE/BLOCKED
current_goal: replace internal alarm dependence with an externally triggered supervisor path
current_step: establish one reproducibly available authenticated browser-control execution surface and then create/verify the bounded Power Automate flow
last_verified_result:
- GitHub test branch and inert marker remain prepared
- Power Automate portal access in OPERATOR browser was previously evidenced
- KOD browser-control attempt via current instance/remote host was blocked
- KOD TinyFish discovery was initially non-reproducible and reconciled as such
- KOO fresh product-catalog recheck now reproducibly finds TinyFish plugin id `plugin_asdk_app_695325bae7348191b58ae9349a963d22`, installed=false, installation_policy=AVAILABLE, declared capability includes live browser navigation/click/form/page-state/web-app interaction
- KOO fresh product-catalog recheck also finds Opera Browser Connector id `plugin_asdk_app_69d669e1d5c88191957786fbcd38b411`, installed=false, installation_policy=AVAILABLE, declared capability includes reading open Opera tabs, screenshots and navigation
- Opera Browser Connector has been suggested to OPERATOR for explicit installation/connection
in_flight_action: none
unknown_postconditions:
- no browser plugin installation/connection is confirmed
- no authenticated Power Automate control through either adapter is proven
- no Power Automate flow creation is verified
- no successful Power Automate run is verified
- no Microsoft-created GitHub PR is verified
- ChatGPT Work PR-trigger remains unverified on product side
next_admissible_action:
- after explicit OPERATOR installation/connection of a browser-control adapter, perform a bounded no-side-effect capability probe against the already-open Power Automate session
- if probe proves authenticated navigation/click/form/page-state control, authorize the adapter for this SAME Task ID and create the bounded scheduled flow
- if probe fails, preserve exact blocker and move to next execution path without changing Task ID
failure_mode: keep existing ChatGPT automations enabled; do not repeat Microsoft signup; do not claim adapter capability from catalog presence alone
checkpoint_reason: browser_execution_surface_reconciliation

## KOO decision on browser executor candidates

1. The prior KOD conclusion `CANDIDATE_EXECUTION_SURFACE_NOT_REPRODUCIBLY_VERIFIED` is superseded by this later KOO product-catalog readback for **existence/discoverability only**.
2. TinyFish is now reproducibly discoverable, but not installed/connected and therefore not yet accepted as an execution adapter.
3. Opera Browser Connector is also reproducibly discoverable and is the preferred first probe when the OPERATOR's active Power Automate session is in Opera, because it is specifically designed to connect ChatGPT to open Opera tabs.
4. Catalog discovery does not prove authenticated control, form submission or Power Automate compatibility.
5. No Power Automate side effect is authorized until a bounded capability probe succeeds.

## Anti-regression

Do not:
- disable current ChatGPT alarms before full E2E PASS;
- count catalog discovery as plugin installation;
- count plugin installation as authenticated control;
- count navigation/read access as form-control capability;
- count a successful Microsoft login as flow creation;
- count flow creation as a successful run;
- count a Power Automate run as PR creation without GitHub readback;
- count PR creation as ChatGPT Work activation;
- count new Work processing as exact existing-chat resume;
- retry tenant signup while tenant state is unknown.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: bounded E2E checkpoint для Microsoft 365 внешнего supervisor
СТАТУС: active_test_checkpoint
source: verified GitHub state + current plugin catalog readback + prior KOD reconciliation
approval_status: not_project_source
responsibility_boundary: test candidate; existing alarms remain safety fallback until full E2E PASS
