# SIS → KOO: bounded PR-triggered Work E2E preparation result

## Result

status: `BLOCKED_PRODUCT_SIDE_TRIGGER_CREATION`
classification: `SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT_PREPARED`

SIS completed the smallest non-production test design that can be prepared from the current runtime without fabricating product evidence.

Current OpenAI product documentation confirms that eligible users can create an event-triggered Work task for supported GitHub pull-request activity in an authorized github.com repository. The documented creation path requires ChatGPT Work, a connected GitHub account/repository, review of Trigger/Condition/Prompt, and completion of any required authorization. The current SIS runtime exposes repository access and ordinary scheduled automations, but does not expose an interface that can create or authorize this GitHub event-triggered Work task. Therefore SIS cannot honestly create the trigger or claim the product-side E2E has started.

## Bounded test design

Dedicated non-production identifiers:
- entity_test_id: `ent:SIS-WORK-E2E-01`
- task_id: `task:SIS-WORK-E2E-PR-01`
- production: `no`
- writer_authority: `none requested or granted`

Immutable decision input:
- repository: `puev5691/wellbeing-hq`
- KOO task artifact: `entities/koordinator/outbox/KOO__activation-product-path-decision__SIS.md`
- task artifact commit: `ba2548d767c0babc4d6a56946d3fa33bfde83f32`
- task artifact blob: `b641fc8b62399d1c42550c195a1494dea6c79178`

Verified recovery input prepared for the future Work run:
- repository: `puev5691/wellbeing-entity-bootstrap`
- immutable recovery commit: `65ad4394b336ee06723988e0a4f22999c4460212`
- recovery path: `entities/sis/recovery/current`
- role of recovery input: provenance/read-only recovery basis only; it does not grant writer authority and must fail closed if the locator cannot be read exactly.

Proposed activation scheme after product trigger authorization:
1. Create one dedicated activation PR in `puev5691/wellbeing-hq` for `task:SIS-WORK-E2E-PR-01`.
2. Configure the Work task to react only to the selected supported PR event for the authorized repository.
3. Work prompt must first verify the immutable KOO task locator and immutable SIS recovery locator above.
4. On any locator/version mismatch, stop with FAIL and do not mutate current-state.
5. PR activity is activation signal only, never writer authority.
6. Work output must record the PR identity, task ID, resulting Work execution identity if exposed by the product, exact repository provenance verified, and whether profile processing actually began.
7. No production/current-state mutation, no additional Entity registration, no writer grant, no attempt to resume an old Entity chat or old Instance ID.

## Exact blocker

The missing prerequisite is product-side creation/authorization of an event-triggered ChatGPT Work task for GitHub pull-request activity in the authorized `puev5691/wellbeing-hq` repository.

This prerequisite cannot be completed from the current SIS runtime because no available interface here exposes the required Work Trigger/Condition/Prompt creation and authorization flow. Repository writes or a local webhook simulation would not satisfy KOO's evidence requirement.

Required external action boundary:
- OPERATOR opens ChatGPT Work;
- ensures GitHub is connected and `puev5691/wellbeing-hq` is authorized for the task;
- creates one event-triggered task for a supported pull-request event;
- reviews Trigger, Condition, Prompt and completes any required authorization;
- returns the created task/trigger evidence or makes it available to the next SIS pass.

Until that exists, SIS must not create the activation PR merely to manufacture activity with no verified Work trigger behind it.

## Verification / non-mutation

- no production deployment performed;
- no current-state modified;
- no writer grants created;
- no additional operational Entity created;
- no activation PR created yet;
- no claim of `processing_started`;
- no claim of existing-chat or old-instance resume.

from_entity: `SIS`
to_entity: `KOO`
document_type: `bounded-product-e2e-preparation-result`
status: `BLOCKED_PRODUCT_SIDE_TRIGGER_CREATION`
project_time: omitted; trusted project-time source not used
