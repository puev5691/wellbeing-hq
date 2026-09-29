# KOO -> KOD: Telegram single-provider Entity dialogue MVP r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended KOD writer:
puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md
blob cf1c84f9df7c90509703e4885844d0cf871ff412

Priority authority:
puev5691/wellbeing-hq@e360ce75dfc8c803a54f69a3aae4188659bf6938:
entities/koordinator/outbox/KOO__telegram-single-entity-mvp-priority__OPERATOR.md

Goal:
prepare the shortest deployable candidate for a closed live Telegram dialogue pilot with one neural Entity and real invited human testers.

Reuse proven project basis where applicable:
- Telegram facilitator core independent PASS @ 947ea4b76d367774fbc2ae37b61d49e0e89d55bc
- normalized-event bridge independent PASS @ c0ed7057da344bf6b10b0718960c36962b8d9536
- Phase1B threading-fix candidate @ 62f82c3322f28adc55b47b1a7064fccb23e4c351
- OpenAI bounded live D0 proven @ 80a87f5920bb26c06c31006b3ccb7a9eabd62bfa

Task:
design and materialize one minimal single-provider Telegram dialogue MVP candidate.

Required:
1. real text-message ingress path;
2. per-chat/thread dialogue state;
3. bounded Entity bootstrap/system prompt input;
4. one OpenAI provider adapter path using existing accepted route where compatible;
5. response generation and Telegram reply path;
6. duplicate/replay protection;
7. minimal privacy/logging behavior;
8. explicit tester allowlist or equivalent closed-pilot gate;
9. timeout/error fallback visible to user;
10. exact deploy/run/stop/rollback instructions;
11. minimal tests, including multi-turn dialogue;
12. exact list of remaining live/runtime dependencies.

Prioritize working dialogue over multi-provider abstraction.
Do not implement Gemini/DeepSeek/Anthropic in this task.
Do not redesign the whole semantic engine.

No live Telegram send.
No provider live call.
No credential disclosure.
No production deployment.
No billing/account mutation.
No Sources/canons mutation.

Return:
one immutable MVP candidate/result to KOO,
with exact package locator,
tests,
runtime dependencies,
and exact next live-pilot gate.

Mandatory RETURN KOO.
Then STOP.
