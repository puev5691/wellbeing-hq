# KOO record: OPERATOR chooses fixed-IP transport for administration routing design

status: OPERATOR_FIXED_IP_ROUTING_DESIGN_DECISION_RECORDED
project_time: omitted

OPERATOR decision:

Проектировать работу именно с использованием IP адресов.

Interpretation for HTTPS/TLS:

- transport destination uses fixed IP addresses;
- TLS SNI remains chatgpt.com;
- HTTP Host remains chatgpt.com;
- certificate validation remains for chatgpt.com;
- DNS is excluded from the normal measured/selected transport path;
- raw https://<IP>/ without correct hostname/SNI is NOT the intended design.

Validated current test IPs:
- 104.18.32.47
- 172.64.155.209

Exact measurement evidence:
puev5691/wellbeing-hq@4f07ba64212a78d7e18d44089292b5838475649e:
entities/sisadmin/outbox/SIS__three-node-chatgpt-https-latency-by-ip-r01__KOO.md
blob a9285466f6541d347309902d21537d2e3c77a0f4

Measured practical administration order by combined fixed-IP TLS median:
1. burzh / ruvds-xnqc6 — 47.336 ms
2. mazhor / p552203.kvmvps — 51.821 ms
3. erefia / ruvds-ygo0w — 87.918 ms

Operational interpretation:
PRIMARY = burzh
SECONDARY = mazhor
TERTIARY = erefia

Burzh and mazhor are near-tie; ordinary route jitter may swap them. Current ordering follows the measured median as requested.

This decision supersedes hostname/DNS-inclusive latency as the design basis for administration ordering.

This decision authorizes document design around fixed-IP transport only.
It does NOT by itself authorize deployment, automatic failover, host mutation, shard WRITE, credential changes, CHECKPOINT_DURABLE, or resume authority.

Fixed IP currentness/change handling must be designed explicitly before implementation. Do not assume these IPs are permanent.
