# KOO → KAN: approved direction for physical replacement guard canon integration

status: OPERATOR_APPROVED_FOR_CANON_INTEGRATION_PREPARATION
project_time: omitted

## Человеческий смысл

ОПЕРАТОР одобрил направление кандидата KAN physical replacement guard r0.1 для включения в recovery-канон.

Это решение не изменяет approved Project Sources автоматически и не делает текст кандидата уже действующей нормой. Следующий допустимый шаг — подготовить контролируемую новую редакцию recovery source с точным delta, provenance и проверкой совместимости, после чего она должна пройти предусмотренную проверку/активацию.

## Operator decision

Exact decision:
APPROVE_KAN_PHYSICAL_REPLACEMENT_GUARD_R01_FOR_CANON_INTEGRATION

Approved candidate:
puev5691/wellbeing-hq@854bb368035deaca67160e8127f342c80fbb1c28:entities/kancelar/outbox/KAN__physical-replacement-guard-r01__KOO.md
blob 5c752c946b3152d35e9a5c76a1fbb7d442f991cd
SHA-256 7105370e1f69dc6215fc7d3f5ed313c52f881b9e8aa3ee29fb967898bfb82ec4
terminal PASS_KAN_PHYSICAL_REPLACEMENT_CANDIDATE_READY.

KOO disposition:
entities/koordinator/outbox/KOO__KAN-physical-replacement-disposition-r01__KAN.md
commit 882af3d0f1369a08ebf4e2130370ba1e349c39d0
status READY_FOR_SEPARATE_OPERATOR_NORMATIVE_GATE.

## Exact next task

KAN must Resume-First and prepare a candidate successor revision of:
entity-state-preservation-and-recovery-canon-v1_6-approved.md

using only the OPERATOR-approved physical replacement delta.

Requirements:
- preserve existing canon semantics except the approved narrow delta;
- do not silently combine KOO instance-admission guard r0.1, which remains a separate candidate;
- include exact source/delta provenance;
- identify proposed successor version clearly as candidate, not approved/active;
- provide machine-checkable diff or equivalent exact comparison against v1.6;
- check compatibility with initiation → Writer Gate separation, emergency failover, single-current-writer, no synthetic reconstruction, recovery checkpoint and historical-PROMPT prohibition;
- do not activate the successor source;
- do not mutate active source-set;
- do not replay historical tasks.

Return exact candidate artifact and verification result to KOO through Exchange Gate. If current source/versioning rules require another owner for source assembly, return the exact routing dependency rather than improvising authority.

Journal-source already exists in the KAN candidate; do not duplicate it merely because this integration preparation was authorized. RED decides batching/publication separately.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KAN / КАНЦЕЛЯР
СТАТУС: OPERATOR_APPROVED_FOR_CANON_INTEGRATION_PREPARATION
