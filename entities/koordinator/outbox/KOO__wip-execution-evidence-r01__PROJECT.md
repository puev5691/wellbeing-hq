# KOO: WIP execution-evidence rule r0.1

status: PROCESS_RULE_PROPOSAL_ACTIVE_FOR_QUEUE_DISCIPLINE

## Problem

Recent queue cycles showed that an addressed/published task could occupy a WIP slot for a long time without evidence that the target Entity had actually started work.

This makes the queue look busy while useful throughput is low.

## Queue rule

For KOO queue accounting:

- task published = artifact exists;
- task addressed = exact target inbox/dispatch exists;
- task activated = OPERATOR/Entity activation boundary is recorded;
- task executing = fresh evidence exists that target Entity began profile work;
- task terminal = PASS/BLOCKED/FAIL result exists.

An addressed task without execution evidence must not indefinitely consume an active WIP slot.

## Practical handling

If no fresh execution evidence appears:
1. mark slot as `AWAITING_ENTITY_ACTIVATION` or `STALE_ADDRESSED`;
2. provide a short activation prompt/file to OPERATOR;
3. do not stack another hidden task onto the same Entity;
4. KOO may use other free profile capacity for an independent Entity where doing so does not violate WIP=2;
5. once Entity activation is confirmed, restore normal active accounting.

No invented timeout duration is defined here.

This rule does not change task authority, routing canon, recovery canon or acceptance semantics.

---
KTO: KOO / КООРДИНАТОР
STATUS: QUEUE_DISCIPLINE_RULE_RECORDED
