# SIS → KOO: three-node ChatGPT HTTPS latency ordering r0.1 — resumed after Erefia access restore

terminal: PASS_SIS_THREE_NODE_CHATGPT_HTTPS_LATENCY_ORDER_R01
scope: BOUNDED_READ_ONLY_NETWORK_MEASUREMENT
project_time: omitted

## TASK

Exact KOO task:
puev5691/wellbeing-hq@418dd00a9ea5bda8557d6ffda459eb1fe1f15a7c:
entities/koordinator/outbox/KOO__three-node-chatgpt-https-latency-order-r01__SIS.md

OPERATOR decision:
puev5691/wellbeing-hq@bc5de8ade8ca98a5042b15714198bc1af47c6fc4:
entities/koordinator/outbox/KOO__select-s1-f2-node-failure-and-openai-latency-order-r01__OPERATOR.md
blob:
69731dc72de85f937a88eda310b99bd944682b4c

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

Fresh HEAD before resumed measurement:
750304e7091c74ac6ff656566f90b3b115b354b3

Historical blocker result preserved:
puev5691/wellbeing-hq@c445151de3a5efdc664e29ec024d88dae2f216d3:
entities/sisadmin/outbox/SIS__three-node-chatgpt-https-latency-order-r01__KOO.md
blob:
e1b7968c02d65665fe883aed43bce41413b2613b
terminal:
BLOCKED_SIS_THREE_NODE_CHATGPT_HTTPS_LATENCY_ORDER_R01_EREFIA_OFFLINE

That blocker referred to Remote Desktop execution-path unavailability, not proof the VPS itself was offline.
After OPERATOR restored exact Erefia Remote Desktop access and explicitly told SIS to continue, the original measurement task was resumed.
No automatic retry is claimed.

## ACTION

Target:
https://chatgpt.com/

Same command/options on all three nodes:

curl -sS -o /dev/null --connect-timeout 10 --max-time 20 -w "%{time_namelookup},%{time_connect},%{time_appconnect},%{time_starttransfer},%{time_total},%{http_code}" https://chatgpt.com/

Sample count:
10 per node.

Measured nodes:
- erefia / ruvds-ygo0w
- burzh / ruvds-xnqc6
- mazhor / p552203.kvmvps

All three exact Remote Desktop devices were online before execution.

No credentials, cookies or project secrets were used.

## RAW RESULT SUMMARY

All 30 curl invocations:
- curl_exit = 0
- HTTPS/TLS connection completed
- HTTP response code = 403

HTTP 403 is treated only as application-layer response evidence.
It does not invalidate the connection/TLS timing comparison.

### erefia / ruvds-ygo0w

10/10 successful curl executions.

DNS seconds:
0.038665
5.024467
5.021893
0.038273
5.026402
5.023731
5.019037
0.891960
5.019252
0.032755

TCP connect seconds:
0.078307
5.059785
5.068284
0.080886
5.049734
5.047288
5.039941
0.912699
5.067988
0.075022

TLS appconnect seconds:
0.127907
5.142236
5.141214
0.136911
5.109058
5.076209
5.070496
0.981612
5.126276
0.167237

Median DNS:
5.019145 s

Median TCP connect:
5.043615 s

Median TLS appconnect:
5.073353 s

TLS appconnect min:
0.127907 s

TLS appconnect max:
5.142236 s

Median total:
5.101228 s

Important note:
the dominant delay is DNS resolution. Several samples resolve quickly, but six samples are approximately 5 seconds at the DNS stage. Therefore this exact proxy metric is materially influenced by resolver behavior on Erefia.

### burzh / ruvds-xnqc6

10/10 successful curl executions.

Median DNS:
0.004634 s

Median TCP connect:
0.010202 s

Median TLS appconnect:
0.054366 s

TLS appconnect min:
0.039791 s

TLS appconnect max:
0.076305 s

Median total:
0.069404 s

### mazhor / p552203.kvmvps

10/10 successful curl executions.

Median DNS:
0.009771 s

Median TCP connect:
0.059811 s

Median TLS appconnect:
0.115004 s

TLS appconnect min:
0.105487 s

TLS appconnect max:
0.126353 s

Median total:
0.173135 s

## REQUIRED TABLE

| node | successful samples | median TCP / TLS appconnect | TLS min | TLS max | notes |
|---|---:|---:|---:|---:|---|
| burzh / ruvds-xnqc6 | 10/10 | 10.202 ms / 54.366 ms | 39.791 ms | 76.305 ms | stable; HTTP 403 after successful TLS |
| mazhor / p552203.kvmvps | 10/10 | 59.811 ms / 115.004 ms | 105.487 ms | 126.353 ms | stable; HTTP 403 after successful TLS |
| erefia / ruvds-ygo0w | 10/10 | 5043.615 ms / 5073.353 ms | 127.907 ms | 5142.236 ms | large DNS jitter/delay dominates median; HTTP 403 after successful TLS |

## RANKING

Primary comparison uses median TLS appconnect as required proxy metric.

1. burzh / ruvds-xnqc6
   median appconnect: 54.366 ms

2. mazhor / p552203.kvmvps
   median appconnect: 115.004 ms

3. erefia / ruvds-ygo0w
   median appconnect: 5073.353 ms

For the exact measured proxy metric:
BURZH < MAZHOR << EREFIA

## INTERPRETATION BOUNDARY

This is a practical relative ordering for administration proximity to the selected common target.

It is NOT:
- full end-to-end ChatGPT control-channel latency;
- OpenAI SLA;
- proof of geographic distance;
- proof of provider quality;
- proof of general Internet latency;
- checkpoint durability evidence;
- failover proof.

Erefia's third-place result is specifically dominated by DNS resolution behavior in this sample set.
Its minimum TLS appconnect was 127.907 ms, showing that when DNS resolves promptly its connection path is not intrinsically five seconds long.

Therefore:
- the exact task ranking is valid for the measured cumulative appconnect metric;
- a future DNS-focused diagnostic could explain the Erefia anomaly, but is NOT authorized by this result.

## CHECK

Comparable method:
PASS

Same target:
PASS

Same curl options:
PASS

Samples:
10 per node

Failures:
0 curl failures

HTTP status:
403 on all 30 requests

Ranking:
ESTABLISHED_FOR_THIS_PROXY_MEASUREMENT

## BOUNDARIES

Package installation:
0

Service/config mutation:
0

Firewall mutation:
0

Provider API:
0

Credentials/secrets:
0

Shard WRITE:
0

Deployment:
0

Memory-layering attempt 3:
NOT_AUTHORIZED

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Resume authority:
NOT_GRANTED

## EXPERIENCE

Идея → сравнить три узла одним одинаковым HTTPS proxy metric до ChatGPT.

Проба → 10 одинаковых curl measurements на каждом exact node с DNS/TCP/TLS/TTFB/total.

Результат → burzh уверенно первая, mazhor вторая, erefia третья по median cumulative TLS appconnect; у erefia почти весь разрыв создаёт DNS resolver delay около 5 секунд в большинстве samples.

Успех/неудача → measurement PASS; interpretation ограничена proxy metric.

Урок → иногда "сервер далеко" означает "резолвер пять секунд думает о смысле жизни". Поэтому cumulative latency полезна для практического выбора, но её компоненты нельзя путать.

## Terminal

PASS_SIS_THREE_NODE_CHATGPT_HTTPS_LATENCY_ORDER_R01

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
