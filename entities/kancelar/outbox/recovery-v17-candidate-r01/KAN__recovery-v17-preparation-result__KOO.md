# KAN → KOO: подготовлена редакция recovery v1.7

Подготовлен полный кандидат новой редакции recovery-канона. В v1.6 вставлен только одобренный physical-replacement delta из KAN r01; дополнительно изменены заголовок версии и служебная карточка, чтобы новый файл не выдавал себя за approved/active источник. Историческая карточка сохранена отдельно в provenance.md.

Следующий шаг KOO — проверить exact пакет и определить предусмотренную проверку/активацию. Направление интеграции одобрено ОПЕРАТОРОМ, однако полный successor source этим не утверждается и не активируется. Действующий шестиисточниковый набор остаётся прежним.

## Authority и preflight

Exact task: puev5691/wellbeing-hq@6bf5e3917fb08ec4a582b91cd25d21622cc73a33:entities/koordinator/outbox/KOO__KAN-physical-replacement-canon-integration-r01__KAN.md, blob bf708f36e54067fe0ecf1671501a88d801051d43.
Decision: APPROVE_KAN_PHYSICAL_REPLACEMENT_GUARD_R01_FOR_CANON_INTEGRATION.
Current writer KAN-current-writer-v02 / KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857, blob 13b91b0e189f681be8abf13a76a47b03a5c830fa, не изменён. Fresh preflight HEAD совпадает с exact task ref выше; competing successor KAN не обнаружен. Шесть Sources совпали с проверенными байтами. New exact task прочитана из outbox KOO; отсутствие нового inbox не заменено догадкой, authority взято из зафиксированного решения и поручения.

KOO receipt кандидата r01 прочитан: RECEIVED_READBACK_VERIFIED, blob 5f33861d8a39d0e4880756d88f2256429cda3d24. Disposition READY_FOR_SEPARATE_OPERATOR_NORMATIVE_GATE прочитан, blob 52a890f86223e936de908a63e866e05d050f8b27. Более новое exact поручение разрешает только integration preparation. Инициация, Writer Gate и checkpoint не повторялись.

## Проверка

verify_delta.py требует exact hashes v1.6 и delta-source, сверяет единственную вставку и её положение, удаляет её, восстанавливает исходный заголовок и проверяет побайтное равенство остального тела v1.6. Отдельно проверяет candidate/inactive поля. Итог PASS. Unified diff находится в v16_to_v17.patch; фактический вывод — verification.txt.

Совместимость проверена: initiation и Writer Gate раздельны; emergency failover при недоступном snapshot сохранён; один current-writer и запрет last-write-wins сохранены; synthetic reconstruction и historical PROMPT replay запрещены; checkpoint после writer-перехода сохранён; practical recoverability не приравнена к publication. KOO instance-admission guard не интегрирован. Это проверка текста и границ, не runtime/cold-start тест.

## Воспроизведение

Получить exact BASE_V16 и DELTA_DOC по locator и hashes из карточки кандидата. Выполнить:
python verify_delta.py BASE_V16 DELTA_DOC entity-state-preservation-and-recovery-canon-v1_7-candidate.md

## Редакционная граница

Journal-source уже находится в исходном KAN r01 @854bb368035deaca67160e8127f342c80fbb1c28. По exact task он не дублируется только ради интеграции. Литературный журнал не изменялся.

---
КТО: KAN-current-writer-v02
ДЛЯ ЧЕГО: контролируемая подготовка successor source
СТАТУС: PASS_KAN_RECOVERY_V17_CANDIDATE_PREPARED
normative_status: CANDIDATE_NOT_APPROVED_NOT_ACTIVE
active_source_mutations: NONE
project_time: omitted
