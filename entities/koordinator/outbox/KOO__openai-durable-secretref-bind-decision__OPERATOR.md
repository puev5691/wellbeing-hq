# KOO → OPERATOR: OpenAI restricted credential durable secretref binding gate

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Что произошло

SIS terminal result:
`BLOCKED_SIS_OPENAI_RESTRICTED_CREDENTIAL_REF_BIND_R01: NO_EXACT_ACTIVE_SECRETREF_EXISTS`.

Verified current state:
- restricted OpenAI project credential already exists;
- current runtime injects it ephemerally through hidden `/dev/tty` input;
- no active durable `secretref:openai:<identifier>` exists;
- credential value reads = 0;
- provider calls = 0.

Therefore the next step is to create one durable reference binding for the existing credential, without reading or publishing the value.

## Proposed exact reference

`secretref:openai:wellbeing-entity-boosters-restricted`

This identifier is chosen as the canonical reference for the already provisioned restricted credential.
It does not contain the credential value.

## Proposed secret-store mechanism

Use `systemd-creds` on the verified OpenAI runtime host.

Target host:
`ruvds-xnqc6`

Runtime lineage:
`/home/pev5691/openai-d0-runtime-r01`

Proposed encrypted credential object name:
`openai-wellbeing-entity-boosters-restricted`

Proposed logical mapping:
`secretref:openai:wellbeing-entity-boosters-restricted`
→ systemd credential object `openai-wellbeing-entity-boosters-restricted`.

## Safe value-injection procedure

The existing credential value is entered manually by OPERATOR in the server TTY.

Rules:
- value is typed only into a no-echo interactive prompt;
- ChatGPT/SIS/KOD must not receive the value;
- value must not be copied into chat, GitHub, files, shell history, logs or command arguments;
- value must not be printed, hashed or compared;
- binding operation may use stdin/TTY directly into `systemd-creds` encryption so the plaintext is never written to project files;
- temporary plaintext files are forbidden;
- environment persistence is forbidden;
- shell history must not contain the credential value.

## Metadata-only verification after binding

After creation, SIS may verify only:
- the exact secretref identifier;
- the exact systemd credential object name/path metadata;
- ownership/mode/existence metadata as applicable;
- that the runtime resolver maps the exact secretref to the expected credential object;
- that no plaintext value appears in project files/logs/history;
- that resolver metadata can identify the reference without decrypting/reading the credential value.

SIS must not decrypt/read/use the credential during this binding-verification task.

## Decision requested

Authorize exactly this durable reference-binding step.

Decision token:

`AUTHORIZE_OPENAI_DURABLE_SECRETREF_BIND_R01`

## Effect if approved

KOO will create one bounded SIS task to:
1. create the durable systemd credential binding for the existing restricted OpenAI credential;
2. establish the exact canonical reference `secretref:openai:wellbeing-entity-boosters-restricted`;
3. require OPERATOR to inject the existing credential value manually through no-echo TTY when the runtime requests it;
4. verify only metadata/reference mapping after binding;
5. return PASS/FAIL/BLOCKER without exposing the credential value.

After PASS, KOO may prepare the separate exact OPERATOR gate for one bounded D0 live call.

## What this decision does NOT authorize

- any OpenAI/provider call;
- credential value read/use/disclosure by any Entity;
- credential replacement or rotation;
- billing/account mutation;
- production deployment;
- project acceptance;
- Project Sources changes;
- automation beyond the exact secret-store binding operation.

## If rejected

The existing ephemeral hidden-TTY injection remains unchanged and no live-call gate will be opened.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED