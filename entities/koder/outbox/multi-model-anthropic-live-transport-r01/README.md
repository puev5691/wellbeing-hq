# Anthropic live transport r0.1

Назначение: последний технический слой перед отдельным account/key/billing/live-D0 gate для прямого маршрута `local gateway → POST https://api.anthropic.com/v1/messages → claude-sonnet-5`.

Текущий пакет **не выполняет live API call** и не содержит credentials. Он наследует без изменения принятые `policy.py` и `anthropic_adapter.py` из adapter r0.1 и добавляет live-capable HTTP transport/launcher с default-deny запуском.

Ключевая граница: accepted D0 config по-прежнему содержит `network_allowed=false`. Это не ошибка и не обход policy. Accepted adapter сначала строит неизменный mock-only request blueprint. Отдельный transport gate может превратить только этот exact validated blueprint в один Anthropic HTTP request после отдельного `--live` и exact live-switch. Никакие tools/search/files/caching/MCP/Managed Agents/code execution/fallback при этом не становятся разрешёнными.

Обычный запуск `launcher.py` без `--live` только валидирует D0 config/blueprint и возвращает `LIVE_DISABLED_DEFAULT_DENY`; API key не читается, сеть не используется.

Live path требует одновременно:
- exact D0 blueprint;
- CLI `--live`;
- `ANTHROPIC_LIVE_D0=EXPLICIT_D0_LIVE`;
- runtime injection `ANTHROPIC_API_KEY`;
- real `UrllibExecutor` and `EnvironmentSecretReader`;
- exact route `https://api.anthropic.com/v1/messages`.

Tests use only injected non-network dependencies and globally patch `urllib.request.urlopen` to fail if invoked.

Pricing remains estimate-only: `$2/MTok` input, `$10/MTok` output for the accepted Sonnet 5 basis. It is not billing evidence.

Project time: omitted; trusted project-time source not used.
