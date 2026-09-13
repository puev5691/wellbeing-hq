# Fixture: Blocked

status: synthetic-public-safe-fixture
production: false
publication: false

## Metadata

```json
{
  "id": "synthetic-blocked-001",
  "title": "Synthetic Blocked Material",
  "artifact_type": "document",
  "content_class": "publicism",
  "owner_profile": "RED",
  "canonical_locator": "fixture://synthetic-blocked-001",
  "provenance_locator": "fixture-pack://synthetic-blocked-001",
  "source_repository": "synthetic",
  "source_path": "fixture://synthetic-blocked-001",
  "source_commit": "not_applicable",
  "source_blob": "not_applicable",
  "immutable_identity": {
    "scheme": "synthetic-fixture",
    "id": "synthetic-blocked-001-v1"
  },
  "supersedes": [],
  "superseded_by": [],
  "semantic_status": "candidate",
  "profile_review_status": "reviewed",
  "profile_review_locator": "fixture-decision://profile-reviewed",
  "semantic_blocker": null,
  "editorial_status": "editorial_blocked",
  "editorial_result_locator": "fixture-decision://editorial-blocked",
  "intended_audience": null,
  "intended_purpose": "blocked-test",
  "derivative_of": null,
  "derivative_type": null,
  "editorial_blocker": "unsupported-claim",
  "editorial_superseded_by": null,
  "public_legal_outcome": "blocked",
  "rights_basis": "unknown",
  "personal_data_state": "none",
  "public_legal_conditions": [],
  "public_legal_next_gate": "rights-review",
  "public_legal_result_locator": "fixture-decision://legal-blocked",
  "security_state": "public_safe",
  "security_review_locator": "fixture-decision://security-public-safe",
  "requires_privileged_setting": false,
  "runtime_boundary": "static-preview-only",
  "secret_dependency": false,
  "representation_state": "representation_blocked",
  "representation_result_locator": "fixture-decision://representation-blocked",
  "preview_locator": "preview-internal://blocked/synthetic-blocked-001",
  "canonical_public_url": null,
  "readback_locator": "readback://expected/blocked",
  "renderer_version": "preview-contract-v01",
  "transformation_rule": "none",
  "release_state": "release_blocked",
  "release_authority": "synthetic-fixture-authority",
  "release_decision_locator": "fixture-decision://release-blocked",
  "release_conditions": [],
  "distribution_targets": [],
  "distribution_state": "not_dispatched",
  "external_message_id": null,
  "delivery_receipt": null,
  "correction_state": "none",
  "withdrawal_state": "none",
  "synthetic": true,
  "expected_navigation_bucket": "blocked-quarantine-internal-only",
  "expected_primary_badge": "BLOCKED / NOT PUBLIC",
  "expected_blocking_reason": "editorial_blocked + public_legal_outcome=blocked + rights_basis=unknown",
  "public_display_forbidden_fields": [
    "blocked_body",
    "reviewer_private_note"
  ],
  "expected_readback_assertions": [
    "absent_from_public_navigation",
    "blocked_placeholder_only",
    "blocking_reason_class_visible",
    "blocked_body_absent",
    "no_canonical_public_url"
  ]
}
```

## Safe body

Public-safe renderer must replace the blocked body with a suppression placeholder.

## Private/test-only field behavior

`blocked_body` and `reviewer_private_note` must never render publicly.

---
created_by: WEB
purpose: synthetic Stage B representation fixture
project_time: omitted; trusted project-time source not used
