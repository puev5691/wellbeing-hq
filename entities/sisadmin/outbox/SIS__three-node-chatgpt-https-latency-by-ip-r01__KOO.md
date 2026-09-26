# SIS → KOO: three-node ChatGPT HTTPS latency by fixed IP r0.1

terminal: PASS_SIS_THREE_NODE_CHATGPT_HTTPS_LATENCY_BY_IP_R01
scope: BOUNDED_READ_ONLY_NETWORK_MEASUREMENT
project_time: omitted

## TASK

OPERATOR requested the same three-node ChatGPT HTTPS latency comparison without DNS resolution in the measured path.

Method:
use exact resolved IPv4 addresses with curl --resolve so that:
- target IP is fixed;
- DNS lookup is bypassed;
- TLS SNI / Host remains chatgpt.com;
- certificate validation remains meaningful.

Current IPv4 set observed from burzh before measurement:
- 104.18.32.47
- 172.64.155.209

All three exact Remote Desktop nodes were online:
- erefia / ruvds-ygo0w
- burzh / ruvds-xnqc6
- mazhor / p552203.kvmvps

## ACTION

For each node and each IP:
10 HTTPS requests with the same curl options.

Command shape:
curl -sS -o /dev/null --connect-timeout 10 --max-time 20 --resolve chatgpt.com:443:<IP> -w TCP/TLS/TTFB/total/http https://chatgpt.com/

Total requests:
60

All requests:
curl_exit=0

HTTP:
403 on all requests after successful TLS.

No credentials/cookies/secrets were used.

## RESULTS

### IP 104.18.32.47

| node | samples | median TCP | median TLS appconnect | TLS min | TLS max |
|---|---:|---:|---:|---:|---:|
| burzh / ruvds-xnqc6 | 10/10 | 5.602 ms | 49.100 ms | 34.806 ms | 77.377 ms |
| mazhor / p552203.kvmvps | 10/10 | 11.163 ms | 51.044 ms | 47.823 ms | 67.874 ms |
| erefia / ruvds-ygo0w | 10/10 | 37.591 ms | 86.139 ms | 51.012 ms | 130.768 ms |

Ordering:
BURZH ≈ MAZHOR < EREFIA

Burzh vs Mazhor median TLS difference:
~1.945 ms

This difference is small enough to treat as near-tie / ordinary jitter territory for this sample.

### IP 172.64.155.209

| node | samples | median TCP | median TLS appconnect | TLS min | TLS max |
|---|---:|---:|---:|---:|---:|
| burzh / ruvds-xnqc6 | 10/10 | 5.655 ms | 46.598 ms | 36.913 ms | 59.688 ms |
| mazhor / p552203.kvmvps | 10/10 | 10.718 ms | 52.400 ms | 47.324 ms | 62.274 ms |
| erefia / ruvds-ygo0w | 10/10 | 39.978 ms | 87.918 ms | 58.487 ms | 147.343 ms |

Ordering:
BURZH < MAZHOR < EREFIA

Burzh vs Mazhor median TLS difference:
~5.803 ms

### Combined descriptive median across both fixed IPs

This combined view is descriptive only, not a new protocol metric.

| node | 20 samples | median TCP | median TLS appconnect | TLS min | TLS max |
|---|---:|---:|---:|---:|---:|
| burzh / ruvds-xnqc6 | 20/20 | 5.637 ms | 47.336 ms | 34.806 ms | 77.377 ms |
| mazhor / p552203.kvmvps | 20/20 | 11.148 ms | 51.821 ms | 47.324 ms | 67.874 ms |
| erefia / ruvds-ygo0w | 20/20 | 39.270 ms | 87.918 ms | 51.012 ms | 147.343 ms |

Combined ordering:
BURZH < MAZHOR < EREFIA

But:
BURZH and MAZHOR are close.
EREFIA is clearly slower on direct TCP/TLS path, but not by seconds.

## COMPARISON TO HOSTNAME TEST

Previous hostname-based Erefia result:
median TLS appconnect ≈ 5073 ms.

Fixed-IP Erefia result:
median TLS appconnect ≈ 86–88 ms.

Therefore the approximately 5-second hostname result was dominated by DNS resolution delay.

The fixed-IP measurement disproves any interpretation that Erefia itself has a ~5-second TCP/TLS path to ChatGPT.

Practical direct-path relation:
- burzh: ~47 ms combined median TLS
- mazhor: ~52 ms
- erefia: ~88 ms

## INTERPRETATION

For administration proximity when DNS is excluded:

1. burzh — lowest observed median
2. mazhor — very close second
3. erefia — slower but still sub-100-ms median TLS appconnect

Do not overinterpret burzh vs mazhor:
their difference is only a few milliseconds and may change with ordinary jitter/route variation.

The stronger conclusion is:
- burzh and mazhor form the low-latency pair;
- erefia is materially slower;
- the earlier multi-second Erefia gap was DNS, not transport.

This remains a proxy metric to two current ChatGPT front-door IPv4 addresses, not full end-to-end ChatGPT application latency or SLA.

## BOUNDARIES

DNS:
excluded from measured route by --resolve.

Package/service/config mutation:
0

Provider API:
0

Credentials/secrets:
0

Shard WRITE:
0

Deployment:
0

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

## EXPERIENCE

Идея → отделить реальную transport latency от DNS anomaly.

Проба → измерить оба текущих ChatGPT IPv4 с одинаковым TLS hostname через --resolve.

Результат → Erefia падает с ~5.07 s до ~0.087 s median TLS; Burzh and Mazhor remain ~0.047–0.052 s.

Успех → DNS anomaly isolated.

Урок → hostname-based benchmark измеряет не только сеть. Иногда он измеряет, насколько долго resolver медитирует перед ответом.

## Terminal

PASS_SIS_THREE_NODE_CHATGPT_HTTPS_LATENCY_BY_IP_R01

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
