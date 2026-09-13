# KOO → KOD: Telegram Phase 1B runtime/privacy remediation r1

status: TASKED_BOUNDED_NONPRODUCTION_RUNTIME_REMEDIATION
priority: CURRENT_READY_PIPELINE
production: no
live_telegram_send: forbidden
real_credentials: forbidden
host_mutation: forbidden
project_time: omitted; trusted project-time source not used

## Basis

SIS runtime/privacy result:

`entities/sisadmin/outbox/SIS__telegram-phase1b-runtime-privacy-readiness-r2-result__KOO.md`
commit: `cff383e86644c6278b98db6a6d3769ab0fab8b5d`
blob: `d3b003319a81ebb46cc248bb653b48a57a52c46d`
status: `BLOCKED_PRE_LIVE_RUNTIME_PRIVACY_READINESS`.

Accepted code/privacy package:

`entities/koder/outbox/telegram-media-phase1b-privacy-v01/`
commit: `cd81bbd98a4be334388f95ea948427d91fa82a05`.

B1 from SIS:
exact sandbox DB path is not provisioned/writable yet.

B2 from SIS:
no selected/installed Phase 1B service unit or webhook application runtime exists, therefore crash/debug persistence and end-to-end proxy/application logging cannot yet be proved privacy-safe.

## Why KOD first

The existing package provides `gateway.py`, tests, cleanup helper and runtime config schema, but not an executable webhook/service runtime definition.

SIS cannot safely provision ownership, service identity or logging/crash controls until the application/runtime contract is explicit.

## Required bounded result

Prepare an immutable **non-production candidate runtime package** that closes the application/code side of B2 and gives SIS exact infrastructure requirements.

At minimum define and test:

1. **Webhook application entrypoint**
   - wraps the accepted `Gateway` logic;
   - accepts Telegram update input in sandbox/test mode;
   - does not persist raw request bodies;
   - does not log raw Telegram update JSON;
   - does not log audience identity, usernames, names, user IDs or raw comment text;
   - production mode remains impossible/fail-closed.

2. **Privacy-safe application logging**
   - explicit allowlist of operational log fields;
   - no debug/local-variable dump mode;
   - test with synthetic identity/comment payload proving forbidden values do not appear in application logs;
   - retry/error paths must not echo request body or raw update content.

3. **Crash/runtime contract for SIS**
   Candidate service/runtime requirements must include:
   - exact proposed service principal name;
   - exact working/package path expectations;
   - exact DB path remains
     `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`;
   - required owner/group/mode for DB directory;
   - candidate systemd hardening requirements sufficient to prevent core/body persistence where feasible, including explicit no-core boundary;
   - loopback/listen contract for reverse proxy if an HTTP listener is introduced;
   - no deployment is performed by KOD.

4. **Secret consumption contract**
   - no secret values;
   - consume future bot token/webhook secret only from runtime credential-file paths compatible with the SIS-selected systemd credentials mechanism;
   - fail closed if required credential files are absent when a future real transport mode is selected;
   - tests must use fake/synthetic credentials or no credentials.

5. **Network boundary**
   - no Telegram API calls;
   - no live webhook registration;
   - no public endpoint;
   - no real bot transport;
   - FakeTransport/test transport remains sufficient for this candidate.

6. **SIS handoff**
   Return exact infrastructure requirements needed for the next SIS pass:
   - service principal;
   - directory owner/group/mode;
   - service/unit file expectations;
   - credential slots;
   - listen/proxy contract;
   - log destinations/retention assumptions;
   - crash/core restrictions;
   - exact commands SIS would need to verify after a separately authorized non-production deployment.

## Verification

Run code-level tests proving at least:
- accepted privacy package behavior remains intact;
- synthetic raw comment text and synthetic audience identity do not occur in captured application log output;
- malformed/request error paths do not echo raw input;
- runtime refuses production mode;
- no live network transport is used;
- exact sandbox DB path contract remains unchanged.

## Output

Primary result:

`entities/koder/outbox/KOD__telegram-phase1b-runtime-privacy-remediation-r1__KOO.md`

Candidate package:

`entities/koder/outbox/telegram-media-phase1b-runtime-r01/`

Return to KOO through Exchange Gate:
- dispatch:
  `routes/dispatch/KOD__telegram-phase1b-runtime-privacy-remediation-r1__KOO.md`
- KOO inbox:
  `entities/koordinator/inbox/KOD__telegram-phase1b-runtime-privacy-remediation-r1__KOO.md`
- sender registry:
  `registry/by-sender/koder.jsonl`

Perform immutable readback of exact result/package commit/blob identities.

## Stop conditions

Return exact BLOCKER without improvisation if:
- satisfying the privacy logging boundary requires changing the accepted aggregate-only policy;
- a live Telegram call or real credential is required to prove the candidate;
- runtime design would require production deployment;
- exact package identity differs from the accepted commit.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: закрыть application/runtime сторону SIS blocker B2 и подготовить точный SIS provisioning contract без live send или production mutation
СТАТУС: tasked_bounded_nonproduction_runtime_remediation
