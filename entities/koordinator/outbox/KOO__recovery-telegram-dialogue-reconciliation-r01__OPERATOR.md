# KOO r1.0 — ARH/KOO recovery + SHT role + Telegram dialogue reconciliation r0.1

status: RECONCILED
project_time: omitted

## Human meaning

ARH and KOO recovery records are consistent once stages are separated.

ARH:
- recovery basis = arh-recovery-r03;
- current replacement initiation cycle = r0.4;
- current-writer artifact file generation = r0.3;
- exact current ARH instance is the one that created initiation r0.4;
- writer status = WRITER_ESTABLISHED.

KOO:
- base recovery r0.9 + delta r1.0;
- emergency replacement initiation r1.0 verified;
- separate Writer Gate established KOO r1.0 current-writer;
- historical task queue was not resumed by initiation or Writer Gate.

SHT:
- active role is process design/review for task/result lifecycle, handoff/failover/failure-state and recovery-process semantics;
- SHT is not the regular preservation executor and does not assume ARH custodial responsibility;
- SHT review/process participation does not make it author of another Entity self-snapshot or ARH preservation state.

## Active Project Sources

Latest active source-set activation found: r07.
No later complete source-set activation found.

Active global blobs:
- Project Core v2.5 — a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- Entity Roles v2.4 — 1772339cb74dae8550bfbd2e33401c34a929e911
- Source Loading Policy v2.2 — 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- Recovery Canon v1.6 — 233117e1c9509d730e1f5ec532b1cabe3f786609
- File Work Canon v2.4 — e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- Task Conveyor Canon v1.2 — df7896d867eeeffff506319538fedad938856686

Staged PRV source after r07 remains pending activation and does not replace this global set.

## Exact writers

KOO:
puev5691/wellbeing-hq@9c5e330719fa4410eca76e91a128bfcc29d56c45:
entities/koordinator/current/KOO__replacement-current-writer-r10.md
blob 8416e945418a4a86764edafbbd06682f6c84682b
status WRITER_ESTABLISHED.

ARH:
puev5691/wellbeing-hq@afe2a1d97cba7d0d489f8e9b935cc30554ac492c:
entities/archivarius/current/ARH__replacement-current-writer-r03.md
blob 3df64956a5ec4a21e11a4f469abaf91a1e4fd092
status WRITER_ESTABLISHED.
This artifact explicitly binds the current instance to initiation r0.4.

SHT:
puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da.

SIS:
current r0.7 established, blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59.

## Recovery stage separation

ARH sequence:
1. recovery r0.3 externally preserved;
2. new replacement instance initiation r0.4;
3. separate Writer Gate;
4. current-writer established.

The historical old cold-start r0.3 result belonged to the prior replacement cycle and is not the current initiation.

KOO sequence:
1. r0.9 recovery base externally preserved;
2. r1.0 delta externally preserved by ARH;
3. ARH prepared emergency cold-start after predecessor technical unavailability;
4. KOO r1.0 initiation verified;
5. separate Writer Gate established r1.0 current-writer;
6. later profile/task state requires fresh task-conveyor reconciliation and is not inherited from recovery.

No contradiction is established by numbering differences among recovery package, initiation cycle and writer artifact.

## Telegram dialogue state

Historical KOD admission correction:
entities/koder/outbox/KOD__telegram-single-entity-discussion-admission-correction-r01__KOO.md
blob 20063aa431721d702f3ad400b57878809f430d37
was an offline package ready for SIS review; it did not prove live dialogue.

More recent verified sequence supersedes that as current evidence:
- human tester provenance PASS;
- tester 6384602715 explicitly confirmed by OPERATOR;
- allowlist corrected and final live gate PASS;
- live r0.2 achieved two COMMITTED provider-backed replies but failed required same-thread continuity;
- read-only diagnosis proved conversation_key semantics and found OPERATOR_UI_PROCEDURE_MISMATCH, with exact placement evidence still insufficient;
- live r0.3 achieved one COMMITTED provider-backed reply, outbound message_id 106, but OPERATOR did not see it in the selected exact comments/thread view; service stopped cleanly;
- KOD then produced routing observability r0.1 candidate to preserve privacy-safe routing metadata.

Latest Telegram/KOD result:
puev5691/wellbeing-hq@b13efdd6fe32a72c4e8a0f58e2a009457b2e329b:
entities/koder/outbox/KOD__telegram-routing-observability-r01-result__KOO.md
blob 20aa087daec5497007b1cd307c36e17047156723
terminal PASS_KOD_TELEGRAM_ROUTING_OBSERVABILITY_R01_CANDIDATE_READY_FOR_SIS_REVIEW
status CANDIDATE_NOT_INSTALLED.

Package:
puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/
package tree bbe40dc80670b33594f997cea52e42508a7ae12b.

This package adds bounded routing metadata and offline tests only; no installation or live dialogue is proven by it.

## Media visitor need

Target remains:
publication/channel entry -> understandable Russian explanation -> voluntary dialogue -> expectation clarification -> suitable next step -> human handoff when needed.

This end-to-end visitor experience is NOT yet proven.

Distinguish:
- bot private chat;
- direct messages to channel;
- linked discussion supergroup.
Current validated runtime line is bound to linked discussion supergroup -1002429106148, not proof of a working private bot-chat or channel-DM visitor path.

## One next permissible step

Independent SIS review/install-readiness of the exact KOD routing-observability candidate.

Reason:
another live retry before this review/install boundary would repeat the visibility ambiguity. The KOD package is candidate-only and its own terminal names SIS independent review/install-readiness as the next gate.

No install and no live start in this next step.
