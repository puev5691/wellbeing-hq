# KOO — сериализованная очередь KOD v0.2

status: ACTIVE_WORKING_QUEUE
project_time: omitted; trusted project-time source not used

## Completed

1. `anthropic-direct-adapter-r01`
   - result: `PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`;
   - result commit: `1fece27e9a35954a55b8225adbcfa7c38d702dfb`;
   - KOO receipt: `395b58cc54f606dd5ee521e70c32dfa8bcddf968`.

## Active KOD lane

2. `anthropic-live-transport-r01`
   - task: `entities/koordinator/outbox/KOO__anthropic-live-transport-r01__KOD.md`;
   - task commit: `00116e5003680fb4a33f18a0d5739bb9c3ac1fd0`;
   - reason: direct OPERATOR priority to begin Anthropic work; this prepares the last technical layer before account/key/billing/live gate;
   - live network call remains forbidden in this pass.

## READY_SERIALIZED after active lane

3. `info-entry-static-preview-E1-evidence-alignment`
   - source: `entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`;
   - remaining defect E1: committed readback report must become byte-reproducible from exact committed verifier output.

4. `activation-lineage-schema-F1-F2`
   - source: `entities/shtabist/outbox/SHT__activation-lineage-schema-org-review-v01__KOO.md`;
   - SHT verdict: `PASS_WITH_EXACT_SCHEMA_ORG_FIXES`;
   - F1: semantic records require non-null non-empty experiment/task IDs;
   - F2: PROVEN acceptance requires `event_claim_verified=true`.

5. `koder-sender-registry-sanitation`
   - source: `entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap__KOD.md`;
   - exact scope: append-only reconciliation only; no history rewrite.

## Rule

- KOD performs only one current-writer lane at a time;
- fresh preflight after each KOD result may reprioritize remaining lanes;
- no lane is considered RUNNING from inbox placement alone;
- service sanitation tail must not be lost behind profile work.

This is a KOO working queue, not Project Source/canon.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: сохранить строгую KOD current-writer serialization after Anthropic adapter completion
СТАТУС: active_working_queue
