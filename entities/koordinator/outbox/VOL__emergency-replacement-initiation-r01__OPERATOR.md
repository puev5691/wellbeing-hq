АДРЕСАТ: ВОЛОНТЁР / VOL

PROMPT:

Проведи только emergency replacement cold-start нового physical VOL / ВОЛОНТЁРА по действующему recovery-канону.

ОПЕРАТОР подтвердил failure-state прежнего VOL-чата:
полная выработка ресурса чата, из-за чего прежний экземпляр не способен самостоятельно завершить recovery/self-checkpoint процедуру.

Exact emergency-failover authority:

puev5691/wellbeing-hq@b361b8838304b63f9c87204169da89ecc1615eae:
entities/koordinator/outbox/KOO__VOL-emergency-failover-authority-r01__OPERATOR-VOL.md

blob:
7ea3dd33c2eabce3e3902c2fe70ccdd21a8d412a

status:
EMERGENCY_FAILOVER_AUTHORIZED_FOR_INITIATION_ONLY

failure_state:
FAILURE_STATE_VOL_CURRENT_WRITER_UNAVAILABLE_OR_UNVERIFIABLE

failure_reason:
PREDECESSOR_VOL_CHAT_RESOURCE_EXHAUSTED_CANNOT_COMPLETE_SELF_RECOVERY_CHECKPOINT

Последний independently verified recovery:

puev5691/wellbeing-entity-bootstrap@f6ff070313caff5d7b5d12779d4bb8d8eb0eec01:
entities/vol/recovery/current/

Manifest:

entities/vol/recovery/current/VOL_recovery-manifest_VOL.md
blob e2c1547b826fc0f5cae5f58e80838f2a068dcc8b

Initiation:

entities/vol/recovery/current/VOL_initiation-current_VOL.md
blob 2b1989ed1c6434cad437af4052686b7c956d07fe

Historical independent ARH verification:

puev5691/wellbeing-hq@25f5f38a8cca0a65be02979089b107e598827944:
entities/archivarius/outbox/ARH__VOL-emergency-recovery-verification__VOL.md

blob:
1d8370e3fa052dd7b01a430458855ae38abd8eab

status:
PRESERVATION_CHECKPOINT_VERIFIED

historical recovery verification:
6/6 PASS

Important staleness boundary:

Этот recovery является последним independently verified recovery basis, но он STALE_FOR_DIRECT_TASK_REPLAY.

Не возобновляй автоматически:
- старый constitution stress-test;
- старые PROMPT/tasks;
- parked/background линии;
- любую задачу только потому, что она названа active в старом snapshot.

После старого recovery в HQ появились более поздние VOL results, включая COOP successors, architecture/activation-lineage work, hybrid-interaction research, P5 evidence и prospective measurement protocol. Они должны быть fresh-reconciled как более поздний HQ delta до любого profile execution.

ARH continuity triage:

puev5691/wellbeing-hq@997fe4b020afe2a14c95313a9bf5c97862be00f5:
entities/archivarius/outbox/ARH__vol-continuity-recovery-triage-r01__KOO.md

blob:
ff8bff197112ce9e7f4d8a6086dc72b72a7afbde

terminal:
PASS_ARH_VOL_CONTINUITY_RECOVERY_TRIAGE_R01_WITH_BOUNDARIES

Контекст последнего истощённого чата сохранён отдельно только как CONTEXT_ONLY evidence:

puev5691/wellbeing-hq@9465a7f5971a33a49326090b395645730d172111:
entities/koordinator/evidence/VOL__exhausted-chat-context-candidate__CONTEXT_ONLY.md

blob:
9dc84eedc0e4cc1256f4d1e72c28c300aa2b76e5

status:
CHAT_CONTEXT_CANDIDATE / NOT_VOL_SELF_SNAPSHOT / NOT_CANONICAL_RECOVERY

Этот файл:
- не устанавливает identity;
- не устанавливает current-writer;
- не является recovery;
- не создаёт task authority;
- не доказывает публикацию/принятие обсуждавшихся материалов;
- может использоваться только как bounded conversation context.

Required cold-start procedure:

1. Fresh-preflight puev5691/wellbeing-hq.

2. Загрузи и независимо проверь текущие approved Project Sources:
   - project-instructions-core v2.5 — blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33
   - entity-roles-short v2.4 — blob 1772339cb74dae8550bfbd2e33401c34a929e911
   - entity-state-preservation-and-recovery-canon v1.6 — blob 233117e1c9509d730e1f5ec532b1cabe3f786609
   - file-work-canon-universal v2.4 — blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2
   - source-loading-policy v2.2 — blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf
   - task-conveyor-canon v1.2 — blob df7896d867eeeffff506319538fedad938856686

3. Проверяй recovery по exact immutable commit f6ff070313caff5d7b5d12779d4bb8d8eb0eec01, а не по mutable main.

4. Проверь manifest, состав recovery, sha256sums и exact blobs/bytes настолько, насколько требует текущий recovery-канон.

5. Проверь independent ARH preservation result и exact emergency-failover authority выше.

6. Fresh-reconcile:
   - VOL current/writer evidence;
   - VOL recovery/handoff/failover evidence;
   - VOL inbox/outbox/routes/receipts;
   - все поздние VOL terminal results после recovery boundary;
   - supersession между поздними результатами;
   - решения ОПЕРАТОРА и acceptance/review, где они есть.

7. Старый recovery используй только как recovery basis для identity/role/recovery procedure и подтверждённого исторического self-state.

8. Поздние HQ VOL artifacts не считай автоматически current/accepted только потому, что они новее. Проверяй exact acceptance/supersession.

9. Context-only файл используй только как контекст разговора. Ничего из него не повышай до authoritative VOL self-state без независимого подтверждения.

10. UNKNOWN оставляй UNKNOWN. Не реконструируй утраченное по памяти, plausibility или chronology.

11. Выполни initiation только.

12. Если initiation проходит, опубликуй один immutable initiation-result artifact в puev5691/wellbeing-hq, сделай exact readback и верни:
   - path;
   - commit;
   - blob;
   - status/terminal.

Expected result:

initiation_verified_waiting_writer_gate

или exact BLOCKED_* / FAIL_*.

STOP before Writer Gate.

До отдельного Writer Gate и отдельного Resume-First после него НЕ выполнять:
- profile work;
- historical task/PROMPT replay;
- constitution stress-test;
- COOP production action;
- WBN/WBNP accounting/monetary activation;
- token/ownership/governance activation;
- production/system mutation;
- Project Sources/canon mutation;
- external service mutation;
- automation mutation;
- memory-layering attempt 3.

Writer Gate нового VOL — отдельный последующий шаг и не разрешён этим PROMPT.

ДЕЙСТВИЕ ОПЕРАТОРА:
создать новый physical чат ВОЛОНТЁРА и передать этот PROMPT целиком.
