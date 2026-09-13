# Live provenance contract

Successful transport result records only bounded metadata:
- provider/model/API version;
- transport version;
- request hash computed before auth injection;
- response hash;
- input/output token counts;
- data class;
- credential source name `ANTHROPIC_API_KEY`, never its value;
- `credential_value_recorded=false`;
- `external_network_used`;
- automatic retry/fallback/tools/search/files/caching/MCP/Managed Agents/code execution/project mutation/production flags.

`external_network_used=false` for all injected/mock tests.

In the real path, `external_network_used` becomes true immediately before the real `UrllibExecutor.request()` attempt. Any timeout/network/HTTP/provider parsing error propagated after that attempt carries `external_network_used=true`. Missing live switch, invalid blueprint, invalid timeout or missing credential occur before provider request and do not claim external network use.

The request hash excludes runtime auth headers and secret values. Provenance/result/error objects must never contain `x-api-key` value or provider error bodies.
