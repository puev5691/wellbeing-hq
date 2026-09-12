# Telegram Media Gateway Phase 1A

Status: candidate, non-production, credential-free, zero-live-network.

Purpose: prepare a real Telegram Bot API adapter/configuration boundary for later SIS/KAN-controlled sandbox integration without performing any Telegram request.

Boundary: no Telegram network calls; no bot token/webhook secret/real numeric IDs/MTProto; injected transport only; composite `(chat_id,message_id)` identity; strict auto-forward origin validation; evidence-based delivery verification; multi-target-safe SQLite; privacy fail-closed pending KAN; Phase 0 remains provenance and is not modified.

Exact test command: `python3 -m unittest -v test_gateway.py`

Dependencies: Python 3 standard library only, including `sqlite3`; no third-party packages.

Phase 1B external dependencies: verified channel numeric chat id, verified linked discussion state/id, publisher bot identity/rights, SIS secret injection for bot token/webhook secret, KAN privacy/retention decision, KOO authorization for one bounded sandbox send, SIS-controlled webhook/runtime endpoint.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: Phase 1A real-adapter/config preparation без live Telegram и credentials
