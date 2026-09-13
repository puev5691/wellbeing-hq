# ARH — KOD chat/UI completion anomaly

status: diagnostic_preserved
project_time: omitted; trusted project-time source not used

## Наблюдение

ОПЕРАТОР сообщил, что старый KOD-чат и replacement KOD-чат выглядят незавершёнными/подвисшими.

## Fresh evidence

Replacement KOD фактически завершил аварийную инициацию и зафиксировал:
- `entities/koder/current/KOD__initiation-verified-current-writer-v01.md`;
- status: `initiation_verified`;
- current_writer_state: `confirmed_replacement_writer`;
- old writer: frozen historical instance;
- competing writer evidence: not found on fresh main.

После этого replacement KOD выполнил профильную работу GitHub information-entry r2:
- immutable package commit: `04753a229afc24ecf724f583e6df3dabed6bfba3`;
- exact tests: 12/12 PASS;
- result commit: `5c4035add167ce980567f58ab46f698432fabeb7`;
- dispatch commit: `2d342e6646823572e13a21c4c35fdce2c81c2ebd`;
- KOO inbox pointer commit: `ecf6b18dab4f08a36599d4e0f9dcd375349b0742`;
- current checkpoint commit: `00d5dd106dff76a141ff072e46114b52ca8addff`;
- state: `WAITING_KOO_R2_TECHNICAL_REVIEW`.

KOD GitHub Work automation is enabled on hourly :12 and points to the verified replacement-writer boundary.

## Diagnosis

Observed UI/chat incompletion is not evidence that KOD profile execution failed. Repository evidence shows execution completed and checkpointed before the visible chat appeared stuck.

Most plausible current failure-mode: response/tool-session completion or client rendering/streaming stall after backend actions, rather than loss of KOD semantic state.

## Operational boundary

1. Old KOD chat must not be used for authoritative work.
2. Replacement KOD remains the current writer by explicit initiation record.
3. Do not create a third KOD chat solely because the visible reply is incomplete.
4. Resume replacement KOD only from fresh GitHub preflight/checkpoint. If the UI cannot accept another prompt at all, then prepare a new recovery from the replacement writer checkpoint before another failover.
5. Treat GitHub checkpoint, not the last rendered chat bubble, as the authoritative completion boundary.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить evidence о расхождении между видимым chat/UI completion и фактически завершённой KOD profile work
СТАТУС: diagnostic_preserved
