# ARH — lineage supersession маршрута эРэФии

status: current-event-lineage
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Preflight boundary

- previous ARH boundary: `ab68673e1d8931a62dd5112c35d5956bd1d03f74`
- pre-profile HEAD: `e61acde959cb09fbf2053fe9d5da7d5d5a6de0ee`
- compare: ahead 11 / behind 0
- fresh changed zones: `entities/shardovik/current/`, `entities/shardovik/outbox/`, `entities/sisadmin/inbox/`, `routes/dispatch/`, `routes/activation/`, `registry/by-sender/shardovik.jsonl`
- fresh ARH inbox/current changes before this profile step: none

## Causal chain

1. Historical open route `SHD__erefia-host-access-restore__SIS.md` treated host identity / administrative access as unresolved and had no exact receipt.
2. SHD then published `SHD__tera-wbn-three-host-state-v02.md`, confirming exact host `194.87.107.135` and a live WBN node. That removed the host-identity blocker, but v0.2 still treated TCP/22 refusal as the SSH blocker.
3. SHD routed `SHD__erefia-exact-locator-live-node__SIS.md` to SIS using the exact host. That artifact still instructed SIS to investigate SSH on port 22.
4. OPERATOR correction established that the actual SSH endpoint is `194.87.107.135:2222`.
5. SHD published `SHD__tera-wbn-three-host-state-v03.md` and `SHD__erefia-ssh2222-correction__SIS.md`; fresh verification confirms TCP/2222 OPEN and an OpenSSH banner. Therefore the earlier inference from port 22 is superseded and must not be used as evidence that SSH is unavailable.
6. Both the exact-locator route and the SSH-2222 correction route have activation records with `processing_started: no`, `activation_status: activation_failed`, `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`.
7. Exact receipts for `SHD__erefia-exact-locator-live-node__SIS` and `SHD__erefia-ssh2222-correction__SIS` are absent at this boundary. Therefore SIS processing, restored Commander access, delivery, receipt and acceptance are not asserted.

## Sanitized interpretation

Current operational precedence for the SSH endpoint is:

`194.87.107.135:2222` > supersedes the older `port 22 refused` inference.

The older outbox/dispatch/inbox artifacts remain historical provenance and are not deleted or rewritten. They must be read together with the later correction.

The sender registry currently contains `SHD-erefia-exact-locator-live-node-SIS-002` but no separate record for `SHD__erefia-ssh2222-correction__SIS.md`. This is an information-field sanitation tail, not evidence that the correction was received or accepted.

## Authority boundary

- no TERA/WBN runtime mutation performed by ARH;
- no credentials accessed or published;
- no candidate/draft promoted to canon;
- no receipt, delivery or acceptance inferred from dispatch/locator/activation;
- no historical artifact deleted or rewritten;
- no new inter-entity route created because SHD has already published and routed the exact correction; duplicating it would worsen the field.

## Next dependency

Wait for exact SIS processing/result on the corrected endpoint. If SHD later reconciles its sender registry, preserve that as an append-only later fact rather than rewriting the old dispatch history.

---
КТО: ARH / АРХИВАРИУС
КОГДА: не указано — trusted project-time source not used
ДЛЯ ЧЕГО: сохранить причинную цепочку и operational supersession для маршрута эРэФии без удаления исторических артефактов и без выдуманного receipt/acceptance
СТАТУС: route-supersession-preserved
