# Fixture: Candidate / Research

status: synthetic-public-safe-fixture
production: false
publication: false

## Metadata

```json
{
  "id": "synthetic-candidate-001",
  "title": "Synthetic Research Candidate",
  "artifact_type": "research-note",
  "content_class": "research",
  "owner_profile": "VOL",
  "canonical_locator": "fixture://synthetic-candidate-001",
  "provenance_locator": "fixture-pack://synthetic-candidate-001",
  "source_repository": "synthetic",
  "source_path": "fixture://synthetic-candidate-001",
  "source_commit": "not_applicable",
  "source_blob": "not_applicable",
  "immutable_identity": {
    "scheme": "synthetic-fixture",
    "id": "synthetic-candidate-001-v1"
  },
  "supersedes": [],
  "superseded_by": [],
  "semantic_status": "candidate",
  "profile_review_status": "candidate",
  "profile_review_locator": "fixture-decision://profile-candidate",
  "semantic_blocker": null,
  "editorial_status": "editorial_reviewed",
  "editorial_result_locator": "fixture-decision://editorial-reviewed",
  "intended_audience": "reviewers",
  "intended_purpose": "research-review",
  "derivative_of": null,
  "derivative_type": null,
  "editorial_blocker": null,
  "editorial_superseded_by": null,
  "public_legal_outcome": "allowed-with-conditions",
  "rights_basis": "project-owned-synthetic",
  "personal_data_state": "none",
  "public_legal_conditions": [
    "must-remain-labelled-candidate"
  ],
  "public_legal_next_gate": "profile-acceptance",
  "public_legal_result_locator": "fixture-decision://legal-conditional",
  "security_state": "public_safe",
  "security_review_locator": "fixture-decision://security-public-safe",
  "requires_privileged_setting": false,
  "runtime_boundary": "static-preview-only",
  "secret_dependency": false,
  "representation_state": "preview_ready",
  "representation_result_locator": "fixture-decision://preview-ready",
  "preview_locator": "preview://research/synthetic-candidate-001",
  "canonical_public_url": null,
  "readback_locator": "readback://expected/candidate",
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
  "correction_state": "none",
  "withdrawal_state": "none",
  "synthetic": true,
  "expected_navigation_bucket": "research-candidate",
  "expected_primary_badge": "CANDIDATE / NOT CURRENT",
  "expected_blocking_reason": "semantic_status=candidate; release_unassessed",
  "public_display_forbidden_fields": [
    "reviewer_private_note"
  ],
  "expected_readback_assertions": [
    "absent_from_current_bucket",
    "candidate_badge_persistent",
    "no_public_ready_claim",
    "release_unassessed_visible",
    "reviewer_private_note_absent"
  ]
}
```

## Safe body

Synthetic research material may be previewed for review but must remain non-current.

## Private/test-only field behavior

`reviewer_private_note` is forbidden in public-safe output.

---
created_by: WEB
purpose: synthetic Stage B representation fixture
project_time: omitted; trusted project-time source not used
