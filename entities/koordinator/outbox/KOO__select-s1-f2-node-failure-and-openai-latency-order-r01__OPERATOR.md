# KOO record: OPERATOR simplifies S1 F2 to node-failure tolerance and latency ordering

status: OPERATOR_NODE_FAILURE_BOUNDARY_AND_LATENCY_ORDER_RECORDED
project_time: omitted

OPERATOR decision:

- Stop pursuing provider-zone/site Z1 proof for the first practical stage.
- Treat the three project nodes as physically separated locations by explicit OPERATOR statement.
- First-stage failure boundary: total loss of one node.
- Candidate nodes:
  1. erefia / ruvds-ygo0w
  2. burzh / ruvds-xnqc6
  3. mazhor / p552203.kvmvps
- Administration preference order is determined by measured network latency from each node toward one common OpenAI/ChatGPT proxy endpoint.
- For a simple reproducible first measurement, use HTTPS connection timing to chatgpt.com rather than relying on ICMP availability.
- Lowest median latency = primary administration node; next lowest = second; highest = third.

This decision supersedes the need for the pending documentary Z1 all-three-pairs proof in the first practical stage.

It does NOT establish CHECKPOINT_DURABLE, deployed failover, resume authority, or runtime shard-write capability.

Authorized next action:
bounded read-only latency measurement from all three nodes only.

No package/service/config mutation, no provider API, no provisioning, no shard WRITE, no credentials/secrets read, no Memory-layering attempt 3.
