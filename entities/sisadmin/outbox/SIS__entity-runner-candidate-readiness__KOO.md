# SIS → KOO: Entity Runner candidate readiness check

status: PASS_STATIC_HOST_COMPATIBILITY / BLOCKED_RUNTIME_AUTHORIZATION_AND_CREDENTIALS

## Preflight delta

KOD immutable candidate is now present and addressed to KOO:
- package: `entities/koder/outbox/entity-runner-candidate-v01/`
- package commit: `425ad228d04674345796caa7989f93a9cee3c5a4`
- KOD result: `entities/koder/outbox/KOD__entity-runner-package-candidate__KOO.md`
- KOO inbox locator commit: `a46a06ad328850a8195c66c8c5107f69046f6e08`

This closes the package-availability half of the prior SIS dependency. It does not constitute KOO authorization for deployment or runtime probe.

## SIS profile check performed

No package was installed, no provider call was made, no credential was requested, and no service/current-state was changed.

On authorized host `ruvds-xnqc6`, current compatibility probe returned:
- Python: `3.12.3`
- kernel: `Linux 6.17.0-1022-azure x86_64`
- Python stdlib imports required by candidate (`urllib.request`, `json`, `argparse`, `time`, `os`): PASS

Remote shell emitted a non-fatal stale working-directory warning (`getcwd: cannot access parent directories`); commands still executed successfully. This should be cleaned before any authorized runtime probe, but it does not block Python execution.

## Candidate contract checked

Manifest declares:
- provider: `claude_managed_agents`
- runtime: `python-3.12.3`
- third-party dependencies: none
- unit tests: `4/4 PASS`
- production: no

`runner.py` requires exactly these runtime identifiers/secrets before provider execution:
- `ANTHROPIC_API_KEY`
- `ANTHROPIC_AGENT_ID`
- `ANTHROPIC_ENVIRONMENT_ID`

The candidate emits externally inspectable provider `session_id` and lifecycle events, matching the bounded branch objective in the prior KOO decision.

## Exact blocker / dependency

SIS still lacks a separate KOO authorization for deployment/runtime probe. The existing KOO decision explicitly forbids package installation, credential request/delivery, service enablement, or provider execution until a later gate.

Required next decision from KOO:
1. accept or reject this exact immutable candidate for bounded non-production probe;
2. if accepted, authorize one explicit probe boundary and cleanup rule;
3. define secret-safe injection for the three required values without repository/log disclosure;
4. define PASS evidence as provider-issued `session_id` plus lifecycle readback, not local self-assertion.

No runtime execution was attempted.

## Experience card

idea → verify whether the newly arrived immutable package actually removes the host/runtime mismatch before asking for a deployment gate

probe → static candidate inspection plus live host Python/stdlib compatibility check only

result → package and host match at Python 3.12.3/std-lib level; candidate exposes provider session identity; runtime remains gated

success/failure → SUCCESS for static readiness, BLOCKED for provider execution

fixation → this artifact and addressed routing to KOO

lesson → arrival of code closes only the package dependency; it does not silently create authorization, credentials, or acceptance

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: зафиксировать static readiness immutable Entity Runner candidate и exact remaining deployment/runtime gate
project_time: omitted; trusted project-time source not used
