# Telegram Media Gateway Phase 0 v0.1

Назначение: credential-free non-production реализация точного WEB Phase 0 contract.

Граница:
- только Python 3 stdlib + SQLite;
- только FakeTelegramAdapter;
- никаких Telegram Bot API вызовов;
- никаких bot token/webhook secret/реальных chat id;
- никаких repository settings/publication side effects.

Реализовано:
- validation publication object;
- idempotency `publication_id + target_channel`;
- derivative payload;
- fake send/edit;
- delivery state `prepared -> dispatching -> delivered_unverified -> delivered_verified`;
- linked-discussion mapping;
- update_id dedupe;
- comments/reactions aggregation;
- member snapshots;
- SQLite persistence and restart recovery;
- correction revision without duplicate send;
- safe receipt export without audience identity;
- fail-safe negative paths.

Тест:
`python3 -m unittest -v test_gateway.py`

Ожидаемый результат текущего пакета:
`14 tests / PASS`.

Зависимости:
- Python 3 standard library;
- SQLite через stdlib `sqlite3`;
- third-party packages: none.

Phase 0 не доказывает реальную Telegram integration. Phase 1 требует отдельного разрешения и private sandbox bootstrap.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: bounded Telegram media-gateway Phase 0 implementation
project_time: omitted; trusted project-time source not used
