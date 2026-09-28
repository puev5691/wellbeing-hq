# KOO → SHT: stress-review Entity Operational Continuity Contract r0.1 + r0.2 corrections

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHT / ШТАБИСТ
scope: BOUNDED_DOCUMENT_ONLY_CAUSAL_STRESS_REVIEW
project_time: omitted

Resume-First.

## Current KOO writer

puev5691/wellbeing-hq@9c5e330719fa4410eca76e91a128bfcc29d56c45:
entities/koordinator/current/KOO__replacement-current-writer-r10.md

blob:
8416e945418a4a86764edafbbd06682f6c84682b

status:
WRITER_ESTABLISHED

## Intended SHT writer basis

puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md

writer_generation:
SHT-CURRENT-INSTANCE-R01

SHT must fresh-verify current-writer continuity, supersession, exact task and active Sources before review.

## Exact predecessor candidate

puev5691/wellbeing-hq@7f7aa19e0453580c6c5a17ace7acf29a2da8456a:
entities/koordinator/outbox/KOO__entity-operational-continuity-contract-r01-candidate__KAN.md

blob:
ff2288267c200711c8c34c5b91373c96915a392f

## Exact KAN review

puev5691/wellbeing-hq@f8175895e2a34721830a3816719f2af1a3ffd087:
entities/kancelar/outbox/KAN__entity-operational-continuity-r01-independent-review__KOO.md

blob:
4dc23f7454a691de3ef6f06ea88f3862d2fae509

terminal:
NEEDS_REWORK_KAN_ENTITY_OPERATIONAL_CONTINUITY_CONTRACT_R01_GATE_SEMANTICS_AND_EFFECTIVITY

## Exact correction-only successor

puev5691/wellbeing-hq@0087286864a4f34fe2be1a03d1cd69029dabb4e4:
entities/koordinator/outbox/KOO__entity-operational-continuity-contract-r02-correction-addendum__SHT.md

blob:
6ed793c5797b74e8dd41b7f1059a35a9a4634181

terminal:
CANDIDATE_R02_CORRECTIONS_READY_FOR_SHT_STRESS_REVIEW

Combined candidate under review:
exact r0.1 predecessor bytes + exact r0.2 correction addendum bytes.

Neither artifact is active.

## Stress-review purpose

Determine whether the combined candidate safely prevents the observed failure class:
an Entity restores verified facts but loses, invents or mispackages the next causal transition for the human.

Review causality and failure modes only.
Do not activate candidate and do not implement code.

## Mandatory cases

At minimum test:

1. Initiation PASS, Writer Gate not yet granted.
2. Explicit HOLD/WAIT with a possible but not currently enabled next transition.
3. Automatic capability exists but authority is absent.
4. Automatic activation is authorized but not observed.
5. Capsule and Head agree but both are stale.
6. Fresh terminal evidence contradicts Capsule/Head.
7. Emergency recovery where Capsule/Head are absent, stale or unavailable.
8. Completed profile task with defective/missing human handoff.
9. Current KOO line BLOCKED while another line is separately authorized.
10. UNKNOWN/missing recipient/scope/evidence.
11. Publication/dispatch/inbox without receipt/processing evidence.
12. Decision request exists but granted authority does not.
13. Granted authority exists but prompt/task materialization is stale.
14. Human-facing result and derived projections disagree.
15. PRE_SEND_GATE UNVERIFIED while execution terminal is valid BLOCKED/FAIL/PASS.
16. Historical PROMPT points to COMPLETED/SUPERSEDED task.
17. WAIT is used to conceal a manual action that is actually required.
18. Capsule/Head disagreement is "fixed" by last-write-wins.
19. Candidate pilot operates without modifying active Sources.
20. Proposed mandatory rollout would change active Source meaning without amendment/effectivity.

## Review questions

Determine:
- whether R1-R5 fully close KAN's documentary defects;
- whether new false PASS / false FAIL paths remain;
- whether C01-C10 are safe as a candidate hypothesis;
- which predicates are not yet machine-checkable;
- whether Capsule/Head can remain derived/non-authoritative;
- whether PRE_SEND_GATE can fail without erasing execution terminal;
- whether WAIT/NONE can be used safely;
- whether decision request vs granted authority is correctly separated;
- whether emergency failover remains possible without Capsule/Head;
- whether minimality is preserved;
- whether candidate is safe for one bounded implementation/pilot decision.

## Result

Return one exact terminal:

PASS_SHT_ENTITY_OPERATIONAL_CONTINUITY_R02_STRESS_REVIEW_WITH_BOUNDARIES

or exact:
NEEDS_REWORK_SHT_ENTITY_OPERATIONAL_CONTINUITY_R02_<reason>

or:
BLOCKED_SHT_ENTITY_OPERATIONAL_CONTINUITY_R02_<reason>

If PASS:
- list residual implementation concerns;
- identify exact minimum input contract for a future linter;
- state whether bounded pilot is safe to put to OPERATOR decision;
- do not authorize KOD or activate candidate.

If NEEDS_REWORK:
- identify only exact remaining causal defects;
- propose minimal corrections;
- do not redesign unrelated sections.

## Prohibited

- Project Source/canon mutation;
- candidate activation;
- KOD implementation;
- automation;
- foreign current-state mutation;
- historical PROMPT replay;
- treating review publication as receipt/acceptance/effectivity.

Publish one immutable result, exact readback it, return locator/identity to KOO, then STOP.
