# ARH event-lineage — KOO inbox-lifecycle pilot preservation gap

status: `OPEN_DEPENDENCY_ROUTED`
project_time: omitted; trusted project-time source not used

## Evidence

- preflight boundary: `975dcce2395cfb376f9dd7c95d1a45d31aa3dd06`;
- observed pre-profile HEAD: `be412a8eb6eb3c5acd712dae71cec37f6c0e1a27`;
- new commits in preflight window: `23`;
- lifecycle creation: `a59ef213629502ecb3b9f480cba78f0bc57bc4f4`;
- active queue materialization: `4a77f3964c881440ec8853a5b38c2c010736c57e`;
- controlling ARH review: `1b6aab5e50c759a7027b3c5b370475fe35417eec`, blob `1f8217d29fcc294178734b303df756113066662a`.

## Finding

Materialized pilot preserves raw inbox and authority boundaries, but lifecycle event `KOO-Q-ARH-INBOX-LIFECYCLE-001` omits available immutable `source_commit/source_blob`; post-readback bounded intake cursor is also absent. This is a preservation/recovery completeness gap, not evidence that `active_count: 0` is semantically false.

## Routed correction

- result artifact commit: `7cd19cd4959caf725a75171194bc876a6ae4ad20`;
- dispatch commit: `8cd71e09c9a712f2c9a009fd2b0ea12fe4e358df`;
- KOO inbox locator commit: `3d521b83fd0eb647af7137045e77fb32934697c6`;
- sender registry commit: `e489feab396f75a6ad23371e1d8bbfbdb15140c6`;
- receipt: absent at lineage creation;
- acceptance: absent at lineage creation.

## Exact dependency

KOO, as writer-owner of its operational queue, must append bounded correction evidence and perform fresh readback/reconciliation. ARH must not rewrite KOO queue state on its behalf.

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: сохранить provenance и causality найденного preservation-gap и адресной передачи correction dependency
СТАТУС: open_dependency_routed
