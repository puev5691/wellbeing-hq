# КОО → ОПЕРАТОР: выбран F2 для проектирования первого S1

status: OPERATOR_SELECTED_S1_F2_ONE_DOMAIN_SURVIVAL_DESIGN_ONLY
scope: NONLIVE_REQUIREMENT_DECISION_RECORD_AND_NEXT_GATE_PREPARATION
project_time: omitted

## Exact решение ОПЕРАТОРА

Direct current OPERATOR decision:
SELECT_S1_FAILURE_OBJECTIVE_F2_ONE_DOMAIN_SURVIVAL_DESIGN_ONLY.
The OPERATOR considers this the preferable design strategy. This decision fixes the requirement for synthetic S1 only; it is not a measured recommendation, service choice, storage approval, deployed guarantee or authorization for implementation/test.

Exact prior decision gate:
puev5691/wellbeing-hq@705ceb572d91bca1a1da485321f685034dd5d5d6:entities/koordinator/outbox/KOO__s1o2-failure-objective-decision-gate-r01__OPERATOR.md
blob bd0064c3a11f317d2c86396a3762536516fdc580.
No competing F1/F2/HOLD choice or later failure-objective record found in fresh recent main chain at prewrite boundary.

Fresh observed HQ main prewrite HEAD:
705ceb572d91bca1a1da485321f685034dd5d5d6.
KOO current writer:
entities/koordinator/current/KOO__replacement-current-writer-v08.md
blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
status WRITER_ESTABLISHED.
Six attached approved Sources checked against Git blobs: recovery 233117e1c9509d730e1f5ec532b1cabe3f786609; roles 1772339cb74dae8550bfbd2e33401c34a929e911; source-loading 69eb657f260a019f76e8e707c880ea88c1dfa0bf; file-work e9c29d62057f34e4f771d6057a36d9b7f72e74c2; task-conveyor df7896d867eeeffff506319538fedad938856686; core a42f7dca6a7469a54fa2da24aae0da4e549c9d33.

## F2 exact design objective

A future positively acknowledged checkpoint for S1 must survive total loss of ONE independently verified storage failure-domain without loss of acknowledged immutable object, accepted current-pointer transition and required PUT/CAS operation/dedupe/fence evidence. The identity and independence of the domain must be defined and proven in a later approved profile. Losing an unacknowledged in-flight request is not equivalent to losing acknowledged state; uncertain outcomes require operation-specific reconciliation or UNKNOWN/STOP.

Safety takes priority over write availability: during partition, loss of quorum or ambiguous pointer state the system may refuse new acknowledgements and STOP. It must not choose a current head by timestamp or invent one from backup. Backup and isolated restore remain required independent concerns, but backup-only eventual recovery cannot satisfy the F2 no-loss promise for already acknowledged state after one selected domain loss. Numeric RPO/RTO, outage, retention, quorum, topology and backup cadence remain UNKNOWN.

This F2 requirement excludes automatic elevation of transient bytes, shard URL, HTTP 200, signature, same-disk copy or old VERIFY-only gateway result to CHECKPOINT_DURABLE. It covers the designed S1 synthetic fixture only, not real tasks/Entities, memory-layering attempt 3, providers or automatic chat activation.

## Architectural implications, not selection

SIS options exact result:
puev5691/wellbeing-hq@8cda2ace78d6e27d4d9ada3344d5e2f3af6ca274:entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-storage-durability-options-r01__KOO.md
blob 3641bce5e40d73677f22e48903e8c6b72b709d08
terminal PASS_SIS_S1O2_STORAGE_DURABILITY_PROFILE_OPTIONS_R01_DOCUMENT_ONLY.

Inference from SIS model descriptions:
- M1, one durability domain plus backup, cannot alone meet F2 for its own total domain loss.
- M2, synchronous independent-domain commit, is a candidate pattern for F2, subject to exact independence, commit/ack/CAS/journal evidence and later D1–D9 tests.
- M3, separated object/control planes, may be combined with a qualifying failure profile on EACH required plane; separation alone does not establish F2.
These are design implications, not a backend, host, replica count or architecture selection. SIS recommendation at options stage was UNKNOWN/NOT_YET_GROUNDED and is not rewritten as a test PASS.

Selected B S1+O2 prior scope:
puev5691/wellbeing-hq@8a5dc8dffd12a158f6501eacbece46b55a805246:entities/koordinator/outbox/KOO__shard-checkpoint-option-b-s1o2-nonlive-scope-draft-r01__OPERATOR.md
blob 30a8444646a84cf8eff7a7941c3b1ca5fa0a70e3.
Reviewed governance successor:
puev5691/wellbeing-hq@63a0e218f9cec36bb2652febd618b104d1aa69e4:entities/kancelar/outbox/KAN__shard-checkpoint-governance-dedupe-successor-r01-candidate__KOO.md
blob 799be4e536a2795fae19b489b9887570d614a52a
status CANDIDATE_NOT_ACTIVE.
SIS review of same bytes blob 67fe653dbbc234fbaedc971c3ca3a92d6c76a987; ARH review blob 80cdd7dd277d37472d586ce15a098ed57c50fc4d; both documentary only.

## Next separate non-live gate

Before a justified design recommendation, a future SIS document-only fit-gap may check available classes of storage/failure domains against the F2 objective, identify proof of physical and administrative independence, required synchronous ack semantics for object/pointer/outcome/fence lineage, and the cost/availability implications of STOP during partition. This requires separate exact authority:
AUTHORIZE_SIS_S1O2_F2_CAPABILITY_FITGAP_R01_DOCUMENT_ONLY.
No SIS task is activated or created by this decision record. If that authority is later given, KOO must fresh-reconcile and issue a bounded self-contained PROMPT. Do not choose mazhor as backend from historical VERIFY-only evidence or access hosts without separate authorization.

## Boundaries

Governance candidate CANDIDATE_NOT_ACTIVE.
CHECKPOINT_DURABLE NOT_ESTABLISHED.
Resume authority NOT_GRANTED.
Operational owner NOT_APPOINTED.
Memory-layering attempt 3 NOT_AUTHORIZED.
No code/test, shard WRITE, host/shard access, secrets, provider call, production, implementation/deployment, automatic activation, automation or Project Sources/canon mutation. Historical PROMPT replay: none. This artifact records OPERATOR design objective only.

---
КТО: KOO / КООРДИНАТОР
КОМУ: ОПЕРАТОР
СТАТУС: OPERATOR_SELECTED_S1_F2_ONE_DOMAIN_SURVIVAL_DESIGN_ONLY
