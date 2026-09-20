# KOO → SIS: install and verify booster v2 host readiness r0.1

status: TASK
execution_mode: BOUNDED_NON_LIVE_HOST_INSTALL_READINESS
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary before host mutation.

## Exact OPERATOR authority

`AUTHORIZE_BOOSTER_V2_HOST_INSTALL_READINESS_R01`

decision record:
`entities/koordinator/current/KOO__booster-v2-host-ready-decision.md`

decision commit:
`ccb1d035b61914322594ba79639a14604a2678f9`

## Exact verified integration basis

SIS terminal:
`entities/sisadmin/outbox/SIS__booster-result-v2-integration-r01-verify__KOO.md`

commit:
`8b849b3ec1c0cd3d754539c16eb8f51b474ea8be`

verdict:
`PASS_SIS_BOOSTER_RESULT_V2_INTEGRATION_R01_VERIFY`

Integration candidate:
`entities/koder/outbox/openai-booster-result-v2-integration-r01/`

boundary commit:
`b0779b4215de43ca96888df94835e97e3e15402e`

package tree:
`600f4ba691152db74dc5818c85dc822bba000bc3`

## Host

`ruvds-xnqc6`

## Goal

Install the exact verified integration candidate into the bounded host runtime in a non-live, disabled state and independently verify host-level readiness.

This is not a live provider task and not project acceptance.

## Required work

1. Freshly inspect current host runtime and existing live-child installation before changes.
2. Verify exact candidate bytes from immutable package before installation.
3. Install only the exact verified integration runtime files required by the candidate.
4. Install/register the exact candidate systemd unit derived from `wellbeing-openai-booster-result-v2.service.candidate`.
5. Preserve exact canonical credential mechanism:
   - `systemd LoadCredentialEncrypted`;
   - `secretref:openai:wellbeing-entity-boosters-restricted`;
   - exact encrypted object identity.
6. Keep the unit disabled.
7. Do not enter live mode.
8. Create/verify future result directory if required:
   `/var/lib/wellbeing/openai-booster-live-child-r01/review-results`.
9. Verify ownership/modes/write scope:
   - state boundary remains narrow;
   - result artifacts expected mode 0600;
   - no broader write paths than verified candidate.
10. Verify exact installed unit/runtime SHA-256 values against immutable candidate.
11. Verify systemd parses/loads the installed unit correctly.
12. Verify no legacy TTY credential injection path is used or newly introduced.
13. Verify ordinary KOD-triggered invocation boundary if possible without live provider transport.
14. If a sentinel/dry path is used, it must be provably unable to perform provider transport.
15. Verify result path is readable later for requester review without provider access.

## Required preserved runtime contract

Future live execution contract remains:
`claim → transport → normalize → persist schema v2 → strict readback → terminal`

Preserve:
- provider=openai;
- endpoint=`https://api.openai.com/v1/responses`;
- model=`gpt-5.6-luna`;
- D0_SYNTHETIC;
- synthetic_only;
- tools=none;
- calls=1;
- retries=0;
- fallback=none;
- max output tokens=64;
- max response bytes=16384;
- timeout=30s;
- use-once;
- requester_review_required=true;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false.

## Explicitly forbidden

- any OpenAI/provider call;
- credential value read/use/exposure;
- live mode;
- unit enablement or automatic/persistent start;
- changing canonical secretref/object identity;
- retry/fallback expansion;
- billing/account mutation;
- deployment to another host;
- project acceptance;
- production acceptance.

## Security caveat

The systemd host credential key remains not located on encrypted media.
No full-disk or host-key compromise protection is claimed.

## Expected terminal result

Return exactly one:

`PASS_SIS_BOOSTER_V2_HOST_INSTALL_READINESS_R01`

or

`BLOCKED_SIS_BOOSTER_V2_HOST_INSTALL_READINESS_R01: <exact blocker>`

or exact FAIL.

Human-facing result must state:
- exact installed runtime/unit identities;
- unit installed state;
- unit enabled state (must remain disabled);
- systemd/load/readiness result;
- result-path/write-boundary result;
- ordinary KOD-triggered invocation readiness result;
- provider calls=0;
- credential value reads/exposure=0;
- project_acceptance remains NOT_GRANTED;
- whether KOO may now consider a separate live capability acceptance/next-authority gate.

Address terminal result to KOO.
Stop after terminal result.