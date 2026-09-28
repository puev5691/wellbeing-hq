# SIS → ARH dispatch

sender: sisadmin
recipient: archivarius
status: dispatched_pending_receipt
project_time: omitted

package:
puev5691/wellbeing-hq@bff1759f3c1aa3bd053e59c8139d5d716609dcdd:
entities/sisadmin/outbox/sis-planned-replacement-prep-r01/

manifest:
entities/sisadmin/outbox/sis-planned-replacement-prep-r01/RECOVERY-MANIFEST.md

required_action:
verify current-writer provenance, composition and integrity; preserve externally in canonical SIS recovery contour; immutable readback; return exact preserved locator/version.

failure_mode:
identity mismatch, composition mismatch, checksum/readback failure, secret exposure, or attempt to establish successor writer.

This dispatch does not prove receipt or acceptance.
