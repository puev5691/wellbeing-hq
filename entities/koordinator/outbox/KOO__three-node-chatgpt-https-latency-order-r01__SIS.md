# KOO → SIS: three-node HTTPS latency ordering r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: BOUNDED_READ_ONLY_NETWORK_MEASUREMENT
project_time: omitted

## Authority

Use OPERATOR decision:

puev5691/wellbeing-hq@bc5de8ade8ca98a5042b15714198bc1af47c6fc4:
entities/koordinator/outbox/KOO__select-s1-f2-node-failure-and-openai-latency-order-r01__OPERATOR.md

## Nodes

- erefia / ruvds-ygo0w
- burzh / ruvds-xnqc6
- mazhor / p552203.kvmvps

## Measurement target

Use one common target:
https://chatgpt.com/

Purpose:
practical relative ordering of nodes for administration proximity.

This is a proxy metric only; it is not a claim about full end-to-end control-channel latency or SLA.

## Measurement method

For each node:

1. Resume-First and verify exact node identity before measurement.
2. Read-only network measurement only.
3. Perform repeated HTTPS connection timing to the same target.
4. Prefer a simple reproducible client such as curl, capturing at minimum:
   - DNS lookup time;
   - TCP connect time;
   - TLS handshake/appconnect time;
   - time to first byte or total time if available.
5. Use the same command/options and sample count on all three nodes.
6. Minimum 10 samples per node if practical.
7. Report median for the primary comparison; also report min/max and any failures.
8. If chatgpt.com is unreachable or measurement method is not comparable across all three, STOP and return exact blocker rather than substituting a different target silently.

## Result

Return one concise table:
node | successful samples | median connect/appconnect | min | max | notes

Then rank:
1 = lowest median latency
2 = next
3 = highest

Do not overinterpret small differences if they are within obvious jitter/noise.

## Prohibited

- package installation;
- service/config changes;
- firewall changes;
- provider API;
- credentials/secrets;
- shard WRITE;
- deployment;
- Memory-layering attempt 3.

Expected terminal:
PASS_SIS_THREE_NODE_CHATGPT_HTTPS_LATENCY_ORDER_R01
or exact BLOCKED_* / FAIL_*.

After one immutable result and addressed return to KOO, STOP.
