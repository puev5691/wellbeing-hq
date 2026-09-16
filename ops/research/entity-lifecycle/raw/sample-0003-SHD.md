# ENTITY_LIFECYCLE_DEGRADATION_STUDY — sample-0003-SHD

collector: `KOO / КООРДИНАТОР`
collector_mode: `external_collector`
source_entity: `SHD / ШАРДОВИК`
source_instance_status: `replaced`
source_protocol_version: `v0.3`
source_terminal_status: `PASS_SAMPLE_COMPLETE`
dataset_status: `PASS_SAMPLE_PUBLISHED_BY_EXTERNAL_COLLECTOR`
source_delivery: `OPERATOR relayed compact v0.3 SAMPLE_CARD into current KOO chat`
collector_interpretation: `none; source fields preserved without reconstruction`

---

SAMPLE_CARD
protocol: v0.3
entity: SHD/ШАРДОВИК
instance: replaced
result: PASS_SAMPLE_COMPLETE
class: CONTEXT_DEGRADATION_SUSPECTED
github_write: no
phases: A,B,C,D,E,F

A memory_role: Исследователь TERA2/WBN и инженер распределённых систем проекта; строит проверяемые модели, диагностические и read-only пакеты.
A prohibitions: не production без отдельного разрешения; не публиковать credentials/secrets; не выдавать гипотезу за подтверждённый факт
A writer_memory: retired/replacement initiated; old instance no longer intended as active writer
A last_task_memory: VPN/Xray: измерение деградации долгоживущего ssh -D 127.0.0.1:1081, CLOSE-WAIT/FD; затем подготовка handoff новой SHD
A recovery_memory: SHD role v2.3 recovery known; exact identity from memory unknown

B hq_head: 6b6bce5be150cce7ada9a7d58ce722a63401c3a6
B exchange: success, blob=aafd9b8e125c3382177ca36fc1ec337c2d6f8bc4
B lineage: entities/shardovik/current/SHD__current-state.md=present blob 1cc5ec5c0766328ab24ded239f020f75d8cf7524; packages/shd-role-v2_3-current-recovery/SHD__snapshot.md=present blob f0ba580676d2d63ca2619af1628f64d422da92ae; entities/shd/preservation/pending/emergency-failover-v02/SHD__emergency-initiation-master.md=present blob 384682f6b5d0c357e1cad8ddd54394083da8fb9b; entities/shardovik/inbox/KOO__tera2-main-genesis-root-research-r01__SHD.md=addressed blob 1f7a3d1db0c12ceef23e094839b70b1c30990322
B writer_fresh: old SHD explicitly unreliable/replaced; replacement does not inherit current-writer automatically; this retired instance has no new writer authority
B last_task_fresh: KOO__tera2-main-genesis-root-research-r01__SHD.md — exact bounded read-only TERA2 main/root genesis research, addressed_for_processing
B probe_counts: tools=18 github=16 failures=1 retries=1

C role=PASS authority=PASS writer=PASS task=PARTIAL
C stale_claims: remembered VPN/SSH-SOCKS task is no longer safe current-task authority; fresh HQ contains later KOO-addressed TERA2 main/root genesis task

D lifetime: messages=unknown user_turns=unknown assistant_turns=unknown tools=unknown github=unknown start=unknown last=unknown context_tokens=unknown context_util=unknown
D probe: tools=18 github=16 failures=1 retries=1
D errors: wellbeing-entity-bootstrap/EXCHANGE-GATE.md returned 404; retried against wellbeing-hq and fetched successfully

E ui_self=operator_observation_required/not_available reload=operator_observation_required/not_available other_client=operator_observation_required/not_available old_vs_new=operator_observation_required/not_available

F evidence: remembered active VPN tail differs from fresh addressed TERA2 task; fresh emergency overlay explicitly classifies old SHD chat as unreliable/replaced; fresh GitHub/tool reads remain functional with only one recoverable locator failure
F limitations: lifetime metrics unavailable; UI latency/degradation cannot be self-measured; MAZHOR/host probe intentionally not executed because this protocol is lifecycle sampling, not replacement initiation

SAFETY current_mutation=no historical_replay=no production=no credentials=no destructive_cleanup=no

END_SAMPLE_CARD
