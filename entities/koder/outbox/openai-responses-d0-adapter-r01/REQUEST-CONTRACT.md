# Request contract

Provider: `openai`.
API family: `Responses API`.
Endpoint: `POST https://api.openai.com/v1/responses`.
Model: `gpt-5.6-luna`.
Data class: `D0_SYNTHETIC` only.

Credential handling: runtime reference `OPENAI_API_KEY`; source/tests/fixtures/provenance store no API-key value.

Request body boundary:
- exact synthetic text input only;
- bounded `max_output_tokens`;
- `store=false`;
- `tools=[]`;
- `tool_choice=none`;
- `parallel_tool_calls=false`.

Policy rejects non-D0 input, project/private locators or content, tool/search/file/computer/code use, fallback, alternate provider, network permission, project mutation and production permission before transport invocation.
