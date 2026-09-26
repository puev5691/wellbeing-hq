# KOO → SIS: fixed-IP administration routing design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: BOUNDED_DOCUMENT_ONLY_ROUTING_DESIGN
project_time: omitted

## Authority

OPERATOR decision:
puev5691/wellbeing-hq@06e7ca126548b9423ca24c968559c927bf0aafed:
entities/koordinator/outbox/KOO__fixed-ip-administration-routing-design-decision-r01__OPERATOR.md

## Current measured order

PRIMARY:
burzh / ruvds-xnqc6

SECONDARY:
mazhor / p552203.kvmvps

TERTIARY:
erefia / ruvds-ygo0w

Current validated ChatGPT test IP set:
- 104.18.32.47
- 172.64.155.209

## Required design

Prepare one concise document describing how administration traffic should use fixed IP transport while preserving:
- TLS SNI = chatgpt.com
- HTTP Host = chatgpt.com
- certificate validation for chatgpt.com

Design must cover:

1. How the current IP set is stored and versioned.
2. How an IP is health-checked without DNS.
3. How node priority is applied:
   burzh → mazhor → erefia.
4. When to fail over from one node to the next.
5. How to distinguish:
   - target IP failure;
   - node failure;
   - TLS/certificate failure;
   - HTTP application response.
6. How to handle current IP becoming invalid/stale.
7. How a new IP can be admitted:
   - discovered separately;
   - verified against chatgpt.com TLS/SNI;
   - recorded as a successor;
   - never silently replacing the current list.
8. Whether two IPs should be tried in-order or health-selected.
9. Exact manual fallback if all configured IPs fail.
10. What evidence would later be required before automatic failover deployment.

Keep design implementation-neutral.

## Boundaries

No deployment.
No host/config mutation.
No DNS changes.
No provider/API access.
No credential/secret access.
No shard WRITE.
No automation mutation.
No Project Sources/canon mutation.
No CHECKPOINT_DURABLE claim.
No resume authority.
No Memory-layering attempt 3.

Expected terminal:
PASS_SIS_FIXED_IP_ADMINISTRATION_ROUTING_DESIGN_R01_DOCUMENT_ONLY
or exact BLOCKED_* / FAIL_*.

After one immutable result and addressed return to KOO, STOP.
