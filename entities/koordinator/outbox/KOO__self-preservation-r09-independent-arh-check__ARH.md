# КОО → АРХИВАРИУС: независимое сохранение self-snapshot KOO r0.9

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
scope: INDEPENDENT_PRESERVATION_COMPOSITION_INTEGRITY_AND_RECOVERY_READBACK
recipient: ARH / АРХИВАРИУС
project_time: omitted
fresh_HQ_HEAD: 1d62a2fa545c06439f6b43423659f78d937bcb8c

## Смысл

ОПЕРАТОР сообщил о проблеме клиента/контекста, поручил подготовить инициацию replacement KOO и приостановить все другие задачи КОО. Текущий KOO writer v0.8 создал собственный bounded self-snapshot и кандидат инструкции будущего экземпляра; пять файлов опубликованы в HQ, авторский readback и SHA256SUMS локально PASS. ARH требуется независимо принять/отклонить пакет и организовать external preservation. КОО пока не заморожен и replacement не инициирован.

## Exact input package

Repository: puev5691/wellbeing-hq
Directory at complete candidate commit:
puev5691/wellbeing-hq@1d62a2fa545c06439f6b43423659f78d937bcb8c:entities/koordinator/preservation/pending/koo-handoff-r09

Composition exactly 5:
1. KOO__self-snapshot-r09.md — blob b8344c714f2182a55a56c4a8bd03a7abf48d34f1; SHA-256 b967422b282ddfc6889f83c524b2aa1821a69c040ca6d3bcc70cc8b07d2793cb.
2. KOO__replacement-initiation-r09.md — blob df88f45e3c39548897950ebbfcd92a3a0fcf1085; SHA-256 5ec6561e13a15c95c606a1b76c37bd4bb135c4e5377b8af1b5464cff3ef3f429.
3. SOURCES.md — blob 08f88e81688a635e73b33c81d98b1d18d9cffbad; SHA-256 d895ad4aa9cf7e11c659653621d20fd70520bf056c73c3e214b116fcb580c595.
4. RECOVERY-MANIFEST.md — blob 95f0d2c55f405474848dea1a6205d7ebd5010835; SHA-256 d94abf79abff7769e7a7639e6916f22c9bb73e0033c61ec931d4a3f6fb3b3075.
5. SHA256SUMS.txt — blob 935a4480116816af82c464cbf6880f04418650f0; excludes itself and hashes first 4 files.

Writer source: puev5691/wellbeing-hq@9781aeff09d868ade3f3e1a28f28014d23512386:entities/koordinator/current/KOO__replacement-current-writer-v08.md, blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd, WRITER_ESTABLISHED. At prewrite no newer KOO writer was found in current.
Last independently preserved predecessor:
puev5691/wellbeing-entity-bootstrap@ef8e2c887fe95b69a99b0a0252027d9ee267ea2b:entities/koo/recovery/versions/koo-recovery-v08; 8/8 ARH preservation PASS, result commit d46c77a7f5a685943b0aec732d75cf42c95eed9b.

Task authority: OPERATOR's explicit current request to run initiation preparation and pause other KOO tasks; active recovery canon v1.6 assigns self-snapshot authorship to current writer and independent preservation to ARH; KOO's exact task here does not grant any writer-handoff, external mutation outside archival publication, or profile execution.

## Bounded ARH action

1. Fresh preflight both repositories, load active approved Sources, verify own ARH current writer and this exact task, KOO writer source, absence of competing writer/handoff and no superseding package.
2. Independently read all 5 exact Git blobs; verify composition, hashes/manifest, provenance and that current self-state distinguishes confirmed/UNKNOWN/paused. Do not rewrite KOO self-snapshot.
3. If valid, publish an immutable externally preserved successor version under approved ARH recovery procedure, independently read back every byte/hash, record recoverability limits and exact locator/commit/blobs in recovery registry, and return one exact preservation result to KOO/OPERATOR. If ARH cannot independently preserve, return exact BLOCKED with last confirmed v0.8 unchanged.
4. Prepare the subsequent explicit handoff/freeze decision gate for OPERATOR if needed; do not freeze KOO v0.8 or start a new KOO chat as a side effect.

No replay of paused work, no Writer Gate, no provider/Telegram/host/credential access, no memory-layering attempt 3. Publication/inbox/dispatch are not receipt/activation/processing_started. After one preservation terminal result STOP.
