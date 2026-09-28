# SHD emergency failover marker

status: OPERATOR_REQUESTED_CHAT_REPLACEMENT
purpose: prevent accidental continuation from the degraded SHD chat before replacement initiation

Boundary:
- existing SHD chat is not to be used for new authoritative profile mutations;
- local lab data is preserved before replacement;
- replacement SHD must verify external recovery and fresh GitHub state before resuming work;
- this marker is not a technical writer lock and does not itself grant writer authority;
- no WBN/TERA2 launch, firewall change, production mutation, secret handling, or destructive cleanup is authorized by this marker.

Local backup:
/data/wellbeing-lab/backups/shd-pre-reinit-v01

Secrets/log contents were excluded from the backup artifact set.
