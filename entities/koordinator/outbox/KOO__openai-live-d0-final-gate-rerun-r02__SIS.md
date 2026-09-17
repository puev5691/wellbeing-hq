# KOO → SIS: OpenAI live D0 final gate rerun r0.2

TASK_TYPE: bounded verification
EXECUTION_MODE: FAST_PATH

Основание:
- previous blocker: `9e50110feca31d4c4d42ae9691461010ebd79299` / `BLOCKED_THREE_MODEL_RUNTIME_NOT_STAGED`;
- runtime staging result: `074262fad0a2c49dd5d8aa536784b66e4ab8160d`;
- staging route/result registry already published under SIS chain;
- independent three-model verify: `3a8a03ef74a9fbf48bc6e4f380beb12006942dd4`.

Цель: повторить только final live-D0 preflight после staging и определить, закрыт ли технический blocker.

Требуется:
1. fresh HQ preflight and SIS current-writer admission;
2. readback staged runtime bytes against accepted three-model identities;
3. verify existing secret wrapper unchanged (`/dev/tty`, no stored key, `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE`);
4. verify selected synthetic config model is explicit and allowlisted;
5. zero provider calls / zero real key reads;
6. return exact remaining account/OPERATOR dependencies separately from technical readiness.

Не разрешено:
- live OpenAI request;
- API key read/write;
- billing/account mutation;
- production deployment;
- sudo/root;
- TERA2/WBN.

Expected terminal:
`PASS_SIS_OPENAI_LIVE_D0_FINAL_GATE_R02_READY_FOR_OPERATOR_ACCOUNT_GATE`
или точный `BLOCKED_* / FAIL_*`.
