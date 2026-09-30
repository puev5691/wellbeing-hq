# ПКТБ Engineering Entity Lifecycle r0.1 candidate

status: CANDIDATE_ONLY_NOT_ACTIVE
project_time: omitted
Inherited: Project Core v2.5 a42f7dca6a7469a54fa2da24aae0da4e549c9d33; Entity Roles v2.4 1772339cb74dae8550bfbd2e33401c34a929e911; Source Loading v2.2 69eb657f260a019f76e8e707c880ea88c1dfa0bf; Recovery v1.6 233117e1c9509d730e1f5ec532b1cabe3f786609; File Work v2.4 e9c29d62057f34e4f771d6057a36d9b7f72e74c2; Task Conveyor v1.2 df7896d867eeeffff506319538fedad938856686; approved PKTB/PRO foundation 62a5a65422ac9144aaf2215dce3157f3debb62a3.

NEED → ROLE_DEFINITION → SOURCE_PROFILE → INITIATION → WRITER_GATE → BOUNDED_WORK → PRESERVATION/RECOVERY → INACTIVE | REPLACEMENT | RESUME.

Entity создаётся только при доказанной потребности, не как заранее сформированный штат. NEED фиксирует функцию/result/evidence/verification owner и почему существующая роль недостаточна.

ROLE_DEFINITION: identity candidate, function, responsibility, inputs/outputs, authority boundary, dependencies, verification owner, continuity need. Role != task; capability != authority.

SOURCE_PROFILE: минимальный inherited baseline + task/profile sources. Task-specific material не становится Project Source.

INITIATION требует exact authority; file/chat/memory/historical PROMPT не активируют роль. WRITER_GATE отдельный: competing instance/current-writer, supersession, exact role/foundation и authority. Только PASS даёт authoritative current-state write.

WORK только exact bounded task; stale/consumed/superseded authority → STOP. PRESERVATION/RECOVERY по global canon; утраченное не реконструировать по памяти. INACTIVE сохраняет verified state/recovery, но не разрешает новую работу. REPLACEMENT проходит initiation и отдельный Writer Gate. RESUME допустим только при доказанной continuity.

Этот candidate новых Entities не создаёт и сам authority model не активирует.
