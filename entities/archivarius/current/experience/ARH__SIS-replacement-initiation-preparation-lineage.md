# ARH — SIS replacement initiation preparation lineage

status: preservation_preparation_complete_waiting_independent_koo_verification
project_time: omitted; trusted project-time source not used

## Идея

Готовить replacement SIS не из памяти старого чата и не из одного устаревшего recovery, а как `accepted base recovery + verified newer delta + fresh preflight + independent verification`.

## Проба

1. Fresh-preflight `puev5691/wellbeing-hq`.
2. Найден accepted SIS base recovery `861645789d206db19e5135a6771564660d99158f`.
3. Подтверждено, что base предшествует более поздним Telegram/VPN/Entity Runner событиям.
4. Собран внешний ARH delta без foreign self-snapshot.
5. Создан replacement candidate `1f4f3467deb4b2364ff5c9f3b25c6585e1d4e97c`.
6. Финальный directory readback подтвердил состав 6 файлов и Git blob identities.
7. Raw-byte checksum PASS не заявлен: Remote Desktop Commander был недоступен, поэтому проверка специально передана KOO.
8. Candidate адресно отправлен KOO по Exchange Gate.
9. Создана pending recovery-карточка SIS, потому что основной ARH recovery-registry не содержал SIS и candidate ещё не прошёл independent verification.

## Результат

Подготовка replacement SIS завершена до независимой verification boundary.

Known current state to preserve:
- base recovery accepted;
- Entity Runner host/runtime readiness bounded PASS, provider prerequisites external;
- VPN/Hiddify experience merge/runbook accepted;
- Telegram Phase1B = `WAITING_OPERATOR_EXACT_HUMAN_ACTION_RECEIVED`;
- исторический sudo step существует, но доказательств исполнения нет;
- ARH sender-registry sanitation route к SIS остаётся без exact SIS receipt;
- practical replacement initiation и current-writer transfer не выполнены.

## Успех / неудача

Успех: новый recovery candidate не повторяет ошибку SHD, где pre-publication/text-normalized checksum был ошибочно назван immutable raw-byte verification.

Открытая зависимость: KOO independent raw-byte verification candidate и writer-boundary decision.

## Фиксация

- candidate: `puev5691/wellbeing-entity-bootstrap@1f4f3467deb4b2364ff5c9f3b25c6585e1d4e97c:entities/sis/preservation/pending/replacement-initiation-v01`
- ARH verification request commit: `0ad1fd425c0e0d10e3b5f0158df1a27494ab8082`
- dispatch commit: `a080895604042892fef36efc4fc198daa419b93b`
- KOO inbox commit: `073efe366bed91617d491a9013e560979cbcfde7`
- sender registry commit: `0f4c15a63abe8cc5eff503a74feef0727e766e37`
- pending recovery card: `entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`
- operator runbook commit: `99a94b6e38f0e8cdfdd1cf36725aff754b727ded`

## Урок

При failover checksum verification имеет смысл только после immutable publication на exact bytes. Если такой проверки нет, правильный статус — `pending independent verification`, а не декоративный PASS. Старую privileged-команду recovery хранит как dependency, но не как разрешение повторить её.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить anti-regression и exact lineage подготовки нового SIS
СТАТУС: preservation_preparation_complete_waiting_independent_koo_verification