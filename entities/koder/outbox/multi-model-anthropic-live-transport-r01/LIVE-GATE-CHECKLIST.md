# Future D0 live gate checklist

This checklist is documentation only. Do not execute a live call under the current task.

Before one real D0 call, independently verify all of the following:
1. KOO/OPERATOR explicitly authorizes one live D0 request against this exact immutable package identity.
2. Anthropic/Claude Console account and organization are available to the OPERATOR.
3. Billing/credits are ready. This package does not purchase credits.
4. `claude-sonnet-5` is actually accessible to that account at the time of the gate.
5. Current rate/spend limits are acceptable.
6. A real key is created/managed outside repository artifacts and injected only as `ANTHROPIC_API_KEY`.
7. Payload is independently confirmed `D0_SYNTHETIC`, not project/private data.
8. Tools/search/files/caching/MCP/Managed Agents/code execution/fallback remain OFF.
9. Exact endpoint remains `https://api.anthropic.com/v1/messages`.
10. Exact model remains `claude-sonnet-5`.
11. Timeout and one-attempt/no-retry boundary are accepted.
12. Result provenance is retained and checked for `external_network_used=true` only after actual request attempt.

Future command template, **not to execute now**:

`ANTHROPIC_LIVE_D0=EXPLICIT_D0_LIVE ANTHROPIC_API_KEY='<runtime-secret>' python3 launcher.py --config D0-LIVE-CONFIG.example.json --live`

The placeholder is not a credential. Real secret injection must happen only in the separately authorized live gate.
