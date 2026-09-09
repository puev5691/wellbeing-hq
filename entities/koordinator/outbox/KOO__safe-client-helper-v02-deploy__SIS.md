# СИСАДМИНУ: разместить exact safe client helper v0.2 на Буржуинии

## Цель

Разместить на действующем Stage A OSS exact accepted `safe client helper v0.2` и выполнить только безопасный read-path для существующего `ent:KOO` operational credential.

## Exact artifact

source: `entities/koder/outbox/KOD__safe-client-helper-v02__KOO.py`
source_commit: `5844cd3e7ddd9a0fa275ed943ce021324aad6e2b`
source_blob: `fc28cbda873d9b5cf977c157823591607d8fb512`
required_sha256: `51eda2ef2a79a3a0886e0622bd935cdce9593203df1b0b8227a3a455bb86a32a`
verification_report: `entities/koder/outbox/KOD__safe-client-helper-v02-verification__KOO.md`
verification_report_commit: `16a75c7a69b71e949679915d761db1977fa92927`

## Выполнить

1. Получить exact artifact по immutable commit, не реконструировать и не редактировать.
2. Разместить на Буржуинии вне core/release, как operational client helper.
3. Проверить SHA-256. При несовпадении остановиться и вернуть `HASH_MISMATCH`.
4. Выполнить `python3 -m py_compile`.
5. Использовать уже существующий KOO credential-файл `/home/pev5691/.config/wb-oss/koo-pilot.json`; не выводить и не копировать token.
6. Через helper выполнить только:
   - `state --entity-id ent:KOO`
   - `inbox`
7. Не выполнять provisioning, bootstrap, credential reissue, server/core/schema mutation, writer grant, добавление Entity или production/public ingress.
8. Вернуть КООРДИНАТОРУ verification/result report: путь размещения, SHA-256, py_compile, фактический результат `state`, фактический результат `inbox`, без secrets.
9. Выполнить адресную доставку результата в `entities/koordinator/inbox/` по Exchange Gate.

## Стоп-условия

Остановиться без профильного исполнения при: hash mismatch; credential path отсутствует/не 0600/не принадлежит ожидаемому владельцу; OSS не ready; helper выдаёт fail-closed ошибку; требуется mutation за пределами read-path.

---
sender: KOO
recipient: SIS
status: addressed-task
project_time: omitted; trusted project-time source not used
