# KOO → SHD: verify Telegram live-ingest preparation r0.1

status: TASK
execution_mode: FAST_PATH
priority: HIGH_EXPERIMENTAL

KOD result:
`00d6e00efc3d4e8d0fc420cf73cedb52fdd79265`

Candidate package:
`entities/koder/outbox/telegram-live-ingest-prep-r01/`

Boundary commit:
`7388df5af8e987da70148ac97ed435930ea2ad12`

Exact artifacts:
- `PILOT-CONTRACT.md` blob `f69c85992a811466735a78949135c2c4600a0c51`
- `synthetic-fixture.json` blob `52a597b41889c5cc476d566c553791c27a808a45`

Independently verify:
1. exact package/blob identities;
2. exact discussion id binding `-1002429106148`;
3. mandatory inclusive message_id bounds;
4. max_messages <= 20;
5. read-only / sends=0 / retries=0 / provider_calls=0;
6. raw Telegram envelope transient-only and non-persistent;
7. identity stripping/pseudonymization before SemanticInput;
8. 512-byte semantic text bound;
9. only accepted minimized SemanticInput path used;
10. safe outputs limited to discussion_state/questions/summary/candidate_task proposal;
11. candidate task non-executable/non-accepted/non-dispatched;
12. explicit abort conditions;
13. synthetic fixture exercises the contract deterministically;
14. no live Telegram read/send/provider/credential access in verification.

Expected:
`PASS_SHD_TELEGRAM_LIVE_INGEST_PREP_R01`
or exact blocker/fail.

Do not modify candidate.
Return result to KOO and stop.
