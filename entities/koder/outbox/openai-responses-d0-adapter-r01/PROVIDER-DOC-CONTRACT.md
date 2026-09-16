# OpenAI Responses API provider contract — r0.1

Статус: `NO_MATERIAL_PROVIDER_DOC_DRIFT`.

Проверены текущие официальные источники OpenAI:
- `https://developers.openai.com/api/reference/cli/resources/responses/methods/create`
- `https://developers.openai.com/api/docs/models/gpt-5.6-luna`
- `https://developers.openai.com/api/reference/cli`

Используемая граница:
- endpoint: `POST https://api.openai.com/v1/responses`;
- model: `gpt-5.6-luna`;
- credential reference: `OPENAI_API_KEY`, значение в пакет не входит;
- response object: `object=response`, `id`, `model`, `status`, `output` и `output_text`;
- text content block: `type=output_text`, поле `text`;
- usage: `input_tokens`, `output_tokens`, `total_tokens`;
- optional details: `input_tokens_details.cached_tokens`, `input_tokens_details.cache_write_tokens`, `output_tokens_details.reasoning_tokens`.

Task intentionally disables tools, search, files, computer use, code execution and fallback. Request blueprint additionally fixes `tools=[]`, `tool_choice=none`, `parallel_tool_calls=false`, `store=false`.

Project time omitted; trusted project-time source not used.