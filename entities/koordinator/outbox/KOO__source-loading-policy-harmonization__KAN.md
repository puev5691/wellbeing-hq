# KOO → KAN: harmonize source-loading-policy after OPERATOR decision

status: TASK
priority: governance
source_change_type: harmonization_after_explicit_operator_decision

## Basis

ОПЕРАТОР explicitly selected `Вариант 1` for the delivery-rule conflict.

Effective decision record:
`entities/koordinator/current/KOO__delivery-rule-operator-decision.md`

decision_commit:
`b8b74a7ad58111b58e02f6a82b693d152e09a39b`.

## Conflict to remove

Current approved sources are semantically inconsistent:

- `project-instructions-core-v2.1` and `file-work-canon-universal-v2.3` allow verified locator-based delivery;
- `source-loading-policy-v2` section 5 still reflects the older physical-upload-only terminal model.

The OPERATOR decision already resolves execution semantics now. This task is to harmonize the source text so future instances do not encounter the obsolete contradiction.

## Required result

Prepare one harmonized replacement candidate for `source-loading-policy-v2`.

Preferred version:
`source-loading-policy-v2_1-candidate.md`
unless KAN finds a versioning conflict requiring a different next version.

The candidate must:

1. preserve the rest of the current policy unless a change is required by the same conflict;
2. revise section 5 so that two valid delivery modes are explicit:
   - actual file transfer;
   - verified locator-based delivery;
3. state the locator-based conditions:
   - artifact exists;
   - concrete recipient;
   - addressed dispatch;
   - accessible locator;
   - immutable/version identity verifiable where required;
   - receipt;
   - failure-mode for missing locator/version mismatch;
4. keep publication, delivery, receipt and acceptance distinct;
5. state that physical OPERATOR file carriage is not required when valid locator-based delivery is available;
6. preserve the old v2 source as superseded provenance rather than rewriting history;
7. include a concise change note and explicit supersedes relationship;
8. avoid introducing unrelated policy changes.

## Approval boundary

KAN prepares harmonized candidate text and an exact delta explanation.

KAN does not self-approve the new Project Source unless an existing explicit authority says otherwise.

Return to KOO:
- candidate locator;
- immutable commit/blob;
- concise delta;
- any remaining conflict;
- recommendation for OPERATOR activation/replacement.

No Project Sources UI mutation is claimed by this task.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: привести source-loading-policy в соответствие с уже действующим решением ОПЕРАТОРА и новым каноном доставки
СТАТУС: assigned
