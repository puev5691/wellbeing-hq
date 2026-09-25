# КОДЕР → КОО: матрица изолированного admission r0.2

Status: 25/25 executed synthetic cases PASS.

Каждая строка ниже исполнена локально; evidence — одноимённый ключ в `KOD__detector-worker-admission-r02-evidence__KOO.json`. `PASS` означает соответствие ожидаемому локальному исходу, а не запуск реальной Сущности.

| Случай | Ожидалось | Фактически | Статус |
|---|---|---|---|
| `01_exact_event` | exit 0, `result_dispatched`, `None` | exit 0, `result_dispatched`, `None`; synthetic_result=true | EXECUTED PASS |
| `02_blob_mismatch` | exit 21, `activation_failed`, `artifact_blob_mismatch` | exit 21, `activation_failed`, `artifact_blob_mismatch`; synthetic_result=false | EXECUTED PASS |
| `02_commit_mismatch` | exit 21, `activation_failed`, `artifact_commit_not_found` | exit 21, `activation_failed`, `artifact_commit_not_found`; synthetic_result=false | EXECUTED PASS |
| `03_wrong_dispatch` | exit 21, `activation_failed`, `dispatch_commit_not_found` | exit 21, `activation_failed`, `dispatch_commit_not_found`; synthetic_result=false | EXECUTED PASS |
| `03_wrong_recipient` | exit 21, `activation_failed`, `dispatch_recipient_mismatch` | exit 21, `activation_failed`, `dispatch_recipient_mismatch`; synthetic_result=false | EXECUTED PASS |
| `04_initial` | exit 0, `result_dispatched`, `None` | exit 0, `result_dispatched`, `None`; synthetic_result=true | EXECUTED PASS |
| `04_interrupted_reservation_unknown` | exit 27, `activation_failed`, `event_state_unknown_requires_reconcile` | exit 27, `activation_failed`, `event_state_unknown_requires_reconcile`; synthetic_result=false | EXECUTED PASS |
| `04_same_id_digest` | exit 23, `activation_failed`, `duplicate_event_same_digest` | exit 23, `activation_failed`, `duplicate_event_same_digest`; synthetic_result=false | EXECUTED PASS |
| `05_same_id_changed_valid_digest` | exit 24, `activation_failed`, `event_id_digest_conflict` | exit 24, `activation_failed`, `event_id_digest_conflict`; synthetic_result=false | EXECUTED PASS |
| `06_missing_authority` | exit 25, `activation_failed`, `authority_not_trusted` | exit 25, `activation_failed`, `authority_not_trusted`; synthetic_result=false | EXECUTED PASS |
| `06_wrong_authority` | exit 25, `activation_failed`, `authority_not_trusted` | exit 25, `activation_failed`, `authority_not_trusted`; synthetic_result=false | EXECUTED PASS |
| `07_missing_recovery` | exit 22, `activation_failed`, `recovery_missing_fields:recovery_identity` | exit 22, `activation_failed`, `recovery_missing_fields:recovery_identity`; synthetic_result=false | EXECUTED PASS |
| `07_missing_sources` | exit 25, `activation_failed`, `approved_source_set_missing_or_untrusted` | exit 25, `activation_failed`, `approved_source_set_missing_or_untrusted`; synthetic_result=false | EXECUTED PASS |
| `07_missing_writer` | exit 25, `activation_failed`, `writer_not_trusted` | exit 25, `activation_failed`, `writer_not_trusted`; synthetic_result=false | EXECUTED PASS |
| `07_wrong_source` | exit 25, `activation_failed`, `approved_source_set_missing_or_untrusted` | exit 25, `activation_failed`, `approved_source_set_missing_or_untrusted`; synthetic_result=false | EXECUTED PASS |
| `08_unavailable_provider` | exit 21, `activation_failed`, `provider_unavailable_or_unreadable` | exit 21, `activation_failed`, `provider_unavailable_or_unreadable`; synthetic_result=false | EXECUTED PASS |
| `09_handler_failure` | exit 30, `processing_failed`, `None` | exit 30, `processing_failed`, `None`; synthetic_result=false | EXECUTED PASS |
| `10_local_marker_no_entity` | exit 0, `result_dispatched`, `None` | exit 0, `result_dispatched`, `None`; synthetic_result=true | EXECUTED PASS |
| `event_commit_mismatch` | exit 25, `activation_failed`, `event_commit_missing` | exit 25, `activation_failed`, `event_commit_missing`; synthetic_result=false | EXECUTED PASS |
| `event_digest_tamper` | exit 25, `activation_failed`, `event_digest_mismatch` | exit 25, `activation_failed`, `event_digest_mismatch`; synthetic_result=false | EXECUTED PASS |
| `event_inbox_binding_mismatch` | exit 25, `activation_failed`, `event_inbox_binding_mismatch:artifact_path` | exit 25, `activation_failed`, `event_inbox_binding_mismatch:artifact_path`; synthetic_result=false | EXECUTED PASS |
| `event_inbox_blob_mismatch` | exit 25, `activation_failed`, `event_inbox_blob_mismatch` | exit 25, `activation_failed`, `event_inbox_blob_mismatch`; synthetic_result=false | EXECUTED PASS |
| `missing_trusted_profile` | exit 25, `activation_failed`, `trusted_profile_missing_or_invalid` | exit 25, `activation_failed`, `trusted_profile_missing_or_invalid`; synthetic_result=false | EXECUTED PASS |
| `superseded_authority` | exit 25, `activation_failed`, `authority_not_current_or_valid` | exit 25, `activation_failed`, `authority_not_current_or_valid`; synthetic_result=false | EXECUTED PASS |
| `superseded_writer` | exit 25, `activation_failed`, `writer_not_current_or_valid` | exit 25, `activation_failed`, `writer_not_current_or_valid`; synthetic_result=false | EXECUTED PASS |

## Что именно установлено

- Event envelope связывает ID/digest с source commit, inbox path/blob, recipient и immutable artifact/dispatch. Worker перечитывает inbox по exact commit и сверяет поля с locator. Допуск authority, recovery, writer и шести обязательных synthetic approved-source refs выполняется до handler; approval поступает из отдельного supervisor trust profile, а не выводится из наличия файла в Git.
- Persistent key в изолированном state dir = SHA-256(task_id + `|` + event_id); при одинаковом digest после terminal отказ без повторного handler, при другом digest отдельный конфликт. Созданная, но не завершённая reservation означает UNKNOWN и требует ручной сверки. Atomic file replacement применяется в локальной FS, однако durability при аварии узла и rollback не установлены.
- `processing_failed` возвращает supervisor exit 30. В успешном synthetic случае локальная отметка — `worker_handler_invoked_synthetic`; `real_entity_processing_started=false` во всех строках.

## Границы

- Эти 25 cases покрывают исходные десять классов и дополнительные отрицательные варианты. Реальный detector workflow не подключался к worker; подлинность происхождения envelope от GitHub Actions и сохранность supervisor trust вне test harness не проверялись. Реальная актуальность полномочий и approved Project Sources требует независимого admission, а не создания тестовых refs. Реального Entity instance, receipt, project acceptance и durable checkpoint нет.
- Базовый worker v0.2 Git blob `c680878806fd2fb6d20df8b6e8938d3f3ead5053` не изменялся. Successor — отдельный candidate. Предыдущие дефекты Exchange Gate не исправлялись.

No provider calls, real Entity spawn, host/shard access or memory-layering attempt 3.
