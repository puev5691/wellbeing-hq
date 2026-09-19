# KOO → SHD: independent verify Telegram semantic synthetic r0.1

status: TASK
execution_mode: FAST_PATH
priority: HIGH_EXPERIMENTAL

KOD result:
`e02534cb73dc472a2c7e8152d18a2eb39d0e94d6`

Candidate package:
`entities/koder/outbox/telegram-semantic-synth-r01/`

Package boundary commit:
`a9de14997080d753f1676161ac6bb5c19b26bd9d`

## Independently verify

1. exact package/blob identities;
2. synthetic provenance explicit;
3. raw/unbounded Telegram update shapes rejected;
4. unnecessary participant identity not introduced;
5. no raw discussion-text persistence outside bounded synthetic fixtures;
6. SemanticInput contract preserved;
7. discussion_state generated from synthetic events;
8. candidate questions/summary/candidate_task generated as claimed;
9. candidate_task remains candidate-only;
10. `executable=false`;
11. `approved_for_execution=false`;
12. no dispatch/acceptance;
13. zero live Telegram reads/sends;
14. zero live provider calls;
15. no credentials or external mutation.

Expected:
`PASS_SHD_TELEGRAM_SEMANTIC_SYNTH_R01`
or exact blocker/fail.

Do not modify candidate.
Return result to KOO and stop.
