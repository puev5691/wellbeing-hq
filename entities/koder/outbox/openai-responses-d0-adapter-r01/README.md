# OpenAI Responses API D0 adapter/transport r0.1

Status: bounded candidate, non-production, credential-free, zero live provider calls.

Purpose: add an OpenAI Responses provider path to the existing provider-neutral multi-model architecture without opening a second orchestration stack.

Scope:
- `D0_SYNTHETIC` only;
- provider `openai`, model `gpt-5.6-luna`;
- exact endpoint `POST https://api.openai.com/v1/responses`;
- injected/mock execution for this task;
- future-live transport present but default-deny;
- no API key value in package;
- no tools, web search, file search, computer use, code execution, fallback or project mutation.

Verification target:
- compile;
- deterministic unit tests;
- secret-like rejection;
- response/usage normalization;
- auth/rate-limit/5xx/timeout fail-closed behavior;
- checksum generation only after final bytes;
- immutable Git readback and rerun.

Provider output remains candidate/evidence only. Project acceptance is always `NOT_GRANTED` inside adapter provenance.