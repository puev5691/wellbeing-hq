# SIS-GWR-MAINT-R01 r0.2 — corrected reusable bounded authority candidate

status: CANDIDATE_NOT_ACTIVE
document_type: correction-successor-candidate
predecessor:
puev5691/wellbeing-hq@15c3f5eb3a7c7599d78825bf9ad2427421a98de0:entities/koordinator/outbox/KOO__SIS-GWR-MAINT-R01-reusable-bounded-authority-candidate__OPERATOR.md
predecessor_blob: 3e468bc07e5e0a26f11a82e01388d90b85d5d0f7
project_time: omitted

## Человеческий смысл

Цель сохраняется: ОПЕРАТОР один раз утверждает узкую reusable authority для завершения retirement старого wellbeing-shard-gateway на exact host p552203.kvmvps, а SIS не возвращается за отдельным разрешением на каждый безопасно классифицированный остаточный файл.

r0.2 закрывает опасные двусмысленности:
- approval authority не создаёт задачу и не запускает SIS;
- allowlisted path не является разрешением удалить объект;
- mutation допускается только после отдельного object admission;
- container/tree нельзя удалить при UNKNOWN/active/sensitive descendant;
- pre-mutation evidence связывается с exact filesystem object;
- preservation prerequisite должен быть exact и проверяемым;
- helper не получает authority сверх контракта;
- после полного retirement mutation authority становится DORMANT/CONSUMED для старого contour и не применяется к объектам, появившимся позже только потому, что путь совпадает.

Этот файл остаётся кандидатом. Фраза «ОПЕРАТОР утверждает» появляется только в отдельном future approval decision, не здесь.

## 1. Authority identity and scope

Candidate authority ID:
SIS-GWR-MAINT-R01

Revision:
r0.2-candidate

Intended recipient after approval:
current authoritative SIS / СИСАДМИН.

Exact host:
p552203.kvmvps

Purpose:
bounded completion/retirement of residual objects proven to belong to the retired wellbeing-shard-gateway contour.

Standard causal chain:

APPROVAL
→ STANDING_AUTHORITY_DORMANT
→ CURRENT_EXACT_MAINTENANCE_TASK_OR_EXPLICIT_ACTIVATION
→ PRE_CYCLE_GATE
→ INSPECT
→ CLASSIFY
→ OBJECT_RETIREMENT_ADMISSION
→ PRE_MUTATION_REVERIFY
→ RETIRE
→ VERIFY
→ NEXT_OBJECT_OR_RETIREMENT_COMPLETE
→ STANDING_AUTHORITY_DORMANT_OR_CONSUMED

Invariant:
authority exists != task exists != activation occurred != object admitted != mutation executed != retirement complete.

## 2. Approval/effectivity

While this file has status CANDIDATE_NOT_ACTIVE:
- no standing authority exists from this file;
- no mutation is authorized by this file;
- no helper implementation/update/run is authorized by this file.

A future exact OPERATOR decision may activate this revision.

Approval effect:
SIS-GWR-MAINT-R01 r0.2 becomes APPROVED / DORMANT standing bounded authority.

Approval alone does NOT start work.

Execution starts only when all are true:
1. current authoritative SIS writer verified;
2. exact host verified;
3. a NEW current exact maintenance task or explicit activation event addressed to current SIS exists and is not superseded;
4. required preservation prerequisite is verified;
5. no conflict with active approved Sources/current state.

Historical task/PROMPT, file appearance, standing authority itself, detector event or automation event cannot activate execution.

No automatic activation authority is created.

## 3. Closed gateway allowlist

Mutation allowlist only:

1. /etc/systemd/system/wellbeing-shard-gateway-verify.service
2. /opt/wb-shard-gateway
3. /run/wb-shard-gateway
4. /var/lib/wellbeing/shard-gateway
5. /var/log/wb-shard-gateway

Minimal read-only dependency tracing outside these paths is permitted only when necessary to determine whether an allowlisted object has a current consumer/dependency.

No mutation outside the allowlist.

Path presence in this list means only:
ELIGIBLE_FOR_INSPECTION/CLASSIFICATION.

It never means:
ELIGIBLE_FOR_DELETION.

## 4. Separate helper allowlist

Potential helper paths:

- /home/shd/SIS-GWR-INSPECT.sh
- /home/shd/SIS-GWR-RETIRE.sh

These are a separate helper allowlist, not gateway residue.

If a future exact implementation authority permits creation/update/run of these helpers:
- helper code must be reviewed/version-bound before first mutation-capable use;
- helper may perform only operations already permitted by SIS-GWR-MAINT-R01;
- helper cannot widen path, host, task, writer, dependency or secret boundaries;
- RETIRE helper must fail closed on missing/ambiguous classification evidence;
- helper mutation outside gateway allowlist is forbidden;
- helper itself is not evidence that an object is stale;
- shell/root capability does not create authority.

This r0.2 candidate does not by itself authorize new helper implementation.

If existing exact reviewed helper implementations already have separate valid authority, this candidate neither revokes nor expands it.

## 5. Object identity and classification

Classification applies to an exact filesystem object/evidence unit, not merely a pathname string.

Minimum identity where available/applicable:
- normalized/canonical path;
- object type;
- device/filesystem identity;
- inode or equivalent stable identity;
- symlink state/target;
- owner/group/mode;
- relevant size/content metadata;
- mount/bind-mount status where applicable.

Classification states:

ACTIVE_DEPENDENCY
STALE_RETIRABLE_CANDIDATE
SECRET_OR_SENSITIVE
UNKNOWN
OUT_OF_SCOPE

Meaning of STALE_RETIRABLE_CANDIDATE:
the object is a candidate for the separate OBJECT_RETIREMENT_ADMISSION gate.
It is NOT itself mutation authority.

## 6. Dependency/current-consumer minimum check

Before OBJECT_RETIREMENT_ADMISSION, inspect applicable evidence for:
- running process/executable/working-directory use;
- open-file references;
- active/listening socket references;
- systemd unit/dependency/reference;
- timer/cron/service invocation where discoverable in bounded host evidence;
- current configuration/reference that would make removal causally unsafe;
- mount/bind-mount relation;
- symlink/path escape;
- any other exact consumer surfaced by the bounded inspection.

Absence of one evidence class does not imply absence of all consumers.

If required dependency evidence is unavailable/incomplete:
UNKNOWN → STOP affected retirement.

## 7. Recursive/container rule

A directory/tree/container may receive OBJECT_RETIREMENT_ADMITTED only when:
- every descendant that would be removed is enumerated or otherwise deterministically covered by bounded evidence;
- every such descendant is STALE_RETIRABLE_CANDIDATE and still fresh at admission;
- no descendant is ACTIVE_DEPENDENCY;
- no descendant is SECRET_OR_SENSITIVE;
- no descendant is UNKNOWN or OUT_OF_SCOPE;
- no symlink/mount/path escape crosses the allowlist;
- no unexpected descendant appears before mutation.

One UNKNOWN/active/sensitive/out-of-scope descendant blocks retirement of the containing recursive tree.

No wildcard/recursive deletion over unclassified contents.

## 8. Preservation prerequisite

Destructive retirement requires an exact preservation prerequisite.

Before the first mutation in each activated maintenance task/cycle, SIS must bind:
- exact preservation package/artifact locator;
- immutable identity/version;
- required scope/content relation to the old gateway contour;
- successful readback/integrity evidence required by the applicable preservation/file canon.

Mere existence of “some preservation package” is insufficient.

If no exact preservation locator/version is available in current authoritative evidence:
PRESERVATION_UNVERIFIED → STOP before mutation and return blocker for the minimum evidence/decision needed.

This candidate does not invent the missing preservation locator.

## 9. OBJECT_RETIREMENT_ADMISSION gate

Only after STALE_RETIRABLE_CANDIDATE classification may SIS evaluate:

OBJECT_RETIREMENT_ADMITTED.

Required:
- current SIS writer PASS;
- current exact task/activation PASS;
- exact host PASS;
- preservation prerequisite PASS;
- object identity PASS;
- allowlist containment PASS;
- dependency/current-consumer absence PASS;
- secret-sensitive check PASS;
- recursive/container rule PASS where applicable;
- no supersession/conflict PASS.

Only OBJECT_RETIREMENT_ADMITTED may proceed to mutation.

Thus:
STALE_RETIRABLE_CANDIDATE != OBJECT_RETIREMENT_ADMITTED.

## 10. Pre-mutation reverify / TOCTOU boundary

Immediately before each mutation or atomic bounded mutation group, repeat critical checks against the exact object identity.

At minimum reverify:
- current SIS writer;
- current task/activation and no supersession;
- exact host;
- normalized path and object type;
- inode/device or equivalent identity where applicable;
- symlink/mount state;
- no new descendant/unexpected object;
- no new process/open-file/socket/systemd/current consumer;
- preservation prerequisite still valid;
- object remains OBJECT_RETIREMENT_ADMITTED.

Identity/evidence mismatch:
STOP before mutation.

Do not treat a previous pathname classification as permission to delete a replacement object later appearing at the same path.

## 11. Permitted mutation after admission

Only OBJECT_RETIREMENT_ADMITTED objects may be retired.

Permitted bounded actions:
- remove exact admitted stale files/directory entries;
- remove old gateway unit only if admitted and dependency-free;
- remove /opt/wb-shard-gateway tree only under recursive/container rule;
- remove runtime/log/data directories only when all removed contents are admitted;
- systemctl daemon-reload only when causally required by admitted unit removal;
- bounded post-mutation verification.

Allowlist membership never bypasses admission.

## 12. Secret/sensitive exception semantics

SECRET_OR_SENSITIVE:
- do not disclose raw secret/token/private-key content;
- do not retire affected object under this standing authority;
- stop mutation of the affected object/subtree and any causally dependent mutation;
- return exact bounded blocker to OPERATOR/KOO.

Independent already-admitted objects may continue only if:
- their mutation cannot affect the sensitive object;
- the current task explicitly permits independent continuation;
- no cycle-wide stop condition applies.

If independence is ambiguous:
STOP entire cycle.

Separate OPERATOR decision is required for treatment of the sensitive exception.

## 13. Other fail-closed states

STOP affected retirement/cycle as applicable on:
- writer mismatch/freeze/replacement;
- host mismatch;
- missing/stale/superseded task;
- path escape;
- active dependency/current consumer;
- UNKNOWN;
- OUT_OF_SCOPE;
- object identity change;
- unexpected descendant;
- incomplete evidence;
- malformed helper output;
- preservation unverified;
- need for mutation outside allowlist;
- ambiguity whether object belongs to retired gateway contour.

No “best effort delete”.

## 14. Post-mutation verification

After each mutation:
- verify intended object absence/change;
- verify no collateral allowlist escape;
- verify relevant service/process/socket/systemd state;
- record actual mutation, not intended mutation;
- preserve failure evidence without fabricating completion.

Failure to verify:
FAIL/BLOCKED according to evidence; do not declare retirement complete.

## 15. Standing authority lifecycle

States:

CANDIDATE_NOT_ACTIVE
→ APPROVED_DORMANT
→ ACTIVE_EXECUTION_INSTANCE
→ APPROVED_DORMANT
or
→ RETIREMENT_COMPLETE_CONSUMED

APPROVED_DORMANT:
authority exists, but no work is running.

ACTIVE_EXECUTION_INSTANCE:
a new exact task/activation plus all pre-cycle gates are valid.

RETIREMENT_COMPLETE_CONSUMED:
the identified old gateway contour has been verified retired under the current task and terminal result.

After RETIREMENT_COMPLETE_CONSUMED:
- this authority cannot delete a future object merely because it appears under an old allowlisted path;
- reappearance/new deployment/new ownership is a new fact requiring fresh task/authority reconciliation;
- no automatic reactivation.

If retirement is incomplete because residue remains safely classifiable later:
return to APPROVED_DORMANT with exact remaining scope, not CONSUMED.

## 16. Result classes

Per execution/cycle:

PASS_SIS_GWR_MAINT_CYCLE_COMPLETE
BLOCKED_SIS_GWR_MAINT_<reason>
FAIL_SIS_GWR_MAINT_<reason>

Final contour terminal:
PASS_SIS_GWR_RETIREMENT_COMPLETE_CONSUMED

Result records:
- exact task/activation;
- exact host;
- preservation evidence locator/version;
- inspected scope;
- object identities/classifications;
- admission decisions;
- mutations actually performed;
- verification;
- remaining residue;
- authority lifecycle state.

Publication/result does not itself prove receipt/acceptance.

## 17. Explicit exclusions

No authority for:
- /data/wellbeing-lab mutation;
- proof roots;
- backend install/run;
- T01-T20;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- credential/provider/Telegram work;
- Project Sources/canons;
- unrelated host/service cleanup;
- reset/reimage;
- historical PROMPT replay;
- automatic activation.

## 18. Proposed OPERATOR decision

This candidate itself does not approve anything.

If accepted, exact decision:

APPROVE_SIS_GWR_MAINT_R01_R02_STANDING_BOUNDED_AUTHORITY

Effect:
activate r0.2 as standing bounded authority in state APPROVED_DORMANT.

It still requires a NEW exact task/activation addressed to current SIS before execution.

Alternative:

REJECT_SIS_GWR_MAINT_R01_R02

or

HOLD_SIS_GWR_MAINT_R01_R02

## 19. Exact decision warning

Do not use predecessor decision phrase
AUTHORIZE_SIS_GWR_MAINT_R01_REUSABLE_BOUNDED_AUTHORITY_P552203
without binding it to r0.2 exact identity.

Approval must identify this exact revision/immutable artifact to avoid accidentally activating predecessor r0.1 semantics.

## Terminal

CANDIDATE_SIS_GWR_MAINT_R01_R02_READY_FOR_OPERATOR_DECISION

## EXPERIENCE

Идея → reusable authority должна убирать микроменеджмент, не превращая allowlist в разрешение на удаление.

Проба → разложить процедуру на approval/task/activation/classification/admission/mutation/consumption и проверить recursive, TOCTOU, preservation и helper boundaries.

Результат → standing authority стала reusable для старого contour, но не самозапускающейся и не бессрочной лицензией на любой будущий объект по тем же путям.

Успех → correction successor готов к OPERATOR decision.

Урок → хороший standing authority экономит решения человека только после того, как точно определено, какие решения он уже принял один раз и какие факты всё равно обязаны проверяться заново.
