# KOO → SIS: documentary Z1 check of all three candidate pairs r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: BOUNDED_DOCUMENTARY_PAIRWISE_Z1_CHECK
project_time: omitted

## Exact authority

Use the current OPERATOR authority record for:
AUTHORIZE_SIS_S1O2_F2_Z1_ALL_THREE_PAIRS_DOCUMENTARY_CHECK_R01

## Candidate pool

A. erefia — current known project host identity: ruvds-ygo0w
B. burzh — current known project host identity: ruvds-xnqc6
C. mazhor — current known project host identity: p552203.kvmvps

Evaluate all three pairs:
- erefia ↔ burzh
- erefia ↔ mazhor
- burzh ↔ mazhor

## Purpose

Determine, from documentary evidence only, whether any pair can be shown to belong to distinct provider availability zones or physical sites under provider-defined failure-domain semantics.

## Permitted evidence

1. Existing immutable project evidence.
2. Public authoritative provider documentation.
3. OPERATOR-provided personal-cabinet screenshots/exports/fields.
4. OPERATOR-provided support attestations.
5. Non-secret resource IDs and zone/site/location metadata.

## Required per-resource fields

For each candidate, collect if available:
- provider name;
- exact provider resource/server ID;
- product/service type;
- region/location;
- availability zone / datacenter / site / facility identifier;
- storage placement/failure-domain field if exposed;
- provider semantics/reference explaining what the zone/site field means;
- evidence locator/source;
- currentness/date/version if shown.

If a field is unavailable, mark UNKNOWN.

## Pairwise result

For each pair return one of:
- Z1_DOCUMENTARY_BASIS_PLAUSIBLE
- Z1_DOCUMENTARY_BASIS_NOT_ESTABLISHED
- Z1_DOCUMENTARY_BASIS_CONTRADICTED

Do not use names, public IPs, DNS, subnets, cities, latency or traceroute as proof of Z1 independence.

## Stop boundary

If personal-cabinet evidence is needed, state exactly which screen/field OPERATOR must provide.
Do not request credentials or account access.

No provider API, host access, runtime test, provisioning, shard WRITE, implementation or backend choice.

## Required output

One concise result addressed to KOO:
- per-resource evidence table;
- three pairwise conclusions;
- exact missing evidence for any unresolved pair;
- smallest next operator action.

Expected terminal:
PASS_SIS_S1O2_F2_Z1_ALL_THREE_PAIRS_DOCUMENTARY_CHECK_R01
or exact BLOCKED_* / FAIL_*.
