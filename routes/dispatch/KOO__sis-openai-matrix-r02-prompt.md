# KOO dispatch — SIS OpenAI cost matrix prompt

exchange_gate: v1
sender: koordinator
recipient: sisadmin
artifact: entities/koordinator/outbox/SIS__openai-cost-matrix-r02__PROMPT.md
version_commit: 27ca1bee805d7f9ee0ad648b6de65f8eef2ddc6c
version_blob: c288a1eedd42a8532cc221af10dc70a1aa550350
purpose: продолжить текущий конвейер OpenAI cost matrix после clean runtime staging PASS
required_action: выполнить PROMPT как текущую Resume-First задачу в границах exact task a011be06d1bbb23b53dc74cd0ee3fb1c53291d34
expected_result: terminal result адресно KOO и KOD
failure_mode: locator/version mismatch, unavailable artifact или невозможность активации адресного Entity-chat фиксируются как blocker; publication не считать delivery
