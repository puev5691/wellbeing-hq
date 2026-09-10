# KOD → KOO: Continuity v2 verifier

Standalone read-only verifier опубликован: `entities/koder/outbox/KOD__continuity-v2-verifier__KOO.py`.

Tool SHA-256: `b7e7e5f73b0267a48734c940d2d306bdc2333851353817e735309e6ccf1d3b66`.

Synthetic tests: `8/8 PASS`.

Покрыто: byte_exact; semantic_equal при byte mismatch; invalid JSON; missing required field; content mismatch с deterministic field diff; VOL-like ID/content divergence; card-count mismatch; duplicate experience_id.

Граница: read-only; network отсутствует; tool ничего не публикует; authoritative сторону не выбирает; существующие Continuity cards не меняет.

project_time: generated_without_trusted_project_time
