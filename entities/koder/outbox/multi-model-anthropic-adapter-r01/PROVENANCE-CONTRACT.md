# Provenance contract

Successful mock execution records:
- provider = `anthropic`;
- model = `claude-sonnet-5`;
- SHA-256 request identity excluding credential value;
- SHA-256 exact mock response body identity;
- input/output token usage parsed from response;
- adapter version;
- D0 data class and synthetic locator/hash;
- policy decision;
- `external_network_used=false`;
- tools/search/files/caching/MCP/Managed Agents/code execution/fallback/project mutation all false;
- cost estimate based only on returned usage.

No credential value may appear in provenance.

Cost basis accepted by task:
- input: `$2 / MTok`;
- output: `$10 / MTok`;
- estimate only, not billing evidence.
