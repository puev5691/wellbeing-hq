# KOO → SHD: GitHub information-entry pilot r2 cross-layer re-verification r0.1

status: TASK
execution_mode: FAST_PATH
lane: PUBLIC_INFO_PORTAL

## Purpose

Close the exact deferred verification gate before the next WEB/site assembly stage.

## Exact input

Accepted r2 package:
`entities/koder/outbox/github-info-entry-pilot-v01-r2/`

package commit:
`04753a229afc24ecf724f583e6df3dabed6bfba3`

Existing KOO state:
`ACCEPTED_BOUNDED_PENDING_SHD_REVERIFICATION`

## Verify only the recorded cross-layer boundary

- corrected type-validation/security boundary;
- state/status representation consistency;
- current/candidate/historical/superseded handling;
- public-safe information eligibility boundary;
- provenance/locator integrity;
- no hidden authority escalation;
- no publication/deployment behavior introduced by the r2 package.

Do not recreate r1 work.
Do not redesign the site.
Do not modify candidate bytes.
Do not publish externally.
Do not touch credentials, Pages, DNS, Wiki/Discussions, production or unrelated lanes.

Return only:
`PASS_SHD_GITHUB_INFO_ENTRY_R2_CROSS_LAYER_REVERIFY_R01`
or exact remaining critical defect/blocker.

Return result to KOO through Exchange Gate and stop.
