# Anthropic direct adapter r0.1

Credential-free, network-disabled preparation for a later separately authorized `D0_SYNTHETIC` live gate.

Future target route:
`local gateway → https://api.anthropic.com/v1/messages → claude-sonnet-5`.

Current package cannot perform live HTTP. `AnthropicDirectAdapter.run_mock()` accepts only `MockTransport`; the implementation imports no socket/HTTP/provider SDK/process-execution module.

Auth contract is reference-only: environment/secret injection named `ANTHROPIC_API_KEY`. No secret value is stored in request plans, provenance, tests, logs, or package files.

Request body is deliberately minimal: `model`, bounded `max_tokens`, and one synthetic text message. Tools, search, files, caching, MCP, Managed Agents, code execution, fallback, alternate provider, project mutation and production are rejected fail-closed.

The future live transport is **not implemented** in r0.1. Separate KOO authorization plus account/billing/key/model-access evidence is required before any live request.

Local checks:
- `python3 -m py_compile anthropic_adapter.py test_anthropic_adapter.py`
- `python3 -m unittest -v`

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: подготовить credential-free/network-disabled Anthropic Messages adapter для будущего D0 live gate
СТАТУС: candidate_nonproduction_mock_only
