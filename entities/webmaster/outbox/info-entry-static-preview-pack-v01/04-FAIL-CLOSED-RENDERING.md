# Fail-Closed Rendering

Unknown/blocked/inconsistent applicable gate prevents optimistic public-ready rendering.

Modes:
- allowed representation;
- candidate/review-only representation;
- historical representation;
- blocked placeholder.

Blocked placeholder shows only safe id/title, blocking badge, reason class, safe provenance, safe next gate, and suppression notice.

Hard blocks include immutable mismatch, credential-like unresolved content, blocked_secret, legal blocked, editorial blocked, required privacy unknown, release blocked, unresolved current/supersede conflict.

Secret-like test marker may exist internally, but rendered/public-safe output must never echo it.

---
created_by: WEB
project_time: omitted; trusted project-time source not used
