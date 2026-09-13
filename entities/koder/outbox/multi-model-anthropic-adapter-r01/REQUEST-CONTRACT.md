# Request contract

## Future route

- Method: `POST`
- URL: `https://api.anthropic.com/v1/messages`
- Model: `claude-sonnet-5`
- `anthropic-version`: `2023-06-01`
- content type: `application/json`
- credential reference: environment secret injection `ANTHROPIC_API_KEY`

The adapter never places a secret value in the plan. A future separately authorized network launcher must resolve the credential at the final transport boundary.

## Current body

Only:
- `model`;
- `max_tokens` (1..1024);
- `messages`, with one `user` text block containing only D0 synthetic content.

Not permitted:
- tools;
- web/search;
- Files API;
- prompt caching;
- MCP connector;
- Managed Agents;
- code execution;
- alternate provider/model;
- fallback;
- project/private locators or payload;
- production mutation.

## Current transport

`mock_only`; `network_execution_enabled=false`.

No live transport implementation exists in this package.
