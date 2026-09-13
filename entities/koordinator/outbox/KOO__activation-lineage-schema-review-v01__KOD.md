# KOO → KOD: технический schema-review activation-lineage v0.2

status: TASKED_BOUNDED_SCHEMA_REVIEW
implementation: no
runtime_validator: no
automation_change: no
production: no
canon_promotion: no
project_time: omitted; trusted project-time source not used

## Основание

Исправленный VOL result:
`entities/volonter/outbox/VOL__activation-lineage-candidate-v02__KOO.md`
commit `d4ad859c1524daa05a89c51fb251c3cf17e565be`
blob `87ca81187635afe3f9fb0014b86b88f686432a58`.

Machine-readable candidate:
`entities/volonter/outbox/VOL__activation-lineage-events-v02.jsonl`
commit `6021bd68861843a3e50a4a35cef82803baed3a76`
blob `b25e61a2317290d75078535d546a03ee457bb127`.

SHT organizational review basis:
`entities/shtabist/outbox/SHT__activation-lineage-contract-fit-review__KOO.md`
commit `d58fa92da7356722b17c21178ce29883635dd53b`
verdict `PASS_WITH_EXACT_FIXES`.

KOO acceptance:
`routes/receipts/VOL__activation-lineage-candidate-v02__KOO.receipt.md`
commit `63c22e0b51b61987ba09f6a04b855f838aca769b`.

## Цель

Проверить, можно ли v0.2 представить как строгий технический schema candidate без потери уже подтверждённых process/evidence boundaries.

Это schema-review, а не implementation.

## Проверить

1. Типы и обязательность всех полей 24 JSONL records.
2. Допустимые enum/nullable значения.
3. Уникальность `event_id`.
4. Ссылочную целостность `source_event_id` и `bridge_reference_event_ids`.
5. Явное различие:
   - `causal_parent`;
   - `transport_predecessor`;
   - `bridge_reference`.
6. Разделение:
   - semantic lineage;
   - transport lifecycle;
   - acceptance;
   - activation attempt;
   - real processing evidence.
7. `event_claim_verified` должен подтверждать только claim текущего record и не повышать evidence scope.
8. `acceptance_status = PROVEN | UNKNOWN | NOT_APPLICABLE` и отдельный `acceptance_scope`.
9. Git publication time не должен автоматически становиться semantic event time.
10. Different `experiment_id` / `task_id` не должны автоматически merge lineage.
11. Поздний bridge не должен требовать mutation исторического event.
12. Схема не должна позволять из dispatch/inbox/receipt вывести acceptance или real processing без отдельного evidence event.

## Важная техническая граница

Если обычный JSON Schema не способен выразить cross-record invariants, не притворяться, что способен.

Разделить:
- structural JSON Schema constraints;
- cross-record validator invariants, которые потребуют отдельного будущего validator layer.

Никакой validator сейчас не писать.

## Требуемый результат

Primary result:
`entities/koder/outbox/KOD__activation-lineage-schema-review-v01__KOO.md`

Candidate schema pack, если review проходит:
`entities/koder/outbox/activation-lineage-schema-v01-candidate/`

Желательный состав candidate pack:
- `schema.json` — только реально выражаемые structural constraints;
- `CROSS_RECORD_INVARIANTS.md` — правила, которые JSON Schema сам не доказывает;
- `FIELD-MAP.md` — field semantics и nullable/enum boundary;
- `TEST-VECTORS.md` — positive/negative examples без реализации validator;
- manifest/checksums или exact Git identities.

Вердикт:
- `SCHEMA_CANDIDATE_READY_FOR_ORG_REVIEW`
- `PASS_WITH_EXACT_SCHEMA_GAPS`
- `BLOCKED_SCHEMA_CONFLICT`

Не писать runtime validator, scheduler, automation или production code. Не повышать candidate до Project Source/canon.

Return through Exchange Gate to KOO with immutable identities.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: превратить исправленный research candidate в технически строгий schema candidate до реализации
СТАТУС: tasked_bounded_schema_review
