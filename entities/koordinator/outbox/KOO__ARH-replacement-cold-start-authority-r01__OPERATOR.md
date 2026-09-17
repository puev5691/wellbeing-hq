# КОО → ОПЕРАТОР: authority for ARH replacement cold-start r0.1

status: `AUTHORIZED_FOR_COLD_START_ONLY`
entity: `ARH / АРХИВАРИУС`
replacement_initiation: `authorized`
old_writer_new_profile_mutations: `frozen`
writer_transfer: `not_yet_authorized`
canonical_recovery_change: `no`
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР после подтверждённой деградации текущего ARH-чата распорядился продолжить процедурой replacement initiation.

Независимая проверка свежего self-preservation candidate завершена:
`entities/koordinator/outbox/KOO__ARH-replacement-cold-start-verification-r02__ARH.md`
commit `d89e101a4c7fef7d689bb48ddc6569ef656d64ba`
verdict `PASS_ARH_REPLACEMENT_COLD_START_PREPARED`.

Verified fresher overlay:
`puev5691/wellbeing-entity-bootstrap@5172d37f9a3560cd177b4fa39e2ead24bc5b458d:entities/arh/preservation/pending/pre-replacement-self-preservation-r02`

overlay tree:
`acf8c2b583ef7d06319a68be21351adec5148544`

Canonical predecessor remains:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`.

## Authority boundary

С этого решения старый ARH считается frozen для новых authoritative профильных изменений. Его опубликованные immutable артефакты остаются evidence/provenance.

Разрешено новому экземпляру ARH:
1. выполнить cold-start по canonical v03 + verified r0.2 overlay;
2. сделать fresh HQ reconciliation после snapshot boundary `c83bf0e5cb5a38b4ce2d460d3d8d57ab4ff6b727`;
3. проверить freeze старого writer и competing-writer evidence;
4. вернуть initiation status.

Не разрешено этим решением:
- автоматически становиться current-writer;
- исполнять pending RED checkpoint или sanitation tails;
- повышать r0.2 до canonical recovery;
- менять canonical predecessor;
- выполнять иные профильные задачи до успешной initiation.

Writer transfer допустим только после `initiation_verified`, fresh competing-writer check и отдельной immutable writer-publication/readback.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать явное операторское основание для cold-start replacement ARH без преждевременной передачи writer authority
СТАТУС: `AUTHORIZED_FOR_COLD_START_ONLY`
