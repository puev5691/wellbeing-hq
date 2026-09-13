# KOD current: GitHub information-entry pilot r2

status: WAITING_KOO_R2_TECHNICAL_REVIEW
production: no
public_ready_promotion: blocked

source_task:
`entities/koder/inbox/KOO__github-info-entry-pilot-r1-defect__KOD.md`

source_task_commit:
`a05b80fc9041561c659ddaf19574b7550dd8e96b`

immutable_package:
`entities/koder/outbox/github-info-entry-pilot-v01-r2/`

immutable_package_commit:
`04753a229afc24ecf724f583e6df3dabed6bfba3`

result:
`entities/koder/outbox/KOD__github-info-entry-pilot-r2-result__KOO.md`

result_commit:
`5c4035add167ce980567f58ab46f698432fabeb7`

dispatch:
`routes/dispatch/KOD__github-info-entry-pilot-r2-result__KOO.md`

dispatch_commit:
`2d342e6646823572e13a21c4c35fdce2c81c2ebd`

KOO inbox pointer:
`entities/koordinator/inbox/KOD__github-info-entry-pilot-r2-result__KOO.md`

pointer_commit:
`ecf6b18dab4f08a36599d4e0f9dcd375349b0742`

## Verified result

- proven r1 bypass `"secret_dependency": "true"` is rejected as `invalid_type:secret_dependency`;
- strict type validation precedes semantic gates;
- unknown properties fail closed;
- local exact suite: `12/12 cases PASS`;
- `py_compile`: PASS;
- final `MANIFEST.sha256` verified before publication;
- GitHub package readback matched tested bytes and exact manifest;
- no production/settings/credentials/Project Sources mutation.

## Waiting boundary

KOD does not claim acceptance.
Required next external event:
1. KOO technical review;
2. if accepted for that stage, SHD cross-layer re-verification;
3. no public-ready promotion before those decisions.

## Experience fixation

Идея: security gate нельзя строить на Python truthiness или проверке только одного literal boolean.
Проба: malformed string `"true"` против r1.
Результат: SHD defect подтверждён; r2 блокирует malformed type до semantic evaluation.
Успех: 12/12 fixtures PASS, включая исходный bypass и соседние type-errors.
Фиксация: типовая валидация должна быть отдельным fail-closed слоем до смысловых правил; unknown security-relevant keys нельзя молча принимать.

project_time: omitted; trusted project-time source not used.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать Resume-First checkpoint после публикации и адресной доставки r2
СТАТУС: waiting_KOO_review
