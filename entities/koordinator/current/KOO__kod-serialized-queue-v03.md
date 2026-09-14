# KOO — сериализованная очередь KOD v0.3

status: ACTIVE_WORKING_QUEUE
project_time: omitted; trusted project-time source not used

## Completed

1. `anthropic-direct-adapter-r01`
   - result: `PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`;
   - result commit: `1fece27e9a35954a55b8225adbcfa7c38d702dfb`;
   - KOO receipt: `395b58cc54f606dd5ee521e70c32dfa8bcddf968`.

2. `anthropic-live-transport-r01`
   - result: `PASS_ANTHROPIC_LIVE_TRANSPORT_READY_FOR_ACCOUNT_GATE`;
   - result commit: `f020d79563c691cec86e2fd70437ca9d2d2686cb`;
   - package commit: `48ea999e957242cbf472febecf5aa92889b67f13`;
   - KOO receipt: `e7564272a4fc0ddcf6c11e56f2b25c6639f0eed7`;
   - live request still NOT authorized.

## Active KOD lane

3. `info-entry-static-preview-E1-evidence-alignment-v03`
   - task: `entities/koordinator/outbox/KOO__info-entry-static-preview-E1-fix-v03__KOD.md`;
   - task commit: `ed84c8c379dc1ba450310fd6be46b2fa30e30fad`;
   - scope: exact E1 byte-reproducibility defect only;
   - representation semantics must not be reopened.

## READY_SERIALIZED after active lane

4. `activation-lineage-schema-F1-F2`
   - source: `entities/shtabist/outbox/SHT__activation-lineage-schema-org-review-v01__KOO.md`;
   - SHT verdict: `PASS_WITH_EXACT_SCHEMA_ORG_FIXES`;
   - F1: semantic records require non-null non-empty experiment/task IDs;
   - F2: `acceptance_status=PROVEN` requires `event_claim_verified=true`;
   - no validator/runtime/automation until this correction is independently rechecked.

5. `koder-sender-registry-sanitation`
   - original finding: `entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap__KOD.md`;
   - scope update r2: `entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md`;
   - preserve append-only history;
   - reconcile known stale receipt-state gaps including Anthropic adapter receipt F3;
   - no semantic state promotion beyond exact receipts.

## Waiting external gate

`anthropic-live-D0`
- technical adapter and live-capable transport are ready;
- state: `WAITING_OPERATOR_ACCOUNT_BILLING_KEY_AND_EXPLICIT_LIVE_D0_AUTHORIZATION`;
- KOD must not perform account/key/billing/live call work until that gate is explicitly opened.

## Rule

- one KOD current-writer lane at a time;
- fresh preflight after every result;
- inbox placement != RUNNING;
- no task may silently absorb a later lane;
- account/live gate is external to the KOD serialization queue until explicitly authorized.

This is a KOO working queue, not Project Source/canon.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: reconcile completed Anthropic transport and activate the next exact KOD lane
СТАТУС: active_working_queue
