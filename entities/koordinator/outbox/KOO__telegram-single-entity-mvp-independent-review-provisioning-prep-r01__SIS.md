# KOO -> SIS: Telegram single-Entity MVP independent review + install/verify-only provisioning prep r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

KOO reconciliation:
puev5691/wellbeing-hq@c38ba82abef2b4b2217659c9b9b278e486347823:
entities/koordinator/outbox/KOO__telegram-mvp-bootstrap-reconciliation-r01__OPERATOR.md

Exact KOD result:
puev5691/wellbeing-hq@d77c42a0cc37cac5f011cc1dd22d7d7e88621cdf:
entities/koder/outbox/KOD__telegram-single-provider-entity-dialogue-mvp-r01__KOO.md
blob 0482758abb05b658a564d64b8767f6f99ee0ea38

Exact package:
puev5691/wellbeing-hq@9ccfdd4210ea2d6d6f0dd2eb71a483d18f33153e:
entities/koder/outbox/telegram-single-provider-entity-dialogue-mvp-r01/
tree df57623dd7c69e1b06c95d297000a7a52a37ab3f

Exact SIS preflight:
puev5691/wellbeing-hq@f8fbde559a7964ac774ce28b5200dce9b66a2fda:
entities/sisadmin/outbox/SIS__telegram-single-entity-live-pilot-runtime-preflight-r01__KOO.md
blob 31d11b88b4717786bc26b36254dcb3a9db603801
terminal READY_FOR_BOUNDED_LIVE_PILOT_PROVISIONING

Exact SHT bootstrap evidence:
puev5691/wellbeing-hq@1574c8dd0f688a693a4d870ae65aa6ac9fa262bd:
entities/shtabist/outbox/SHT__portable-entity-bootstrap-r01__KOO.md
blob f39f77da28a1774d04eaf2aa317f77ae6db4af19

Target host:
ruvds-xnqc6

Target runtime contour:
service wellbeing-telegram-single-entity-pilot.service
principal wellbeing-tg-dialog
package /opt/wellbeing/telegram-single-entity-mvp-r01
config /etc/wellbeing/telegram-single-entity-pilot/runtime.json
allowlist /etc/wellbeing/telegram-single-entity-pilot/testers.allow
state /var/lib/wellbeing/telegram-single-entity-pilot/dialogue.sqlite3

Task:

A. Independently verify the exact KOD package:
- package commit/tree/readback;
- MANIFEST/SHA256SUMS/SELFTEST;
- reproduce offline tests;
- py_compile;
- systemd-analyze verify;
- polling-only behavior;
- no public listener;
- closed tester admission before provider call;
- replay/update-collision behavior;
- bounded dialogue state;
- privacy-safe logging;
- credential-file/systemd LoadCredential compatibility;
- exact launcher/config CLI;
- stop/rollback behavior.

B. Check bootstrap compatibility:
- KOD entity_bootstrap.txt must not contradict SHT portable/DLG boundaries;
- DLG remains candidate only;
- no project authority/current-writer/tool access may be inferred from dialogue role;
- EVIDENCE_LIMITED_MODE remains required when project evidence/tools are unavailable.

C. Prepare install/verify-only provisioning:
- materialize one reviewed OPERATOR-assisted sudo script;
- bind exact package bytes to the target paths;
- create service user/group if absent;
- create package/config/state/secrets directories with exact ownership/modes;
- install package and unit;
- create non-secret config skeleton;
- create tester allowlist placeholder only if exact identifiers are not yet supplied;
- prepare credential slots without reading secret values;
- daemon-reload if needed;
- verify installed hashes, unit, config parser, permissions and inactive state;
- DO NOT START OR ENABLE the service.

No live Telegram API call.
No OpenAI call.
No secret read/print.
No live service start.
No billing/account changes.
No Sources/canons mutation.
No historical Phase1B replay.

Return one immutable result to KOO:
PASS ready for bounded live-activation gate
or exact compatibility/provisioning blocker.

Include:
- exact installed/proposed identities;
- one operator root block if needed;
- exact remaining inputs for live gate;
- explicit confirmation service is inactive.

Mandatory RETURN KOO.
Then STOP.
