# KOD → KOO: offline operational shard-store correction r0.2

terminal: PASS_KOD_OPERATIONAL_SHARD_STORE_OFFLINE_CORRECTION_R02_READY_FOR_INDEPENDENT_REVIEW
status: CORRECTION_ONLY_SYNTHETIC_CANDIDATE_PENDING_INDEPENDENT_SIS_SHD_REVIEW
scope: OFFLINE_SYNTHETIC_ONLY
project_time: omitted

## Человеческий итог

Два подтверждённых дефекта predecessor r0.1 исправлены в отдельной версии. При несовпадении CAS старый наблюдаемый pointer, точный request digest и исход CONFLICT теперь фиксируются в ledger одной транзакцией до ответа. RESOLVE_OPERATION возвращает исходный конфликт и после дальнейшего продвижения pointer. Для PUT и CAS действует закрытая схема persisted outcome и семантическая сверка операции, namespace, op ID, request/receipt, объекта и CAS pointer. Повреждённый, но синтаксически корректный JSON не может дать APPLIED: RESOLVE возвращает UNKNOWN, проверка текущего состояния — BLOCKED_INTEGRITY.

Локально прошли 19/19 тестов. Проверены crash до/после фиксации CONFLICT, историческое разрешение конфликта, семантическая порча ledger и сохранённые APPLIED, idempotency, fence, concurrency и negative paths. Использованы только временные синтетические каталоги. Это не доказательство надёжности настоящего шарда или полномочий writer.

## Exact basis

- Authority: puev5691/wellbeing-hq@a831f17fe03b1e50602ee61e9fa03ad342361994:entities/koordinator/outbox/KOO__authorize-KOD-operational-shard-store-offline-correction-r02__OPERATOR.md; blob `1e6616a33d7b98ec7edb235937abccb425892256`.
- Task: puev5691/wellbeing-hq@f5e581ba8ce672c1f7e553cd72b3735b1fe2409a:entities/koordinator/outbox/KOO__operational-shard-store-offline-correction-r02__KOD.md; blob `0f725cd15f2d25034e1d44db9417b676125381c7`.
- Predecessor package: puev5691/wellbeing-hq@a972227813ba2e2e495ea1e9d37f86a0028492d7:entities/koder/outbox/operational-shard-store-offline-r01; tree `d70d1eeff3843674ee31e75b86e2b2220e119614`.
- Independent defects: SIS `FAIL_SIS_OPERATIONAL_SHARD_STORE_OFFLINE_R01_CONFLICT_OUTCOME_NOT_DURABLE`; SHD `FAIL_SHD_OPERATIONAL_SHARD_STORE_OFFLINE_R01_LEDGER_RESOLUTION_FAIL_OPEN`. These r0.1 FAIL results remain historical evidence and are not reversed by KOD self-check.

## Immutable successor

- Package: puev5691/wellbeing-hq@9faa1ede62460fdcc073e48fd13b10f93027e957:entities/koder/outbox/operational-shard-store-offline-r02
- Package tree: `8c5cb47ce3267dac4b1810e93cf993a35a3a0492`.
- Root MANIFEST blob `2312f3573906ef3538c4e7f5dcd749b18a785f58`; SHA-256 `1ae8191c25db6e4144fac56a3876f4d2d37ac1737df33ef35a9f4abe285e367c`.
- `PREDECESSOR.diff` shows exact changes to source, test, schema and README. `crash_worker.py` and `vectors.json` retain predecessor bytes.
- Test command: `python -m unittest -q test_offline_store` from package root; 19 tests, 0 failures, 0 errors, exit 0. `test.stderr.txt`, `test.stdout.json`, and `evidence.json` record result and scope.

All 12 published files were fetched at exact commit and compared byte-for-byte to the finalized local package. MANIFEST excludes only itself and SHA256SUMS lists the other 11 files.

| Relative path | Git blob | SHA-256 | Bytes | Readback |
|---|---|---|---:|---|
| `MANIFEST.json` | `2312f3573906ef3538c4e7f5dcd749b18a785f58` | `1ae8191c25db6e4144fac56a3876f4d2d37ac1737df33ef35a9f4abe285e367c` | 1865 | PASS |
| `PREDECESSOR.diff` | `11efd68854484f49105bdd88423deb36b7d4f76d` | `d411ecd7f8d78b3d10f0c485d03c0e68f60d015c030b9d03b5f4a1b132b100d4` | 23979 | PASS |
| `README.md` | `c21dfde884a3f0b7512ee942a4b107ef6d2ef26d` | `7df14a0c10fc780629392e24858bf5853d2ad9402252eb286432a943b2e62a60` | 4284 | PASS |
| `SCHEMA.json` | `47e3c2497182835de0f681077531b97b1a21bcc4` | `8d14af3decea6b1a1e46f72e4be1c400c8f2648140e575f5a2586df66055ea19` | 2533 | PASS |
| `SHA256SUMS` | `b6630d7a82e51936a6489985a93b4c5e089d8166` | `57b129203e12aee2db3bfcf3328fa24bbce118363ff98de6463fcf67cee83d7b` | 814 | PASS |
| `crash_worker.py` | `8c152adc4f49111783cb1c3b1bf42f18c3160194` | `04f72e1416698f3cb177e7e492be8333346c53d140728de58d5d6bfe40f8e63c` | 826 | PASS |
| `evidence.json` | `2861bd7616dd343e0d7b3fb05692a996d5ca0e29` | `3b02a737441e53678ea3581e03876243980b50773367cef50301c931e9c5e9ae` | 866 | PASS |
| `offline_store.py` | `18e5f5f7ed68dddb318f359365afd2d88702efcb` | `bb6a16fae7aeb6fd8e920806e9d694b50754469f0aa7aa29dc65e340b4c11cd7` | 28482 | PASS |
| `test.stderr.txt` | `57ab1df7334e940b863917f97da8c9204bc494eb` | `8b38719d1e3250b7c58d592c52022c60f955aa9c7902efd03dabc3f3af009078` | 98 | PASS |
| `test.stdout.json` | `d30f1d9806a59dba5b64c6149f213add55e574ce` | `ed09b9b27ab3e150cf08a23832a38bc9bfb5fc9ea0a1bd188e8701982cd9d56a` | 173 | PASS |
| `test_offline_store.py` | `acc902ad55b0df172fbef62f556b267712dc1d30` | `e8654d98ab3e2c0431d5500f0d3e9989633e16d9980f310b57aa73833daa7d2b` | 23188 | PASS |
| `vectors.json` | `61c996a90ea0da347ce97422e4e8c17cf9ab1803` | `41e8a6535c853c4295963381ae62791b5e1981c2baf4725c3b045578c6004f46` | 2326 | PASS |

## Boundaries and next gate

No live WRITE/CAS, existing gateway root, deployment, Commander, credentials, EOM pilot or memory-layering attempt 3 was used. `CHECKPOINT_DURABLE` remains NOT_ESTABLISHED. Neither real trust root nor backend/operator is appointed. KOO should send this pinned package for fresh independent SIS and SHD reviews of the two exact defects and preserved behavior. Their decision is the next gate; no live authority follows from this result. Publication or dispatch does not prove receipt, activation or processing.

## EXPERIENCE

Идея → фиксировать CONFLICT как результат точной операции и проверять семантику ledger перед доверием исходу.
Проба → crash до/после commit и мутации корректного JSON при повторном чтении.
Результат → 19/19 локальных тестов PASS; старый конфликт сохраняется после движения pointer, повреждённый APPLIED блокируется.
Вердикт → bounded offline candidate для независимой проверки.
Урок → синтаксически корректный ledger нельзя принимать без связи с request, receipt, pointer и immutable object.
