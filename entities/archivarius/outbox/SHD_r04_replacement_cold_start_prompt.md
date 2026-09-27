АДРЕСАТ: ШАРДОВИК / SHD

Resume-First.

ОПЕРАТОР разрешил replacement после graceful preservation r0.4.

Exact recovery:
puev5691/wellbeing-entity-bootstrap@6a5b09807bb8a6b4525620a1cbd7d6a4561f0817:
entities/shd/recovery/versions/shd-recovery-r04

Exact freeze authority:
puev5691/wellbeing-hq@80fba20328fb9e01072aa9c1f247b0e8f652127f:
entities/archivarius/outbox/ARH__SHD-current-writer-handoff-freeze-r04__OPERATOR-SHD.md
blob d15afe3082970a8435454f353a693b8ba2470e1d

Выполни только Initiation Gate:

1. fresh preflight wellbeing-hq;
2. загрузи active approved Project Sources;
3. проверь recovery r0.4: composition, blobs, SHA256SUMS и ARH preservation;
4. проверь predecessor writer и freeze authority;
5. проверь отсутствие competing SHD writer/supersession;
6. восстанови только подтверждённое состояние;
7. не исполняй pending File Service, Telegram или TERA задачи.

Верни:
initiation_verified_waiting_writer_gate
или точный BLOCKED_* / FAIL_*.

Если PASS — опубликуй immutable initiation result и сделай readback.

STOP перед Writer Gate.

ДЕЙСТВИЕ ОПЕРАТОРА: открыть новый physical чат SHD и передать этот блок целиком.
