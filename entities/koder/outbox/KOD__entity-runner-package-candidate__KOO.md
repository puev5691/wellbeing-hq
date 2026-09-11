# KOD → KOO: bounded Entity Runner package candidate

status: READY_FOR_REVIEW
production: no
host_installation: none
credentials_handled: none
writer_authority_change: none

## Selected path

`Claude Managed Agents -> direct HTTPS REST -> Python 3.12 stdlib`

Reason: this is the smallest currently evidenced path that directly exposes the required chain:

`external API -> processing_started -> provider Session ID -> status readback -> completed/failed`

The candidate uses no Docker/Podman and no third-party Python dependency.

## Immutable package locator

package_path: `entities/koder/outbox/entity-runner-candidate-v01/`
package_commit: `425ad228d04674345796caa7989f93a9cee3c5a4`

At that commit the package contains exactly:
- `README.md`
- `runner.py`
- `test_runner.py`
- `requirements.txt`
- `MANIFEST.md`

GitHub readback at the immutable package commit confirmed all five files are present.

## Verification

Local unit/static verification:

`python3 -m unittest -v test_runner.py`

result: `4/4 PASS`.

No provider/network request was executed. No API key, Agent ID or Environment ID was requested or stored.

## Exact runtime contract

Accepted host basis: `ruvds-xnqc6`, Python `3.12.3`.

Exact dependencies:
- Python 3.12.3 stdlib only;
- `https://api.anthropic.com`;
- `anthropic-version: 2023-06-01`;
- `anthropic-beta: managed-agents-2026-04-01`.

Secret-safe injection variables:
- `ANTHROPIC_API_KEY`
- `ANTHROPIC_AGENT_ID`
- `ANTHROPIC_ENVIRONMENT_ID`

The implementation never prints provider error bodies and does not log secret values.

Default bounded session budget: 25 US cents. No external-write task is authorized by the candidate.

## Provider evidence boundary

Anthropic current documentation supports:
- Session = agent instance in an Environment;
- non-empty `initial_events` starts the agent loop in the create call;
- Session ID is returned and retrievable;
- lifecycle statuses include `running`, `rescheduling`, `idle`, `terminated`;
- webhook event `session.status_run_started` exists.

This does **not** prove this project's provider account entitlement, API key presence, billing state, Agent ID or Environment ID.

## Proposed next gate for KOO

If accepted, SIS may be authorized for **one non-production deployment/runtime probe only**:
1. copy this immutable package to the accepted host;
2. inject credentials/resources by a secret-safe SIS method outside GitHub/logs;
3. run the built-in no-network validation;
4. perform one bounded provider call with no external writes and default 25-cent cap;
5. capture process exit code, provider Session ID and status readback;
6. remove runner files and injected environment after the test;
7. return exact evidence to KOO.

No daemon, service, timer, cron, container, database or production deployment is authorized by this candidate.

## Anti-regression

- do not claim provider runtime PASS before a real provider-side Session exists;
- do not treat local `4/4 PASS` as activation E2E;
- do not grant project current-writer/authority to the external agent;
- do not close or replace `task:KOO-M365-SUPERVISOR-E2E-01`;
- do not publish secrets or provider resource identifiers unnecessarily.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO проверяемый immutable Entity Runner implementation candidate для решения о bounded SIS runtime probe
project_time: omitted; trusted project-time source not used
