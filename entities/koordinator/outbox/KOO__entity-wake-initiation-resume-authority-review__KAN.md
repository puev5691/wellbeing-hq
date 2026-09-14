# KOO → KAN: authority/terminology review общей процедуры Wake → Resume / Initiation → Writer Gate → Exact Task

status: `TASKED_AUTHORITY_TERMINOLOGY_REVIEW`
canon_change_authority: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## Exact input

Revised candidate:
`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r02.md`
commit `bb2e9b9e5e9368a2ae34dc987e37db1fb5a3b9bc`.

Source selection:
`entities/koordinator/outbox/KOO__entity-wake-initiation-resume-source-selection__OPERATOR.md`
commit `bb6bac4360ec7632ddc3ab1212143c311a80c26a`.

SHT process review:
`entities/shtabist/outbox/SHT__entity-wake-initiation-resume-process-review__KOO.md`
commit `60592e7aacf7a4c2dfb6a322bc88988cc8aabbf7`
verdict `PASS_WITH_EXACT_PROCESS_FIXES`.

KOO receipt of SHT fixes:
`routes/receipts/SHT__entity-wake-initiation-resume-process-review__KOO.receipt.md`
commit `8b1dec456eec02a21681c24d49b91ca10931ce1e`.

## Active basis

Use only active approved sources needed for authority/terminology review:
- `project-instructions-core-v2_1-approved.md`;
- `source-loading-policy-v2-approved.md`;
- `entity-state-preservation-and-recovery-canon-v1_4-approved.md`;
- `entity-roles-short-v2_3-approved.md`;
- `file-work-canon-universal-v2_3-approved.md`.

Candidate r0.2 is not active norm.

## Task

Perform bounded authority/terminology review only.

Check especially:
1. whether any proposed state accidentally creates authority from capability, wake, availability, dispatch or initiation;
2. whether `Writer Gate` wording is compatible with one-current-writer rule and worker/read-only instances;
3. whether `authority basis`, `authoritative mutation`, `writer continuity`, `writer established`, `worker/read-only` and `exact task authority` are sufficiently unambiguous;
4. whether OPERATOR/non-delegable/high-impact boundaries remain intact;
5. whether wake router is correctly defined as technical component, not Entity/authority source;
6. whether any proposed label conflicts with existing initiation/delivery/acceptance terminology;
7. whether `WAITING_OPERATOR`, `WAITING_EXTERNAL`, `WRITER_REQUIRED_UNVERIFIED`, `WRITER_CONFLICT` and `WAITING_EXACT_TASK` are semantically safe;
8. whether language about automatic writer establishment/failover could be misread as standing authorization;
9. whether candidate improperly promotes implementation details or research artifacts;
10. whether the universal scope should be constrained to recovery-managed Entities only.

## Required result

Return:
`entities/kancelar/outbox/KAN__entity-wake-initiation-resume-authority-review__KOO.md`

Verdict exactly one of:
- `PASS_AUTHORITY_TERMINOLOGY_READY_FOR_RECOVERY_REVIEW`
- `PASS_WITH_EXACT_AUTHORITY_FIXES`
- `FAIL_AUTHORITY_CONTRADICTION`

If fixes are needed, return only exact required wording/boundary changes and reasons. Do not approve candidate or rewrite unrelated process sections.

## Boundary

Do not:
- approve or activate v1.5;
- create a new role/Entity;
- select scheduler/runtime/provider/adapter/lock technology;
- alter current-writer state;
- authorize production/external execution;
- convert test vectors into policy claims beyond their review purpose.

After KAN result, KOO will integrate exact fixes if any and then route ARH preservation/recovery compatibility review.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: проверить authority и терминологические границы универсальной процедуры до recovery-операционного review
СТАТУС: tasked_authority_terminology_review
