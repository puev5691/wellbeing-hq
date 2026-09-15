# Fixture: Withdrawn

status: synthetic-public-safe-fixture
production: false
publication: false

## Metadata

```json
{
  "id": "synthetic-withdrawn-001",
  "title": "Synthetic Withdrawn Publication",
  "artifact_type": "publication",
  "content_class": "publicism",
  "owner_profile": "RED",
  "canonical_locator": "fixture://synthetic-withdrawn-001",
  "provenance_locator": "fixture-pack://synthetic-withdrawn-001",
  "source_repository": "synthetic",
  "source_path": "fixture://synthetic-withdrawn-001",
  "source_commit": "not_applicable",
  "source_blob": "not_applicable",
  "immutable_identity": {
    "scheme": "synthetic-fixture",
    "id": "synthetic-withdrawn-001-v1"
  },
  "supersedes": [],
  "superseded_by": [],
  "semantic_status": "withdrawn",
  "profile_review_status": "withdrawn",
  "profile_review_locator": "fixture-decision://profile-withdrawn",
  "semantic_blocker": "withdrawn-by-authority",
  "editorial_status": "editorial_withdrawn",
  "editorial_result_locator": "fixture-decision://editorial-withdrawn",
  "intended_audience": "historical-readers",
  "intended_purpose": "withdrawal-record",
  "derivative_of": null,
  "derivative_type": null,
  "editorial_blocker": "withdrawn",
  "editorial_superseded_by": null,
  "public_legal_outcome": "allowed-with-conditions",
  "rights_basis": "project-owned-synthetic",
  "personal_data_state": "none",
  "public_legal_conditions": [
    "withdrawal-notice-only"
  ],
  "public_legal_next_gate": null,
  "public_legal_result_locator": "fixture-decision://legal-withdrawal-notice",
  "security_state": "public_safe",
  "security_review_locator": "fixture-decision://security-public-safe",
  "requires_privileged_setting": false,
  "runtime_boundary": "static-preview-only",
  "secret_dependency": false,
  "representation_state": "representation_withdrawn",
  "representation_result_locator": "fixture-decision://representation-withdrawn",
  "preview_locator": "preview://withdrawn/synthetic-withdrawn-001",
  "canonical_public_url": null,
  "readback_locator": "readback://expected/withdrawn",
  "renderer_version": "preview-contract-v01",
  "transformation_rule": "none",
  "release_state": "release_withdrawn",
  "release_authority": "synthetic-fixture-authority",
  "release_decision_locator": "fixture-decision://release-withdrawn",
  "release_conditions": [],
  "distribution_targets": [],
  "distribution_state": "withdrawn",
  "external_message_id": null,
  "delivery_receipt": null,
  "correction_state": "none",
  "withdrawal_state": "withdrawn",
  "synthetic": true,
  "expected_navigation_bucket": "withdrawn-historical",
  "expected_primary_badge": "WITHDRAWN",
  "expected_blocking_reason": "release/profile/editorial withdrawn",
  "public_display_forbidden_fields": [
    "withdrawn_private_body"
  ],
  "expected_readback_assertions": [
    "absent_from_current_bucket",
    "withdrawn_badge_visible",
    "withdrawal_record_visible",
    "prior_body_not_presented_as_current",
    "release_withdrawn_visible"
  ]
}
```

## Safe body

Synthetic publication withdrawn. Historical record retained; current/public representation is invalid.

## Private/test-only field behavior

`withdrawn_private_body` must not render publicly.

---
created_by: WEB
purpose: synthetic Stage B representation fixture
project_time: omitted; trusted project-time source not used
