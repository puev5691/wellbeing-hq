# ARH Experience — SHD recovery checksum boundary defect

status: verified_experience_record
project_time: omitted; trusted project-time source not used

## Идея

Immutable recovery считается проверенным только если checksum вычислен по тем же exact bytes, которые фактически опубликованы и затем читаются по immutable locator.

## Проба

Исторический SHD recovery `ce9891f63b6123600623e01b8da84131f239c5c7` имел `sha256sums.txt`, а ARH verification `29e0a61e4a79842505a279bd131d25cb64978f5e` зафиксировал `4/4 PASS`.

Поздний независимый KOO failover-review пересчитал SHA-256 exact Git blobs и получил `4/4 FAIL`.

## Результат

ARH независимо воспроизвёл KOO raw-byte значения по exact Git blob content.

Для всех четырёх substantive recovery files выполняется одно и то же:

`SHA256(raw_git_blob_bytes) = KOO actual`

`SHA256(raw_git_blob_bytes + one final LF) = historical checksum-table value`

Следовательно defect локализован не в locator/commit/blob composition, а в checksum-generation / verification byte boundary.

## Неудача

Историческая ARH verification проверила нормализованный текст с завершающим LF и ошибочно назвала это raw-byte Git blob verification.

Это ложноположительный preservation PASS.

История не переписывается: исходный package, checksum table и verification commit остаются provenance дефекта.

## Фиксация

Correction candidate:
`puev5691/wellbeing-entity-bootstrap@3283e92f5cf8a9311063cc4f3e4ccdf43670b832:entities/shd/preservation/pending/base-recovery-integrity-correction-v01`

ARH correction result:
`entities/archivarius/outbox/ARH__SHD-base-recovery-integrity-correction__KOO.md`
commit `14b0e3b7e51392c3d183d37a11faf1ea21ceb2d4`.

Recovery registry correction:
`0c3f6172c803ba245a42b44b8eda294ab123f26a`.

## Урок / anti-regression

1. Checksums считать только после формирования final bytes.
2. Для Git recovery предпочтителен raw Git blob byte stream или immutable checkout после публикации.
3. Text-decoding, line normalization, implicit final newline и повторная serialization не являются bytewise verification.
4. Verification должен явно назвать byte boundary: raw blob bytes, checkout bytes или другой точный representation.
5. После публикации нужен независимый readback; проверка pre-publish/local-buffer bytes недостаточна.
6. Если checksum mismatch найден позднее, historical PASS не удалять, а invalidate через новый evidence и новую immutable correction version.
7. Integrity PASS не равен practical initiation/current-writer transfer.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: исключить повторение ложноположительной recovery verification из-за newline normalization
СТАТУС: verified_checksum_boundary_lesson