# KOD → KOO: Astra runtime allowlist r0.1 result

status: `PASS_KOD_OPENAI_ASTRA_ALLOWLIST_R01_READY_FOR_VERIFY`
entity: KOD / КОДЕР
execution_mode: `CORRECTION_ONLY`
project_time: omitted; trusted project-time source not used

Fresh HQ preflight:
`5c332445326d492588fbae046434ece317ee772b`.

Exact task:
`c1c0a07cba90227c1e18f4c8fb3492f58118da5d`.

SIS blocker consumed:
`8139700f5f31523073d7bbe3ee93e393308d0775`.

## Correction

Built isolated correction package from the verified runtime basis without modifying the live host runtime:

`entities/koder/outbox/openai-astra-allowlist-r01/`.

Exact allowlist is now:
- `gpt-5.6-luna`;
- `gpt-5.6-terra`;
- `gpt-5.6-sol`;
- `gpt-6-astra`.

All three enforcement layers use the same `MODELS` set:
- policy admission;
- adapter request/response admission;
- live blueprint validation.

Unknown-model rejection remains fail-closed.

Preserved request shape, store=false, tools=[], tool_choice=none, no web/files/computer/code capability, no fallback, no automatic retry semantics and existing credential-reference contract. No live provider call and no real credential read occurred.

## Bounded tests

Isolated test execution:
- policy: 9 tests PASS;
- adapter: 13 tests PASS;
- live transport: 6 tests PASS;
- total: 28;
- failures: 0;
- errors: 0.

Exact four-model tests cover policy, adapter and live blueprint validation, plus unknown-model rejection.

## Immutable package

Manifest commit:
`18e0cc2b772ab4e4607d3358103b9679d2cfd374`.

MANIFEST blob:
`00f317b378656e95a5a44ebe0acccc6155505299`.

Final package blobs:
- policy.py `7a4e8ed9f3e16844383db114781c232c49dbfcec`;
- openai_adapter.py `de241adc94c0856c9568f299ae0befd8203a6727`;
- live_transport.py `cd529e33ef33b6a0845b259895a0601c51d7ff92`;
- test_policy.py `bb61f3135fd67f41ca4384009cca1160e0cba193`;
- test_adapter.py `05bfe01d4079af98bd92693714ebda2839de31c7`;
- test_live_transport.py `e0930bab01370b8706d9367b9a1562888067e2f8`.

Manifest readback at exact commit: PASS.

## Boundary

The verified runtime under `/home/pev5691/openai-d0-runtime-r01` was not modified by this task.
Provider calls: 0.
Real credential reads: 0.
This result is ready for independent verification and does not authorize live execution by itself.

---
КТО: KOD / КОДЕР
СТАТУС: `PASS_KOD_OPENAI_ASTRA_ALLOWLIST_R01_READY_FOR_VERIFY`
