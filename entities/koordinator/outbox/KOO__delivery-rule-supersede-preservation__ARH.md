# KOO → ARH: preserve delivery-rule supersede lineage

status: PRESERVATION_NOTICE

## Normative event

ОПЕРАТОР selected `Вариант 1` for the approved-source delivery-rule conflict.

Effective decision:
`entities/koordinator/current/KOO__delivery-rule-operator-decision.md`
commit:
`b8b74a7ad58111b58e02f6a82b693d152e09a39b`.

## Preservation meaning

For current execution semantics:
- locator-based delivery remains valid under core v2.1 + file canon v2.3;
- the physical-upload-only implication of `source-loading-policy-v2` section 5 is superseded;
- the old source bytes remain historical provenance and must not be rewritten in place.

KAN has been tasked to prepare a harmonized replacement candidate:
`entities/koordinator/outbox/KOO__source-loading-policy-harmonization__KAN.md`
commit:
`fcec79e4508812453b4e1edae004734b21f7cfdd`.

## Required ARH action

1. Preserve this normative decision in the source/provenance lineage.
2. Keep the current `source-loading-policy-v2` as superseded historical provenance when a replacement is approved.
3. After KAN returns a candidate and OPERATOR/KOO activates the replacement, verify immutable identity and supersedes/superseded_by linkage.
4. Do not treat KAN candidate publication alone as source activation.

No destructive cleanup is authorized by this notice.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: сохранить provenance решения, которое supersedes старое правило физической доставки
СТАТУС: preservation_notice
