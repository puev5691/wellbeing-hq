# KOO → SIS: establish verified OpenAI booster live-child execution path r0.1

status: TASK
execution_mode: BOUNDED_INFRASTRUCTURE_LIVE_CHILD_PREP
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary before execution.

## Exact causal blocker

KOD terminal blocker:
`entities/koder/outbox/KOD__openai-entity-booster-d0-live-r02-blocker__KOO.md`

commit:
`c23b7499d1b96db2b514802e981aaf706e576c6a`

blob:
`689e8b5c8e8350801af592516c530adc05e96d3e`

status:
`BLOCKED_KOD_OPENAI_ENTITY_BOOSTER_D0_LIVE_R02: VERIFIED_RESOLVER_IS_PROBE_ONLY_NO_VERIFIED_LIVE_CHILD_PATH`

Verified blocker facts:
- exact immutable task/writer/provider/model/bounds matched;
- canonical secretref mapping matched;
- exact SIS resolver bytes matched;
- fresh R02 authority durable claim = 0;
- provider calls = 0;
- credential value reads/exposure = 0;
- retries = 0;
- fallback = none;
- legacy TTY fallback was not used.

## Existing verified canonical secret path

Host:
`ruvds-xnqc6`

Canonical reference:
`secretref:openai:wellbeing-entity-boosters-restricted`

Credential mechanism:
`systemd LoadCredentialEncrypted`

Encrypted object:
`/etc/credstore.encrypted/openai-wellbeing-entity-boosters-restricted.cred`

Existing resolver probe service:
`wellbeing-openai-secretref-resolver.service`

Do not change canonical reference or encrypted object identity.

## Goal

Create and independently verify the minimal live-child execution path on `ruvds-xnqc6` that:

1. loads the same canonical encrypted credential through `LoadCredentialEncrypted`;
2. supplies it only to the exact authorized live child process;
3. is capable of the exact future OpenAI HTTPS request path;
4. preserves the immutable D0 task scope;
5. performs zero provider calls during this preparation/verification task.

## Immutable future call scope to preserve

Task identity:
`entities/koordinator/outbox/KOO__openai-booster-d0-live-r01__KOD.md`

task commit:
`b988066e0e018627cc24b95f409f3ccd0a416990`

task blob:
`691af722274bc51f87d5eeda6e7054d21ee3c9c3`

Bound future execution parameters:
- provider = `openai`;
- endpoint = `https://api.openai.com/v1/responses`;
- model = `gpt-5.6-luna`;
- data class = `D0_SYNTHETIC`;
- privacy = `synthetic_only`;
- tools = none;
- calls = 1;
- retries = 0;
- fallback = none;
- max output tokens = 64;
- max response bytes = 16384;
- timeout = 30 s;
- requester review required;
- project_acceptance = `NOT_GRANTED`;
- project-state mutation = false.

## Required work

1. Freshly inspect the existing probe resolver/unit and current OpenAI booster/live-worker runtime.
2. Create the smallest separate live-child systemd path; do not mutate the existing probe-only unit into a dual-purpose unit unless exact evidence proves that is safer and clearer.
3. Use the same `LoadCredentialEncrypted` object and canonical mapping.
4. Ensure the credential is available only inside the intended child execution context and is not emitted to stdout/stderr/logs/project artifacts.
5. The child path must be able to support AF_INET/AF_INET6 HTTPS access needed for the exact OpenAI endpoint, while preserving fail-closed scope and avoiding unrelated network capability where practical.
6. Preserve one-call / retries=0 / fallback=none / timeout / response bound semantics.
7. Preserve exact provider/model/task/writer/privacy/tools binding before transport.
8. Preserve durable one-shot claim ordering before credential resolution/provider transport for the eventual live execution.
9. Provide a non-live verification mode/sentinel that proves:
   - exact systemd credential loading reaches the intended child;
   - exact canonical mapping is used;
   - intended child path is executable by the normal KOD-triggered boundary;
   - network-capable unit/path exists, but provider transport is disabled during this verification;
   - no legacy TTY injection is reachable;
   - wrong task/writer/model/provider/privacy/tools/reference blocks;
   - missing credential object blocks;
   - result/project authority remains unchanged.
10. Independently verify installed bytes/configuration and exact service/unit identities after installation.

## Fresh R02 provider authority state

Do NOT use or claim the previous R02 provider authority in this task.
KOD confirmed durable claim count = 0, but that activation session ended with a pretransport blocker.
This task grants no provider-call authority.

## Security caveat

The systemd host credential key remains not located on encrypted media.
Do not claim full-disk/host-key compromise protection.

## Forbidden

- OpenAI/provider call;
- credential value read/print/export/hash comparison;
- legacy TTY credential injection;
- canonical secretref change;
- credential rotation/replacement;
- retries/fallback expansion;
- model/provider/task-scope change;
- billing/account mutation;
- project acceptance;
- project-state mutation;
- new provider-call authority.

## Expected terminal result

Return exactly one:

`PASS_SIS_OPENAI_BOOSTER_LIVE_CHILD_PATH_R01_READY`

or

`BLOCKED_SIS_OPENAI_BOOSTER_LIVE_CHILD_PATH_R01: <exact blocker>`

or exact FAIL.

Human-facing result must state:
- whether a verified live-child path now exists;
- exact installed mechanism/unit/path identities;
- whether normal KOD-triggered execution can invoke it without manual elevation;
- whether exact future D0 scope is preserved;
- credential value reads/exposure = 0;
- provider calls = 0;
- whether KOO may now perform a fresh causal reconciliation and consider a new one-shot live authority gate.

Address terminal result to KOO.
Stop after terminal result.