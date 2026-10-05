# Sandbox Effect Outcome Evidence
status: DESIGN_ONLY

EVIDENCED_SUCCESS requires:
invocation evidence; exact operation key; OS/filesystem success evidence; exact created file canonical path; regular-file/no-symlink proof; byte count; payload hash match; readback content/hash match; post-effect target inventory; no forbidden spillover evidence within declared observation scope.

EVIDENCED_FAILURE requires positive evidence that attempted allowed operation failed before achieving success criterion, plus failure evidence/class and target state observation.

UNRESOLVED when effect may have happened but success/failure boundary cannot be proved: timeout, transport/session loss, incomplete readback, ambiguous target state, missing outcome evidence.

NOT_EXECUTED requires positive evidence mutation was not invoked because admission/invocation gate rejected or blocked; mere absence of success is insufficient.

Timeout/transport ambiguity never becomes success or failure by guess.
