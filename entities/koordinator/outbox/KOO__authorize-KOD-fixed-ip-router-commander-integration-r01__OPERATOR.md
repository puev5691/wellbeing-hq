# KOO record: OPERATOR authorizes fixed-IP router → Remote Desktop Commander integration r0.1

status: OPERATOR_AUTHORITY_RECORDED
project_time: omitted

Exact OPERATOR authority token:

AUTHORIZE_KOD_FIXED_IP_ROUTER_COMMANDER_INTEGRATION_R01_OPERATOR_ASSISTED

Purpose:
connect the already active fixed-IP/node-selection logic to the existing Remote Desktop Commander control path so project Entities can actually use the selected node for administration.

Current node mapping:
- burzh -> ruvds-xnqc6
- mazhor -> p552203.kvmvps
- erefia -> ruvds-ygo0w

Current node policy:
burzh -> mazhor -> erefia

Current fixed IP set:
- 104.18.32.47
- 172.64.155.209

Authorized scope:
- implementation/design of an operator-assisted integration adapter;
- exact mapping from logical node name to existing Commander device identity;
- explicit manual selection/invocation flow;
- bounded local/synthetic verification;
- no new credential acquisition;
- no provider/API integration;
- no automatic failover;
- no autonomous node switching;
- no automatic IP discovery/admission;
- no DNS fallback;
- no shard WRITE;
- no Project Sources/canon mutation;
- no resume authority;
- Memory-layering attempt 3 remains NOT_AUTHORIZED.

Important:
this authority does not by itself authorize arbitrary production commands on the three hosts.
The integration must preserve the authority boundary of each future profile task/action.
