# SIS: corrected-broker runtime readmission r0.1

terminal: PASS_SIS_MEMORY_LAYERING_E2E_R01_CORRECTED_BROKER_RUNTIME_READMISSION
project_time: omitted

## Человеческий итог

Исправленный broker установлен на p552203.kvmvps и стал частью новой admitted runtime identity.

Фактический successor broker имеет SHA-256:
1b263ca6525be9a0e0847380b8824ca0476db8d93863269f66a7985aff0b1973

Harmless readiness на установленном runtime подтвердила:
- обязательные 7 restoration reads проходят;
- после 7 чтений semantic accounting = 3531 bytes;
- 32-е чтение проходит;
- 33-е отклоняется как DENY_READ_LIMIT;
- unknown locator отклоняется;
- full-corpus отклоняется;
- oracle/checker-private отклоняется;
- socket создаётся с mode 0600 и после завершения отсутствует.

Isolation сохранилась:
- OLD-01 и NEW-01 получают разные user/mount/pid/network namespaces;
- package root worker не видит;
- oracle worker не видит, supervisor читает oracle;
- host/project home/repository worker не видит;
- arbitrary outbound network denied;
- environment после env -i: LC_CTYPE=C.UTF-8;
- capability sets = 0;
- NoNewPrivs=1;
- deadline <=5 s подтверждён harmless sleep probe;
- standing worker/broker после проверки отсутствуют;
- runtime roots пусты;
- worker task logic не запускалась.

## Новая runtime identity

Fresh corrected runtime policy host SHA-256:
bfc19a4faa2e0841098c061890aba4c1ddc4e748a08ebd362bee348e89b5e868

Published policy:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-corrected-runtime-policy.json
commit: fe2733df2fff713b8a44fbde7e5a3a9d1bfa7a9a
blob: 2b5008c453214d186b52e7de895dc97ee140da8e

Fresh corrected runtime admission host SHA-256:
181c79ff334551ccbe26530c6e162c1d83cad02fc21c33c415d459ad9e9ef1fb

Published admission:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-corrected-runtime-admission.json
commit: 2ff79de579d4ca07c3171138abc66a5baa1826b4
blob: 97fc6c4ca4b6b719732c71e607b4adcc81305b9c

## Authority boundary

Historical claim remains:
main_attempts_started=1
main_authority_consumed=true
automatic_retries=0

Historical terminal:
BLOCKED_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ADMITTED_BROKER_REQUEST_BUDGET_MISMATCH

OLD-01 task execution=0
NEW-01 task execution=0

Old MAIN authorities remain consumed historical authority and were not replayed or reset.

new_MAIN_authority=NOT_GRANTED
MAIN_NOT_STARTED_AFTER_READMISSION

Runtime is technically ready for a separate future decision about MAIN, but no such decision is created by this readmission.

## EXPERIENCE

Идея → заменить только дефектный lifecycle broker, не ослабляя остальные isolation и retrieval bounds.

Проба → установить exact independently verified successor на admitted p552203, затем заново проверить реальный socket, 7/32/33, deny-cases, namespace/filesystem/environment/capability isolation и deadline без запуска task logic.

Результат → successor работает в пределах 32 reads, 33-й блокируется, isolation сохранилась, новая runtime identity сформирована и опубликована, прежняя MAIN authority подтверждена как consumed.

Вердикт → PASS corrected-broker runtime readmission. Runtime технически исправлен и заново admitted, но MAIN не разрешён.

Урок → изменение даже одного компонента admitted runtime требует новой identity и полной bounded readmission; техническая готовность runtime и право выполнить one-shot MAIN являются разными gate.

---
КТО: SIS / СИСАДМИН r0.6
СТАТУС: PASS_SIS_MEMORY_LAYERING_E2E_R01_CORRECTED_BROKER_RUNTIME_READMISSION
