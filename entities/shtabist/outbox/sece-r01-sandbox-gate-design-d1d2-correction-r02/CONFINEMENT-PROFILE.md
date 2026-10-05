# SANDBOX_CONFINEMENT_PROFILE_R02
status: DESIGN_ONLY
implementation: NOT_IMPLEMENTED
activation: NOT_ACTIVE
profile_id: SECE_SANDBOX_CONFINEMENT_PROFILE_R02
predecessor_tree: e5f875af2322f460a2d02af4d47c56e8d2ae2ce9

## D1 exact leaf grammar
Accepted leaf_name is exactly one basename component encoded in the platform profile's declared filename encoding and must round-trip byte/codepoint-equivalent under the platform API used.

Reject if:
empty; absolute; "."; ".."; contains "/" or "\"; contains any platform-recognized alternate separator; contains NUL; contains drive/device/UNC/network/namespace prefix; contains colon or reserved namespace syntax where it can change namespace semantics; contains a platform-specific escape form; normalization/case/encoding transform required by the selected API would make the effective component differ from the admitted exact component; contains more than one path component.

The future platform evidence profile MUST enumerate any additional reserved names/forms. Unknown platform filename semantics => BLOCKED.
Security never relies on string startsWith(root) or post-hoc canonical path containment.

## Anchored root
SANDBOX_ROOT_OBJECT_IDENTITY fields:
sandbox_target_id; environment_instance_id; owner_attempt_id; explanatory_root_locator; stable_root_object_identity_or_platform_equivalent; object_type=DIRECTORY; ownership_evidence; isolation_evidence; expected_parent_boundary_identity where applicable; currentness_evidence_version; platform_evidence_profile_id.

It is derived from an already opened/verified root directory object or platform-equivalent stable namespace reference before admission.

After admission, creation and later object operations remain relative/object-bound to this anchored identity. The security boundary MUST NOT re-resolve root from explanatory_root_locator.

If root/parent identity at invocation differs from admission => NOT_EXECUTED.

## Race-safe creation semantics
Required properties, syscall-neutral:
- leaf creation relative to anchored root object;
- exclusive create;
- no-follow / reparse-point-equivalent denial;
- leaf proven absent at the atomic create boundary;
- no overwrite;
- no traversal/re-resolution of mutable parent components;
- no fallback to unanchored absolute/pathname open;
- returned open object reference is retained as the primary created-object reference.

Platform implementation may differ only if it proves equivalent properties.

## Created object identity
CREATED_SANDBOX_OBJECT_IDENTITY fields:
operation_key; attempt_id; sandbox_target_id; confinement_profile_id/version; anchored_root_identity; exact_leaf_name; stable_filesystem_object_identity_or_platform_equivalent; open_object_reference_class; object_type=REGULAR_FILE; no_symlink_reparse_evidence; ownership_evidence; creation_evidence; payload_digest; expected_length; maximum_length; platform_evidence_profile_id; hardlink_replacement_evidence.

Identity is derived from the actual object returned by successful exclusive create, never from later pathname lookup.

## Same-object continuity
create -> write -> stat -> readback -> hash -> EffectOutcome -> cleanup must refer to the same created object identity.

Where operations require reopening, the implementation must compare platform-supported stable identity/equivalent evidence against CREATED_SANDBOX_OBJECT_IDENTITY before treating observation as the same object.

If mutation has not occurred and same-object proof cannot be established => NOT_EXECUTED/BLOCKED.
If mutation may have occurred and continuity cannot be established => UNRESOLVED.
Never reopen pathname and assume equality.

## Hardlink/replacement boundary
Security property: the object observed/read/cleaned must remain the exact attempt-created object and must not be silently substituted or rebound to a foreign object.

Platform evidence profile defines available proof: stable file ID/device+inode/file-ID/handle identity; link count or platform equivalent when meaningful; reparse/symlink state; replacement/change indicators.

No universal inode/link-count assumption.
If platform cannot prove required non-replacement/same-object property for this effect class => BLOCKED before mutation; if proof is lost after possible mutation => UNRESOLVED.
