# KOO -> SIS: Telegram live runtime config identity reconciliation r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

## Exact blocker result

puev5691/wellbeing-hq@1ce88ff9f5aa25fe6a10f8c33eb52c671e86371c:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-install-verify-result__KOO.md

blob:
f6586bcfbfe8ba6f45c631b25772d483318778cf

terminal:
BLOCKED_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_STATIC_RUNTIME_IDENTITY_MISMATCH

Verified mismatch:

current live runtime.json SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

reviewed package config.example.json SHA-256:
5737bd42abd092e3adf0f690f8928348a0df104a6a649d67cb1abb4064a91e6d

Verified non-mutations from blocked install:
- code mutation NONE
- DB mutation NONE
- config mutation NONE
- allowlist mutation NONE
- credential mutation NONE
- service start NONE
- Telegram/OpenAI calls NONE

Service final:
loaded / inactive / dead / disabled / MainPID=0

## Exact reviewed candidate basis

SIS independent review:

puev5691/wellbeing-hq@a6873d9b2fe0200dc2d02a17c20aeb9e52c2efcb:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-review-result__KOO.md

blob:
fe98163b93e5bb7266d2d11a01e4a52012b89495

terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_REVIEW_READY_FOR_SEPARATE_INSTALL_VERIFY

KOD package result:

puev5691/wellbeing-hq@b13efdd6fe32a72c4e8a0f58e2a009457b2e329b:
entities/koder/outbox/KOD__telegram-routing-observability-r01-result__KOO.md

blob:
20aa087daec5497007b1cd307c36e17047156723

Package:

puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/

tree:
bbe40dc80670b33594f997cea52e42508a7ae12b

## Goal

Perform a READ-ONLY reconciliation of the exact current live runtime.json identity and semantics against the accepted Telegram r0.2 runtime contract / installation evidence.

Return exactly one normative operational decision:

ACCEPT_CURRENT_LIVE_CONFIG_IDENTITY

or

NEEDS_CONFIG_CORRECTION

If NEEDS_CONFIG_CORRECTION, provide exact authorized candidate bytes/content hash for a future separate correction task. Do not mutate anything in this task.

## Scope

### 1. Current runtime.json exact identity

Read the current runtime.json without reading credential files or secret values.

Determine and preserve:
- exact path;
- exact byte length;
- exact SHA-256;
- exact normalized semantic JSON structure;
- keys and non-secret values;
- owner/group/mode metadata.

If runtime.json itself contains a secret unexpectedly:
STOP, redact content from result, report exact blocker.
Do not publish the secret.

### 2. Accepted r0.2 basis search

Perform a narrowly scoped fresh repository reconciliation for the accepted Telegram r0.2 installation/runtime evidence.

Search only relevant Telegram SIS/KOD/KOO artifacts needed to establish:
- accepted r0.2 runtime installation;
- runtime.json generation/placement;
- accepted discussion/bot/model/provider/polling bindings;
- any exact config content/hash/manifest recorded at installation time.

Do not load broad unrelated archive.

If an exact immutable accepted runtime.json content/hash exists:
return locator + commit + blob/hash and compare directly.

If it does not exist:
state:
ACCEPTED_LIVE_CONFIG_HASH_PREVIOUSLY_UNPINNED
and use the strongest exact semantic installation evidence that actually exists.
Do not invent a historical hash.

### 3. Semantic comparison against reviewed package config.example.json

Compare current live runtime.json to:

reviewed package config.example.json
SHA-256:
5737bd42abd092e3adf0f690f8928348a0df104a6a649d67cb1abb4064a91e6d

Classify every difference as one of:

FORMAT_ONLY
INSTALL_PATH_SPECIFIC
RUNTIME_SECRET_REFERENCE_SPECIFIC
RUNTIME_STATE_PATH_SPECIFIC
EXPECTED_LIVE_VALUE
MATERIAL_SEMANTIC_DELTA
UNKNOWN

Do not equate byte mismatch with semantic mismatch.

At minimum compare:
- discussion_chat_id
- discussion_chat_type
- bot_id
- bot_username
- activation command
- provider
- model
- polling settings
- allowed_updates
- transcript/history limits
- DB/state paths
- allowlist path
- credential reference paths
- any admission-related setting
- any provider/model fallback setting
- any retention/privacy-related setting

### 4. Contract compatibility

Determine whether current live runtime.json is semantically compatible with the accepted r0.2 runtime contract already proven in prior live/preflight work.

Use only exact evidence.

Specifically verify current live config still binds:
- discussion chat -1002429106148
- supergroup
- bot id 8866633840
- username WBNP_Media_Bot
- OpenAI provider
- model gpt-5.6-luna
- expected long-polling behavior
- exact current allowlist reference
- expected DB/state path
- expected credential reference mechanism

Also check there is no unexpected:
- second chat;
- fallback provider/model;
- widened admission;
- extra tester source;
- webhook mode;
- altered privacy/retention semantics;
- unreviewed runtime behavior toggle.

### 5. Immutable accepted identity decision

If the current live runtime.json is semantically identical/compatible and differences from config.example.json are non-material installation/runtime-specific:

Return:

decision:
ACCEPT_CURRENT_LIVE_CONFIG_IDENTITY

Pin:
- exact live runtime.json SHA-256;
- exact non-secret semantic content identity;
- exact path;
- exact accepted semantic basis locators;
- statement that byte mismatch to config.example.json is non-material.

This decision is evidence for a future NEW install/verify task only.
It does not activate installation or live use.

If a material semantic delta exists:

Return:

decision:
NEEDS_CONFIG_CORRECTION

Specify:
- exact differing fields;
- why material;
- exact desired corrected non-secret runtime.json content or deterministic transformation;
- exact candidate SHA-256 if fully determinable from non-secret bytes;
- whether credential/path placeholders require SIS-side installation rendering.

Do not write corrected file.

If evidence is insufficient:
return exact BLOCKED_/UNKNOWN rather than choosing either decision by guess.

## Safety boundary

READ-ONLY ONLY.

Do NOT:
- mutate runtime.json;
- mutate any config;
- mutate code;
- migrate DB;
- create DB backup requiring mutation if avoidable;
- start/enable service;
- call Telegram;
- call OpenAI;
- read credential contents;
- mutate allowlist;
- change webhook/bot/channel settings;
- replay blocked install task.

Service must remain:
loaded / inactive / dead / disabled / MainPID=0.

Dialogue process must remain absent.

## Expected terminal

PASS_SIS_TELEGRAM_LIVE_RUNTIME_CONFIG_IDENTITY_RECONCILIATION_R01

with decision:
ACCEPT_CURRENT_LIVE_CONFIG_IDENTITY
or
NEEDS_CONFIG_CORRECTION

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- current runtime path/hash/size/metadata;
- whether accepted historical hash existed;
- exact accepted r0.2 evidence locators;
- semantic diff table/classification;
- compatibility verdict;
- exact decision;
- pinned accepted live config identity OR exact correction bytes/transform;
- confirmation mutation NONE;
- service final state;
- Telegram/OpenAI calls NONE;
- exact next condition:
  READY_FOR_NEW_ROUTING_OBSERVABILITY_INSTALL_VERIFY
  or exact blocker.

Then STOP.
