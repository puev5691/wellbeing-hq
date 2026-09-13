# Future D0 live gate checklist

This package does **not** authorize or perform a live request.

Before a future one-request `D0_SYNTHETIC` live pilot, independently verify and authorize:

1. KOO has issued an explicit live-D0 authorization for this exact adapter/package identity.
2. OPERATOR-side Anthropic/Claude Console organization exists and is accessible.
3. Billing/credits arrangement is ready; this package does not purchase credits.
4. `claude-sonnet-5` access is confirmed for the exact organization/workspace.
5. Current rate/spend limits are read back for that account if materially required.
6. A dedicated approved credential is available through secret injection as `ANTHROPIC_API_KEY` or a separately approved equivalent; no value is written to GitHub.
7. Live transport implementation is separately reviewed. r0.1 contains no live network transport.
8. Input is independently confirmed `D0_SYNTHETIC`; no project/private data is present.
9. Tools/search/files/caching/MCP/Managed Agents/code execution/fallback remain OFF.
10. Provenance for the live run must record exact request/response identity and actual external-network-used=true; it must not reuse the mock provenance flag.

Any missing item is fail-closed.
