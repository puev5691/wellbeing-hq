# Fixture: Superseded

status: synthetic-public-safe-fixture
production: false
publication: false

## Metadata

```json
{
  "id": "synthetic-superseded-001",
  "title": "Synthetic Superseded Guide",
  "artifact_type": "document",
  "content_class": "technical-guide",
  "owner_profile": "WEB",
  "canonical_locator": "fixture://synthetic-superseded-001",
  "provenance_locator": "fixture-pack://synthetic-superseded-001",
  "source_repository": "synthetic",
  "source_path": "fixture://synthetic-superseded-001",
  "source_commit": "not_applicable",
  "source_blob": "not_applicable",
  "immutable_identity": {
    "scheme": "synthetic-fixture",
    "id": "synthetic-superseded-001-v1"
  },
  "supersedes": [],
  "superseded_by": [
    "synthetic-fixture://synthetic-current-successor-001-v2"
  ],
  "semantic_status": "superseded",
  "profile_review_status": "superseded",
  "profile_review_locator": "fixture-decision://profile-superseded",
  "semantic_blocker": "superseded-by-newer-version",
  "editorial_status": "editorial_superseded",
  "editorial_result_locator": "fixture-decision://editorial-superseded",
  "intended_audience": "historical-readers",
  "intended_purpose": "historical-reference",
  "derivative_of": null,
  "derivative_type": null,
  "editorial_blocker": null,
  "editorial_superseded_by": "synthetic-fixture://synthetic-current-successor-001-v2",
  "public_legal_outcome": "allowed",
  "rights_basis": "project-owned-synthetic",
  "personal_data_state": "none",
  "public_legal_conditions": [
    "historical-label-required"
  ],
  "public_legal_next_gate": null,
  "public_legal_result_locator": "fixture-decision://legal-allowed",
  "security_state": "public_safe",
  "security_review_locator": "fixture-decision://security-public-safe",
  "requires_privileged_setting": false,
  "runtime_boundary": "static-preview-only",
  "secret_dependency": false,
  "representation_state": "representation_superseded",
  "representation_result_locator": "fixture-decision://representation-superseded",
  "preview_locator": "preview://historical/synthetic-superseded-001",
  "canonical_public_url": null,
  "readback_locator": "readback://expected/superseded",
  "renderer_version": "preview-contract-v01",
  "transformation_rule": "none",
  "release_state": "release_unassessed",
  "release_authority": null,
  "release_decision_locator": null,
  "release_conditions": [],
  "distribution_targets": [],
  "distribution_state": "not_dispatched",
  "external_message_id": null,
  "delivery_receipt": null,
  "correction_state": "stale",
  "withdrawal_state": "none",
  "synthetic": true,
  "expected_navigation_bucket": "historical-superseded",
  "expected_primary_badge": "SUPERSEDED",
  "expected_blocking_reason": "superseded_by newer version; not current",
  "public_display_forbidden_fields": [
    "obsolete_private_note"
  ],
  "expected_readback_assertions": [
    "absent_from_current_bucket",
    "superseded_badge_visible",
    "successor_locator_visible",
    "historical_bucket_only",
    "stale_warning_visible"
  ]
}
```

## Safe body

Synthetic former guide retained only to test historical/superseded rendering.

## Private/test-only field behavior

`obsolete_private_note` must not render publicly.

---
created_by: WEB
purpose: synthetic Stage B representation fixture
project_time: omitted; trusted project-time source not used
