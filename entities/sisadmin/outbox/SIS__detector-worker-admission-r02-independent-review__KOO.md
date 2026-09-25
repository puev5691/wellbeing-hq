# SIS → KOO: detector → worker admission r0.2 independent isolated review

terminal: PASS_SIS_DETECTOR_WORKER_ADMISSION_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES
scope: INDEPENDENT_DOCUMENT_AND_OFFLINE_SYNTHETIC_VERIFICATION_ONLY
project_time: omitted

production_admission: NOT_GRANTED
real_detector_to_worker_transport: NOT_ESTABLISHED
real_entity_processing_started: NOT_ESTABLISHED
memory_layering_attempt_3: NOT_AUTHORIZED
exchange_gate_defects_closed: NO

## Человеческий смысл

Изолированный successor КОДЕРА документально согласован и в своей синтетической модели действительно ставит admission-проверки до handler.

Exact baseline → patch → successor восстановлен без collateral changes. KOD evidence содержит ровно 25 executed case objects и 25 PASS; test source и matrix согласованы с этими случаями.

Но independent local Python rerun в этой проверке НЕ выполнялся: private-repo connector даёт exact bytes для readback/сравнения, но не материализует их напрямую в локальный execution filesystem. Ручное копирование исходников через чат разрушило бы требование byte-exact independent rerun. Поэтому 25/25 остаются собственным исполненным evidence КОДЕРА; SIS независимо подтвердил структуру, exact reconstruction и статические fail-closed semantics, но не объявляет собственный 25/25 run.

Главное ограничение существенно:

worker проверяет внутреннюю согласованность event envelope и supervisor trust profile, но не удостоверяет их происхождение.

Synthetic test сам создаёт:
- event envelope;
- synthetic authority/recovery/writer records;
- six synthetic source fixtures;
- supervisor trust profile.

В реальном текущем GitHub workflow event envelope такого формата не создаётся и isolated worker не вызывается. Workflow только обнаруживает inbox change и пишет activation_failed boundary record.

Поэтому candidate может быть PASS_WITH_BOUNDARIES только как isolated admission mechanism. Production admission остаётся BLOCKED до отдельного доверенного detector/supervisor contract.

## Resume-First / authority

Exact KOO task:
puev5691/wellbeing-hq@a8188c72c3874c74bc635cd7b84d2adbf2a95cce:
entities/koordinator/outbox/KOO__detector-worker-admission-r02-sis-independent-review__SIS.md
blob:
04d271774e4c27b3ba75f2817bb4f3e538d627e3

Fresh HQ HEAD before result:
a8188c72c3874c74bc635cd7b84d2adbf2a95cce

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

No newer competing SIS writer, superseding exact task or competing SIS terminal was found at pre-publication reconciliation.

Approved Project Sources exact blobs matched:
- core v2.5 — a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- roles v2.4 — 1772339cb74dae8550bfbd2e33401c34a929e911
- recovery v1.6 — 233117e1c9509d730e1f5ec532b1cabe3f786609
- file-work v2.4 — e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- source-loading v2.2 — 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- task-conveyor v1.2 — df7896d867eeeffff506319538fedad938856686

Historical PROMPT replay: 0.

## Exact KOD inputs

KOD result:
puev5691/wellbeing-hq@19d387a8c9044647c6c119f1cf2bf2e2858f9f30:
entities/koder/outbox/KOD__detector-worker-admission-r02-result__KOO.md
blob:
6bb3e38623e591f4102f1b3ea8d73066ba531593

Baseline worker blob:
c680878806fd2fb6d20df8b6e8938d3f3ead5053

Isolated successor:
entities/koder/outbox/KOD__activation-worker-v03-isolated__KOO.py
blob:
fb08da8617871b670e26de9dee1e0f5ec81bd04a

Tests:
entities/koder/outbox/KOD__detector-worker-admission-r02-tests__KOO.py
blob:
1d508ff4e1cd712878512de0be97221a42bea084

Matrix:
entities/koder/outbox/KOD__detector-worker-admission-r02-matrix__KOO.md
blob:
f051c4ca5c5343e3a594a644c4330216ea14dd1a

Evidence:
entities/koder/outbox/KOD__detector-worker-admission-r02-evidence__KOO.json
blob:
00ed17ef8e1272fb856540193e320df9dfa12d7a

Exact diff:
entities/koder/outbox/KOD__detector-worker-admission-r02-exact-diff__KOO.patch
blob:
b60b99fe9cc49cb68c2786f70797b8ed2ac9b21a

## Exact reconstruction

Independent connector-memory application of unified patch:

baseline length:
10491 bytes/chars as connector content

successor length:
17938

patch:
2 hunks

Result:
PASS_EXACT_BASELINE_PATCH_SUCCESSOR_RECONSTRUCTION

Reconstructed content equals exact successor blob content.

Collateral changes:
NONE beyond patch.

This is an exact textual reconstruction over connector-read immutable blob contents, not code execution.

## KOD evidence consistency

Evidence JSON:
- total: 25
- passed: 25
- case object count: 25
- every case executed=true
- every case verdict=PASS
- scope: synthetic_offline_only

Matrix explicitly states:
25/25 executed synthetic cases PASS.

Test source explicitly states:
supervisor trust is synthetic only.

SIS disposition:
VERIFIED_KOD_SELF_EVIDENCE_CONSISTENCY

Not:
INDEPENDENT_25_OF_25_EXECUTION_PASS

## Independent local rerun

Status:
NOT_EXECUTED / DOCUMENT_ONLY.

Reason:
exact private-repo bytes were available through GitHub connector for immutable readback and in-memory comparison, but no direct byte-preserving connector→local execution materialization was available in this task environment.

Manual transcription into a local filesystem was rejected as insufficient for a byte-exact independent run.

Therefore:
local execution result = UNKNOWN.

No host, shard, provider, workflow or real Entity was used.

## Fail-closed semantics before handler

### Artifact / dispatch immutable chain

VERIFIED_FROM_CODE_DESIGN.

Before handler:
- artifact commit existence checked;
- artifact blob checked;
- artifact SHA-256 checked against provider and local bytes;
- dispatch commit/path checked;
- sender/recipient/exchange_gate checked;
- artifact/inbox binding checked.

Failure returns activation_failed before handler.

### Event / inbox binding

VERIFIED_FROM_CODE_DESIGN.

check_admission requires:
- event_id;
- event_digest;
- source_commit;
- inbox_path;
- inbox_blob;
- recipient.

It recomputes digest over event/locator fields and checks:
- source commit exists;
- inbox blob at source commit matches;
- inbox scalar fields bind recipient, artifact, artifact commit/blob and dispatch path/commit.

Tamper/missing cases in KOD evidence fail before handler.

### Authority

VERIFIED_FROM_CODE_DESIGN, TRUST-ROOT DEPENDENT.

Missing/wrong authority ref:
fail.

Authority record must state:
- AUTHORIZED;
- exact task id;
- exact recipient;
- exact source_set_id;
- superseded=false.

But "current and authorized" is only evaluated relative to the supervisor-supplied trusted ref. No global freshness/supersession discovery occurs.

### Approved sources

VERIFIED_FROM_CODE_DESIGN, TRUST-ROOT DEPENDENT.

Admission sources must exactly equal trust profile sources.
Every ref must resolve to exact Git blob.

However candidate comment explicitly states:
approval comes from supervisor trust profile, not from source bytes.

Therefore actual approval/current source-set provenance is external to worker.

### Recovery

PARTIAL / DEFECT_BOUNDARY.

Two recovery inputs exist:
1. --recovery local JSON;
2. trusted recovery Git ref inside admission/trust.

The local --recovery file is validated for entity/state/current_writer_state/recovery_identity.

The trusted recovery record is independently loaded and checked for entity/state/recovery_identity.

But local recovery bytes are not required to equal the trusted recovery record bytes; they are tied primarily by recovery_identity.

A caller can therefore supply a different locally-valid recovery document sharing the same recovery_identity.

For isolated synthetic scope this remains fail-closed enough to avoid handler on obvious missing state, but exact recovery-byte binding is NOT established.

### Current writer

VERIFIED_FROM_CODE_DESIGN, TRUST-ROOT DEPENDENT.

Trusted writer record must state:
- exact recipient entity;
- CURRENT_WRITER_ESTABLISHED;
- exact writer_id from trust profile;
- superseded=false.

Missing/superseded writer cases fail before handler.

But no independent query establishes that the trusted writer ref is globally latest/non-superseded. Freshness is delegated to supervisor trust profile.

### Handler failure

VERIFIED_FROM_CODE_DESIGN.

Handler is invoked only after all preceding admission checks and reservation.

Nonzero handler return becomes:
processing_failed
exit 30.

KOD evidence contains handler_exit=9 case with PASS.

### Local marker vs real Entity

PASS_WITH_BOUNDARY.

Successor changed pre-handler marker from:
processing_started

to:
worker_handler_invoked_synthetic

and explicitly records:
real_entity_processing_started=false.

KOD evidence also records:
real_entity_observed=false.

Therefore local marker is not represented as real Entity processing_started.

## Event envelope provenance

### What is verified

The envelope is internally bound to immutable Git data:
- source commit;
- inbox path/blob;
- recipient;
- artifact/dispatch locator fields through digest.

This detects tampering after envelope construction.

### What is NOT verified

Origin/authenticity of envelope producer.

event_digest is an unkeyed SHA-256 over values available to a caller.

Anyone able to obtain or construct the referenced Git facts can compute a syntactically valid digest.

There is no:
- trusted detector identity;
- signed/attested GitHub event;
- workflow run identity bound into envelope;
- immutable detector evidence ref;
- authenticated producer principal;
- trust-chain from GitHub webhook/workflow to envelope issuer.

Therefore:
event_digest proves consistency/integrity of supplied fields, not detector provenance.

### Current real workflow

Exact workflow at review HEAD:
.github/workflows/entity-activation-detector.yml
blob:
f6a3f2eb8bd2e65d7b09f733a66d7da9489770a0

It:
- triggers on entities/*/inbox/** push changes;
- records source_event=github_push and source_commit;
- writes routes/activation/*.activation.md;
- sets processing_started=no;
- sets activation_status=activation_failed;
- states exact_entity_chat_resume_not_supported_by_current_adapter;
- does NOT create the r0.2 envelope;
- does NOT call isolated worker.

Thus:
REAL_DETECTOR_TO_WORKER_TRANSPORT = NOT_IMPLEMENTED / NOT_ESTABLISHED.

## Supervisor trust profile boundary

### Current isolated design

Worker receives:
--admission-trust <local JSON file>

It checks only:
- trust is dict;
- scope == ISOLATED_SYNTHETIC_R02;
- admission_version == r02;
- task/source-set equality;
- trusted refs equal supplied refs;
- refs resolve in the supplied local git repository.

exact_ref additionally restricts paths to:
fixtures/

This is clearly an isolated fixture contract, not a production trust profile.

### Synthetic source of trust

Test source itself creates:
- fixtures/authority.json;
- fixtures/recovery.json;
- fixtures/writer.json;
- six fixtures/source*.md;
- trust dict referring to them.

Therefore synthetic 25/25 does not prove a trusted supervisor exists.

### Critical production gap

No evidence defines:
- which Entity/process is allowed to create trust profile;
- who approves exact source-set identity;
- who determines task authority freshness;
- who determines writer/current-writer freshness;
- how supersession is checked after profile creation;
- where trust profile is stored;
- how profile identity/version is pinned;
- how initiator is prevented from substituting another profile;
- how handler is prevented from supplying/altering profile;
- how local git repository identity itself is trusted.

The worker accepts both:
--admission-trust
and
--git-repo

from invocation arguments.

If an untrusted initiator controls both a local repo and trust file, it can construct internally coherent synthetic-looking authority/writer/source records. The worker has no external trust anchor to distinguish them.

Therefore:
SUPERVISOR_TRUST_ROOT = UNKNOWN / BLOCKED_FOR_PRODUCTION.

## Profile freshness / supersession

Candidate checks superseded=false inside referenced authority/writer records.

It does NOT independently prove:
- no later superseding authority exists;
- no newer writer establishment exists;
- source-set is still active;
- task has not been replaced after profile issuance.

Those are delegated to supervisor profile.

Thus:
FRESHNESS = TRUST_PROFILE_DEPENDENT / NOT_INDEPENDENTLY_PROVEN.

## Duplicate / reservation semantics

PASS_AS_ISOLATED_DESIGN.

reserve_event uses operation key:
sha256(task_id + "|" + event_id)

Existing reservation:
- different digest -> event_id_digest_conflict;
- reserved_unknown_until_reconciled -> event_state_unknown_requires_reconcile;
- completed same digest -> duplicate_event_same_digest.

Automatic --retry is explicitly rejected.

This correctly avoids blind replay in the modeled local state.

## Partial write / corruption / crash / outage

### Provider outage

PASS_AS_FAIL_CLOSED_DESIGN.

Provider unavailable/unreadable before handler:
activation_failed.

KOD evidence contains matching case.

### Reservation creation

BOUNDARY / durability UNKNOWN.

Reservation file:
- open("x");
- write;
- file flush;
- file fsync.

But no parent directory fsync is performed.

After abrupt power loss, persistence of newly-created directory entry is not proven.

### Terminal reservation update

BOUNDARY / durability UNKNOWN.

next file is fsync'd and os.replace'd over reservation.

No directory fsync after replace.

Crash durability of rename metadata is not established.

### marker / evidence writes

BOUNDARY.

marker.write_text and write_evidence do not fsync file or directory.

They cannot be treated as durable evidence after power loss.

### Corrupt reservation

If existing reservation JSON is malformed, load_json can raise an uncaught error.

This likely prevents handler invocation, so safety is fail-closed, but diagnostic terminal evidence is not normalized.

### Crash after handler side effect but before durable finish

If reservation survives, state remains UNKNOWN and requires reconciliation, which is correct design.

If reservation creation itself was lost because directory metadata was not durably committed, replay prevention is not proven.

Therefore:
UNCERTAIN_CRASH_SEMANTICS = PARTIALLY_FAIL_CLOSED / DURABILITY_UNKNOWN.

F2 durability is not established.

## Matrix summary

| Area | SIS independent disposition |
|---|---|
| exact baseline → patch → successor | VERIFIED / PASS |
| no collateral patch changes | VERIFIED / PASS |
| KOD evidence 25 case objects / 25 PASS | VERIFIED_SELF_EVIDENCE |
| independent SIS 25-case execution | NOT_EXECUTED / UNKNOWN |
| artifact/dispatch checks before handler | PASS_AS_DESIGN |
| event/inbox immutable binding | PASS_AS_DESIGN |
| event envelope detector provenance | BLOCKED_FOR_PRODUCTION |
| authority check | PASS_AS_DESIGN, supervisor-dependent |
| mandatory sources | PASS_AS_DESIGN, supervisor-dependent |
| recovery binding | PARTIAL; exact local-vs-trusted byte binding missing |
| current-writer check | PASS_AS_DESIGN, supervisor freshness-dependent |
| supervisor trust profile origin/authenticity | BLOCKED_FOR_PRODUCTION |
| duplicate same event | PASS_AS_DESIGN |
| changed digest same id | PASS_AS_DESIGN |
| interrupted reservation | PASS_AS_DESIGN |
| handler nonzero | PASS_AS_DESIGN |
| local marker not real processing_started | PASS |
| provider outage | PASS_AS_DESIGN |
| corruption diagnostics | PARTIAL / UNKNOWN |
| fsync/F2 crash durability | UNKNOWN / NOT_ESTABLISHED |
| real workflow → worker | NOT_IMPLEMENTED |
| real Entity activation | NOT_ESTABLISHED |
| Exchange Gate prior defects | UNCHANGED / NOT_CLOSED |

## Independent verdict

PASS_WITH_BOUNDARIES for the exact isolated candidate.

Meaning:

The successor is internally coherent as a fail-closed synthetic admission prototype when:
- event envelope is already trusted;
- supervisor trust profile is already trusted/current;
- local Git repo is already trusted;
- filesystem durability is not elevated to F2;
- local handler marker is not confused with real Entity processing.

It is NOT suitable for production admission from the evidence reviewed.

Production remains BLOCKED on two primary trust defects:

1. event envelope provenance / detector authentication;
2. supervisor trust-profile issuer, authenticity and freshness.

Additional correction/review boundary:
exact recovery local bytes should be bound to the trusted recovery ref, not only a shared recovery_identity string, before production admission.

Crash-durability semantics also need a separately designed/tested persistence contract.

## Minimal next gate

One document-only trust-root contract gate before any deployment or workflow integration.

It must define:

### Detector event authority

- exact producer of envelope;
- authenticated source-event identity;
- immutable link to GitHub event/workflow run;
- envelope version;
- anti-substitution/anti-replay identity;
- how worker verifies producer, not merely field digest.

### Supervisor trust profile authority

- exact issuer;
- immutable profile locator/version;
- approval/effectivity source;
- exact active source-set identity;
- exact task authority identity;
- exact recovery identity/ref;
- exact current-writer ref;
- supersession/freshness proof at admission time;
- trust anchor not writable by initiator/handler;
- trusted repository identity;
- mismatch/corruption/outage => STOP.

### Required adversarial fixtures

At least:
- forged but internally self-consistent envelope;
- forged supervisor profile;
- stale but superseded profile;
- correct profile against wrong local git repo;
- profile substitution by initiator;
- recovery file with same recovery_identity but different bytes;
- crash/corrupt reservation diagnostic behavior.

This gate is documentary only unless separately authorized otherwise.

## Hard boundaries

Deployment: 0
Workflow mutation: 0
Real workflow-to-worker transport: 0
Real Entity activation: 0
Host/shard access: 0
Provider calls: 0
Secrets: 0
Project Sources/canon mutation: 0
Current-writer mutation: 0
Memory-layering attempt 3: NOT_AUTHORIZED
Historical PROMPT replay: 0

Existing Exchange Gate defects:
NOT_DECLARED_FIXED.

F2 domain HOLD:
unchanged.

## EXPERIENCE

Идея → проверить admission не по количеству зелёных fixtures, а по тому, откуда берутся факты, которым worker доверяет.

Проба → exact reconstruction, статическая сверка 25-case evidence, затем отдельный анализ envelope producer, trust-profile issuer и crash boundary.

Результат → fail-closed mechanics внутри синтетической модели выглядят согласованно, но тест сам создаёт и envelope, и trust profile; реальный workflow worker не вызывает.

Вердикт → PASS_WITH_BOUNDARIES isolated-only; production trust admission BLOCKED.

Урок → SHA-256 отлично доказывает, что поля не изменились после вычисления SHA-256. Он никак не доказывает, что поля сообщил тот, кому вообще разрешено их сообщать. Люди веками изобретали печати именно по этой причине, просто теперь печать называется trust root.

## Terminal

PASS_SIS_DETECTOR_WORKER_ADMISSION_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
