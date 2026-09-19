# Credential boundary

status: DESIGN_ONLY
package_contains_secrets: false
credential_access_performed: 0

## Local read-only VERIFY mode

The adapter itself requires no provider/API credential for local filesystem/Git read-only operations.

Target access should be represented by OS filesystem permissions of the dedicated `arh-preserve` identity, not by stored application credentials.

## Forbidden storage/inheritance

Do not store or inherit credential values in:
- adapter package;
- `verify.json`;
- service environment;
- systemd unit;
- audit records;
- repository/archive roots;
- command line;
- working directory.

Explicitly avoid inheriting token/secret/password/API-key/private-key environment variables.

## Remote/forced-command future modes

No remote credential class is authorized by this preparation.

If a future SSH forced-command or cross-host transport is chosen, credential class, provisioning owner, storage and rotation require a separate OPERATOR authority. Do not infer authority from capability.

Provisioning owner:
`UNKNOWN_REQUIRES_OPERATOR_DECISION`.

## Proof of absence proposal

Predeploy verification should inspect environment variable NAMES only, not values, and verify the service unit has an explicit minimal environment with no credential directives.

Current bounded read-only checks found no secret-like environment variable names in the inspected shell environments, but this is not proof of future systemd service environment.
