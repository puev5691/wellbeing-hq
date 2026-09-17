# KOO → OPERATOR: recovery canon v1.4 status clarification

status: `OPERATOR_STATUS_CLARIFICATION`
project_time: omitted; trusted project-time source not used

## Exact immutable source

File:
`entity-state-preservation-and-recovery-canon-v1_4-approved.md`

Expected SHA-256:
`984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda`

Observed internal conflict in the same immutable file:
- title line contains `v1.4 candidate`;
- service card at end contains `status: approved_for_active_use`, `Approval status: approved_by_operator`, `Effective: true`.

## OPERATOR decision

ОПЕРАТОР подтверждает, что для exact immutable файла выше его нормативный статус определяется служебной карточкой в конце документа:

`approved_for_active_use / approved_by_operator / Effective: true`.

Слово `candidate` в заголовке считается редакционной ошибкой и не понижает нормативный статус этого exact immutable файла.

Bytes файла не изменять в рамках emergency initiation. Данное решение не создаёт новую редакцию канона и не меняет его содержательные положения.

## Scope

Эта clarification применяется только к exact immutable identity указанного файла и только для устранения status ambiguity при source-loading / recovery initiation.

Она не даёт право автоматически повышать любые другие candidate/draft файлы до approved.

---
КТО: OPERATOR через KOO
ДЛЯ ЧЕГО: устранить внутренний конфликт статуса exact recovery canon v1.4 при аварийной инициации KOD
СТАТУС: `RECOVERY_CANON_V14_APPROVED_STATUS_CONFIRMED`
