# KOO -> SIS: OpenAI credential validation before Telegram live activation r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Current Telegram pilot preparation task:
puev5691/wellbeing-hq@b63d4909b16fcf96c6edf7deef9e6e0a2726f593:
entities/koordinator/outbox/KOO__telegram-discussion-pilot-final-live-gate-prep-r01__SIS.md
blob 73fd697fcee2aee319020284949f0931bcd12610

Installed Telegram dialogue package basis:
puev5691/wellbeing-hq@59455e46db80c490e740ce96fa3834348576506c:
entities/sisadmin/outbox/SIS__telegram-discussion-admission-r02-independent-review-install-verify__KOO.md
terminal PASS_SIS_TELEGRAM_DISCUSSION_ADMISSION_R02_READY_FOR_BOUNDED_LIVE_DISCUSSION_PILOT_GATE

Installed runtime:
host ruvds-xnqc6
service wellbeing-telegram-single-entity-pilot.service
code /opt/wellbeing/telegram-single-entity-mvp-r02

Protected OpenAI credential source:
/etc/wellbeing/telegram-single-entity-pilot/secrets/openai_api_key

OPERATOR concern:
current task checked only non-secret credential-slot metadata.
Actual OpenAI credential validity/entitlement remains UNKNOWN.

Goal:
validate the existing protected OpenAI credential with the smallest possible provider-side effect before Telegram live activation.

Task:

1. Fresh-verify:
   - current SIS writer;
   - exact current Telegram pilot task lineage;
   - no superseding Telegram/OpenAI credential task/result;
   - dialogue service remains loaded/inactive/dead/disabled;
   - MainPID=0;
   - protected OpenAI credential source exists, root:root, mode 0600, non-empty;
   - do not print/read credential value into chat/log/result.

2. Use the existing protected credential locally on ruvds-xnqc6.

3. Perform one minimal OpenAI authentication/entitlement check with zero or the minimum possible provider effect.
   Preferred order:
   a) use an official read-only account/model-list endpoint already supported by the proven project OpenAI route if it can validate authentication without creating a response;
   b) if authentication alone cannot establish the exact model entitlement needed by the installed Telegram MVP, perform one minimal non-private D0 request using a synthetic fixed prompt with:
      - no project/private/user data;
      - no tools;
      - no file input;
      - no external actions;
      - store=false where applicable;
      - minimum practical output;
      - retries=0;
      - fallback=none.

4. Exact model/endpoint used must be taken from the installed Telegram MVP config/package or previously accepted OpenAI route.
   Do not silently substitute another model/provider.

5. Record only non-secret result classes:
   - VALID_AUTHENTICATION;
   - VALID_AUTH_AND_REQUIRED_MODEL_ENTITLEMENT;
   - REJECTED_CREDENTIAL;
   - ENTITLEMENT_BLOCKED;
   - RATE_OR_QUOTA_BLOCKED;
   - PROVIDER_UNAVAILABLE;
   - exact HTTP status/class where available;
   - provider call count;
   - whether any billed generation occurred.

6. Do NOT record:
   - API key;
   - Authorization header;
   - raw provider request/response body;
   - project/private data;
   - secret-bearing traceback/debug locals.

7. No billing/account mutation.
8. No credential replacement in this task.
9. No Telegram API call.
10. No Telegram send.
11. No dialogue service start/enable.
12. No tester interaction.
13. No Telegram rights/settings mutation.
14. No Project Sources/canons mutation.

14. After validation, fresh-check service remains:
   loaded / inactive / dead / disabled
   MainPID=0.

Expected terminal:

PASS_SIS_OPENAI_CREDENTIAL_VALIDATED_FOR_TELEGRAM_PILOT_R01

only if:
- credential authentication PASS;
- exact required model/route entitlement needed by the installed MVP is proven;
- no boundary violation occurred.

Otherwise return exact BLOCKED_/FAIL_ reason with non-secret HTTP/result class.

Mandatory RETURN KOO:
- validation class;
- exact endpoint/model identity used;
- provider call count;
- whether billed generation occurred;
- no-secret-leak confirmation;
- service inactive confirmation;
- explicit statement whether KOO may issue NEW exact bounded Telegram live-activation task.

Then STOP.
