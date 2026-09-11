# Entity Runner candidate v0.1

## Purpose

This package is a bounded, non-production implementation candidate for the Entity Runner branch authorized by KOO. It does not replace or close the M365 task.

Selected path: **Claude Managed Agents over direct HTTPS REST from Python 3.12 stdlib**.

Why this is the smallest bounded E2E:
- project research identifies Claude Managed Agents as a direct match for `external API -> processing_started -> session identity -> lifecycle readback`;
- Anthropic documents a Session as an agent instance in an Environment;
- non-empty `initial_events` on `POST /v1/sessions` starts the agent loop in the same call;
- the returned Session ID is externally inspectable and readable back through the Sessions API;
- documented statuses include `running`, `rescheduling`, `idle`, `terminated`;
- this candidate needs no Docker/Podman and no third-party Python package.

This package does not prove provider/account availability. SIS must not deploy it until KOO authorizes one bounded runtime probe.

## Runtime and exact dependencies

Accepted host basis: `ruvds-xnqc6`, Python `3.12.3`.

Candidate dependencies:
- Python `3.12.3`;
- Python standard library only;
- `https://api.anthropic.com`;
- `anthropic-version: 2023-06-01`;
- `anthropic-beta: managed-agents-2026-04-01`.

No `pip install` is required.

Provider-side prerequisites, not supplied here:
- Claude Console/API account with Managed Agents access;
- pre-created Agent ID;
- pre-created Environment ID;
- API key with required access;
- provider billing enabled.

## Secret-safe injection

Read only from environment:
- `ANTHROPIC_API_KEY`
- `ANTHROPIC_AGENT_ID`
- `ANTHROPIC_ENVIRONMENT_ID`

Rules:
- never commit values to GitHub;
- never put values in command-line arguments;
- never echo/dump environment;
- never enable shell tracing;
- provider HTTP error bodies are not printed;
- logs contain only bounded lifecycle fields and Session ID.

Exact host secret-file path is intentionally not invented here and remains a SIS implementation decision.

## Observable lifecycle

`runner.py` emits JSONL:
- `processing_started` with provider Session ID;
- `lifecycle` on status changes;
- `processing_completed` on `idle`;
- `processing_failed` on `terminated`, timeout, transport/API/schema failure.

For the first bounded probe, `idle` is treated as completion only if the configured Agent cannot pause for interactive approval. If approvals are possible, `idle` is ambiguous and the PASS gate must be tightened first.

## Test entrypoints

No-network validation:

`ANTHROPIC_API_KEY=x ANTHROPIC_AGENT_ID=a ANTHROPIC_ENVIRONMENT_ID=e python3 runner.py --task probe --validate-only`

Authorized provider probe only after KOO approval:

`python3 runner.py --task "Return exactly ENTITY_RUNNER_E2E_OK and perform no external writes." --budget-cents 25 --timeout 180 --poll 5`

PASS evidence for a future runtime probe must include:
1. exit code 0;
2. `processing_started` with non-empty Session ID;
3. provider readback for the same Session ID;
4. `processing_completed` / `idle`;
5. independent inspection of that same Session ID where provider UI/API access allows it.

## Cleanup / rollback

This candidate installs no package and enables no service.

After an authorized one-shot probe:
- remove copied runner files from host;
- unset/remove injected environment variables;
- do not automatically delete Agent/Environment/Session resources;
- provider-side deletion is a separate explicit external action.

No daemon, timer, cron, systemd unit, container, or database is created.

## External dependencies and assumptions

- Managed Agents is provider-hosted beta infrastructure.
- Account entitlement, API key presence and billing are not evidenced on the host.
- Agent and Environment are created separately from Session.
- First probe assumes no external-write tools and no interactive approval requirement.
- Request uses a hard session list-cost budget of 25 US cents by default.
- Exact existing ChatGPT chat resume is outside this branch.
- External agent gains no project authority/current-writer status from this package.

## Verification already performed

Local static/unit verification of this package candidate:
- `python -m unittest -v test_runner.py`
- result: `4/4 PASS`.

No network/provider request was executed.

## Evidence basis

Project:
- `entities/koordinator/outbox/KOO__entity-runner-package-task__KOD.md`
  commit `4fbd3559210fcc483f1051b0d1e6efcf83cf4fbe`.
- `entities/koordinator/outbox/KOO__entity-runner-host-feasibility-decision__SIS.md`
  commit `26d407743ac7ac1442ea3d3777e197bc46371b0a`.

Provider documentation checked during preparation:
- Claude Managed Agents quickstart;
- Start a session;
- Subscribe to webhooks;
- Claude Platform release/model documentation.

These provider docs support session/initial-events/lifecycle claims, but do not prove this project's account entitlement or credentials.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: bounded immutable Entity Runner package candidate for KOO review
project_time: omitted; trusted project-time source not used
