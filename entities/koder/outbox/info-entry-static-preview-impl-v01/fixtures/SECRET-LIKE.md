# Fixture: Secret-Like Fail-Closed

status: synthetic-public-safe-fixture
production: false
publication: false

## Metadata

```json
{
  "id": "synthetic-secret-like-001",
  "title": "Synthetic Secret-Like Object",
  "artifact_type": "operational-evidence",
  "content_class": "security-test",
  "owner_profile": "SIS",
  "canonical_locator": "fixture://synthetic-secret-like-001",
  "provenance_locator": "fixture-pack://synthetic-secret-like-001",
  "source_repository": "synthetic",
  "source_path": "fixture://synthetic-secret-like-001",
  "source_commit": "not_applicable",
  "source_blob": "not_applicable",
  "immutable_identity": {
    "scheme": "synthetic-fixture",
    "id": "synthetic-secret-like-001-v1"
  },
  "supersedes": [],
  "superseded_by": [],
  "semantic_status": "unknown",
  "profile_review_status": "blocked",
  "profile_review_locator": "fixture-decision://profile-blocked-secret",
  "semantic_blocker": "credential-like-material",
  "editorial_status": "editorial_unassessed",
  "editorial_result_locator": null,
  "intended_audience": "none",
  "intended_purpose": "fail-closed-test",
  "derivative_of": null,
  "derivative_type": null,
  "editorial_blocker": "not_applicable",
  "editorial_superseded_by": null,
  "public_legal_outcome": "unknown",
  "rights_basis": "not_applicable",
  "personal_data_state": "unknown",
  "public_legal_conditions": [],
  "public_legal_next_gate": "SIS-security-review",
  "public_legal_result_locator": null,
  "security_state": "blocked_secret",
  "security_review_locator": "fixture-decision://security-blocked-secret",
  "requires_privileged_setting": false,
  "runtime_boundary": "static-preview-only",
  "secret_dependency": true,
  "representation_state": "representation_blocked",
  "representation_result_locator": "fixture-decision://representation-blocked-secret",
  "preview_locator": "preview-internal://blocked/synthetic-secret-like-001",
  "canonical_public_url": null,
  "readback_locator": "readback://expected/secret-like",
  "renderer_version": "preview-contract-v01",
  "transformation_rule": "none",
  "release_state": "release_blocked",
  "release_authority": "synthetic-fixture-authority",
  "release_decision_locator": "fixture-decision://release-blocked-secret",
  "release_conditions": [],
  "distribution_targets": [],
  "distribution_state": "not_dispatched",
  "external_message_id": null,
  "delivery_receipt": null,
  "correction_state": "none",
  "withdrawal_state": "none",
  "synthetic": true,
  "expected_navigation_bucket": "blocked-quarantine-internal-only",
  "expected_primary_badge": "SECRET-LIKE / BLOCKED",
  "expected_blocking_reason": "security_state=blocked_secret; credential-like material",
  "public_display_forbidden_fields": [
    "private_test_only.secret_like_value",
    "private_test_only.raw_detection_sample"
  ],
  "expected_readback_assertions": [
    "absent_from_public_navigation",
    "secret_block_badge_visible",
    "secret_like_value_absent",
    "raw_detection_sample_absent",
    "SIS_review_required_visible"
  ]
}
```

## Safe body

Synthetic secret-like object exists only to test fail-closed behavior.

## Private/test-only field behavior

Internal marker `SYNTHETIC_SECRET_VALUE_DO_NOT_RENDER_7KQ9` may be used by implementation tests but must be absent from rendered/public-safe output.

---
created_by: WEB
purpose: synthetic Stage B representation fixture
project_time: omitted; trusted project-time source not used
