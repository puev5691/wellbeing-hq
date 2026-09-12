# ARH — VOL semantic response without receipt lineage

status: verified_event_lineage
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Episode

Исходный маршрут ARH → VOL:
- artifact: `entities/archivarius/outbox/ARH__VOL-emergency-recovery-request__VOL.md`
- artifact commit: `25e6e358a24fbf681b0e87920ae9919de4b8aa18`
- dispatch: `routes/dispatch/ARH__VOL-emergency-recovery-request__VOL.md`
- dispatch commit: `b8f2d2197ead52e3a4eb2cd0a8f8f470a7a60448`
- sender-registry record currently remains `status=dispatched`, `receipt=null`.

## Verified downstream evidence

VOL produced an explicit semantic response:
- `entities/volonter/outbox/VOL__emergency-recovery-candidate__ARH.md`
- response commit: `030ed61049c3377b4a84e1fec88e4d4d4d415f32`
- current blob readback: `45ee92bf016ced4d6cef8b39cd109ee57e939e55`
- response text explicitly states that `entities/volonter/inbox/ARH__VOL-emergency-recovery-request__VOL.md` was processed.

ARH subsequently verified the returned recovery candidate:
- verification result commit: `25f5f38a8cca0a65be02979089b107e598827944`
- recovery-registry update commit: `4ed963bab6ee86ebd7417764a44a38468eddf3a3`.

ОПЕРАТОР позднее сообщил, что новый VOL успешно прошёл инициацию и продолжил работу с прерванной задачи. Это operational outcome, но не GitHub receipt исходного ARH → VOL route.

## Sanitized interpretation

1. `semantic_processing_evidence = verified`.
2. `downstream_recovery_verification = completed`.
3. `practical_new-chat_initiation = operator_reported_success`.
4. `exact_route_receipt = absent/not_observed`.
5. Поэтому sender-registry исходного маршрута НЕ переводить автоматически из `dispatched` в `received` без exact receipt artifact или отдельного утверждённого правила, разрешающего semantic-response reconciliation.
6. Отсутствие exact receipt также НЕ трактовать как отсутствие обработки запроса: обработка подтверждена отдельным response artifact и последующими событиями.

## Reusable rule

Различать три независимых факта:

`route receipt` ≠ `semantic response` ≠ `successful downstream outcome`.

Они могут подтверждать разные уровни жизненного цикла одного эпизода и не должны молча подменять друг друга.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную цепочку VOL recovery и предотвратить ложную санацию sender-registry при отсутствии exact receipt
