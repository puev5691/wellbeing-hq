# SIS shard gateway VERIFY unit candidate

status: CANDIDATE_FOR_AUTHORIZED_OPTION_A

```ini
[Unit]
Description=Wellbeing shard gateway VERIFY bounded oneshot
After=local-fs.target

[Service]
Type=oneshot
User=arh-preserve
Group=arh-preserve
WorkingDirectory=/var/lib/wellbeing/shard-gateway
Environment=PATH=/usr/bin:/bin
Environment=LC_ALL=C
ExecStart=/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --audit-module /opt/wb-shard-gateway/audit_sink.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ProtectHome=yes
ReadWritePaths=/var/lib/wellbeing/shard-gateway /run/wb-shard-gateway /var/log/wb-shard-gateway
RestrictAddressFamilies=AF_UNIX

[Install]
WantedBy=multi-user.target
```

ExecStart is argv-equivalent to pinned INVOCATION.json production contract. Unit is oneshot, non-network, non-credential, not enabled by this artifact.
